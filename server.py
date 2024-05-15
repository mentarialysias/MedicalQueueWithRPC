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
# waktu_pasien dalam format menit
daftar_klinik = [
    {
        "id": 1,
        "nama": "Poli Gigi",
        "buka": "09:00",
        "tutup": "19:00",
        "antrian": [],
        "jml_pasien": 0,
        "waktu_pasien": 30,
        "dokter": [
			{
				"nama": "dr. Mentari",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:00"
			},
			{
				"nama": "dr. Yanti",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "11:00"
			},
			{
				"nama": "dr. Yadi",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "19:00"
			},		
			{
				"nama": "dr. Anto",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "11:00",
				"jam_akhir_kerja": "16:00"
			},				
			
		]
    },
    {
        "id": 2,
        "nama": "Poli Mata",
        "buka": "09:00",
        "tutup": "18:00",
        "antrian": [],
        "jml_pasien": 0,
        "waktu_pasien": 15,
        "dokter": [
			{
				"nama": "dr. Azis",
				"hari_kerja": ["Senin", "Rabu", "Kamis"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:30"
			},
			{
				"nama": "dr. Ayu",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:00"
			},
			{
				"nama": "dr. Sinta",
				"hari_kerja": ["Senin", "Rabu", "Kamis"],
				"jam_awal_kerja": "13:30",
				"jam_akhir_kerja": "18:00"
			},		
			{
				"nama": "dr. Anto",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00"
			},	
		]
    },
    {
        "id": 3,
        "nama": "Poli Saraf",
        "buka": "08:00",
        "tutup": "17:00",
        "antrian": [],
        "jml_pasien": 0,
        "waktu_pasien": 50,
        "dokter": [
			{
				"nama": "dr. Delvito",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00"
			},
			{
				"nama": "dr. Asep",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00"
			},
			{
				"nama": "dr. Santy",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00"
			},		
			{
				"nama": "dr. Floresia",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00"
			},	
		]
    },
    {
        "id": 4,
        "nama": "Poli Anak",
        "buka": "07:00",
        "tutup": "18:00",
        "antrian": [],
        "jml_pasien": 0,
        "waktu_pasien": 20,
        "dokter": [
			{
				"nama": "dr. Aini",
				"hari_kerja": ["Senin", "Rabu", "Kamis"],
				"jam_awal_kerja": "07:00",
				"jam_akhir_kerja": "13:00"
			},
			{
				"nama": "dr. Budi",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "07:00",
				"jam_akhir_kerja": "13:00"
			},
			{
				"nama": "dr. Soni",
				"hari_kerja": ["Senin", "Rabu", "Kamis"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00"
			},		
			{
				"nama": "dr. Laurence",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00"
			},	
		]
    },
    {
        "id": 5,
        "nama": "Poli Jantung",
        "buka": "08:00",
        "tutup": "17:00",
        "antrian": [],
        "jml_pasien": 0,
        "waktu_pasien": 50,
        "dokter": [
			{
				"nama": "dr. Rafi",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00"
			},
			{
				"nama": "dr. Rachmat",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00"
			},
			{
				"nama": "dr. Alysia",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00"
			},		
			{
				"nama": "dr. Saldy",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00"
			},	
		]
    }
]
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

    def regis(self, id, no_reg, nama, tgl_lahir, tgl_input):
        """ Menyimpan data pasien yang melakukan registrasi pada klinik tertentu, dan mengembalikan nomor antrian
        yang didapat """
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                klinik['antrian'].append({'no': klinik['jml_pasien']+1, 'no_reg': no_reg,
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

    def tampil_daftar_dokter(self):
        """ Menampilkan seluruh daftar klinik beserta jadwal dokter """
        global daftar_klinik
        daftar_str = ""
        for klinik in daftar_klinik:
            daftar_str += f"\n[Klinik: {klinik['nama']}]\n"
            daftar_str += "   Daftar Dokter:\n"
            for dokter in klinik['dokter']:
                daftar_str += f"   ->  Nama: {dokter['nama']}\n"
                daftar_str += f"       Hari Kerja: {', '.join(dokter['hari_kerja'])}\n"
                daftar_str += f"       Jam Kerja: {dokter['jam_awal_kerja']} - {dokter['jam_akhir_kerja']}\n\n"
        return daftar_str


# meregisterkan class pada server
server.register_instance(RumahSakit())

# menjalankan server
server.serve_forever()

