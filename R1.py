__author__ = 'rostik'

def f(a):
        m=[]
        A=a+1
        div=list(range(1,A))
        for x in div:
                if a%x==0:
                        m+=[x]
        return m

def F(*b):
        L=[]
        for x in b:
                L+=[f(x)]
        return L

def func(L):
        if len(L)==1:
                return L
        q=len(L)-1
        x=list(set(L[q])&set(L[q-1]))
        return func(L[:-2]+[x])

print(func(F(1024, 2048)))
