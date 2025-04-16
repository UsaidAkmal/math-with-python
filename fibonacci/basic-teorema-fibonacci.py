# SIMPLE IMPLEMENTATION FIBONACCI TEOREMA WITH MY SNAKE AKA Python

# Pendahuluan:

# Bayangkan Anda sedang berjalan di taman, mengamati kelopak bunga yang mekar dengan sempurna. Atau mungkin Anda memperhatikan pola spiral pada kerang laut. Tanpa Anda sadari, ada sebuah pola matematika kuno yang hadir dalam keindahan alam di sekitar Anda. Pola ini bernama deret Fibonacci—suatu rangkaian bilangan sederhana namun memiliki kedalaman yang luar biasa.

# Deret Fibonacci pertama kali diperkenalkan oleh matematikawan Italia bernama Leonardo Pisano, yang lebih dikenal dengan nama Fibonacci, pada abad ke-13. Dalam bukunya "Liber Abaci" (1202), ia menyajikan sebuah teka-teki tentang perkembangbiakan kelinci yang melahirkan konsep matematika yang hingga kini mempesona para ilmuwan, seniman, dan bahkan para pengamat alam.


# Konsep Dasar: Apa itu Deret Fibonacci?
#Deret Fibonacci dimulai dengan angka 0 dan 1. Setelah itu, setiap angka berikutnya didapatkan dengan menjumlahkan dua angka sebelumnya. Mari kita lihat beberapa suku awal dalam deret ini:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# dimana bilangan baru akan muncul ketika bilangan sebelumnya d jumlahkan.

# Magic of The Fibonacci

# Bunga dan Daun: Banyak bunga memiliki jumlah kelopak yang merupakan bilangan Fibonacci. Misalnya, lily memiliki 3 kelopak, buttercup memiliki 5 kelopak, dan bunga aster memiliki 21 kelopak.

# Spiral Pohon Pinus: Jika Anda mengamati spiral pada kerucut pinus, Anda akan menemukan bahwa jumlah spiral searah dan berlawanan jarum jam hampir selalu berupa bilangan Fibonacci yang berdekatan, seperti 8 dan 13, atau 5 dan 8.

# Nanas dan Bunga Matahari: Pola sisik pada nanas dan biji pada bunga matahari membentuk spiral dengan jumlah yang mengikuti bilangan Fibonacci.

# Pola Pertumbuhan Tanaman: Cara daun tumbuh pada batang (phyllotaxis) sering mengikuti sudut emas, yang terkait erat dengan rasio Fibonacci.

def fibonacci_recursive(n): # mendefinisikan variabel fungsi yang akan di gunakan dan di buat yaitu fibonacci_recursive