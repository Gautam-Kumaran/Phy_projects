from numpy import *
from math import *
A = array([[6,1,0],[1,8,2],[0,2,9]],float)
n = len(A)
c = []
d = []

for i in range(0,n):
    for j in range (0,n):
        if i==j:
           d.append(A[i,j])
        if i<j and A[i,j]!=0:
            c.append(A[i,j])

C = array([c],float).reshape(len(c),1)
D = array([d],float).reshape(len(d),1)
p = ones((n),float)

def sturm(lam):
    
    n = len(D) + 1
    p = ones((n),float)
    p[1] = D[0] - lam
    for i in range(2,n):
        p[i] = (D[i-1] - lam)*p[i-1] - (C[i-2]**2)*p[i-2]

    n = len(p)
    sign = 1
    count = 0
    for i in range(n):
        if p[i] > 0.0: signcheck = 1
        elif p[i] < 0.0: signcheck = -1
        else: signcheck = -sign
        if sign!=signcheck:
            count +=1
            sign = signcheck

    return(count)

tol = 0.1*10**-5

def counteigenvalue(lowerlim,upperlim):
    return sturm(upperlim)-sturm(lowerlim)

def FindEigenValue(guess1,guess2):
    if((guess2-guess1)<tol):
        print(guess1)        
        return None
    half = (guess1+guess2)/2
    firsthalfvalues = counteigenvalue(guess1, half) 
    secondhalfvalues = counteigenvalue(half, guess2)
    if firsthalfvalues>0:
        FindEigenValue(guess1, half)
    if secondhalfvalues>0:
        FindEigenValue(half, guess2)

def gerschgorin(a):
    aMINUSr = zeros(len(a),float)
    aPLUSr = zeros(len(a),float)
    r = zeros(len(A),float)
    for i in range(len(A)):
        for j in range(len(A)):
            if(i!=j):
                r[i] += A[i,j]
    r = abs(r)
    for i in range(len(a)):
        aMINUSr[i] = a[i]-r[i]
        aPLUSr[i] = a[i]+r[i]
    return min(aMINUSr),max(aPLUSr)

a,b = gerschgorin(D)
FindEigenValue(a,b)