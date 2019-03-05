import time

x = [[1,1], [-1,1], [1,-1], [-1,-1]]
Y = [1, -1, -1, -1]

def hebb_learn(x, Y):
    w1=0
    w2=0
    b=0
    print('\nInitial weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
    for i in range(0,len(x)):
        w1 = w1 + (x[i][0]*Y[i])
        w2 = w2 + (x[i][1]*Y[i])
        b = b + Y[i]
        print('Updating weights: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
    return w1,w2,b
    
print('Input set is: ',x)
print('Output set is: ',Y)
print('Training neural net with weights w1 and w2...')
w1, w2, b = hebb_learn(x, Y)
print('\nTraining complete!\n')
print('Final weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
