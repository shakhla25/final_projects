import numpy as np

def get_after_market_values(a):
    """
    This function computes the values after the marketing strategy is applied. 
    Again, since this is a simulation similar to the ones in the simulations.py,
    I have not inluded the doctests here (as it would be pointless and repetitive to include it here.)
    
    Arguments:
    Input values array

    Returns:
    After marketing values array
    """
    a2 = [i for i in a]
    for i in range(len(a2)):
        temp = np.random.randint(0, 1000)
        a2[i] += temp
    return a2

def get_hypothesis_CTR(CTR):
    """
    The function below takes an input CTR 
    and converts the probabilities according to the 
    improved marketing strategy mentioned in the hypothesis.

    Arguments:
    CTR - Input CTR without marketing applied

    Returns:
    CTR - CTR with the marketing strategy applied
    """
    
    CTR.iloc[0, :] = 0.0
    CTR.iloc[0, 1] = 1.0
    return CTR

def printStats(revenue, bounceTotal, item1Total, item2Total, iterations):
    """
    This function takes in the statistics produced by the simulations and prints out the stats. 

    Arguments:
    All the stats produced by the simulations

    Returns:
    Nothing - Only prints that stats.
    """
    
    print("Average Revenue/user: ", np.mean(revenue)/iterations)
    print("Average Bounce Rate: ", np.mean(bounceTotal)/iterations)
    print("Average Item 1 Purchases: ", np.mean(item1Total)/iterations)
    print("Average Item 2 Purchases: ", np.mean(item2Total)/iterations)
    print ("")