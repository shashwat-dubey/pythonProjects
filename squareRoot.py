def calcSquareRoot(num, epsilon):
    high = num
    low = 0
    for iteration in range(0, 100):
        iteration += 1
        ans = (high + low) / 2.0
        margin = (num - ans*ans)
        #print 'num', num, 'ans*ans', ans*ans, 'margin', margin
        if abs(margin) <= epsilon:
            print 'ans: ', ans, 'Iteration: ', iteration
            return
        else:
            if margin > 0:
                low = ans
            else:
                high = ans
    print 'ans: ', ans, 'Iteration: ', iteration

calcSquareRoot(2, 0.000000000000001)