import numpy as np

def logistic_reader(coefficient):
    """Finds the % increase in probability based on coefficient (b). 
    Function logic == for each X unit increase, the probability of Y 
    happening increases by `exp(b) - 1 * 100`

    Args:
        coefficient (int or float): coefficient from logistic regression

    Returns:
        probability, message (float, str): probability of success and message
    """
    
    probability = round((np.exp(coefficient) - 1) * 100, 2) # exponential of coefficient - 1 to get odds ratio mult by 100 to get %
    
    message = None 
    
    if probability > 0: 
        message = f'The likelihood increases by {probability}%'
    
    elif probability == 0: 
        message = 'Probability is 0. The likelihood is not affected'
    
    else: 
        message = f'The likelihood decreases by {abs(probability)}%'
    
    return probability, message


if __name__ == '__main__':
    
    probability, message = logistic_reader(0.5)
    
    print(probability,type(probability) )
    print(message, type(message))