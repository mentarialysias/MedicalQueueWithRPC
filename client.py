#client
from datetime import datetime
from datetime import timedelta
import jsonrpclib

# membuat stub pada client
s = jsonrpclib.Server('http://127.0.0.1:8081')

def select_menu():
    """ Menampilkan menu utama """
    global pilihan
    print('======= Selamat datang di Rumah Sakit Semangka! =======')
    print('1. Menampilkan daftar klinik yang buka')
    print('2. Registrasi')
    print('0. Keluar')
    pilihan = input('Masukkan pilihan menu: ')
    while pilihan != '0':
        if pilihan == '1':
            tampil_daftar()
            return_menu()
        elif pilihan == '2':
            registrasi()
            return_menu()
        else:
            print('Pilihan menu tidak sesuai, silahkan pilih kembali')
            print()
            select_menu()

def return_menu():
    """ Menampilkan menu untuk kembali ke menu utama """
    global pilihan
    print()
    kembali = input('Kembali ke menu utama? (Y/N): ')
    while kembali != 'Y' and kembali != 'y' and kembali != 'N' and kembali != 'n':
            kembali = input('Kembali ke menu utama? (Y/N): ')
    if kembali == 'Y' or kembali == 'y':
        print()
        select_menu()
    elif kembali == 'N' or kembali == 'n':
        pilihan = '0'  

def time_in_range(start, end, x):
    """ Mengembalikan True jika x berada dalam range [start, end] """
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def tampil_daftar():
    """ Menampilkan daftar klinik yang buka saat program dijalankan """
    tgl = datetime.now()
    waktu = tgl.strftime("%H:%M")
    day = tgl.strftime("%d")
    # jika hari sudah berganti, maka data antrian pada seluruh klinik akan direset
    if (day != s.get_hari()):
        s.reset_antrian()
        s.set_hari(day)
    klinik_buka = s.get_klinik_buka(waktu)
    if klinik_buka:
        for klinik in klinik_buka:
            print('[', klinik['id'], ']', sep='')
            print('Nomor Klinik            :', klinik['id'])
            print('Nama Klinik             :', klinik['nama'])
            print('Jam Buka - Jam Tutup    :', klinik['buka'], '-', klinik['tutup'])
            print('Jumlah Pasien Terdaftar :', klinik['jml_pasien'])
            print()
    else:
        print('Tidak ada klinik yang buka')

def registrasi():
    """ Fungsi untuk melakukan registrasi """
    # menerima input id klinik, selama tidak valid akan diminta input kembali
    ids = input('Masukkan nomor klinik: ')
    while not ids.isdigit():
        print('Klinik tidak valid, silahkan pilih kembali')
        ids = input('Masukkan nomor klinik: ')
    id = int(ids)
    klinik = s.get_klinik(id)
    tgl_input = datetime.now()
    waktu = tgl_input.strftime("%H:%M")
    day = tgl_input.strftime("%d")
    # jika hari sudah berganti, maka data antrian pada seluruh klinik akan direset
    if (day != s.get_hari()):
        s.reset_antrian()
        s.set_hari(day)
    # menerima input id klinik, selama tidak valid atau klinik tersebut tidak buka, akan diminta input kembali
    while s.get_klinik(id) == -1 or (not time_in_range(klinik['buka'], klinik['tutup'], waktu)):
        print('Klinik tidak valid, silahkan pilih kembali')
        ids = input('Masukkan nomor klinik: ')
        while not ids.isdigit():
            print('Klinik tidak valid, silahkan pilih kembali')
            ids = input('Masukkan nomor klinik: ')
        id = int(ids)
        klinik = s.get_klinik(id)
        tgl_input = datetime.now()
        waktu = tgl_input.strftime("%H:%M")
        day = tgl_input.strftime("%d")
        # jika hari sudah berganti, maka data antrian pada seluruh klinik akan direset
        if (day != s.get_hari()):
            s.reset_antrian()
            s.set_hari(day)
    # menerima input data pasien
    no_rek = input('Masukkan nomor rekam medis: ')
    nama = input('Masukkan nama: ')
    tgl_lahir = input('Masukkan tanggal lahir (dd-mm-yyyy): ')
    # memanggil fungsi regis() yang ada di komputer remote
    no_antri = s.regis(id, no_rek, nama, tgl_lahir, str(tgl_input))
    # memanggil fungsi get_antri() yang ada di komputer remote
    antri = s.get_antri(id, no_antri)
    # memanggil fungsi get_klinik() yang ada di komputer remote
    klinik = s.get_klinik(id)
    # menampilkan data antrian yang didapatkan
    print('-------------------------------------------------------')
    print('Nomor antrian:', antri['no'])
    print('Antrian di depan Anda:', klinik['jml_pasien']-1)
    # menghitung waktu giliran pasien masuk ke klinik
    lama_antri = (klinik['jml_pasien']-1) * klinik['waktu_pasien']
    waktu_masuk = tgl_input + timedelta(minutes=lama_antri)
    print('Perkiraan waktu Anda mendapat giliran:', waktu_masuk)

# memanggil fungsi select_menu()
select_menu()