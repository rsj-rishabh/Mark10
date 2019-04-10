x = [[1,1], [-1,1], [1,-1], [-1,-1]]
t = [1, -1, -1, -1]


def yin(x, w1, w2, b):
    yin = b + x[0]*w1 + x[1]*w2
    
    return yin


def activate(ip):
    if ip>=0:
        return 1
    else:
        return 0


def calc_z(x, w1, w2, b):
    z = []
    zin = []
    zin.append( yin(x, w1[0], w2[0], b[0]) )
    zin.append( yin(x, w1[1], w2[1], b[1]) )
    z.append( activate(zin[0]) )
    z.append( activate(zin[1]) )
        
    return z,zin


def update_weights(w1, w2, b, x, a, t, z):
    w1 = round( w1 + (a * x[0] * (t-z)) , 4)
    w2 = round( w2 + (a * x[1] * (t-z)) , 4)
    b = round( b + (a * (t-z)) , 4)
    
    return w1,w2,b

def madaline_learn(x, Y, alpha, iterations):
    #configuration of adaline layer
    w1=[0.05, 0.1]
    w2=[0.2, 0.2]
    b_ad=[0.3, 0.15]
    
    #configuration of madaline layer
    v=[0.5, 0.5]
    b_mad=0.5
    
    print('\nInitial weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b_ad)+'\n')
    print('Training model for '+str(iterations)+' iterations...\n')
    for j in range(0, iterations):
        print('Iteration '+str(j+1)+'\n')
        for i in range(0, len(x)):
            z, zin = calc_z(x[i], w1, w2, b_ad)
            y = activate( yin(z, v[0], v[1], b_mad) )
            if y!=t[i]:
                
                #if t is +1, update weights for which zin is closest to zero
                if t[i]==1:
                    if abs(zin[0])<abs(zin[1]):
                        w1[0], w2[0], b_ad[0] = update_weights(w1[0],w2[0],b_ad[0],x[i],alpha,1,zin[0])
                    elif abs(zin[0])>abs(zin[1]):
                        w1[1], w2[1], b_ad[1] = update_weights(w1[1],w2[1],b_ad[1],x[i],alpha,1,zin[1])
                    else:
                        w1[0], w2[0], b_ad[0] = update_weights(w1[0],w2[0],b_ad[0],x[i],alpha,1,zin[0])
                        w1[1], w2[1], b_ad[1] = update_weights(w1[1],w2[1],b_ad[1],x[i],alpha,1,zin[1])
                
                #if t is -1, update weights for which zin is postive
                elif t[i]==-1:
                    if zin[0]>0:
                        w1[0], w2[0], b_ad[0] = update_weights(w1[0],w2[0],b_ad[0],x[i],alpha,-1,zin[0])
                    if zin[1]>0:
                        w1[1], w2[1], b_ad[1] = update_weights(w1[1],w2[1],b_ad[1],x[i],alpha,-1,zin[1])
                
                print('Updating weights: w1='+str(w1)+' w2='+str(w2)+' b='+str(b_ad)+'\n')
        j = j+1
    
    return w1,w2,b_ad
    

print('Input set is: ',x)
print('Target set is: ',t)
print('Training perceptron with weights w1 and w2 with tolerance 0.9')
w1, w2, b = madaline_learn(x,t,0.1,3)
print('\nTraining complete.')
print('Final Weights are: w1='+str(w1)+' w2='+str(w2)+' b='+str(b))
