class Ucus():
  havayolu = 'THY'

  def  __init__(self, kod,kalkış, varış, süre, kapasite, yolcu):
    self.kod = kod
    self.kalkış = kalkış
    self.varış = varış
    self.süre = süre
    self.kapasite = kapasite
    self.yolcu = yolcu
  
  def anons_yap(self):
    print(f"{self.kod}, sefer sayılı uçağımız {self.kalkış} dan {self.varış} a {self.süre} dakika sürecektir.")

  def koltuk_sayısı_güncelle(self):
    return self.kapasite - self.yolcu

  def bilet_satıs(self, bilet_adedi = 1):
    if bilet_adedi + self.yolcu <= self.kapasite:
      self.yolcu += bilet_adedi 
      self.koltuk_sayısı_güncelle()
      print(f"{bilet_adedi} adet koltuk satılmıştır. kalan koltuk adedi {self.koltuk_sayısı_güncelle()}.")
    else:
      print('Mevcut kapasiteyi aştığınızdan dolayı, işlem gerçekleitirilemedi.')
  
  def bilet_iptal(self, bilet_sayısı = 1):
    if self.yolcu >= bilet_sayısı:
      self.yolcu -= bilet_sayısı
      self.koltuk_sayısı_güncelle()
      print('{} adet koltuk iptal edilmiştir. Güncel koltuk sayısı : {} dır.'.
            format(bilet_sayısı, self.koltuk_sayısı_güncelle()))
    else:
      print('işlem başarısız.')

  def hava_şartları_rötar(self, rötar_süresi):
    self.süre += rötar_süresi   
    print(f" {self.kod} sefer sayılı {self.kalkış} dan {self.varış} giden uçagımız \
    {rötar_süresi} dak. rötar yapmıştır. {self.süre} de ulaşacaktır. ")

ucus3 = Ucus('TK54', 'USA', 'IST', 240, 250, 240)
ucus3.koltuk_sayısı_güncelle()
ucus3.bilet_satıs(5)
ucus3.bilet_iptal(25)
ucus3.hava_şartları_rötar(45)
ucus3.anons_yap()

