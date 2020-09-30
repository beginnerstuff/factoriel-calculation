

print("Faktoriyel hesaplama uygulamasına hoşgeldiniz\n")

        
def factoriel(sayı):
    if sayı == 0:
        return 1
    return sayı * factoriel(sayı-1)

while True:
    try:
        number = int(input("Bir sayı giriniz:"))
        print("girmiş olduğunuz sayının faktoriyeli ",factoriel(number)," dir.")
        input("\nçıkmak için bir tuşa basınız.")
        break

    except ValueError:
        print("Lütfen pozitif bir sayı girdiğinize emin olunuz !!")

