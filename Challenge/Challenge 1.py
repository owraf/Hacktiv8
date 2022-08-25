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
if tebakkan1 == acak:
    print('Selamat, tebakkan Anda Benar')
    print('Skor anda',skor)
    print('ANDA MENANG')

elif tebakkan1 > acak:
    print('tebakkan terlalu besar')
    skor = skor - 10
    print('Skor anda saat ini adalah',skor)
    print('')
    tebakkan2 = int(input('Masukkan tebakkan anda : '))
    if tebakkan2 == acak:
        print('Selamat, tebakkan Anda Benar')
        print('Skor anda',skor)
        print('ANDA MENANG')
        
    elif tebakkan2 > acak:
        print('tebakkan terlalu besar')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    elif tebakkan2 < acak:
        print('tebakkan terlalu kecil')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    else:
        print('Tebakkan harus berupa angka')
        print('Pinalty, poin dikurangi 20')
        skor = skor - 20
        print('Skor anda saat ini adalah',skor)    
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

elif tebakkan1 < acak:
    print('tebakkan terlalu kecil')
    skor = skor - 10
    print('Skor anda saat ini adalah',skor)
    print('')
    tebakkan2 = int(input('Masukkan tebakkan anda : '))
    if tebakkan2 == acak:
        print('Selamat, tebakkan Anda Benar')
        print('Skor anda',skor)
        print('ANDA MENANG')
        
    elif tebakkan2 > acak:
        print('tebakkan terlalu besar')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    elif tebakkan2 < acak:
        print('tebakkan terlalu kecil')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    else:
        print('Tebakkan harus berupa angka')
        print('Pinalty, poin dikurangi 20')
        skor = skor - 20
        print('Skor anda saat ini adalah',skor)    
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

else:
    print('Tebakkan harus berupa angka')
    print('Pinalty, poin dikurangi 20')
    skor = skor - 20
    print('Skor anda saat ini adalah',skor)    
    print('')
    tebakkan2 = int(input('Masukkan tebakkan anda : '))
    
    if tebakkan2 == acak:
        print('Selamat, tebakkan Anda Benar')
        print('Skor anda',skor)
        print('ANDA MENANG')
        
    elif tebakkan2 > acak:
        print('tebakkan terlalu besar')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    elif tebakkan2 < acak:
        print('tebakkan terlalu kecil')
        skor = skor - 10
        print('Skor anda saat ini adalah',skor)
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')

    else:
        print('Tebakkan harus berupa angka')
        print('Pinalty, poin dikurangi 20')
        skor = skor - 20
        print('Skor anda saat ini adalah',skor)    
        print('')
        tebakkan3 = int(input('Masukkan tebakkan anda : '))
        if tebakkan3 == acak:
            print('Selamat, tebakkan Anda Benar')
            print('Skor anda',skor)
            print('ANDA MENANG')
            
        elif tebakkan3 > acak:
            print('tebakkan terlalu besar')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        elif tebakkan3 < acak:
            print('tebakkan terlalu kecil')
            skor = skor - 10
            print('Skor anda saat ini adalah',skor)
            print('GAME OVER')

        else:
            print('Tebakkan harus berupa angka')
            print('Pinalty, poin dikurangi 20')
            skor = skor - 20
            print('Skor anda saat ini adalah',skor)    
            print('GAME OVER')