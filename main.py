#import eminmodule #Bu şekilde tüm kütüphaneyi çağırdık.Ama;
#eminmodule.example_func() #Tüm kütüphane çağrılırsa bu şekilde çalışır.

from eminmodule import example_func #Bu şekilde sadece eminmodule'de example_func çağırdık.
example_func() #from eminmodule import example_func, bu şekilde yazılırsa çalışır.

from AnimalPackage import info
info.info()

from AnimalPackage.CatPackage import meow #Paketin içindeki alt paketi çağırırken.

#meow dosyasında;if __name__=="__main__": yazdığımız için herhangi bir fonksiyon çağrılmasa => 
#direk import olacak kısımı çalıştırdı.