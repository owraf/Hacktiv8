from random import randint

judul = 'PERMAINAN TEBAK ANGKA'
print('-'*len(judul))
print(judul)
print('-'*len(judul))
print('Saya memikirkan sebuah angka dari 1 - 20')
print('Silahkan tebak angka yang saya pikirkan') 
print('Input harus berupa Angka')
print('Skor anda saat ini adalah 100')

skor = 100
acak = randint(0, 9)

tebakkan1 = int(input('Masukkan tebakkan anda : '))
if type(tebakkan1) is string :
    print("salah cook")
else:
    if tebakkan1 == acak:
        print('Selamat, tebakkan Anda Benar')
        print('Skor anda',skor)
        print('ANDA MENANG')

    elif tebakkan1 > acak:
        print('tebakkan terlalu besar')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)

    elif tebakkan1 < acak:
        print('tebakkan terlalu kecil')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)

    else:
        print('Tebakkan harus berupa angka')
        print('Pinalty, poin dikurangi 20')
        skor = skor - 20
        print('Skor anda saat ini adalah',skor)    