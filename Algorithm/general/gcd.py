# -*- coding: utf-8 -*-
##经典gcd求最大公约数
import sys  

def gcd(a,b):  
    if a%b == 0:  
        return b  
    else :  
        return gcd(b,a%b)  
  
a = input()  
n , m = a.split(' ')  
n = int(n)  
m = int(m)  
print(gcd(n,m)) 

