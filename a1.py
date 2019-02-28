def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    busses_filled = n/50 #This should fill one bus
    '''A check will done to see if another bus will be needed for
    for a group of people under 50.
    '''
    if (n % 50) > 0:
        busses_filled += 1
    return busses_filled

def stock_price(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    gains = 0
    losses = 0
    for value in price_changes:
        if value > 0:
            gains += value
        else:
            losses += value
    return(gains, losses)

import itertools
        
def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    L.reverse()
    """Create sublists the length of k"""
    chunk = [L[x:x+k] for x in range(0, len(L), k)]
    #sort each sort list.
    for i in chunk:
        i.sort()
    #join sublists into one big list.
    merged = list(itertools.chain(*chunk))
    return merged
