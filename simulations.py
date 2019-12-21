import numpy as np, pandas as pd
import CTR

def simulate_single_user(ctr):  
    """
    The function below simulates the movements of a single user 
    and returns the final page of the user 
    (that is did the user purchase a product or leave the website).

    Arguments:
    CTR: The CTR dataframe obtained from the CTR.py module

    Returns:
    The revenue earned by the actions of a single user within the page. 
    This will be  either:
    0 (user purchases nothing) or 
    100 (user purchases item 1) or
    75 (user purchases item 2)

    Providing only one Doctest as that is enought to explain the given function.

    >>> CTR = CTR.generate_CTR_dataFrame()
    >>> a = simulate_single_user(CTR)
    >>> a in [0, 100, 75]
    True

    """
    
    
    pages, current_page, revenue = np.arange(8), 0, {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:100, 7:75}
    
    while True: 
        current_page = np.random.choice(pages, p=ctr.iloc[current_page].values.tolist())
        if (current_page == 0) or (current_page == 6) or (current_page == 7): break
    return revenue[current_page]

def simulate_iterations(iterations, ctr):
    """
    This funciton simulates the process for multiple users. 
    It makes use of the above function and calculates the stats based on that. 
    
    >>> ctr = CTR.generate_CTR_dataFrame()
    >>> a, b, c, d = simulate_iterations(100, ctr)
    >>> a == (100*c + 75*d)
    True

    >>> ctr2 = CTR.generate_CTR_dataFrame()
    >>> a2, b2, c2, d2 = simulate_iterations(100, ctr2)
    >>> b2 == 100 - c2 - d2
    True

    """
     

    cash, bounce, item1, item2 = 0.,  0., 0., 0.

    for _ in range(iterations):
        current = float(simulate_single_user(ctr))

        if current == 100: item1 += 1.
        elif current == 75: item2 += 1.
        else: bounce += 1
        cash += current

    return cash, bounce, item1, item2

def simulate_for_groups():
    """
    The function below uses the function above as skeleton and feeds in different iterations and CTR values.

    Arguments:
    None

    Returns:
    Revenue - Total revenue earned by the website for the simulation
    bounceTotal - Total number of people who left the website without purchasing anything
    item1Total - Total item1's bought
    item2Total - Total item2's bought

    Since this is exactly similar to the function above, I am not including doctests for it. 
    Because it is only a more compute intensive simulation of the one above. 

    """

    revenue, item1Total, item2Total, bounceTotal, groups, iterations = [], [], [], [], 1000, 1000
    ctr = CTR.generate_CTR_dataFrame()
    for i in range(groups):
        one, two, three, four = simulate_iterations(iterations, ctr)
        revenue, bounceTotal, item1Total, item2Total = revenue + [one],  bounceTotal + [two], item1Total + [three], item2Total + [four]
    return revenue, bounceTotal, item1Total, item2Total
