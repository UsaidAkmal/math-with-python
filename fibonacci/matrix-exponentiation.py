# UNTUK INPUT YANG LEBIH BESAR LAGI ITERATI DAN MEMOIZATION SAJA TIDAK CUKUP,DAN BISA MENJADI LAMBAT. dalam kasus inputan yang jauh jauh llebih besar kita dapat melakukan pendekatan matematika yang jauh jauh lebih canggih yang menggunakan pemangkatan matriks.

# Dalam dunia komputasi, efisiensi adalah segalanya. Kita bisa menulis algoritma Fibonacci dengan cara naïf (rekursif biasa), lalu meningkat ke iteratif atau memakai memoization (top-down dengan cache). Tapi, saat kita ingin menghitung Fibonacci ke-1.000.000, bahkan pendekatan tersebut akan kelimpungan. Di sinilah pemangkatan matriks (matrix exponentiation) masuk sebagai senjata pamungkas dari dunia matematika diskret (adalah displin ilmu matematika yang membahas objek2 terpisah atau diskrit) dan aljabar linear (cabang matematika yang fokus pada mempelajari sistem persamaan linear, vektor, matriks, dan transformasi linear) untuk menyelamatkan waktu komputasi secara drastis.

# APA ITU PEMANGKATAN MATRIKS ?

# pemangkatan matriks merupakan sebuah perkalian matriks menggunakan bilangan berpangkat, yang dimana matriks tersebut jumlah barisnya sama dengan jumlah kolomnya, atau yang di sebut dengan MATRIKS KUADRAT. yang natinya matriks kuadrat tersebut akan dikalikan dengan dirinya sendiri dengan rasio bilangan pangkatnya.

# Contoh :

# A = [1 2]
#     [3 4]

# hitungalah metriks A pangkat 2 (A²):

# maka [1 2] akan dikalikan dengan [1 2]
#      [3 4] akan dikalikan dengan [3 4]

# Baris pertama × kolom pertama: [1 2] * [1]
#                                        [3] maka : 1 * 1 + 2 * 3 = 1 + 6 = [7]

# Baris pertama x kolom kedua: [1 2] * [2]
#                                      [4] maka : 1 * 2 + 2 * 4 = 2 + 8 = [10]

# Baris kedua x kolom pertama: [3 4] * [1]
#                                      [3] maka : 3 * 1 + 4 * 3 = 3 + 12 = [15] 

# Baris kedua x kolom kedua : [3 4] * [2]
#                                     [4] maka : 3 * 2 + 4 * 4 = 6 + 16 = [22]

# Setelah kita melakukan perkalian matriks berpangkat ini, kita sudah mengetahui bilangan apa saja yang menjadi hasil dari perkalian matriks ini, yaitu 7, 10, 15, 22, maka matriks yang akan di hasilkan adalah 

# baris pertama berada di baris pertama hasil
# dan baris kedua berada di baris kedua hasil

# [7  10] hasil dari perhitungan baris pertama 7 dan 10.
# [15 22] hasil dari perhitungan baris kedua, yaitu 15 dan 22.

# maka hasil dari matriks A pangkat 2 adalah [7  10]
#                                            [15 22]
 
# penjelasan singkatnya adalah setiap elemen baris dari matriks pertama dengan elemen kolom dari matriks kedua.

# mulanya kita akan mendefinsikan fungsinya terlebih dahulu.
 
