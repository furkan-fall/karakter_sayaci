#Renk katmak için colorama  kütüphanesi kullandım
import colorama

#Önce gerekli değişkenleri oluşturalım

font_color = colorama.Fore.LIGHTRED_EX  #font rengi
inputs_colors = colorama.Fore.LIGHTYELLOW_EX #input rengi
sayi_colors = colorama.Fore.LIGHTMAGENTA_EX #karakter sayısı rengi
print("")
uyarı_metni = colorama.Fore.RED+colorama.Style.BRIGHT+f"""\t\t\t\t\t\t\t＊＊＊ Ｂｕ  ｐｒｏｇｒａｍ  ｇｉｒｄｉｎｉｉｚ  ｂｉｒ  ｍｅｔｎｉｎ  ｓｉｚｅ  ｋａｒａｋｔｅｒ  ｄｅｅｒｉｎｉ  ｇöｓｔｅｒｉｒ．＊＊＊ \n""" #uyarı değişkenine gerekli metni atadım.
print(uyarı_metni) #Uyarı metnini göster

kullanici_girdi = input( inputs_colors+colorama.Style.BRIGHT+f"Lütfen Adınızı Giriniz:{colorama.Fore.WHITE+colorama.Style.BRIGHT} ")
print("") #kullanıcıdan input("Girdi") alıyoruz bu girdiyi de bir değişkene atıyoruz.. 
karakter_hesaplama =  len(kullanici_girdi) #len fonksiyonu ile kullanıcıdan gelen inputu alıp kaç karakter olduğunu hesaplıyoruz.

#Burada formatted str ile sonuçları gösteriyoruz, str ve int bir arada yazmak için kullandım "," kullansamda olur

print(font_color +f"Adınızın Karakter Sayısı -> "+ f"{sayi_colors}{colorama.Style.BRIGHT}{karakter_hesaplama}\n")

#Direk kapanmasını önlemek için boş bir input 
input(colorama.Fore.LIGHTWHITE_EX+colorama.Style.BRIGHT+"Çıkmak için herhangi bir tuşa basınız....")

print("")
print("")

