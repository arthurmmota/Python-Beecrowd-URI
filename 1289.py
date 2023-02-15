from math import  pow, comb
def Binomial(n,p, x):
    return round( (comb(n,x) * pow(p,x)* pow(1-p,(n-x))), 4)

print(Binomial(2,0.166666,1))