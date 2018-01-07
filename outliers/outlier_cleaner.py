#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    i = 0
    for age in ages:
        error = net_worths[i] - predictions[i]
        cleaned_data.append([age, net_worths[i], error])
        i += 1
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    
    return cleaned_data[9:]

