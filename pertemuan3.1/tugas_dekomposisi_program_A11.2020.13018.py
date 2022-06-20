"""
Program sederhana untuk input, tampil, edit, dan hapus data nilai mahasiswa.
Program yang dibuat menggunakan input dan output berbasis console dengan
satu fungsi main saja.
"""
daftar_nilai = [78, 95, 67, 58, 82] 

def input_data():
    """Menambahkan nilai baru dengan pada daftar_nilai
    """
    print("Aplikasi Input Nilai")
    print("="*20)
    nilai_baru = float(input('Input nilai baru: '))
    print("="*20)
    daftar_nilai.append(nilai_baru)
    print("="*20)
    print("Input nilai berhasil")
    print("="*20)

def tampil_data():
    """menampilkan daftar nilai
    """
    print("Aplikasi Input Nilai")
    print("="*20)
    print('Daftar Nilai mahasiswa')
    print("="*20)
    for num,nilai in enumerate(daftar_nilai):
        print(f'{num+1}. {nilai}')
    print("="*20)

def edit_data():
    """Mengedit atau mengganti nilai pada daftar_nilai
    """
    print("Aplikasi Input Nilai")
    print("="*20)
    idx = int(input('Nilai ke berapa yang akan dirubah: '))-1
    nilai_baru = float(input('Inputkan nilai baru: '))
    daftar_nilai[idx] = nilai_baru
    print("="*20)
    print("Nilai berhasil dirubah")
    print("="*20)

def hapus_data():
    """Menghapus nilai yang ada pada daftar_nilai
    """
    print("Aplikasi Input Nilai")
    print("="*20)
    idx = int(input('Nilai ke berapa yang akan dihapus: '))-1
    daftar_nilai.pop(idx)
    print("="*20)
    print("Nilai berhasil dihapus")
    print("="*20)

def main():
    menus = ['Input data', 'Tampil data', 'Edit data', 'Hapus data']

    while True:
        print("Aplikasi Input Nilai")
        print("="*20)
        print("Menu Aplikasi")
        print("="*20)
        for num,menu in enumerate(menus):
            print(f"{num+1}. {menu}")
        print("x. Keluar")
        print("="*20)
        inp_menu = input("pilih menu: ")
        print("="*20)
        if inp_menu == '1':
            input_data()
        if inp_menu == '2':
            tampil_data()
        if inp_menu == '3':
            edit_data()
        if inp_menu == '4':
            hapus_data()
        if inp_menu == 'x':
            break
        else:
            print('Tidak ada pilihan menu tersebut')
    print('Terima kasih telah menggunakan aplikasi, jangan lupa gunakan lagi di lain waktu')
  
main()