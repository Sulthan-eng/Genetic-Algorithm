import copy
import random
from collections import defaultdict

#Konstanta Algoritma Genetika
ukuran_populasi = 100
banyak_generasi = 100
rate_mutasi = 0.1

#bobot penalti
pinalti_keras = 100
pinalti_santai = 10

class MataKuliah:
    #konstruktor
    def __init__(self, kode_matkul, mata_kuliah, kelas, nama_dosen, ruang, kapasitas):
        self.kode_matkul = kode_matkul
        self.mata_kuliah = mata_kuliah
        self.kelas = kelas
        self.nama_dosen = nama_dosen
        self.ruang = ruang
        self.kapasitas = int(kapasitas)
        self.slot_waktu = None

List_Matkul = [
    MataKuliah("IF2514201","Aljabar Linier dan Geometri","A","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","B-103-00",40),
    MataKuliah("IF2514201","Aljabar Linier dan Geometri","B","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","E-307-00",40),
    MataKuliah("IF2514301","Arsitektur Komputer","A", "Aninditya Anggari Nuryono, S.T., M.Eng.", "E-101-00", 40),
    MataKuliah("IF2514301","Arsitektur Komputer","B","Riska Kurniyanto Abdullah, S.T., M.Kom.","E-104-00",60),
    MataKuliah("IF2514301","Arsitektur Komputer","C","Aninditya Anggari Nuryono, S.T., M.Eng.","E-303-00",40),
    MataKuliah("IF2514701","Capstone Project","-","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","E-102-00",80),
    MataKuliah("IF2514601","Deep Learning","-","Boby Mugi Pratama, S.Si., M.Han.","A-308-00",80),
    MataKuliah("IF2514501","Desain Web","A","Rizal Kusuma Putra, M.T.","E-307-00",40),
    MataKuliah("IF2514501","Desain Web","B","Rizal Kusuma Putra, M.T.","B-103-00",40),
    MataKuliah("IF2514503","Implementasi dan Pengujian Perangkat Lunak","A","Nur Fajri Azhar S.Kom., M.Kom.","E-201-00",60),
    MataKuliah("IF2514503","Implementasi dan Pengujian Perangkat Lunak","B","Nur Fajri Azhar S.Kom., M.Kom.","E-305-00",100),
    MataKuliah("IF2514503","Implementasi dan Pengujian Perangkat Lunak","C","Nur Fajri Azhar S.Kom., M.Kom.","E-305-00",100),
    MataKuliah("IF2514502","Interaksi Manusia dan Komputer","A","Nisa Rizqiya Fadhliana, S.Kom., M.T.","B-106-00",40),
    MataKuliah("IF2514502","Interaksi Manusia dan Komputer","B","Nisa Rizqiya Fadhliana, S.Kom., M.T.","B-103-00",40),
    MataKuliah("IF2514502","Interaksi Manusia dan Komputer","C","Nisa Rizqiya Fadhliana, S.Kom., M.T.","E-301-00",60),
    MataKuliah("IF2515002","Kapita Selekta","-","Nisa Rizqiya Fadhliana, S.Kom., M.T.", "E-104-00",60),
    MataKuliah("IF2515102","Keamanan Siber","X","Darmansyah, S.Si., M.T.I","E-302-00",40),
    MataKuliah("IF2515203","Kecerdasan Web","-","Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom.","E-206-00",40),
    MataKuliah("IF2514702","Keprofesian Informatika","A","Nur Fajri Azhar S.Kom., M.Kom.","E-103-00",40),
    MataKuliah("IF2514702","Keprofesian Informatika","B","Darmansyah, S.Si., M.T.I","E-307-00",40),
    MataKuliah("IF2516703","Kerja Praktek","-","Nisa Rizqiya Fadhliana, S.Kom., M.T.","0000",40),
    MataKuliah("IF2515202","Komputasi Evolusioner","-","null","null",0),
    MataKuliah("IF2514504","Manajemen Basis Data","A","Bowo Nugroho, S.Kom., M.Eng.","E-105-00",40),
    MataKuliah("IF2514504","Manajemen Basis Data","B","Bowo Nugroho, S.Kom., M.Eng.","E-301-00",60),
    MataKuliah("IF2514504","Manajemen Basis Data","C","Bowo Nugroho, S.Kom., M.Eng.","E-204-00",60),
    MataKuliah("IF2515301","Manajemen Proyek TIK","-","Riska Kurniyanto Abdullah, S.T., M.Kom.","B-106-00",40),
    MataKuliah("IF2514101","Matematika Diskrit","A","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","E-201-00",60),
    MataKuliah("IF2514101","Matematika Diskrit","B","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","E-301-00",60),
    MataKuliah("IF2514506","Pemrograman Fungsional","A","Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom.","E-305-00",100),
    MataKuliah("IF2514506","Pemrograman Fungsional","B","Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom.","E-204-00",60),
    MataKuliah("IF2515206","Pemrosesan Bahasa Alami","-","Bima Prihasto, S.Si., M.Si., Ph.D.","E-103-00",40),
    MataKuliah("IF2514102","Pengantar Informatika","A","Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.","E-206-00",40),
    MataKuliah("IF2514102","Pengantar Informatika","B","Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.","E-202-00",80),
    MataKuliah("IF2514302","Pengantar Kecerdasan Artifisial","A","Bima Prihasto, S.Si., M.Si., Ph.D.","E-307-00",40),
    MataKuliah("IF2514302","Pengantar Kecerdasan Artifisial","B","Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom.","B-103-00",40),
    MataKuliah("IF2514302","Pengantar Kecerdasan Artifisial","C","Bima Prihasto, S.Si., M.Si., Ph.D.","E-205-00",80),
    MataKuliah("IF2514704","Pengembangan Aplikasi Perangkat Bergerak","A","Rizal Kusuma Putra, M.T.","F-103-00",40),
    MataKuliah("IF2514704","Pengembangan Aplikasi Perangkat Bergerak", "B", "Rizal Kusuma Putra, M.T.", "B-103-00",40),
    MataKuliah("IF2514505","Pengolahan Citra Digital","A","Rizky Amelia, S.Si., M.Han.","E-305-00",100),
    MataKuliah("IF2514505","Pengolahan Citra Digital","B","Rizky Amelia, S.Si., M.Han.","E-306-00",40),
    MataKuliah("IF2517801","Proposal Tugas Akhir","-","Nisa Rizqiya Fadhliana, S.Kom., M.T.","E-304-00",40),
    MataKuliah("IF2515403","Sains Data (Pengayaan)","X","Ramadhan Paninggalih S.Si., M.Si., M.Sc.","E-306-00",40),
    MataKuliah("IF2514103","Sistem Digital","A","Boby Mugi Pratama, S.Si., M.Han.","E-101-00",40),
    MataKuliah("IF2514103","Sistem Digital","B","Boby Mugi Pratama, S.Si., M.Han.","E-303-00",40),
    MataKuliah("IF2514103","Sistem Digital","C","Boby Mugi Pratama, S.Si., M.Han.","B-102-00",40),
    MataKuliah("IF2514303","Sistem Operasi","A","Darmansyah, S.Si., M.T.I","E-103-00",40),
    MataKuliah("IF2514303","Sistem Operasi","B","Darmansyah, S.Si., M.T.I","B-103-00",40),
    MataKuliah("IF2514303","Sistem Operasi","C","Darmansyah, S.Si., M.T.I","E-205-00",80),
    MataKuliah("IF2514604","Sistem Paralel dan Terdistribusi","A","Riska Kurniyanto Abdullah, S.T., M.Kom.","E-103-00",40),
    MataKuliah("IF2514604","Sistem Paralel dan Terdistribusi","B","Riska Kurniyanto Abdullah, S.T., M.Kom.","B-103-00",40),
    MataKuliah("IF2514305","Struktur Data","A","Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.","E-305-00",100),
    MataKuliah("IF2514305","Struktur Data","B","Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.","E-202-00",80),
    MataKuliah("IF2514305","Struktur Data","C","Bowo Nugroho, S.Kom., M.Eng.","A-308-00",80),
    MataKuliah("IF2517802","Tugas Akhir","-","Nisa Rizqiya Fadhliana, S.Kom., M.T.","A-105-00",80),
    MataKuliah("IF2515404","Visi Komputer","-","Rizky Amelia, S.Si., M.Han.","E-307-00",40)
]

