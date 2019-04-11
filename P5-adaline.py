x = [[1,1], [-1,1], [1,-1], [-1,-1]]
t = [1, -1, -1, -1]


def yin(x, w1, w2, b):
    yin = b + x[0]*w1 + x[1]*w2
    
    return yin


def calc_error(w1,w2,b):
    error = 0
    for i in range(0, len(x)):
        yi = yin(x[i],w1,w2,b)
        e = (t[i]-yi)*(t[i]-yi)
        error = error + e
        
    return error


def adaline_learn(x, Y, alpha, tolerance):
    w1=0.1
    w2=0.1
    b=0.1
    sq_error = calc_error(w1,w2,b)
    print('Initiating sequence...')
    print('\nInitial weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b)+'\n')
    
    while(sq_error>=tolerance):
        for i in range(0, len(x)):
            y = yin(x[i], w1, w2, b)
            w1 = w1 + (alpha * x[i][0] * (t[i]-y))
            w2 = w1 + (alpha * x[i][1] * (t[i]-y))
            b = b + (alpha * (t[i]-y))
            sq_error = calc_error(w1,w2,b)
            print('Updating weights: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
        print('Error: '+str(sq_error)+'\n')
    
    print('Model is now under tolerance limit.')
    
    return w1,w2,b
    

print('Input set is: ',x)
print('Target set is: ',t)
print('Training perceptron with weights w1 and w2 with tolerance 0.9')
w1, w2, b = adaline_learn(x, t, 0.1, 1.9)
print('\nTraining complete.')
print('Final Weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
