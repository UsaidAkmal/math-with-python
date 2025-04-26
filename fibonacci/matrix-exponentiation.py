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
#                                        [3] maka : 1 * 1 + 2 * 3 = 1 + 6 = 7

# Baris pertama x kolom kedua: [1 2] * [2]
#                                      [4] maka : 1 * 2 + 2 * 4 = 2 + 8 = 10

# Baris kedua x kolom pertama: [3 4] * [1]
#                                      [3] maka : 3 * 1 + 4 * 3 = 3 + 12 = 15 

# Baris kedua x kolom kedua : [3 4] * [2]
#                                     [4] maka : 3 * 2 + 4 * 4 = 6 + 16 = 22

# 

