import json
import os
from types import new_class

def login():
    batas_input = 1
    clear_screen()
    print("----- Student Database -----")
    while batas_input <= 3:
        user = input("\nUsername: ")
        password = input('Password: ')
        batas_input +=1
        if user == 'NoVan':
            if password == 'semangatAlgoB':
                clear_screen()
                input ('Hi, Welcome!')
                program()
            else:
                print('Password salah')
        else:
            if password == 'semangatAlgoB':
                print('Username salah')
            else:
                print('Username dan password salah')
    exit()

def lihatdata():
    try:
        with open('note.json', 'r') as file:
            data = json.load(file)
            print('''
                
                                    Data Mahasiswa Prodi Sistem Informasi Universitas Jember                             
                +____________________________________________________________________________________________________________________+''')
            print('')    
            indeks=0
            for user in data['data']:
                indeks += 1
                print('        |',indeks,'.  NAMA: >>>>[', user['nama'] ,'] - NIM: [',user['nim'],'] - Tempat tanggal lahir: >>>>[', user['ttl'],'] - Asal: >>>>[',user['asal'],']')
                print('''        |''''-----------------------------------------------------------------------------------------------------------------------') 
                print('')
            

    except:
        print('\nData anda belum ada! silahkan buat data baru terlebih dahulu\n')
        buatData()
    finally:
            pertanyaan=input("Apakah ingin kembali ke program? [y] untuk lanjut/[t] untuk menambahkan : ")
            if pertanyaan == 'y' :
                program()
            elif pertanyaan == 't' :
                tambahData()

def simpanData(inp):
    data = {}
    data['data'] = inp
    with open('note.json','w') as simpan:
        json.dump(data, simpan, indent=4)
        
def buatData():   
    data = {}
    data['data'] = [
        {"nama":input('Masukkan nama lengkap anda: '),"nim":input('Masukkan NIM anda: '), "ttl": input('Masukkan Tempat tanggal lahir anda: '), 'asal': input('Masukkan asal daerah anda: ')}
        ]
    try:
        with open('note.json','w') as filebaru:
            json.dump(data,filebaru,indent=4)
    finally:
        pertanyaan= input("\nApakah anda ingin lanjut menambahkan data? [y] untuk lanjut/[t] untuk kembali ke program: ")
        if pertanyaan == 'y' :
            tambahData()
        else :
            print('---------- Data anda telah berhasil disimpan ----------')
            program()

def tambah_data(data, filename='note.json'):
    with open(filename, 'w') as p:
        json.dump(data, p, indent=4)

def tambahData():
    with open ('note.json') as file_json:
        data=json.load(file_json)
        change=data['data']
        a= {"nama":input('Masukkan nama lengkap anda: '),"nim":input('Masukkan NIM anda: '), "ttl": input('Masukkan Tempat tanggal lahir anda: '), 'asal': input('Masukkan asal daerah anda: ')}
        change.append(a)
        tambah_data(data)
        pertanyaan= input("\nApakah anda ingin lanjut menambahkan? [y] untuk lanjut/[t] untuk kembali ke program: ")
        if pertanyaan == 'y' :
            tambahData()
        else :
            print('---------- Data anda telah berhasil disimpan ----------')
            program()

def view():
    with open('note.json', 'r') as file:
        data = json.load(file)
        print('''
            
                             Data Mahasiswa Prodi Sistem Informasi Universitas Jember                             
+____________________________________________________________________________________________________________________+''')
        print('')    
        indeks=-1
        for user in data['data']:
            indeks += 1
            print( indeks,'<Nama>:', user['nama'] ,'- <Nim>',user['nim'],'- <Tempat tanggal lahir>: ', user['ttl'],'- <Asal>: ',user['asal'])

def hapus_Data():
    view()    
    try:
        with open ('note.json', "r") as f:
            new_data = []
            data = json.load(f)
            temp = data['data']      
            data_length = len(temp)-1
            print ("Data mana yang akan anda hapus?")
            opsi_delete = input(f"pilih nomor 0-{data_length}: ")
            i=0
            for entry in temp:
                if i == int(opsi_delete):
                    pass
                    i=i+1
                else:    
                    new_data.append(entry)
                    i=i+1
    finally:         
        simpanData(new_data)
        view()
        print("data anda berhasil dihapus !!!")
        jawaban = input('apakah ingin menghapus lagi? y untuk melanjutkan/ t untuk kembali ke program : ')
        if jawaban == 'y':
            hapus_Data()
        else: 
            program()      
    
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    
def program():
    print(''''
    >-----------------------------------------------<
    | Data Mahasiswa Sistem Informasi angkatan 2021 |
    >-----------------------------------------------<
  
    [1] Lihat data
    [2] Tambah data
    [3] Hapus data
    [4] Buat data baru
    [5] Keluar
    ''')

    jawaban = input("silahkan pilih : ")
    if jawaban == "1" :
        lihatdata()
    elif jawaban == "2" :
        tambahData()
    elif jawaban == "3" :
        hapus_Data()
    elif jawaban == "4" :
        buatData()
    elif jawaban == "5" :
        pertanyaan= input("\nApakah anda yakin?[y/t]: ")
        if pertanyaan == 'y' :
            print('\n----------------- Terima Kasih -----------------')
            exit()
        else :
            program()
    else:
        print("Maaf program yang anda pilih tidak ada")
    
program()