def fibonacci_matrix(n) :
     
     # lalu selanjutnya kita akan membuat base case untuk menjadi dasar dari algoritma atau alur dari kode kita .
     
     if n == 0: # jika n sama dengan 0, maka
         return 0 # kembalikan nilai 0
         
     # sebelum sebuah matriks atau kombinasi bilangan dalam satu variabel ini dapat digunakan dalam kode kita, kita harus dan wajib untuk melakukan inisialisasi agar tidak terjadi infinity loops yang akan sangat merusak.
     
     # APA YANG DIMAKSUD DENGAN INISIALISASI MATRIKS ?
     
     # inisialisasi matriks merupakan proses pendefinisian sebuah nilai yang ada di dalam matriks, layaknya array, matriks juga perlu di definisikan menggunakan nilai terlebih dahulu, tentu nilainya lebih dari satu ya, dan nilainya berupa variabel, angka, fungsi, boolean.
     
     # matriks dalam bahasa pemrograman python nilainnya akan diwakilkan menggunakan array 2 dimensi, mengapa haru array 2 dimensi?, karena Matriks itu pada dasarnya adalah kumpulan elemen (angka, bilangan kompleks, simbol, dsb) yang disusun dalam baris dan kolom.
     
     # dan konsep array  dimensi lah yang mewakilkan sifat matriks dalam pemrograman, matriks adalah array yang tersusun didalam variabel, yang berjumlah baris dan kolom.
     
     # mengapa bukan array 1 dimensi atau 3 dimensi saja?, array 1 dimensi hanya mampu menampung nilai yang berderet linear, sedangkan array 3 dimensi,memiliki dimensi yang terlalu banyak, yaitu 3 sedangkan matriks hanya memerlukan 2 dimensi untuk dapat menjalankan operasi matematikanya.
     
     # FUNGSI INISIALISASI MATRIKS :
    
     # menentukan ukuran matriks.
     # memberikan nilai awal ke setiap elemen.
     # membentuk struktur kosong (matriks nol) untuk nantinya akan di isi dengan bilangan yang kita inginkan.

     # selanjutnya kita akan membuat inisialisasi matriks yang akan kita gunakan untuk operasi hhitung fibonacci ini. lets started!

     F = [[1, 1],
          [1, 0]] # disini saya menginisialisasikan sebuah matriks bernama F.
     # nilai matriks F adalah:
     #    [1, 1]
     #    [1, 0] ini adalah nilai inisialisasi awal dari matriks F.

     # matriks F ini nantinya akan berfungsi untuk menjadi transformasi dasar(matriks dasar), atau perubahan awal. dalam kode kita, matriks ini adalah representasi dari hubungan F(n)=F(n−1)+F(n−2) dalam fibonacci.

     # yang artinya kita bisa menghitung angka Fibonacci ke-n jauh lebih cepat daripada menggunakan metode rekursi biasa.

     # mengapa hal itu bisa terjadi? 

     # berikut adlah perbandingan Metode yang kita gunakan mulai dari rekursi, iterasi, dan matriks:

# Fungsi Fibonacci didefinisikan sebagai F(n) = F(n-1) + F(n-2) dengan F(0) = 0 dan F(1) = 1

# REKURSI |
# Pendekatan rekursif naif menghitung F(n) dengan memanggil F(n-1) dan F(n-2), yang masing-masing memanggil dua fungsi lagi, dan seterusnya. Ini menciptakan pohon rekursi dengan jumlah node yang tumbuh secara eksponensial. Untuk n=1000, jumlah operasi yang diperlukan melebihi jumlah atom di alam semesta, jelas tidak feasible.Jika dihitung secara rekursif langsung, untuk mendapatkan F(1000) komputer harus:
# 
# Menghitung F(999) dan F(998)
# Untuk menghitung F(999), perlu F(998) dan F(997)
# Proses itu akan berulang hngga dasra F(0) dan F(1)
# ini akan menghasilkan pohon rekursi dengan sekitar 2 pangkat 1000 operasi, ini akan mengakibatkan proses komputasi akan meningkat secara drastis.


# ITERASI |
# Pendekatan iteratif dengan menyimpan dua nilai terakhir memiliki kompleksitas O(n), sudah lebih baik tetapi masih memerlukan 1000 iterasi untuk F(1000).
# Kompleksitas: O(n)
# 
# Penjelasan:
# Dilakukan tepat n-1 iterasi untuk menghitung F(n)
# Setiap iterasi melakukan operasi O(1) (penjumlahan dan penugasan)
# Total operasi: n-1 → O(n)
          
# MATRIKS |
#  Ketika kita mendengar kata "Fibonacci", yang terlintas di pikiran biasanya adalah sebuah barisan angka yang dimulai dari 0 dan 1, lalu setiap angka setelahnya merupakan penjumlahan dari dua angka sebelumnya:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ... dan seterusnya.