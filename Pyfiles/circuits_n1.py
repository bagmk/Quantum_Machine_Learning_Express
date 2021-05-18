from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

def circuit1(qc,theta,L,repeat):
    #circuit 1 
    #theta is list of the parameters
    #theta length is 8L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1
    
    if repeat!=0: 
    
        for l in range(L):

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1    
     
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
     
    return qc


def circuit2(qc,theta,L,repeat):
    #circuit 2
    #theta is list of the parameters
    #theta length is 8L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            
        qc.cx(3,2)
        qc.cx(2,1)
        qc.cx(1,0)
    
    
    if repeat!=0:    
        
        for l in range(L):
        
            qc.cx(1,0)
            qc.cx(2,1)
            qc.cx(3,2)
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc




def circuit3(qc,theta,L,repeat):
    #circuit 3
    #theta is list of the parameters
    #theta length is (11)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            
        qc.crz(theta[count],3,2)
        count=count+1 
        qc.crz(theta[count],2,1)
        count=count+1 
        qc.crz(theta[count],1,0)
        count=count+1 

    if repeat!=0:           
        
    
        
        for l in range(L):
        
            qc.crz(theta[count],1,0)
            count=count+1 
            qc.crz(theta[count],2,1)
            count=count+1 
            qc.crz(theta[count],3,2)
            count=count+1 
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc



def circuit4(qc,theta,L,repeat):
    #circuit 4
    #theta is list of the parameters
    #theta length is (11)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat
    

    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            
        qc.crx(theta[count],3,2)
        count=count+1 
        qc.crx(theta[count],2,1)
        count=count+1 
        qc.crx(theta[count],1,0)
        count=count+1 

    if repeat!=0:               
        
    
        
        for l in range(L):
        
            qc.crx(theta[count],1,0)
            count=count+1 
            qc.crx(theta[count],2,1)
            count=count+1 
            qc.crx(theta[count],3,2)
            count=count+1 
        
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc




def circuit5(qc,theta,L,repeat):
    #circuit 5
    #theta is list of the parameters
    #theta length is (28)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            

            
        for j in range(4):
            for i in range(4):
                if i!=j:
                    qc.crz(theta[count],3-j,3-i)
                    count=count+1

 

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            
            
    if repeat!=0:             
        
    
        
        for l in range(L):
        

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1     
        
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
        

            for j in range(4):
                for i in range(4):
                    if i!=j:
                        qc.crz(theta[count],j,i)
                        count=count+1
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc



def circuit6(qc,theta,L,repeat):
    #circuit 6
    #theta is list of the parameters
    #theta length is (28)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            

            
        for j in range(4):
            for i in range(4):
                if i!=j:
                    qc.crx(theta[count],3-j,3-i)
                    count=count+1

 

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            
            
    if repeat!=0:             
        
    
        
        for l in range(L):
        

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1     
        
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
        

            for j in range(4):
                for i in range(4):
                    if i!=j:
                        qc.crx(theta[count],j,i)
                        count=count+1
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc


def circuit7(qc,theta,L,repeat):
    #circuit 7
    #theta is list of the parameters
    #theta length is (19)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    
    


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            

            
        qc.crz(theta[count],1,0)
        count=count+1

        qc.crz(theta[count],3,2)
        count=count+1



        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1

        
        qc.crz(theta[count],2,1)    
        count=count+1
        
            
    if repeat!=0:             
        
    
        
        for l in range(L):
        
            qc.crz(theta[count],2,1)    
            count=count+1
        
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1        
        
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
                
        
            qc.crz(theta[count],3,2)
            count=count+1
        
            qc.crz(theta[count],1,0)
            count=count+1
        
        
        
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc



def circuit8(qc,theta,L,repeat):
    #circuit 8
    #theta is list of the parameters
    #theta length is (19)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    
    


    count=0
    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1            

            
        qc.crx(theta[count],1,0)
        count=count+1

        qc.crx(theta[count],3,2)
        count=count+1



        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1

        
        qc.crx(theta[count],2,1)    
        count=count+1
        
            
    if repeat!=0:             
        
    
        
        for l in range(L):
        
            qc.crx(theta[count],2,1)    
            count=count+1
        
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1        
        
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
                
        
            qc.crx(theta[count],3,2)
            count=count+1
        
            qc.crx(theta[count],1,0)
            count=count+1
        
        
        
    
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1         
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1                
     
    return qc


def circuit9(qc,theta,L,repeat):
    #circuit 9
    #theta is list of the parameters
    #theta length is (4)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    
    


    count=0
    for l in range(L):

        for i in range(4):
            qc.h(i)

        qc.cz(3,2)
        qc.cz(2,1)
        qc.cz(1,0)
        
        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
        
            
    if repeat!=0:             
        
    
        
        for l in range(L):
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1
                
            qc.cz(1,0) 
            qc.cz(2,1)
            qc.cz(3,2)
            
                 
        
            for i in range(4):
                qc.h(i)                  
     
    return qc







