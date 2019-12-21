import numpy as np, pandas as pd

def generate_random_row(rowNumber):
    """
    This function takes in the row number, that is which row we want to generate the random numbers for. 
    Based on the row number, it generates the values of each column of the row. 
    For eg, the row representing the Item 1 and Item 2 pages should have a 0.15 value in the Purchase 1 and Purchase 2 pages respectively. 
    Also, this functions considers all the row based constrainsts before generating the random values. 
    Constraint 1: All values in the row sum to 1. 
    Constraint 2: The probablities of a user traversing from the item page to the purchase page is always 0.15 
    Constraint 3: All the random variables must be < 1

    Arguments:
    rowNumber: A random integer between 0 and 8

    Returns: 
    arr: An array with values signifying the row values.

    >>> generate_random_row(5)[-1]
    0.15

    >>> round(sum(generate_random_row(2)))
    1

    >>> len(generate_random_row(3))
    8

    """    
    arr = np.random.random([8]).tolist()
    arr[rowNumber], arr[-1], arr[-2] = 0.0, 0.0, 0.0
    
    s = sum(arr)
    arr = [(i/s) for i in arr]
    if rowNumber in [4, 5]:
        sub = 0.0
        while sub != 0.15:
            for i in range(len(arr)):
                if sub == 0.15: break
                if arr[i] < 0.01: continue
                else:
                    arr[i] -= 0.01
                    sub += 0.01
        arr[rowNumber + 2] = 0.15
    return arr

def generate_CTR():

    """
    This function calls the above generate_random_row function and concatenates the returned arrays
    to form a 2d array. 

    Arguments:
    None 

    Returns:
    A 2d matrix that signifies the internal probability values of the final CTR data frame. 

    >>> len(generate_CTR())
    8

    >>> len(generate_CTR()[0])
    8

    >>> round(sum(generate_CTR()[0]))
    1

    """

    CTR, temp = [], [0.0] * 8
    for row in range(6):
        curr_row = generate_random_row(row)
        CTR.append(curr_row)
    CTR.append(temp)
    CTR.append(temp)
    return CTR

def generate_CTR_dataFrame():
    """
    This function takes a 2d matrix from the generate_CTR() function and converts it to a dataframe for further use. 

    Arguments:
    None 

    Returns:
    A dataframe with the CTR values. 

    >>> len(generate_CTR_dataFrame()["FAQ"].values.tolist())
    8

    >>> sum(generate_CTR_dataFrame()["Purchase 1"].values.tolist())
    0.15

    >>> type(generate_CTR_dataFrame())
    <class 'pandas.core.frame.DataFrame'>
    """
    
    CTR = generate_CTR()
    cols = ["Internet", "Home", "FAQ", "Products", "Item 1", "Item 2", "Purchase 1", "Purchase 2"]
    df = pd.DataFrame(CTR, columns=cols, index=cols)
    return df
