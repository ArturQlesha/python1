#Stałe do obliczeń
szer=29
gest_mat={'stal':0.00786, 'alu':0.00270}
mat=input("Podaj jaki materiał chcesz wyliczyć. Wybierz: stal lub alu: " )
print("Wybrałeś: "+mat)
g=float(gest_mat.get(mat))

#funkcje
def obj_mat(sr_pret, dl_pret):
    V=((3.14*(sr_pret**2))/4)*dl_pret
    return V

def wagaKG(V,g):
    C=(V*g)/1000
    return C
    

#Wprowadzanie zmiennych
sr_pret=float(input("Podaj średnicę pręta w mm: "))
dl_pret=float(input("Podaj długość pręta w mm: "))
print ("\nWybrałeś dane do obliczenia ciężaru. \n Średnica: {}mm\n długość pręta: {:.0f}mm\n".format(sr_pret,dl_pret))

#Obliczenie objętości i wagi pręta
V=obj_mat(sr_pret, dl_pret)
#print("Objętość= {:6.2f}".format(obj_mat(sr_pret,dl_pret)))
#rint ("Gęstość materiału dla {} wynosi {:1.6f}".format(mat,(gest_mat[mat])))
C=wagaKG(V,g)

#Prezentacja danych
print ("| Wymiar pręta | Waga pręta |")
print ("|    [mm]      |   [kg]     |")
print ("-" *szer)
print ("|{:6.1f} x {:5.0f}|{:12.1f}|" .format(sr_pret,dl_pret,C))
print ("-" *szer)

#Obliczenie ceny
cena_kg=float(input("Podaj cenę za kilogram w zł: "))
print("Koszt materiału: {:.2f}".format(C*cena_kg))

#zapisywanie wyników do pliku
import datetime
x = datetime.datetime.now()
print(x.strftime("%c"))
f = open("waga.txt", "w")
f.write("Przygotowano w dniu {}\nCiężar pręta: {:6.2f}, cena za kg: {:2.2f}zł, koszt materiału {:5.2f}".format(x.strftime("%c"),C,cena_kg,(C*cena_kg)))
f.close()