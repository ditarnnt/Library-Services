from Perpustakaan import Library
import pandas as pd

lib1 = Library()
lib = lib1.tambah_buku("Sukses Python",2021,3)

lib1.check_data_buku()

lib1.tambah_buku("Sukses Python3",2015,1)

lib1.check_data_buku()

lib1.update_judul("Sukses Python","Sukses Python9")

lib1.check_data_buku()

lib1.check_pinjam_buku()

lib1.pinjam_buku('Sukses Python9')

lib1.check_pinjam_buku()

lib1.kembali_buku('Sukses Python9')

lib1.check_data_buku()