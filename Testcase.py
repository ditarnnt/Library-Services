from Library_System import Library
import pandas as pd

lib1 = Library()
lib = lib1.tambah_buku("Python",2021,3)

lib1.check_data_buku()

lib1.tambah_buku("Introduction to ML",2015,1)

lib1.check_data_buku()

lib1.update_judul("Introduction to ML","Introduction to ML ed 2")

lib1.check_data_buku()

lib1.check_pinjam_buku()

lib1.pinjam_buku('Introduction to ML ed 2')

lib1.check_pinjam_buku()

lib1.kembali_buku('Introduction to ML ed 2')

lib1.check_data_buku()