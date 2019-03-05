x = [[1,1], [-1,1], [1,-1], [-1,-1]]
t = [1, -1, -1, -1]

def activate(ynet):
    if ynet>0:
        return 1
    elif ynet==0:
        return 0
    else:
        return -1

def output(x, w1, w2, b):
    ynet = b + x[0]*w1 + x[1]*w2
    return activate(ynet)

def check(x, w1, w2, b):
    for i in range(0,len(x)):
        Y = output(x[i],w1,w2,b)
        if Y!=t[i]:
            return False
        else:
            print('Finalizing weights: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
    print('\nThe model is now stable.\n')
    return True

def perceptron_learn(x, Y, alpha):
    w1=0
    w2=0
    b=0
    i=0
    print('\nInitial weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
    while(i<len(x)):
        print('Updating weights: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
        Y = output(x[i], w1, w2, b)
        if Y==t[i] and check(x,w1,w2,b):
            break
        else:
            w1 = w1 + (alpha * x[i][0] * t[i])
            w2 = w2 + (alpha * x[i][1] * t[i])
            b = b + t[i]
            if i==len(x)-1:
                i = 0
        i+=1
    
    return w1,w2,b
    
print('Input set is: ',x)
print('Target set is: ',t)
print('Training perceptron with weights w1 and w2...')
w1, w2, b = perceptron_learn(x, t, 1)
print('Final Weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
