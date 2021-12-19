from program_bangun import persegi,segipanjang,segitiga,belahketupat,lingkaran
while True:
 print "Di bawah ini pilihlah program Bangun Ruang...!:"
 print "1.Persegi"
 print "2.segipanjang"
 print "3.segitiga"
 print "4.belahketupat"
 print "5.lingkaran"
 print "6.keluar"
 a=int(raw_input("masukkan angka pilihian diatas:"))
 if a==1:
  print "anda memilih persegi"
  print "1.luas\n 2.keliling\n3.kembali\n"
  x=int(raw_input("masukkan pilihan"))
  while True:
   if x==1:
    y=float(raw_input("masukkan sisi"))
    c=persegi(y)
    print "luasnya adalah:",c.luas()
    break
   elif x==2:
    y=float(raw_input("masukkan sisi"))
    c=persegi(y)
    print "kelilingnya adalah",c.keliling()
    break
   elif x==3:
    print "kembali"
    break
   else:
    print "salah"
 elif a==2:
  print "Anda memilih Segipanjang!"
  print "1.Luas\n2.Keliling\n3.Kembali\n"
  x=int(raw_input("masukkan pilihan:"))  
  while True:
   if x==1:
    y=float(raw_input("masukkan panjang:"))
    o=float(raw_input("masukkan lebar:"))
    c=segipanjang(y,o)
    print "luasnya adalah:",c.luas()
    break
   elif x==2:
    y=float(raw_input("masukkan panjang:"))
    o=float(raw_input("masukkan lebar:"))
    c=segipanjang(y,o)
    print "kelilingnya adalah:",c.keliling()
    break
   elif x==3:
    print "kembali"
    break
   else:
    print "pilihan salah coba lagi!"
 elif a==3:
  print "anda memilih segitiga:"
  print "masukkan pilihan di bawah ini:"
  print "1.Luas\n2.Keliling\n3.Kembali"
  x=int(raw_input("masukkan pilihan"))
  while True:
   if x==1:
    print "Anda memilih luas:"
    y=float(raw_input("masukkan alas:"))
    o=fliat(raw_input("masukkan tinggi:"))
    c=segitiga(y,o)
    print "Luasnya adalah: ",c.luas()
    break
   elif x==2:
    print "Anda memilih Keliling:"
    y=float(raw_input("Masukkan alas   : "))
    o=float(raw_input("masukkan tinggi:"))
    c=segitiga(y,o)
    print "kelilingnya adalah:",c.keliling()
    break
   elif x==3:
    print "kembali"
    break
   else:
    print "Pilihan Anda salah coba lagi"
 elif a==4:
  print " Anda memilih Belah Ketupat!"
  print "pilihlah menu di bawan ini!"
  print "1.Luas\n2.Keliling\n3.Kembali\n"
  x=int(raw_input("Masukkan Pilihan Anda:"))
  while True:
   if x==1:
    print "anda memilih Luas!"
    y=float(raw_input("Masukkan Diagonal Ke-1: "))
    o=float(raw_input("masukkan Diagonal Ke-2: "))
    c=belahketupat(y,o)
    print "Luas Belahketupat Adalah:  ",c.luas()
    break
   elif x==2:
    print "anda memilih Keliling: "
    y=float(raw_input("Masukkan Diagonal Ke-1: "))
    o=float(raw_input("Masukkan Diagonal Ke-2: "))
    c=belahketupat(y,o)
    print "kelilingnya adalah: ",c.keliling()
    break
   elif x==3:
    print "Kembali!"
    break
   else:
    print "Pilihan Salah!! coba lagi!!"
 elif a==5:
  print "Anda Memilih Lingkaran!!"
  print "masukkan pilihan di bawah Ini:"
  print "1.Luas\n2.Keliling\n3.Kembali\n"
  x=int(raw_input("Masukkan Pilihan:")) 
  while True:
   if x==1:
    print "Anda memilih Luas!"
    y=float(raw_input("Masukkan Jari-jari Lingkaran!:"))
    c=lingkaran(y)
    print "Luas Lingkarannya adalah:  ",c.luas()
    break
   elif x==2:
    print "Anda memilih Keliling!"
    y=float(raw_input("Masukkan Jari-jari Lingkaran: "))
    c=lingkaran(y)
    print "keliling Lingkarannya adalah:",c.keliling()
    continue
    break
   elif x==3:
    print "Kembali"
    break
   else:
    print "Pilihan salah Coba lagi!!....:"
 elif a==6:
  print "keluar"
  break
 else:
  print "pilihan salah..!, coba lagi!:"
