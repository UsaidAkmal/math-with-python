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

n = 15

# kita akan menulis baris baris python yang akan melakukan operasi Factorization ini, bismillah

def find_factor(n) : # merupakan sebuah fungsi untuk dapat menemukan faktor dari sebuah bilangan 
    factor = [] # merupakan sebuah array penampung bilangan faktor yang nantinya akan disimpan

    # kita akan mencari dari 1 sampai bilangan n (bilangan itu sendiri)
    for i in range (1, n + 1): # n + 1 digunakan untuk mendapatkan bilangan n secara utuh tidak dikurangi 1 (n-1) jika tidak menggunakan n+1 maka n akan dikurangi dengan 1 secra default

        # jika i habis membagi n maka nilai i akan disimpan kedalam variabel factor menggunakan fungsi append
        if n % i == 0:
            factor.append(i)
    return factor  # nilai variabel factor yang didapat dari operasi find_factor akan dikembalikan menggunakan fungsi return
print(find_factor(n)) # varibel find_factor(n) akan dicetak serta di tampilkan berdasarkan bilangan variabel n yang sudah di input.

# Penjelasan sederhana untuk kode di atas:

# Kita membuat fungsi bernama temukan_faktor yang menerima bilangan n

# Kita membuat daftar kosong bernama faktor untuk menyimpan semua faktor

# Kita mencoba semua bilangan dari 1 sampai n

# n % i == 0 artinya "apakah n dibagi i tidak ada sisa?". Jika tidak ada sisa, berarti i adalah faktor dari n

# Jika i adalah faktor, kita tambahkan ke daftar faktor

# Terakhir, kita mengembalikan daftar lengkap faktor-faktor tersebut

# Kode di atas akan menghasilkan: [1, 2, 3, 4, 6, 8, 12, 24] untuk n = 24