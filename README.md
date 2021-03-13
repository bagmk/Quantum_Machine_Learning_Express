## Enhance Qiskit papers database & replication study

This project is a replication study of two papers [Expressibility and entangling capability of parameterized quantum circuits for hybrid quantum-classical algorithms, arXiv:1905.10876](https://arxiv.org/abs/1905.10876) and [Evaluation of Parameterized Quantum Circuits: on the relation between classification accuracy, expressibility and entangling capability, arXiv:2003.09887](https://arxiv.org/abs/2003.09887) using Qiskit environment. 

We refer to the first and second paper as Th20 and Sim19, respectively. TH20 studies the relationship between the expressibility of a parameterized quantum circuit (PQC) and the accuracy attained by a simple quantum classifier based on that circuit. Sim19 defined expressibility and entangling capability of parameterized quantum circuits for hybrid quantum-classical algorithms.

The key ideas in TH20 are:

- Defining a minimal embedding for 2-dimensional data (Figure 3) using 4 qubits
- Utilizing the PQCs of Sim19 as templates for doing classification (See Figure 2 of Sim19.)
- Defining a particular aggregation function (mapping from bitstrings to classification labels)
- Utilizing L1 and L2 loss to measure error in the classifier
- Looking at both Gradient Descent and Adam optimizers for optimizing the loss function
- Utilizing 9 particular datasets on which to evaluate the classifier (Figure 2).
- TH20 utilizes the data already present in Sim19 regarding the expressibility and entangling capability of PQCs. We can do the same here.

The end result of our study should be:

- A replication of Figure 4 of TH20 using the statevector simulator
- A study of the results of Figure 4 in the presents of finite-sampling (shot) noise
- A study of the results of Figure 4 utilizing simulation of noisy hardware
- ["Hero result"] Actually doing Figure 4 on hardware


## Timeframes
In terms of dates, I think this should be feasible:
- By late-March, the circuits and data sets are coded up.
- By the mid-term review, we have replicated Figure 1 using the QASM simulator.
- By mid-May, we have utilized noisy HW directly.

## Repository Organization
The repository should contain a few different pieces:
- A directory holding the data sets
- A file containing the circuits
- A directory for Jupyter notebooks
