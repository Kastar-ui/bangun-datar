import math
class persegi:
 def __init__(self,sisi):
  self.sisi=sisi
 def luas(self):
  return self.sisi* self.sisi
 def keliling(self):
  return self.sisi*4
class segipanjang:
 def __init__(self,panjang,lebar):
  self.panjang=panjang
  self.lebar=lebar
 def luas(self):
  return self.panjang*self.lebar
 def keliling(self):
  return 2*(self.panjang+self.lebar)
class segitiga:
 def __init__(self,alas,tinggi):
  self.alas=alas
  self.tinggi=tinggi
 def luas(self):
  return (self.alas*self.tinggi)/2
 def keliling(self):
  return self.alas+self.tinggi+math.sqrt(self.alas**2+self.tinggi**2)
class belahketupat:
 def __init__(self,diagonal1,diagonal2):
  self.diagonal1=diagonal1
  self.diagonal2=diagonal2
 def luas(self):
  return self.diagonal1*self.diagonal2*(1/2)
 def keliling(self):
  return 4*math.sqrt((self.diagonal1/2)**2+(self.diagonal2/2)**2)
class lingkaran:
 def __init__(self,jari):
  self.jari=jari
 def luas(self):
  return self.jar**2*(22/7)
 def keliling(self):
  return self.jari*2*(22/7)