def circuit10(qc,theta,L,repeat):
    #circuit 10
    #theta is list of the parameters
    #theta length is (4)L+4
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    
    


    count=0
    
    for i in range(4):
        qc.ry(theta[count],i)
        count=count+1
    
    for l in range(L):

        qc.cz(3,2)
        qc.cz(2,1)
        qc.cz(1,0)
        qc.cz(3,0)



        
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1

        
            
    if repeat!=0:             
        
        for l in range(L):
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1
            
            qc.cz(3,0)            
            qc.cz(1,0)
            qc.cz(2,1)
            qc.cz(3,2)
        
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1
            
                 
              
     
    return qc




def circuit11(qc,theta,L,repeat):
    #circuit 11
    #theta is list of the parameters
    #theta length is (12)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):

        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1    
    

        qc.cx(1,0)
        qc.cx(3,2)



        qc.ry(theta[count],1)
        count=count+1 
        qc.ry(theta[count],2)
        count=count+1 
        qc.rz(theta[count],1)
        count=count+1 
        qc.rz(theta[count],2)
        count=count+1 
        qc.cx(2,1)
        
            
    if repeat!=0:             
        
        for l in range(L):
            qc.cx(2,1)
            
            qc.rz(theta[count],2)
            count=count+1 
            qc.rz(theta[count],1)
            count=count+1 
            qc.ry(theta[count],2)
            count=count+1 
            qc.ry(theta[count],1)
            count=count+1 
        
            qc.cx(3,2)
            qc.cx(1,0)
            
            
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1            
            
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1            

                 
              
     
    return qc









def circuit12(qc,theta,L,repeat):
    #circuit 12
    #theta is list of the parameters
    #theta length is (12)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):

        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1
        
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1    
    

        qc.cz(1,0)
        qc.cz(3,2)



        qc.ry(theta[count],1)
        count=count+1 
        qc.ry(theta[count],2)
        count=count+1 
        qc.rz(theta[count],1)
        count=count+1 
        qc.rz(theta[count],2)
        count=count+1 
        qc.cz(2,1)
        
            
    if repeat!=0:             
        
        for l in range(L):
            qc.cz(2,1)
            
            qc.rz(theta[count],2)
            count=count+1 
            qc.rz(theta[count],1)
            count=count+1 
            qc.ry(theta[count],2)
            count=count+1 
            qc.ry(theta[count],1)
            count=count+1 
        
            qc.cz(3,2)
            qc.cz(1,0)
            
            
            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1            
            
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1            

                 
              
     
    return qc



def circuit13(qc,theta,L,repeat):
    #circuit 13
    #theta is list of the parameters
    #theta length is (16)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1

        qc.crz(theta[count],3,0)
        count=count+1 
        qc.crz(theta[count],2,3)
        count=count+1 
        qc.crz(theta[count],1,2)
        count=count+1 
        qc.crz(theta[count],0,1)
        count=count+1 
  

        
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1    


        qc.crz(theta[count],3,2)
        count=count+1 
        qc.crz(theta[count],0,3)
        count=count+1 
        qc.crz(theta[count],1,0)
        count=count+1 
        qc.crz(theta[count],2,1)
        count=count+1 

            
    if repeat!=0:             
        
        for l in range(L):
         
            qc.crz(theta[count],2,1)
            count=count+1 
            qc.crz(theta[count],1,0)
            count=count+1                  
            qc.crz(theta[count],0,3)
            count=count+1 
        
            qc.crz(theta[count],3,2)
            count=count+1         
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1    

            qc.crz(theta[count],0,1)
            count=count+1           
            
            qc.crz(theta[count],1,2)
            count=count+1         
            qc.crz(theta[count],2,3)
            count=count+1 
        
            qc.crz(theta[count],3,0)
            count=count+1         
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1
            
            
    return qc




