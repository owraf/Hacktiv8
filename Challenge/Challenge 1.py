from random import randint

judul = 'PERMAINAN TEBAK ANGKA'
print('-'*len(judul))
print(judul)
print('-'*len(judul))
print('Saya memikirkan sebuah angka dari 1 - 9')
print('Silahkan tebak angka yang saya pikirkan') 
print('Input harus berupa Angka')
print('Skor anda saat ini adalah 100')

skor = 100
acak = randint(0, 9)
percobaan = 3

while True:
    try :
        if percobaan == 0:
            print('GAME OVER')
            print('')
            break

        else:
            tebakkan = int(input('Masukkan tebakkan anda : '))
            if tebakkan == acak:
                print('Selamat, tebakkan Anda Benar')
                print('Skor anda',skor)
                print('ANDA MENANG')
                print('')
                break

            elif tebakkan > acak :
                print('tebakkan terlalu besar')
                skor = skor - 10
                percobaan = percobaan - 1
                print('Skor anda saat ini adalah',skor)
                print('')

            else:
                print('tebakkan terlalu kecil')
                skor = skor - 10
                percobaan = percobaan - 1
                print('Skor anda saat ini adalah',skor)
                print('')


    except ValueError:
        print('Tebakkan harus berupa angka')
        print('Pinalty, poin dikurangi 20')
        skor = skor - 20
        percobaan = percobaan - 1
        print('Skor anda saat ini adalah',skor)
        print('')
