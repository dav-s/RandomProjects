def collatzRecur(curNum, count=0):
    '''This recursively solves the Collatz Conjecture'''
    if curNum<=1:#Base case
        return count
    if curNum%2==0:
        return collatzRecur(curNum/2, count+1)
    else:
        return collatzRecur(curNum*3+1, count+1)

#Some tests
print collatzRecur(2) #1
print collatzRecur(3) #7
print collatzRecur(4) #2
print collatzRecur(5) #5
print collatzRecur(6) #8
