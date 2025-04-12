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

def find_factor_optimized(n):
    factor = [] # adalah variabel yang menampung hasil fungsi berupa faktor yang sudah di temukan 

    # hanya merunut sampai akar kuadrat dari n
    for i in range(1, int(math.sqrt(n)) + 1):

        # jika i habis membagi n maka masukan menggunakan append kedalam var factor
        if n % i == 0:
            factor.append(i) # memasukan faktor kecil kedalam var factor

            # Menambahkan pasangan untuk setiap factor
            if i != n // i: # // adalah pembagian bilangan bulat, menghasilkan hasil pembagian tanpa desimal, n // i menghasilkan bilangan yang jika dikalikan dengan i, akan menghasilkan n.

                # kemudian kita akan memeriksa apakah i tidak sama (!=) dengan n // i untuk menghindari menambahkan faktor yang sama dua kali.

                # contoh untuk n-25, jika i adalah 5, maka n // i=5, karena 5=5, dan 5 akan dii simpan hanya sekali pada var factor.

                # setelah menemukan pasangan dari factor yang sudah kita input, selanjutnya kita akan menyimpannya kedalam var factor kembali, menggunakan append seperti factor pertamannya.
                factor.append(n // i)

        # Urutkan factor untuk out-put yang lebih rapih
        factor.sort()
    return factor # kembalikan nilai var factor, lalu cetak menggunakan print 


print(find_factor_optimized(n))


