print('''

 |  ____|       | |           (_)        | | (_)            
 | |__ __ _  ___| |_ ___  _ __ _ ______ _| |_ _  ___  _ __  
 |  __/ _` |/ __| __/ _ \| '__| |_  / _` | __| |/ _ \| '_ \ 
 | | | (_| | (__| || (_) | |  | |/ / (_| | |_| | (_) | | | |
 |_|  \__,_|\___|\__\___/|_|  |_/___\__,_|\__|_|\___/|_| |_|
 
 the origin of a number 

''')

# hello my name is akmal this is my mini project for my experiences
# im from indonesia, Please forgive me if my English is not good. 

# WHAT'S THE NUMBER FACTORIZATION ?

# Bayang kan Faktorisasi seperti memecah coklat batangan menjadi kepingan coklat yang lebih keil
# faktorisasi hakikatnya adalah mecaru bilangan yang lebih kecil yang jika dikalikan akan menghasilkan bilangan aslinya

# EXAMPLE

# if 12 adalah bilangan genap maka berapa dikalikan berapa yang hasilnya adalah 12 ?

# 1 * 12 = 12
# 3 * 4 = 12     
# 2 * 6 = 12

# beberapa kombinasi angka di atas merupakan contoh dari operasi Faktorisasi
# seperti menemukan "bahan dasar" dari sebuah bilangan

# BILANGAN PRIMA DAN FAKTORISASI PRIMA
# Bilangan prima merupakaan bilangan ynag ISTIMEWA karena hanya bisa dibagi dengan dengan 1 dan dirinya sendiri. ( satu bukan merupakan bilanga prima karena hanya memiliki satu faktor yaitu dirinya sendiri )

# CONTOHNYA :

# 60 = 2*2*3*5 

# kita akan menulis baris baris python yang akan melakukan operasi Factorization ini, bismillah

def find_factor (n) : # merupakan sebuah fungsi untuk dapat menemukan faktor dari sebuah bilangan 
    factor = [] # merupakan sebuah array penampung bilangan faktor yang nantinya akan disimpan

    # kita akan mencari dari 1 sampai bilangan n (bilangan itu sendiri)  