Slot_Waktu = [
    {"Hari" : "Senin", "Sesi" : 1, "Jam" : "(07.30-10.00)"},
    {"Hari" : "Senin", "Sesi" : 2, "Jam" : "(10.20-12.00)"},
    {"Hari" : "Senin", "Sesi" : 3, "Jam" : "(13.00-15.30)"},
    {"Hari" : "Senin", "Sesi" : 4, "Jam" : "(16.00-17.30)"},
    {"Hari" : "Selasa", "Sesi" : 1, "Jam" : "(07.30-10.00)"},
    {"Hari" : "Selasa", "Sesi" : 2, "Jam" : "(10.20-12.00)"},
    {"Hari" : "Selasa", "Sesi" : 3, "Jam" : "(13.00-15.30)"},
    {"Hari" : "Selasa", "Sesi" : 4, "Jam" : "(16.00-17.30)"},
    {"Hari" : "Rabu", "Sesi" : 1, "Jam" : "(07.30-10.00)"},
    {"Hari" : "Rabu", "Sesi" : 2, "Jam" : "(10.20-12.00)"},
    {"Hari" : "Rabu", "Sesi" : 3, "Jam" : "(13.00-15.30)"},
    {"Hari" : "Rabu", "Sesi" : 4, "Jam" : "(16.00-17.30)"},
    {"Hari" : "Kamis", "Sesi" : 1, "Jam" : "(07.30-10.00)"},
    {"Hari" : "Kamis", "Sesi" : 2, "Jam" : "(10.20-12.00)"},
    {"Hari" : "Kamis", "Sesi" : 3, "Jam" : "(13.00-15.30)"},
    {"Hari" : "Kamis", "Sesi" : 4, "Jam" : "(16.00-17.30)"},
    {"Hari" : "Jum'at", "Sesi" : 2, "Jam" : "(09.20-11.00)"},
    {"Hari" : "Jum'at", "Sesi" : 3, "Jam" : "(13.30-15.30)"},
    {"Hari" : "Jum'at", "Sesi" : 4, "Jam" : "(16.00-17.30)"},
]

