def bank(X, Y):
    Percent = 10  
    S = X * (1 + Percent / 100) ** Y 
    return S

X = 10000  
Y = 5      

print( str(Y)  + str(bank(X, Y)) )