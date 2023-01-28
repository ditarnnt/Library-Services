import pandas as pd

class Library:
    def __init__(self):
      self.data_buku = dict()
      self.buku_dipinjam = dict()
    
    #function for adding book in library 
    def tambah_buku (self, judul, tahun, jumlah):
      self.data_buku.update({judul: [tahun,jumlah]})
    
    #function for update the tittle
    def update_judul(self, judul, judul_baru):
      temp = self.data_buku[judul]
      self.data_buku.pop(judul)
      self.data_buku.update({judul_baru: temp})
    
    #function for update the year of the book
    def update_tahun (self,judul, tahun_baru):
      self.data_buku[judul][0] == tahun_baru
   
    #function for update the total of the book 
    def update_jumlah (self,judul, jumlah_baru):
      self.data_buku[judul][1] == jumlah_baru
    
    #function for check the list of availability book in library 
    def check_data_buku(self):
        if(len(self.data_buku) == 0):
            print('Perpustakaan Kosong')
        else:
            # print(self.data_buku)
            data = pd.DataFrame(self.data_buku).T
            data.columns = ['Tahun Terbit', 'Jumlah Buku']
            print(data.to_markdown())
   
   #function for reset the list of the book 
    def reset_data (self):
      self.data_buku.clear()

    #function for borrow the book in library 
    def pinjam_buku(self,judul):
      if (self.data_buku[judul][1]==0):
        print('Maaf buku sudah habis')
      else:
        self.update_jumlah(judul, self.data_buku[judul][1]-1)
        try: 
          self.buku_dipinjam[judul][1] == self.buku_dipinjam[judul][1]+1
        except:
          self.buku_dipinjam.update({judul: [self.data_buku[judul][0],1]})
    
    #function for returned the book to library 
    def kembali_buku(self,judul):
       if(self.buku_dipinjam[judul][1]-1 == 0):
         self.buku_dipinjam.pop(judul)
       else:
         self.buku_dipinjam[judul][1] = self.buku_dipinjam[judul][1]-1    
       self.update_jumlah(judul, self.data_buku[judul][1]+1)
    
    #function for check list book that borrow 
    def check_pinjam_buku(self):
        if(len(self.buku_dipinjam) == 0):
            print('Tidak ada buku yang sedang dipinjam')
        else:
            # print(self.data_buku)
            data = pd.DataFrame(self.buku_dipinjam).T
            data.columns = ['Tahun Terbit', 'Jumlah Buku']
            print(data.to_markdown())

