# menggunakan library math dan fungsi math.sqrt untuk mengoptimalisasi input yang besar 

print('''

 |  ____|       | |           (_)        | | (_)            
 | |__ __ _  ___| |_ ___  _ __ _ ______ _| |_ _  ___  _ __  
 |  __/ _` |/ __| __/ _ \| '__| |_  / _` | __| |/ _ \| '_ \ 
 | | | (_| | (__| || (_) | |  | |/ / (_| | |_| | (_) | | | |
 |_|  \__,_|\___|\__\___/|_|  |_/___\__,_|\__|_|\___/|_| |_|
 
 the origin of a number 

''')

import math

n = 15

def find_factor(n):
    factor = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            factor.append(i)
    return factor


print(find_factor(24))


# BELUM KELAR MAU MADANG DULU AWOAKOWKA