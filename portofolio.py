class Portofolio:
    def __init__(self):
        self.aset =[]
    def total_modal(self):
        total = 0
        for aset in self.aset:
            total += aset.modal
        return total
    def total_portofolio(self):
        total = 0
        for aset in self.aset:
            total += aset.nilai_aset()
        return total
    def total_pnl(self):
        total = 0
        for aset in self.aset:
            total += aset.pnl()
        return total
    def total_return(self):
        return self.total_pnl()/self.total_modal()*100
    def alokasi(self, aset):
        return aset.nilai_aset()/self.total_portofolio()*100
    def to_dict(self):
        data = []
        for aset in self.aset:
            data.append(aset.to_dict())
        return data
portofolio = Portofolio()