from qiskit import Aer, execute
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi, sqrt
import numpy as np
from collections import Counter


from circuits import *
list_of_circuit = [circuit1,circuit2,circuit3,circuit4,circuit5,circuit6,circuit7,circuit8,circuit9,circuit10,circuit11,circuit12,circuit13,circuit14,circuit15,circuit16,circuit17,circuit18,circuit19]



def embed(qc,qr,datainput,n):
    r'''generate embedding circuit from the paper
    
    Inputs:
        qc is total quantum circuit 
        qr is the quantum cricuit where the main work is done
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        n is 2 or 4
    Returns:
        data embeded circuit '''
    if n==2:
        qc.rx(0.5*pi*datainput[0],qr[0])
        qc.rx(0.5*pi*datainput[1],qr[1])
    elif n==4:
        qc.rx(0.5*pi*datainput[0],qr[0])
        qc.rx(0.5*pi*datainput[1],qr[1])   
        qc.rx(0.5*pi*datainput[0],qr[2])
        qc.rx(0.5*pi*datainput[1],qr[3])         

    qc.ry(pi/4,qr[:])
    qc.rz(pi/4,qr[:])
    
    return qc



#--------------------------------------------------------------
#
# for two-qubit case
#
#--------------------------------------------------------------


def convertv(input_dict):
    r'''run and count the most frequent value. Print with assigned label
    
    Inputs:
        input_dict is the result of the counting of simualtion
    Returns:
        yprediction'''    
    k = Counter(input_dict)
    val=k.most_common(1)[0][0] 
    list1=['00','11'];
    if val in list1:
        ypredit=-1
    else:
        ypredit=1
    return ypredit


def cir_ex(qc,qr,currentParams):
    r'''example circuit for testing two-qubit gate, two qubit version of circuit3 
    
    Inputs:
        qc is total quantum circuit 
        qr is the quantum cricuit where the main work is done
        currentParams is the current value for the parameters
    Returns:
        print example circuit for two-qubit '''
    
    count=0;

    for i in range(2):
        qc.rx(currentParams[count],qr[i])
        count=count+1
    for i in range(2):
        qc.rz(currentParams[count],qr[i])
        count=count+1
    qc.cz(qr[0],qr[1])
    
    return qc

def Qrun(datainput,currentParams,nshot,nqubit):
    backend = Aer.get_backend('qasm_simulator')
    qr = QuantumRegister(nqubit)
    cr = ClassicalRegister(nqubit)
    qc = QuantumCircuit(qr,cr)

    qc=embed(qc,qr,datainput,nqubit)
    qc=cir_ex(qc,qr,currentParams)

    qc.measure(qr[:],cr[:])
    job = execute(qc, backend, shots=nshot)
    result = job.result()
    count =result.get_counts()
    predict=convertv(count)
    return predict


    
def l1loss(predict,datalabel):
    r'''calculte the loss
    
    Inputs:
        predict prediction from the Qrun
        datalabel actual label value from the data
    Returns:
        calculate l1 loss'''    
    return abs(predict-datalabel)

def loss2qubit(datainput,datalabel,currentParams):    
    r'''L1 loss assmbler, run the Q circuit, and calcualte the loss for the given data.
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        datalabel actual label value from the data
        backend is Qiskit backend        
    Returns:
        calculate l1 loss'''    
    
    nshot=10000; #number of shots on simulation
    nqubit=2; # how many qubit?
    
    predict=Qrun(datainput,currentParams,nshot,nqubit)
    loss=l1loss(predict,datalabel)
   
    return loss

def quick_predict(datainput,currentParams):    
    r'''L1 loss assmbler, run the Q circuit, and calcualte the loss for the given data.
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        datalabel actual label value from the data
        backend is Qiskit backend        
    Returns:
        prediction'''    
    
    nshot=200; #number of shots on simulation
    nqubit=2; # how many qubit?
    
    predict=Qrun(datainput,currentParams,nshot,nqubit)
   
    return predict



#--------------------------------------------------------------
#
# for four-qubit case
#
#--------------------------------------------------------------


def convert_qubitF(input_dict):
    r'''run and count the most frequent value. Print with assigned label
    
    Inputs:
        input_dict is the result of the counting of simualtion
    Returns:
        yprediction'''    
    k = Counter(input_dict)
    val=k.most_common(1)[0][0] 
    list1=['0000','0001','0010','0011','1100','1101','1110','1111'];
    if val in list1:
        ypredit=-1
    else:
        ypredit=1
    return ypredit



def Qrun_qubitF(datainput,currentParams,nshot,nqubit,circuit):
    backend = Aer.get_backend('qasm_simulator')
    qr = QuantumRegister(nqubit)
    cr = ClassicalRegister(nqubit)
    qc = QuantumCircuit(qr,cr)

    qc=embed(qc,qr,datainput,nqubit)
    qc=list_of_circuit[circuit[0]](qc,qr,currentParams,circuit[1],0)

    qc.measure(qr[:],cr[:])
    job = execute(qc, backend, shots=nshot)
    result = job.result()
    count =result.get_counts()
    predict=convert_qubitF(count)
    return predict



def loss_qubitF(datainput,datalabel,currentParams,circuit):    
    r'''L1 loss assmbler, run the Q circuit, and calcualte the loss for the given data.
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        datalabel actual label value from the data
        backend is Qiskit backend        
    Returns:
        calculate l1 loss'''    
    
    nshot=10000; #number of shots on simulation
    nqubit=4; # how many qubit?
    
    predict=Qrun_qubitF(datainput,currentParams,nshot,nqubit,circuit)
    loss=l1loss(predict,datalabel)
   
    return loss

def predict_qubitF(datainput,currentParams,circuit):    
    r'''L1 loss assmbler, run the Q circuit, and calcualte the loss for the given data.
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        datalabel actual label value from the data
        backend is Qiskit backend        
    Returns:
        prediction'''    
    
    nshot=200; #number of shots on simulation
    nqubit=4; # how many qubit?
    
    predict=Qrun_qubitF(datainput,currentParams,nshot,nqubit,circuit)
   
    return predict
