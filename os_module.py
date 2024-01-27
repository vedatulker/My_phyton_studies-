import os

print(os.getcwd())
os.chdir("/Users/vedat/Desktop/git-lesson")
print(os.getcwd())
print(os.listdir())
print(os.listdir("/Users/vedat/Desktop/phyton çalışmalarım/\My_phyton_studies-"))
for dosya in os.listdir():
    print(dosya)
os.chdir("/Users/vedat/Desktop/phyton çalışmalarım/\My_phyton_studies-")
print(os.getcwd())
print(os.listdir())
for dosya in os.listdir():
    print(dosya)
os.chdir("/Users/vedat/Desktop/git-lesson")
print(os.listdir())
#os.makedirs('Clarusway/Deneme/Os_module')  # İç içe klasör oluşturma
#mkdir('DEnene') sadece bir klasör oluşturur
os.rmdir('Deneme Klasörü')  # silme işlemi
