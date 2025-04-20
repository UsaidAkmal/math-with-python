print ('''
       


        .----..-..----.  .----. .-. .-.  .--.   .---.  .---. .-.
        | {_  | || {}  }/  {}  \|  `| | / {} \ /  ___}/  ___}| |
        | |   | || {}  }\      /| |\  |/  /\  \\     }\     }| |
        `-'   `-'`----'  `----' `-' `-'`-'  `-' `---'  `---' `-'
        
        - example,how god communicate with human in the world.
        - base case, and memoization dictionary for optimize.

       ''')

# USING MEMOIZATION TO OPTIMIZE CALCULATION ON THE FIBONACCI SEQUANCE

# kita akan menghitung deret fibonacci dengan memanfaatkan hasil dari perhitungan sebelumnya. tentu dengan tujuan untuk optimalisasi proses komputasi dan perhitungan yang akan di lakukan oleh komputer kita.


# kelemahan deret fibonacci pada python.

# untuk menghitung deret fibonacci dengan akurat python memerlukan kompleksitas waktu O(2^n) yang membuatnya menjadi sangat kurang optimal ketika dijalankan dengan range atau deret yang besar.


    # MEMOIZATION 

    # memoization atau memoisasi merupakan sebuah teknik optimasi dalam pemrograman yang tujuannya adalah menyimpan proses atau hasil dari perhitungan dua angka sebelumnya pada sistem perhitungan  deret fibonacci, untuk nantinya akan digunakan secara terus menerus pada f(n), hingga mencapai range yang di tentukan.

# fungsi utama : Teknik ini digunakan untuk mengoptimalkan perhitungan nilai Fibonacci yang berulang, mengurangi jumlah perhitungan yang tidak perlu dan meningkatkan efisiensi program.

# gas kita ngoding 

# awal kita akan melakukan definisi fungsi beserta dengan argumen
def fibonacci_memo(n, memo={}): # fungsi utama yang akan kita mainkan adalah fibonacci_memo dengan menggunakan tipe data yang menyimpan data dalam bentuk pasangan kunci-nilai(dictionary) yaitu memo. dengan menyertakan bilangan n yang nantinya akan kita isi dengan menggunakan deret fibonacci yang akan kita hitung.

    # Nilai default memo={} adalah dictionary kosong. Pada pemanggilan pertama fungsi, jika tidak ada nilai untuk memo, maka Python akan menggunakan dictionary kosong sebagai nilai default. Ini sangat berguna karena dictionary memungkinkan kita untuk menyimpan hasil-hasil yang sudah dihitung sebelumnya, yang akan digunakan kembali ketika dibutuhkan tanpa perlu menghitung ulang.

# lanjut kita akan memeriksa apakah ada nilai n yang sudah dihitung sebelumnya dan telah di simpan kedalam memo{}.
    if n in memo: # jika n sudah pernah dihitung dan di simpan kedalam memo,maka
        return memo[n] # kembalikan nilai n yang berada didalam memo, menggunakan hasil n yang telah disimpan.
    
    # Teori Memoisasi: Teknik memoization adalah suatu bentuk optimasi yang digunakan untuk menyimpan hasil perhitungan fungsi agar tidak dihitung berulang kali. Ini adalah bagian dari teknik dynamic programming, yang berfokus pada menyelesaikan masalah dengan cara memecah masalah menjadi sub-masalah yang lebih kecil dan menyimpan hasilnya untuk digunakan kembali di masa depan. Dengan cara ini, kita menghindari kalkulasi yang redundant dan dapat mempercepat proses eksekusi.

# lalu seperti biasa kita akan membuat kasus dasar atau base case untuk menjadi dasar dari fungsi yang akan dijalankan. pada kasus rekrusif kita akan selalu menggunakan metode base case seperti ini untuk menghindari kasus infinity loop yang akan terjadi ketika menjalankan fungsi.

    # apalagi untuk fungsi berulang seperti deret fibonacci.dia akan melakukan fungsi yang sama berulang ullang jika tidak ada kasus dara atau base case maka program dan algoritma akan terus berjalan dengan tanpa henti.

# kasus dasar nya pun sama dengan kasus basic recursive sebelumnya,yaitu mendefinisikan n yang berupa 0 dan 1 pada awal perhitungan.

# memulai logika 
    if n == 0: # jika nilai n adalah nol, maka kembalikan nilai nol
        return 0 
    # membuat percabangan logika menggunakan elif
    elif n == 1: # namun jika n adalah satu, maka kembalikan nilai 1
        return 1
    
    # mengapa 0 dan 1? karena deret fibonacci menggunakan konsep angka 0 dari india sebagai salah satu patokan utama untuk memulai perhitungan, dengan mendefinisikannya dimulai dengan angka nol dan satu maka python akan memulai perhitungan dimulai dari 0 + 1, atau dari angka nol ke angka satu, tanpa definisi ini komputer tidak akan tau kapan ia harus berhenti, untuk menghindari dan mencegah infinity loop yang tidak di inginkan.

# Teori Kasus Dasar: Kasus dasar adalah kondisi yang menghentikan rekursi dalam fungsi rekursif. Untuk deret Fibonacci, kita tahu bahwa nilai pada urutan ke-0 adalah 0 dan nilai pada urutan ke-1 adalah 1. Kasus dasar ini digunakan untuk menghindari rekursi tanpa henti (infinite recursion).

# selanjutnya kita akan langsung melakukan operasi perhitungan atau yang akan kita sebut dengan algoritma utama yang akan menghitung deret fibonacci dengan menggunakan fungsi yang telah di optimalkan menggunakan memoisasi.

# Pada baris ini, kita menghitung nilai Fibonacci untuk n dengan cara rekursif yang sudah disertakan dengan dictionary memoization.
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo) # hitunglah nilai dengan menggunakan prinsip yang sama  dengan dasar rekursif namun setelah mendapatkan hasilnya simpanlah kedalam memo,lalu kembalikan nilai memo yang telah di simpan.

    # Fungsi ini memanggil dirinya sendiri untuk menghitung dua nilai sebelumnya dalam deret Fibonacci, yaitu fibonacci_memo(n-1, memo) dan fibonacci_memo(n-2, memo).

    # Hasil dari kedua pemanggilan ini dijumlahkan untuk mendapatkan nilai Fibonacci pada urutan n.

    # Setelah hasil perhitungan didapatkan, nilai tersebut disimpan dalam dictionary memo dengan kunci n, agar bisa digunakan kembali jika diperlukan di masa depan.

    # Teori Rekursi: Rekursi adalah teknik pemrograman di mana fungsi memanggil dirinya sendiri untuk menyelesaikan masalah. Pada deret Fibonacci, kita menghitung setiap nilai dengan menjumlahkan dua nilai sebelumnya, dan proses ini secara alami bisa dipecah menjadi sub-masalah yang lebih kecil. Fungsi akan terus memanggil dirinya sendiri sampai mencapai kasus dasar. Rekursi memudahkan implementasi algoritma ini, meskipun tanpa optimasi memoization, ini akan mengarah pada perhitungan yang berulang.
    return memo[n]

# setelah mendapatkan hasilnya kita akan memeanggil fungsi utama yang didalamnya telah menyimpan hasil dengan variabel n kemudian yang nantinya akan dicetak menggunakan print dengan range atau deret yang telah di tentukan.
for i in range(10): # untuk variabel i dalam deret 0-10
    print(fibonacci_memo(i), end=" ") # cetak lah fungsi fibonacci_memo dengan deret dari range variabel i, lalu akhiri.

# DONE BANG. 


