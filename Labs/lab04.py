import doctest
##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    casc = []

    for i in lst:
        casc += [i]

    i = len(lst) - 1
    while i != -1:
        casc += [lst[i]]
        i -= 1

    return casc


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    maplist = []

    for i in seq:
        maplist += [fn(fn(i))]

    return maplist


# RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    filt = []

    for i in seq:
        if not pred(i):
            filt += [i]

    return filt


# RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    temp = list(range(0, n))    # source: https://stackoverflow.com/questions/18265935/python-create-list-with-numbers-between-2-values
    complist = []

    for i in temp:
        if pred(i):
            complist += [i]

    return complist

# RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.

    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    flats = []

    for i in lst:
        if type(i) != list:
            flats += [i]
        else:
            flats += flatten(i)

    return flats


if __name__ == "__main__":
    doctest.testmod(verbose=True)
