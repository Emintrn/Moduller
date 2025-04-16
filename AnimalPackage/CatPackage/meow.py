def speak_direct():
    print("meow dosyası kendi içinde çalıştırıldığında çalışır.")

def speak_imported():
    print("meow dosyası başka bir kodda import edince çalışır.")

if __name__=="__main__": #__maim__ anlamı, ana dosyanın kendisi yani burada meow dosyasıdır.
    speak_direct()
else:
    speak_imported()