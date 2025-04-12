print ('''
       

 |  ____|       | |           (_)        | | (_)            
 | |__ __ _  ___| |_ ___  _ __ _ ______ _| |_ _  ___  _ __  
 |  __/ _` |/ __| __/ _ \| '__| |_  / _` | __| |/ _ \| '_ \ 
 | | | (_| | (__| || (_) | |  | |/ / (_| | |_| | (_) | | | |
 |_|  \__,_|\___|\__\___/|_|  |_/___\__,_|\__|_|\___/|_| |_|
  
 the origin of number, can you play with this function?

''')

import random # untuk mengimport modul random dari library python

def tebak_bilangan():
    # ini merupakan function untuk kita dapat menebak bilangan dari 1-50 untuk mencari factor terbesar dari beberapa factor kecil yang mempengaruhi.
    secret_number = random.randint(1, 50)

    # find the factors (berdasarkan secret number yang sudah ditentukan oleh modul random dari python)
    factor = find_factors(secret_number)

    # fungsi untuk tidak menampilkan faktor terbesar yaitu bilangan itu sendiri (jawabanya).
    clue = factor