def circuit14(qc,theta,L,repeat):
    #circuit 14
    #theta is list of the parameters
    #theta length is (16)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1

        qc.crx(theta[count],3,0)
        count=count+1 
        qc.crx(theta[count],2,3)
        count=count+1 
        qc.crx(theta[count],1,2)
        count=count+1 
        qc.crx(theta[count],0,1)
        count=count+1 
  

        
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1    


        qc.crx(theta[count],3,2)
        count=count+1 
        qc.crx(theta[count],0,3)
        count=count+1 
        qc.crx(theta[count],1,0)
        count=count+1 
        qc.crx(theta[count],2,1)
        count=count+1 

            
    if repeat!=0:             
        
        for l in range(L):
         
            qc.crx(theta[count],2,1)
            count=count+1 
            qc.crx(theta[count],1,0)
            count=count+1                  
            qc.crx(theta[count],0,3)
            count=count+1 
        
            qc.crx(theta[count],3,2)
            count=count+1         
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1    

            qc.crx(theta[count],0,1)
            count=count+1           
            
            qc.crx(theta[count],1,2)
            count=count+1         
            qc.crx(theta[count],2,3)
            count=count+1 
        
            qc.crx(theta[count],3,0)
            count=count+1         
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1
            
            
    return qc



def circuit15(qc,theta,L,repeat):
    #circuit 15
    #theta is list of the parameters
    #theta length is (8)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1

        qc.cx(3,0)

        qc.cx(2,3)

        qc.cx(1,2)

        qc.cx(0,1)





        
        for i in range(4):
            qc.ry(theta[count],i)
            count=count+1    


        qc.cx(3,2)

        qc.cx(0,3)

        qc.cx(1,0)

        qc.cx(2,1)
            
    if repeat!=0:             
        
        for l in range(L):
         
            qc.cx(2,1)

            qc.cx(1,0)
              
            qc.cx(0,3)

        
            qc.cx(3,2)
      
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1    

            qc.cx(0,1)
             
            qc.cx(1,2)
      
            qc.cx(2,3)

        
            qc.cx(3,0)
     
        
            for i in range(4):
                qc.ry(theta[count],i)
                count=count+1
            
            
    return qc




def circuit16(qc,theta,L,repeat):
    #circuit 16
    #theta is list of the parameters
    #theta length is (11)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):
        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1
    

        qc.crz(theta[count],1,0)
        count=count+1
        qc.crz(theta[count],3,2)
        count=count+1
        qc.crz(theta[count],2,1)
        count=count+1
            
    if repeat!=0:             
        
        for l in range(L):
         

            qc.crz(theta[count],2,1)
            count=count+1            
            qc.crz(theta[count],3,2)
            count=count+1
            qc.crz(theta[count],1,0)
            count=count+1

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1

    return qc


    
def circuit17(qc,theta,L,repeat):
    #circuit 17
    #theta is list of the parameters
    #theta length is (11)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):
        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1
    

        qc.crx(theta[count],1,0)
        count=count+1
        qc.crx(theta[count],3,2)
        count=count+1
        qc.crx(theta[count],2,1)
        count=count+1
            
    if repeat!=0:             
        
        for l in range(L):
         

            qc.crx(theta[count],2,1)
            count=count+1            
            qc.crx(theta[count],3,2)
            count=count+1
            qc.crx(theta[count],1,0)
            count=count+1

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1

    return qc







def circuit18(qc,theta,L,repeat):
    #circuit 18
    #theta is list of the parameters
    #theta length is (12)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1
    


        qc.crz(theta[count],3,0)
        count=count+1
        qc.crz(theta[count],2,3)
        count=count+1
        qc.crz(theta[count],1,2)
        count=count+1
        qc.crz(theta[count],0,1)
        count=count+1
            
    if repeat!=0:             
        
        for l in range(L):
         

            qc.crz(theta[count],0,1)
            count=count+1          
            qc.crz(theta[count],1,2)
            count=count+1
            qc.crz(theta[count],2,3)
            count=count+1

            qc.crz(theta[count],3,0)
            count=count+1       

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1

    return qc



def circuit19(qc,theta,L,repeat):
    #circuit 1
    #theta is list of the parameters
    #theta length is (12)L
    #L is the number of repeatation
    
    # repeat will conjugate the first part and add next the the circuit for expressibility
    # 0:No, 1: Repeat    

    count=0

    for l in range(L):

        for i in range(4):
            qc.rx(theta[count],i)
            count=count+1
    
        for i in range(4):
            qc.rz(theta[count],i)
            count=count+1
    


        qc.crx(theta[count],3,0)
        count=count+1
        qc.crx(theta[count],2,3)
        count=count+1
        qc.crx(theta[count],1,2)
        count=count+1
        qc.crx(theta[count],0,1)
        count=count+1
            
    if repeat!=0:             
        
        for l in range(L):
         

            qc.crx(theta[count],0,1)
            count=count+1          
            qc.crx(theta[count],1,2)
            count=count+1
            qc.crx(theta[count],2,3)
            count=count+1

            qc.crx(theta[count],3,0)
            count=count+1       

            for i in range(4):
                qc.rz(theta[count],i)
                count=count+1
            for i in range(4):
                qc.rx(theta[count],i)
                count=count+1

    return qc