"""Agar hari berurutan ketika ditampilkan"""
Hari_Urut = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"]

def buat_individu():
    """Menciptakan 1 individu jadwal dengan slot acak."""
    jadwal = copy.deepcopy(List_Matkul)
    #Mengisi slot waktu
    for matkul in jadwal:
        matkul.slot_waktu = random.choice(Slot_Waktu)
    return jadwal

def hitung_fitness_function(jadwal):
    """Hitung total penalti, semakin sedikit atau nilai 0, penalti semakin baik.
    Fungsi ini mengiterasi list of dict dan mengakses data melalui key dengan metode pengelompokkan"""
    pinalti = 0

    #dict kosong utk menampung kelompok jadwal
    slots = defaultdict(list)

    # Kelompokkan kelas berdasarkan slot waktu
    for matkul in jadwal:
        key = (matkul.slot_waktu["Hari"], matkul.slot_waktu["Sesi"])
        slots[key].append(matkul)

    """Batasan Keras : 
        Matkul tidak boleh di sesi yg sama, 1 dosen tak bisa mengajar di 2 kelas dalam sesi sama,
        1 ruang kelas tidak bisa dipakai lebih dari 2 mata kuliah di sesi yg sama"""
    for _, jadwal_kelas in slots.items():
        if len(jadwal_kelas) > 1:
            list_kode_matkul = [c.kode_matkul for c in jadwal_kelas]
            list_dosen = [c.nama_dosen for c in jadwal_kelas]
            list_ruang = [c.ruang for c in jadwal_kelas]

            if len(set(list_kode_matkul)) < len(list_kode_matkul):
                pinalti += pinalti_keras
            if len(set(list_dosen)) < len(list_dosen):
                pinalti += pinalti_keras
            if len(set(list_ruang)) < len(list_ruang):
                pinalti += pinalti_keras

    """Batasan Lunak : 
        Kelas Paralel di jadwal sebisa mungkin ga di hari yg sama"""
    hari_matkul = defaultdict(set)
    for matkul in jadwal:
        hari_matkul[matkul.kode_matkul].add(matkul.slot_waktu["Hari"])

    #jumlah kelas paralel
    hitung_matkul = defaultdict(int)
    for matkul in List_Matkul:
        hitung_matkul[matkul.kode_matkul] += 1

    for kode, set_hari in hari_matkul.items():
        if hitung_matkul[kode] > 1 and len(set_hari) < hitung_matkul[kode]:
            pinalti += pinalti_santai * (hitung_matkul[kode] - len(set_hari))

    """Batasan Lunak : 
        1 dosen dalam sehari mengajar tidak lebih dari 3 sesi
    """
    beban_dosen_harian = defaultdict(int)
    for matkul in jadwal:
        beban_dosen_harian[(matkul.nama_dosen, matkul.slot_waktu["Hari"])] += 1

    for beban in beban_dosen_harian.values():
        if beban > 3:
            pinalti += pinalti_santai

    return pinalti


