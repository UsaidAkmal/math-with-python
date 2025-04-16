# SIMPLE IMPLEMENTATION FIBONACCI TEOREMA WITH MY SNAKE AKA Python

# 1. Pendekatan Rekursif Sederhana

# Pendekatan paling langsung adalah mengikuti definisi rekursif ( apa itu rekursif ? rekursif merupakan sebuah pengulangan diri sendiri, Menggunakan struktur pemilihan ) dari deret Fibonacci:

# 

def fibonacci_recursive(n): # mendefinisikan fungsi yang akan di gunakan dan di buat yaitu fibonacci_recursive.

    # membuat kasus dasar untuk pengaplikasian rekursif, tanpa kasus dasar maka rekrusif akan melakukan infinity loop karena tidak memiliki defnisi kasus dasar yang jelas.

    # memulai logika 
    if n == 0: # jika nilai n adalah nol, maka kembalikan nilai nol
        return 0
    # membuat percabangan logika menggunakan elif
    elif n == 1: # namun jika n adalah satu, maka kembalikan nilai 1
        return 1 
    
    # kali ini kita akan mendefinisikannya dimulai dengan angka nol dan satu, atau dari angka nol ke angka satu (tanpa definisi ini komputer tidak akan tau kapan ia harus berhenti), untuk menghindari dan mencegah infinity loop yang tidak di inginkan.

    # kasus rekursif: menjumlahkan duangka yang sudah di definisikan pada base case yaitu 0 dan 1

    else: # atau kembalikan nilai fungsi utama (fibonacci_recursive) dengan penjumlahan dua angka sebelumnya

        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) # n-1 (mengurangi 1 dari bilangan "n") dan n-2 adalah (mengurangi 2 dari bilangan n)
    
    # setelah menulis fungsinya selanjutnya kita akan menampilkan deret fibonacci yang sudah dibuat dengan metode rekursif dengan menggunakan for dan print 

for i in range(40): # untuk variabel i dengan deret 1 - 10 
    print(fibonacci_recursive(i), end=" ") # tampilkan hasil dari fungsi utama dengan  deret 1-10 berupa deret fibonacci.
    
# kekurangan dari pendekatan atau metode ini adalah ketika nilai (n) yang di input terlalu besar maka, akan terjaid proses komputasi yang sangat meningkat secara eksponesial (berpangkat) karena setiap pemanggilan rekursif menghasilkan dua pemanggilan rekursif baru, dan banyak perhitungan duplikat dilakukan.