## Lab 5: Required Questions - Dictionaries  ##
import random


# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    size = len(dict1) + len(dict2)
    counter = 1
    dict3 = {}
    while size != 0:
        if counter in dict1:
            dict3[counter] = dict1[counter]
        else:
            if counter in dict2:
                dict3[counter] = dict2[counter]
        counter += 1
        size -= 1

    return dict3

# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    words = message.split()
    dict1 = {}
    for word in words:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
    return dict1

# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for item in d:
        if d[item] == x:
            d[item] = y

# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    dict1 = {}
    for i in lst:
        for j in i:
            if j in dict1:
                dict1[j] += i[j]
            else:
                dict1[j] = i[j]
    return dict1

def build_successors_table(tokens):
    """Takes in a list of words or tokens. Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)

#RQ5
def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    tweets = []
    tweetsize = []
    for i in range(5):
        tweets.append(random_tweet(table))
        tweetsize.append(len(tweets[i]))
        print(f"{tweets[i]} - length: {tweetsize[i]}\n")

    from statistics import median               #https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
    return f"\n\nThe sentence with the median number of characters is:\n{tweets[tweetsize.index(median(tweetsize))]}" 


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

    shakestokens = shakespeare_tokens()
    shakestable = build_successors_table(shakestokens)
    print(middle_tweet(shakestable))
