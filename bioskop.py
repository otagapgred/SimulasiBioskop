kursi_kosong=['1a', '2a', '4e', '3g', '4g']
horor=['kuntilanak 2', 'annabelle']
romance=['dear nathan', 'Galaksi']
hari=['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
waktu=['1:30', '4:15', '8:15']

kursi_sold=[]
plan_film={}
plan_hari=()
plan_waktu=()


#tampilan awal
print('*****'*5)
user=input('Masukkan Nama : ')
usia=int(input('Usia : '))
hari2=input('masukkan hari : ')
start=input('Pesan tiket?[y/n]')
print('*****'*5)
if start.lower()== 'y':
#perulangan while
    while True:
        if usia >= 13:
            print("silahkan pilih genre film")
            print('horror \nromance')
            planf=input('ketik genre : ')
            print('*****'*5)

            if planf.lower()== 'romance' :
                for x in range(len (romance)) :
                    print(romance[x])
                pilih=input("pilih film :")
                plan_film=pilih
            elif planf.lower()=='horror':
                for x in range(len (horor)) :
                    print(horor[x])
                pilih=input("pilih film :")
                plan_film=pilih
            else:
                print('mohon maaf telah terjadi kesalahan, coba lagi')
                continue

        else:
            print("--Maaf anda masih belum memenuhi syarat usia untuk menonton film kami--")
            
        print('*****'*5)
        kursi=int(input('jumlah kursi : '))
        if hari2.lower()<=hari[3]:
            total=kursi*40000
            
        elif hari2.lower()==hari[4]:
            total=kursi*45000
            
        else:
            total=kursi*50000

        break 


    print('*****'*5)
    for item in range(len(waktu)):
        print(item,'. jam', waktu[item])
    pilah=int(input('Pilih jam nonton [0/1/2]: '))
    plan_waktu=(waktu[pilah])

#cetak tiket
print('\n*****'*5)
print('--------Tiket Nonton--------')
print('Atas nama     :', user)
print('hari          :', hari2)
print('jumlah Bangku :', kursi)
print('waktu         :', plan_waktu)
print(f'Total Harga   : Rp{total}')
print(f'-----film {plan_film}-----')
print('*****'*5)

