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
    data = []
    sorted_data = []
    ### your code goes here


    for i in range(len(predictions)):
        error = predictions[i] - net_worths[i]
        data.append((int(ages[i]), float(net_worths[i]), float(error)))
    sorted_data = sorted(data, key=lambda tup: tup[2])
    cleaned_data = sorted_data[0:81]
    # print len(cleaned_data)
    # print sorted_data
    return cleaned_data
