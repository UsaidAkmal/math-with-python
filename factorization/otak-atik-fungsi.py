# menggunakan fungsi math untuk mengoptimalisasi input yang besar 

import math

n = 15

def find_factor(n):
    factor = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            factor.append(i)
    return factor


print(temukan_faktor(24))