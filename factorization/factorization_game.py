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
    clue = factor[: -1]

    # berikut adalah fungsi untuk menampilak faktor2 kecil yang menjadi pengaruh dari jawaban (Factor aslinya).
    print(f"I think a numbers, the factors is : {clue}") # print akan menampilakn var clue yang sudah di dapatkan dari hasil var secret number yang akan menjadi faktor2 kecil dari jawaban asli.

    # saya akan memberi 3 kali kesempatan untuk menebak, jika salah maka akan mengeluarkan print yang berisi bahwa jawaban yang anda masukan salah.
    for trials in range(3):
        tebakan = int(input(f"Tebakan ke-{trials+1}: ")) # ingat memang harus di + 1, jika tidak maka percobaan akan = - 1 (secara default pemrograman)
        if tebakan == secret_number:
            print(f"Congrats! Your answer is true, the secret number is: {secret_number}") # akan mencetak secret number, karena tebakan sesuai dengan factor terbesar dari factor2 kecil (jawabanya).
            return
        else: # jika salah maka cetak string berikut.
            print("Shit! your answer is false, try again.")

        print(f"OOh nooo, your trials all done, the secret number is: {secret_number}, see you leter!")

tebak_bilangan()