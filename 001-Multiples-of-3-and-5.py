##############################################
#Thinking 1: The basic idea, an O(n) algorithm
res = 0
for i in range(1000):
    if i%3 == 0 or i%5==0:
        res += i
print(res)

###################################
#Thinking2: Using an O(1) algorithm
def muiltipleNum( multifier , below ):
    res = (below-1) // multifier
    return res

def sumOfMutiples( n , below ):
    return ( n + muiltipleNum( n , below )*n ) * muiltipleNum( n , below ) // 2

print( sumOfMutiples( 3 , 1000) + sumOfMutiples( 5 , 1000) - sumOfMutiples( 15 , 1000 ) )
