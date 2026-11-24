def hello_world():
    # menampilkan hello world

    print("hello world")
    print("Kepada Fauzan Zein")
    print("Dan juga kepada Faza Biri Biri")

    def hello_world():
        print("Hello World!")

    hello_world()

# Memanggil fungsi utama
hello_world()



# Program 12.2 Fungsi dengan Argumen
## --- Fungsi dengan Argumen ---

## def nama_fungsi (argumen)
#      Badan Fungsi

def hello_world(nama):
    #fungsi hello wolrd menerima
    print(f"Selamat Datang di Dunia, {nama}")
    
hello_world("ucup")

def tambah(angka_1, angka_2):
    #fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,8)

def say_hi(list_peserta):
    #fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in  data_peserta:
        print(f"Selamat datang {peserta}")

kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]

say_hi(kumpulan_mahasiswa)



# Program 12.3 Fungsi dengan return

# Template fungsi kembalian
# def nama_fungsi(argumen):
#     badan fungsi
#     return output


# Fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat


y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)


# Fungsi tambah dengan dua input
def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2


a = fungsi_tambah(10, 8)
print(a)


# Fungsi operasi matematika
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi


# Memanggil fungsi operasi matematika
hasil = operasi_matematika(10, 5)

print("Hasil tambah:", hasil[0])
print("Hasil kurang:", hasil[1])
print("Hasil kali:", hasil[2])
print("Hasil bagi:", hasil[3])



# Fungsi operasi matematika
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi


# Memanggil fungsi
k, l, m, n = operasi_matematika(9, 5)


# Menampilkan hasil
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")



# Program 12.4 Default Argumen Fungsi 

# DEFAULT ARGUMENT

# Bentuk umum:
# def fungsi(argument):
# def fungsi(argument = nilai_default):


# CONTOH 1: Default argument sederhana
def say_hello(nama="Ojul"):
    print(f"Hello {nama}")


say_hello("Ucup")
say_hello()


# CONTOH 2: Fungsi dengan satu input biasa
# dan satu default argument
def sapa_dia(nama, pesan="Apa kabar?"):
    print(f"Hai {nama}, {pesan}")


sapa_dia("Nanda", "Selamat pagi")
sapa_dia("Budi")


# CONTOH 3: Default argument dengan operasi pangkat
def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)


# CONTOH 4: Default argument dengan perkalian
def faktorial(input_1=1, input_2=2, input_3=3, input_4=4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil


print(faktorial())
print(faktorial(input_3=10))
