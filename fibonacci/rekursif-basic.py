print ('''
       


        .----..-..----.  .----. .-. .-.  .--.   .---.  .---. .-.
        | {_  | || {}  }/  {}  \|  `| | / {} \ /  ___}/  ___}| |
        | |   | || {}  }\      /| |\  |/  /\  \\     }\     }| |
        `-'   `-'`----'  `----' `-' `-'`-'  `-' `---'  `---' `-'
        
        - example,how god communicate with human in the world.

       ''')

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
    
    # mengapa 0 dan 1? karena deret fibonacci menggunakan konsep angka 0 dari india sebagai salah satu patokan utama untuk memulai perhitungan, dengan mendefinisikannya dimulai dengan angka nol dan satu maka python akan memulai perhitungan dimulai dari 0 + 1, atau dari angka nol ke angka satu, tanpa definisi ini komputer tidak akan tau kapan ia harus berhenti, untuk menghindari dan mencegah infinity loop yang tidak di inginkan.

    # kasus rekursif: menjumlahkan dua angka yang sudah di definisikan pada base case yaitu 0 dan 1, yang kemudian nantinya akan digunakan sebagai f(n) pada perhitungan lanjutan dengan waktu eksponensial  O(2^n).

    # disclaimer waktu eksponensial O(2^n) merupakan waktu yang sangat tidak efisien untuk jumlah deret yang banyak,mengapa tidak efisien ?

    # sebelum kita mencap O(2^n) sebagai waktu eksponesial yang tidak efisien,kita juga harus memahami apa itu KOMPLEKSITAS WAKTU.

    # Kompleksitas waktu (time complexity) adalah cara untuk mengukur seberapa cepat atau lambat sebuah algoritma bekerja berdasarkan ukuran input.

    # mengapa input bisa memperlambat proses algoritma? karena setiap fungsi yang kita tulis dengan menggunakan kode pada hakikatnya akan melakukan proses perhitungan yang disebut dengan algoritma, bagaimana algoritma dapat bekerja? untuk algoritma dapat bekerja kita memerlukan yang namanya input atau suatu kondisi dimana nantinya akan memicu proses pada kode yang sudah kita tulis dengan menggunakan fungsi yang di dalamnya terdapat algoritma.

    # misalnya

    else: # atau kembalikan nilai fungsi utama (fibonacci_recursive) dengan penjumlahan dua angka sebelumnya

        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) # n-1 (mengurangi 1 dari bilangan "n") dan n-2 adalah (mengurangi 2 dari bilangan n)
    
    # setelah menulis fungsinya selanjutnya kita akan menampilkan deret fibonacci yang sudah dibuat dengan metode rekursif dengan menggunakan for dan print 

for i in range(10): # untuk variabel i dengan deret 1 - 10 
    print(fibonacci_recursive(i), end=" ") # tampilkan hasil dari fungsi utama dengan  deret 1-10 berupa deret fibonacci.
    
# kekurangan dari pendekatan atau metode ini adalah ketika nilai (n) yang di input terlalu besar maka, akan terjaid proses komputasi yang sangat meningkat secara eksponesial (berpangkat) karena setiap pemanggilan rekursif menghasilkan dua pemanggilan rekursif baru, dan banyak perhitungan duplikat dilakukan.