import json
import os
class Asset:
    def __init__(self, nama, modal, harga_rata_rata, harga_sekarang):
        self.nama = nama
        self.modal = modal
        self.harga_rata_rata = harga_rata_rata
        self.harga_sekarang = harga_sekarang
    def jumlah_aset(self):
        return self.modal/self.harga_rata_rata
    def nilai_aset(self):
        return self.jumlah_aset()*self.harga_sekarang
    def pnl(self):
        return self.nilai_aset()-self.modal
    def persentase(self):
        return (self.pnl()/self.modal)*100
    def to_dict(self):
        return {
            'nama': self.nama,
            'modal': self.modal,
            'harga': self.harga_rata_rata,
            'harga sekarang': self.harga_sekarang
        }

portofolio = []
print('==============================================\n'
      '                SFYFOLIO\n'
      '==============================================\n'
      '')
def load_data():
    global portofolio
    if not os.path.exists('portofolio.json'):
        portofolio=[]
        simpan_data()
        return
    with open('portofolio.json','r') as file:
        data = json.load(file)
    portofolio=[]
    for item in data:
        aset = Asset(
            item['nama'],
            item['modal'],
            item['harga'],
            item['harga sekarang']
      )
        portofolio.append(aset)
def simpan_data():
    data = []
    for aset in portofolio:
        data.append(aset.to_dict())
    with open('portofolio.json','w') as file:
        json.dump(data,file,indent=4)
def lihat_portofolio():
    if len(portofolio) == 0:
        print('Portofolio masih kosong')
        return
    total_modal = 0
    total_portofolio = 0
    total_pnl = 0
    print('\n========PORTOFOLIO ANDA========')
    for aset in portofolio:
        nilai_aset = aset.nilai_aset()
        pnl = aset.pnl()
        total_modal += aset.modal
        total_pnl += pnl
        total_portofolio += nilai_aset
        total_return = (total_pnl/total_modal)*100
    for aset in portofolio:
        nilai_aset = aset.nilai_aset()
        alokasi = nilai_aset/total_portofolio*100
        print('-------------------------------')
        print('Nama            :',aset.nama)
        print(f'Modal           : Rp.{aset.modal :,.0f}')
        print(f'Harga Rata-rata : Rp.{aset.harga_rata_rata :,.0f}')
        print(f'Harga sekarang  : Rp.{aset.harga_sekarang :,.0f}')
        print(f'Jumlah Aset     : {aset.jumlah_aset() :,.7f}')
        print(f'P/L             : Rp.{aset.pnl() :,.0f}')
        print(f'P/L(%)          : {aset.persentase() :,.2f}%')
        print(f'Alokasi aset    : {alokasi:,.2f}%')
        print(f'Nilai aset      : Rp.{aset.nilai_aset():,.0f}')
    print('================================')
    print(f'Total Modal      : Rp.{total_modal:,.0f}')
    print(f'Total Portofolio : Rp.{total_portofolio:,.0f}')
    print(f'Total P/L        : Rp.{total_pnl:,.0f}')
    print(f'Total Return     : {total_return:,.2f}%')

def tambah_aset():
    print('\n=====TAMBAH ASET=====')
    nama = input('Nama Aset :').strip()
    if nama == '':
        print('Nama aset tidak boleh kosong')
        return
    try:
        modal = int(input('modal(Rp) :'))
        if modal <= 0:
            print('Modal harus lebih dari 0')
            return
        harga_rata_rata = int(input('Harga rata-rata (Rp) :'))
        if harga_rata_rata <= 0:
            print('Harga rata rata harus lebih dari 0')
            return
        harga_sekarang = int(input('Harga sekarang  (Rp)  :'))
        if harga_sekarang <= 0:
            print('Harga sekarang harus lebih dari 0')
            return
    except ValueError:
        print('Input harus berupa angka')
        return
    aset = Asset(nama,modal,harga_rata_rata,harga_sekarang)
    portofolio.append(aset)
    simpan_data()
    print('Aset berhasil ditambahkan')
    print('\n===== DATA ASET =====')
    print('Nama Aset        :',nama)
    print('Modal            :',modal)
    print('Harga rata rata  :',harga_rata_rata)
    print('Harga Sekarang   :',harga_sekarang)
def edit_aset():
    print('\n=====EDIT ASET=====')
    nama = input('Nama aset:').strip().lower()
    ditemukan = False
    for aset in portofolio:
        if aset.nama.lower() == nama:
            ditemukan = True
            break
    if not ditemukan:
        print('Aset tidak ditemukan')
        return
    try:
        modal_baru = int(input('Modal baru  :'))
        if modal_baru <= 0:
            print('Modal harus lebih dari 0')
            return
        harga_rata_rata_baru = int(input('Harga rata rata baru  :'))
        if harga_rata_rata_baru <= 0:
            print('Harga rata rata harus lebih dari 0')
            return
        harga_baru = int(input('Harga Baru  :'))
        if harga_baru <= 0:
            print('Harga baru harus lebih dari 0')
            return
    except ValueError:
        print('Input harus berupa angka')
        return
    aset.modal = modal_baru
    aset.harga_rata_rata = harga_rata_rata_baru
    aset.harga_sekarang = harga_baru
    simpan_data()
    print('Data berhasil diubah')
def hapus_aset():
    print('=====HAPUS ASET=====')
    nama = input('Aset yang ingin dihapus:').lower().strip()
    ditemukan = False
    for aset in portofolio:
        if aset.nama.lower() == nama:
            ditemukan = True
            break
    if not ditemukan:
        print('Aset tidak ditemukan')
        return
    konfirmasi = input(f'Yakin ingin menghapus {aset.nama} (y/n):').lower().strip()
    if konfirmasi == 'y':
        portofolio.remove(aset)
        simpan_data()
        print('Aset berhasil dihapus')
    elif konfirmasi == 'n':
        print('Penghapusan dibatalkan')
    else:
        print('Masukkan hanya antara Y atau N')
def cari_aset():
    print('\n=====CARI ASET=====')
    nama = input('Nama Aset :').strip().lower()
    ditemukan = False
    for aset in portofolio:
        if aset.nama.lower() == nama:
            print('Nama            :', aset.nama)
            print(f'Modal           : Rp.{aset.modal:,.0f}')
            print(f'Harga Rata-rata : Rp.{aset.harga_rata_rata:,.0f}')
            print(f'Harga sekarang  : Rp.{aset.harga_sekarang:,.0f}')
            print(f'Jumlah Aset`    : {aset.jumlah_aset():,.7f}')
            print(f'P/L             : Rp.{aset.pnl():,.0f}')
            print(f'P/L(%)          : {aset.persentase():,.2f}%')
            print(f'Nilai aset      : Rp.{aset.nilai_aset():,.0f}')
            ditemukan = True
            break
    if not ditemukan:
        print('Aset tidak ditemukan')
        return

while True:
    load_data()
    print('1. Lihat Portofolio\n'
          '2. Tambah Aset\n'
          '3. Edit Aset\n'
          '4. Hapus Aset\n'
          '5. Cari Aset\n'
          '6. Keluar\n'
          )
    menu = input('Pilih Menu:')
    if menu=='1':
        lihat_portofolio()
    elif menu=='2':
        tambah_aset()
    elif menu=='3':
        edit_aset()
    elif menu=='4':
        hapus_aset()
    elif menu=='5':
        cari_aset()
    elif menu=='6':
        break
    else:
        print('Menu tidak tersedia')