def activate(yin, threshold):
    if yin>=threshold:
        return 1
    else:
        return 0
        
x1 = [[1,1], [0,1], [1,0], [0,0]]
x2 = [1,0]

def validate(w1, w2):
    if w1>0 and w2>0 and w1!=w2:
        return False
    else:
        return True

def check(w1, w2, threshold):
    if ((w1+w2)>=threshold) and (w1<threshold and w2<threshold):
            return 'AND'
    elif w1>=threshold and w2>=threshold and threshold>0:
            return 'OR'
    elif threshold<=0 and w1<threshold and w2<threshold:
            return 'NOT'
    else:
        return 'NONE'
        
                
w1 = int(input('Enter weight1 : '))
w2 = int(input('Enter weight2 : '))

if not validate(w1, w2):
    print('Invalid weights.')
else:
    threshold = int(input('Enter threshold : '))
    gate = check(w1, w2, threshold)
    print(gate+' gate implemented.')
    if gate=='AND' or gate=='OR':
        mul = [ [i[0]*w1, i[1]*w2] for i in x1]
        sigma = [i[0]+i[1] for i in mul]
        output = []
        for i in sigma:
            output.append(activate(i, threshold))
        print('Inputs : ',x1)
        print('Outputs : ',output)
    elif gate=='NOT':
        ynet = [ x2[0]*w1, x2[1]*w2 ]
        output = []
        for i in ynet:
            output.append(activate(i, threshold))
        print('Inputs : ',x2)
        print('Outputs : ',output)
    else:
        print('Weights and threshold are not compatible for implementation of any gate.')
