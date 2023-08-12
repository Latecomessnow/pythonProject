def add(begin, end):
    theSum = 0
    for i in range(begin, end + 1):
        theSum += i
    # print(theSum)
    return theSum


result = add(1, 100)
print(result)