def reproduksi(parent1, parent2):
    """Single-Point Crossover berdasarkan slot waktu"""
    n = len(parent1)
    c = random.randint(1, n - 1)

    anak = copy.deepcopy(parent1)
    for i in range(c, n):
        anak[i].slot_waktu = copy.deepcopy(parent2[i].slot_waktu)

    return anak

def mutasi(jadwal):
    """Mutasi acak yang akan mengubah slot waktu beberapa matkul"""
    jadwal = copy.deepcopy(jadwal)
    for matkul in jadwal:
        if random.random() < rate_mutasi:
            matkul.slot_waktu = random.choice(Slot_Waktu)
    return jadwal

def tampil_jadwal(jadwal, pinalti_final):
    """Mencetak jadwal dgn format yg mudah dibaca"""
    jadwal.sort(key=lambda x: (Hari_Urut.index(x.slot_waktu["Hari"]), x.slot_waktu["Sesi"]))

    print("\n ---JADWAL KULIAH---")
    print("Dengan Nilai Pinalti : ", pinalti_final, "\n")

    hari_ini = ""
    for j in jadwal:
        if j.slot_waktu["Hari"] != hari_ini:
            hari_ini = j.slot_waktu["Hari"]
            print(f"\n--- {hari_ini.upper()} ---")
        print(f" Sesi{j.slot_waktu['Sesi']} {j.slot_waktu['Jam']}: {j.mata_kuliah} ({j.kelas}) | Dosen : {j.nama_dosen}) | Ruang : {j.ruang} | Kapasitas : {j.kapasitas} ")
    # print("--------------------------------------\n")

def genetik_algoritma():
    """Fungsi yg menjalankan proses evolusi"""
    populasi = [buat_individu() for _ in range(ukuran_populasi)]

    for gen in range(banyak_generasi):
        populasi.sort(key = hitung_fitness_function)
        if hitung_fitness_function(populasi[0]) == 0:
            print(f"\nSolusi terbaik ditemukan di generasi ke {gen}\n")
            break

        populasi_baru = populasi[:20]   #elitisme (20 individu terbaik gen skrg dibawa ke gen berikutnya)
        while len(populasi_baru) < ukuran_populasi:
            parent1, parent2 = random.sample(populasi[:50], 2)
            anak = reproduksi(parent1, parent2)
            anak = mutasi(anak)
            populasi_baru.append(anak)

        populasi = populasi_baru

    jadwal_terbaik = populasi[0]
    pinalti_terbaik = hitung_fitness_function(jadwal_terbaik)
    tampil_jadwal(jadwal_terbaik, pinalti_terbaik)

if __name__ == "__main__":
    genetik_algoritma()