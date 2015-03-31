from collections import Counter

#### Assumption, assertion : the code below runs in O(m+n) worst-case time complexity

def fix_machine(debris, product):
    
    debris_counter = Counter(debris)
    '''print debris_counter
    product_counter = Counter(product)
    print product_counter

    A Counter is a container that keeps track of how many times equivalent values are added.
    An empty Counter can be constructed with no arguments and populated via the update() method.

    import collections

    c = collections.Counter()
    print 'Initial :', c

    c.update('abcdaab')
    print 'Sequence:', c

    c.update({'a':1, 'd':5})
    print 'Dict    :', c

    The count values are increased based on the new data, rather than replaced. In this example, the count for a goes from 3 to 4.

    $ python collections_counter_update.py

    Initial : Counter()
    Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
    Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})


    '''

    for letter in product:
        if not debris_counter[letter]:
        # if debris_counter[letter] == 0, then letter doesnot exist in debris
            return "Give me something that's not useless next time."
    return product

    

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'