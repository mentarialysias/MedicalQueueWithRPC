#server

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from datetime import datetime

# Membuat server
server = SimpleJSONRPCServer(("127.0.0.1", 8081))
server.register_introspection_functions()

def time_in_range(start, end, x):
    """ Mengembalikan True jika x berada dalam range [start, end] """
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

# Membuat instansiasi yang dipublikasikan sebagai method XML-RPC
daftar_klinik = [{'id': 1, 'nama': 'gigi', 'buka': '09:00', 'tutup':'19:00', 'antrian': [], 'jml_pasien': 0, 'waktu_pasien': 30},
{'id':2, 'nama': 'mata', 'buka': '09:00', 'tutup':'19:00', 'antrian': [], 'jml_pasien': 0, 'waktu_pasien': 15},
{'id':3, 'nama': 'saraf', 'buka': '08:00', 'tutup':'17:00', 'antrian': [], 'jml_pasien': 0,  'waktu_pasien': 50},
{'id':4, 'nama': 'anak', 'buka': '07:00', 'tutup':'18:00', 'antrian': [], 'jml_pasien': 0,  'waktu_pasien': 20},
{'id':5, 'nama': 'jantung', 'buka': '08:00', 'tutup':'17:00', 'antrian': [], 'jml_pasien': 0,  'waktu_pasien': 50}]
pertama = True # variabel yang bernilai True jika pasien merupakan pasien pertama yang melakukan registrasi pada sistem
tgl_hari_ini = ''

class RumahSakit:
    def get_klinik(self, id):
        """ Diberikan sebuah bilangan bulat id untuk mengembalikan data klinik yang memiliki id tersebut jika ada,
        jika tidak akan mengembalikan -1 """
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                return klinik
        return -1

    def regis(self, id, no_rek, nama, tgl_lahir, tgl_input):
        """ Menyimpan data pasien yang melakukan registrasi pada klinik tertentu, dan mengembalikan nomor antrian
        yang didapat """
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                klinik['antrian'].append({'no': klinik['jml_pasien']+1, 'no_rek': no_rek,
                                        'nama': nama, 'tgl_lahir': tgl_lahir, 'tgl_input': tgl_input})
                klinik['jml_pasien'] += 1
                return klinik['jml_pasien']
                
    def get_antri(self, id, no):
        """ Diberikan sebuah bilangan bulat 'id' dan 'no', untuk mengembalikan data antrian dengan nomor 'no' pada klinik
        dengan id = 'id' """
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                for antri in klinik['antrian']:
                    if antri['no'] == no:
                        data_antri = antri
        return data_antri

    def get_klinik_buka(self, waktu):
        """ Mengembalikan daftar klinik yang buka pada saat 'waktu' """
        global daftar_klinik
        klinik_buka = []
        for klinik in daftar_klinik:
            if time_in_range(klinik['buka'], klinik['tutup'], waktu):
                klinik_buka.append(klinik)
        return klinik_buka
    
    def reset_antrian(self):
        """ Menghapus data pada list antrian dan mengeset jumlah pasien menjadi 0 pada seluruh klinik"""
        for klinik in daftar_klinik:
            klinik['jml_pasien'] = 0
            klinik['antrian'] = []
    
    def get_hari(self):
        """ Mengembalikan tanggal hari ini """
        global pertama, tgl_hari_ini
        if pertama:
            tgl_hari_ini = datetime.now().strftime("%d")
            pertama = False
        return tgl_hari_ini
    
    def set_hari(self, tgl):
        """ Mengeset tanggal hari ini dengan nilai dari 'tgl' """
        global tgl_hari_ini
        tgl_hari_ini = tgl

# meregisterkan class pada server
server.register_instance(RumahSakit())
# menjalankan server
server.serve_forever()