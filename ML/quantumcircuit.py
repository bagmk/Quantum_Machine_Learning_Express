from qiskit import Aer, execute
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi, sqrt



def cN(lists,string):
    r'''Counter string from array called lists
    
    Inputs:
        lists array of the strings i.e. ['0','1','1'....]
        string '1'
        
    Returns:
        count number '''
    if string in lists:
        return lists[string]   
    else:
        return 0


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
        qc.rx(datainput[0],qr[0])
        qc.rx(datainput[1],qr[1])
    elif n==4:
        qc.rx(datainput[0],qr[0])
        qc.rx(datainput[1],qr[1])   
        qc.rx(datainput[0],qr[3])
        qc.rx(datainput[1],qr[4])         

    qc.ry(pi/4,qr[:])
    qc.rz(pi/4,qr[:])
    
    return qc

def circuit1(qc,qr,currentParams):
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
    r'''run the simulation can calculte the average 
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        nshot is number of shots on simulation
        nqubit is number of qubit
    Returns:
        average value of the yprediction'''
  
    backend = Aer.get_backend('qasm_simulator')
    qr = QuantumRegister(nqubit)
    cr = ClassicalRegister(nqubit)
    qc = QuantumCircuit(qr,cr)

    qc=embed(qc,qr,datainput,nqubit)
    qc=circuit1(qc,qr,currentParams)

    qc.measure(qr[:],cr[:])
    job = execute(qc, backend, shots=nshot)
    result = job.result()
    count =result.get_counts()
    lm=-1*(cN(count,'00')+cN(count,'11'))
    lp=1*(cN(count,'10')+cN(count,'01'))
    predict=(lm+lp)/nshot
    return predict
    
def l1loss(predict,datalabel):
    r'''calculte the loss
    
    Inputs:
        predict prediction from the Qrun
        datalabel actual label value from the data
    Returns:
        calculate l1 loss'''    
    return abs(predict-2*(datalabel-0.5))
    

def loss2qubit(datainput,datalabel,currentParams):    
    r'''L1 loss assmbler, run the Q circuit, and calcualte the loss for the given data.
    
    Inputs:
        datainput is the coordinate of the 2D data input i.e. [x1,y1]
        currentParams is the current value for the parameters
        datalabel actual label value from the data
        backend is Qiskit backend        
    Returns:
        calculate l1 loss'''    
    
    nshot=1000; #number of shots on simulation
    nqubit=2; # how many qubit?
    
    predict=Qrun(datainput,currentParams,nshot,nqubit)
    loss=l1loss(predict,datalabel)
   
    return loss
