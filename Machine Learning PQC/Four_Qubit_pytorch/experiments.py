r'''The purpose of this script is to do our QML experiments.'''

# Zeroth bit: code imports
import torch
import numpy as np
from torch import Tensor
from torch.nn import MSELoss
import torch.optim as optim
from torch.optim import SGD,Adam 
from pandas.core.common import flatten


from qiskit.circuit import Parameter
from qiskit  import Aer, QuantumCircuit
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.neural_networks import CircuitQNN
from qiskit_machine_learning.connectors import TorchConnector

from scipy import linalg

import sys
sys.path.append('../../Pyfiles')
from circuits_n1 import *

from helpers import parity

# First bit: Creating the circuits

def make_embedding_circuit():
    r'''Makes the embedding circuit.'''
    feature_map = QuantumCircuit(4, name='Embed')
    feature_map.rx(Parameter('x[0]'),0)
    feature_map.rx(Parameter('x[1]'),1)
    feature_map.rx(Parameter('x[2]'),2)
    feature_map.rx(Parameter('x[3]'),3)

    for j in [0, 2]:
        feature_map.ry(np.pi/4,j)
        feature_map.ry(np.pi/4,j+1)
        feature_map.rz(np.pi/4,j)
        feature_map.rz(np.pi/4,j+1)
    # Remove this word once you've filled in the code.
    return feature_map

def make_classifer_circuit(ID):
    r'''A helper function which makes the classfier circuits.
        Given an ID, it returns the PQC.'''
    param_y=[(Parameter('θ'+str(i))) for i in range(40)]
    ansatz = QuantumCircuit(4, name='PQC')
    ansatz=globals()["circuit"+"{0}".format(ID)](ansatz,param_y,1,0)
    # Remove this word once you've filled in the code.
    return ansatz

# Second bit: Loading data & generating training/validation/testing splits
def load_data(dataSetID):
    
    # Define the directory paths
    dataPath = r'../../dataset/data{0}.txt'.format(dataSetID)
    dataLabel = r'../../dataset/data{0}label.txt'.format(dataSetID)

    # Load in the data
    dataCoords = np.loadtxt(dataPath)
    dataLabels = np.loadtxt(dataLabel)

    # Make a data structure which is easier to work with
    # for shuffling. 
    # Also, notice we change the data labels from {0, 1} to {-1, +1}
    data = list(zip(dataCoords, 2*dataLabels-1))
    
    return data

def generate_train_validate_test_data(data, train_size=100, validate_size=500, test_size=None, randomSeed=0):
    r'''This is a function which, given a dataset, will return 3 distinct datasets from it: a training dataset,
    a validation dataset, and a testing dataset.
    
    The size of the training and validation datasets is set by the function call; the size of the testing
    dataset is the remainder of the data after training & validation dataset have been generated.'''
    
    if test_size is not None:
        assert len(data) >= test_size + train_size+validate_size, 'Not enough data to do the splitting.'
    else:
        assert len(data) > train_size+validate_size, 'Not enough data to do the splitting.'
        
    def generate_data(data, ixs):
        r'''Helper function for generating data.'''
        X= [np.array(list(flatten([data[j][0],data[j][0]]))) for j in ixs]
        y = [data[j][1] for j in ixs]    
    
        # Recast X as a pyTorch tensor
        X = Tensor(X)
        
        # Change how the data is labeled: {-1,+1} --> {0, 1}
        y =  [ (x + 1)/2 for x in y]
        
        return X, y
    
    # At the start, we could use all possible datapoints for training
    possible_ixs = range(len(data))
    
    # Training data
    np.random.seed(randomSeed)
    train_ixs = np.random.choice(possible_ixs, size=train_size)
    train_X, train_y = generate_data(data, train_ixs)
    
    # Update the possible indices we could choose from
    possible_ixs = [x for x in possible_ixs if x not in train_ixs]

    # Validation data
    np.random.seed(randomSeed)
    validate_ixs = np.random.choice(possible_ixs, size=validate_size)
    validate_X, validate_y = generate_data(data, validate_ixs)
    
    # Now, use the rest of the data for testing
    possible_ixs = [x for x in possible_ixs if x not in validate_ixs]
    if test_size is None:
        test_X, test_y = generate_data(data, possible_ixs)
    else:
        test_ixs = np.random.choice(possible_ixs, size=test_size)
        test_X, test_y = generate_data(data, test_ixs)
    
    return train_X, train_y, validate_X, validate_y, test_X, test_y

# --------------- THIRD BIT: TRAINING THE MODEL ---------------------------#
def check_accuracy(model, X, y_target):
    r'''Helper function to compute the accuracy'''
    
    # Evaluate model on input data
    output = model(X)
    
    # Now, do some wrangling to get the data in a better format
    output = output.detach().numpy()
    
    # Output is a list of lists, where the inner list is the probabilities
    # of each class assignment. We pick the most probable class as the prediction
    predictions = np.array([np.argmax(x) for x in output])
    
    return sum(predictions == y_target)/len(y_target)

def train_model(feature_map, ansatz, epochs, learning_rate, train_X, train_y, qi=QuantumInstance(Aer.get_backend('statevector_simulator'))):
    
    qc = QuantumCircuit(ansatz.width())
    qc.append(feature_map, range(ansatz.width()))
    qc.append(ansatz, range(ansatz.width()))
    output_shape = 2
    qnn = CircuitQNN(qc, input_params=feature_map.parameters, weight_params=ansatz.parameters, 
                          interpret=parity, output_shape=output_shape, quantum_instance=qi)

    # Set up the pyTorch model
    np.random.seed(0)  
    initial_weights = 0.1*(2*np.random.rand(qnn.num_weights) - 1)
    model = TorchConnector(qnn, initial_weights)

    # define optimizer and loss function
    optimizer = optim.SGD(model.parameters(),lr=learning_rate)
    f_loss = MSELoss(reduction='mean')

    # Set model to training mode
    model.train()   
    print("__Learning Rate (", learning_rate,") is intialized")

    for epoch in range(epochs):
        optimizer.zero_grad()                        # initialize gradient
        loss = 0.0                                   # initialize loss    
        for x, y_target in zip(train_X, train_y):    # evaluate batch loss
            output = model(Tensor(x)).reshape(1, 2)  # forward pass
            targets=Tensor([y_target]).long()
            targets = targets.to(torch.float32)
            loss += f_loss(output, targets) 
        loss.backward()                              # backward pass

        # run optimizer
        optimizer.step() 
    print("__Learning Rate (", learning_rate,") is done")
    return model