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