def membership(x, S):
    for e in S:
        if x==e[0]:
            return e[1]
    
    return 0 


def union(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        Z.append( [i[0], max(mb, i[1])] )
        if mb!=0:
            Y.remove([i[0],mb])
    Z = Z + Y
    
    return Z        


def intersection(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        if min(mb, i[1])!=0:
            Z.append( [i[0], min(mb, i[1])] )
            
    return Z


def complement(A):
    X = A.copy()
    for i in X:
        i[1] = 1-i[1]
        if i[1]==0:
            X.remove(i)
    
    return X
    
    
def fuzzy_sum(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        if mb!=0:
            m = round( i[1]+mb-(i[1]*mb), 3)
            Z.append( [i[0],m] )
            Y.remove([i[0],mb])
        else:
            Z.append(i)
    Z = Z + Y
    
    return Z
    
    
def fuzzy_product(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        if mb!=0:
            m = i[1]*mb
            Z.append( [i[0],m] )
            Y.remove([i[0],mb])
    
    return Z
    
    
def bounded_sum(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        if mb!=0:
            m = i[1]+mb
            Z.append( [i[0],min(1,m)] )
            Y.remove([i[0],mb])
        else:
            Z.append(i)
    Z = Z + Y
    
    return Z
    
    
def bounded_diff(A, B):
    X,Y = A.copy(),B.copy()
    Z = []
    for i in X:
        mb = membership(i[0],Y)
        if mb!=0:
            m = round( i[1]-mb, 3)
            Z.append( [i[0],max(0,m)] )
            Y.remove([i[0],mb])
        else:
            Z.append(i)
    
    return Z
    
    
A = [[1,0.6], [2,0.3], [3,1]]
B = [[1,0.3], [2,0.6], [4,0.1]]
print('Fuzzy set A is '+str(A))
print('Fuzzy set B is '+str(B)+'\n')
print('A union B is '+str( union(A,B) ))
print('A intersection B is '+str( intersection(A,B) ))
print('Complement of A is '+str( complement(A) ))
print('Algebraic sum of A and B is '+str( fuzzy_sum(A,B) ))
print('Algebraic product of A and B is '+str( fuzzy_product(A,B) ))
print('Bounded sum of A and B is '+str( bounded_sum(A,B) ))
print('Bounded difference of A and B is '+str( bounded_diff(A,B) ))
