# UNTUK MENGATASI PENINGKATAN KOMPUTASI YANG MENINGKAT SECARA EKSPONENSIAL YANG AKAN MEMAKAN BANYAK MEMMORY DAN CORE, MAKA KITA HARUS MENCARU SOLUSINYA.

# YAITU DENGAN MENGGUNAKAN PENDEKATAN ITERATIF / ITERASI
# dengan cara ini kita akan menggunakan iterasi sebagai langkah untuk menghindari komputasi yang berlebihan ketika proses perhitungan bejalan pada komputer.

# dengan menggunakan metode iterasi maka komplesitas waktu O(n) yang dibutuhkan akan meningkat secara linear dengan nilai n,Ini jauh lebih baik dibandingkan pendekatan rekursif yang memiliki kompleksitas waktu O(2^n).

# Iterasi pada kode ini berperan sebagai mekanisme utam untuk menghitung deret fibonacci tanpa menggunakan rekursi (atau tanpa mengulang diri sendiri).

# untuk melakukannya kita akan membuat variabel fungsi 

# membuat fungsi fibonacci_iteratif()
def fibonacci_iteratif(n): # mendefinisikan fungsi yang akan di buat
    
    # jika n adalah nol maka kembalikan nilai nol (ini dilakukan untuk memulai perhitungan di mulai dari angka nol, dan juga untuk memulai loop)
    if n == 0: # mengapa nol ? karena angka pertama dalam fibonacci adalah nol 
        return 0 # python pun akan melakukan perhitungan mula dari angka nol
    
    # melakukan ini sialisasi pada dua angka pertama yaitu 0 dan 1, mengapa hal ini penting dilakukan? karena 0 dan 1 dalam fibonacci merupakan suku utama atau dalam matematika disebut dengan (f0)=0 dan (f1)=1, yang nantinya f(0) akan dijumlahkan dengan f(1),yang akan menghasilkan veriabel f(2).

    # dan proses itu akan berulang hingga tak terhingga.

    a, b = 0, 1 # disini a dan b, a adalah f(0)=0 dan b adalah f(1)=1

    # mulai melakukan iterasi menggunakan f(1)=1 dan f(n-1) untuk 




