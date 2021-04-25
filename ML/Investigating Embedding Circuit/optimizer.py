import numpy as np

def SPSA_gradient(loss, currentParams, gradientCoefficient):
    r'''Computes an estimator of the gradient using the procedure
    described in the SPSA algorithm.
    
    Inputs:
        loss: The loss function
        currentParams: The current value for the parameters
        gradientCoefficient: The coefficient c_n, which controls how much the current parameters are
                                               perturbed when computing the gradient
    
    Returns:
        gradient: The SPSA-based gradient of the loss function at currentParams'''
    
    numParams = len(currentParams)
    # Generate a random perturbation using the Rademacher distribution
    randomPerturbation = 2*np.random.binomial(1, .5, size=numParams) - 1
    
    gradient = (loss(currentParams + gradientCoefficient*randomPerturbation) - loss(currentParams - gradientCoefficient*randomPerturbation))\
                        /(gradientCoefficient*randomPerturbation)
    
    return gradient

def SPSA_update(loss, currentParams, updateCoefficient, gradientCoefficient):
    r'''Performs a parameter update according to the SPSA approach.
    
    NOTE: This function isn't aware of the notion of iterations, or anything of that sort.
    
    Inputs:
        loss: The loss function
        currentParams: The current value for the parameters
        updateCoefficient: The coefficient a_n, which controls how the current parameters are updated
                                            when including the gradient
        gradientCoefficient: The coefficient c_n, which controls how much the current parameters are
                                               perturbed when computing the gradient

    Returns:
        The updated parameter values'''
    
    grad = SPSA_gradient(loss, currentParams, gradientCoefficient)
    
    return currentParams - updateCoefficient*grad
