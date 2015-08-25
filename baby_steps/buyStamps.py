# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(pence):
    five_pence = 0
    two_pence = 0
    one_pence = 0
    money_left = pence
    denominations = [5,2,1] #in case of dictionary {} list is read from the highest index first
    for d in denominations:
        if d == 5:
            (five_pence, money_left) = buy_stamp(money_left,d)
        if d == 2:
            (two_pence, money_left) = buy_stamp(money_left,d)
        if d == 1:
            (one_pence, money_left) = buy_stamp(money_left,d)
    return (five_pence, two_pence, one_pence)
    
def buy_stamp(money, denomination):
    return (money/denomination, money%denomination)

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps