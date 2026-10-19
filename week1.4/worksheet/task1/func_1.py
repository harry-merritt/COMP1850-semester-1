
def func_1(lst_value):
    '''
    Sums the digits in a number and returns the mean average.
    '''

    sum = 0
    num_of_value = len(lst_value)
    for value in lst_value:
        sum = sum + value
    return sum/num_of_value
