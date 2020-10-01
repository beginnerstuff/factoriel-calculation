

class FactorielCalculation:
    print("Faktoriyel hesaplama uygulamasına hoşgeldiniz\n")
    number = 0

    def factorielCalculate(self,arg):
        if arg == 0:
            return 1
        
        return arg * self.factorielCalculate(arg-1)

    def showResult(self):

        while True:
            try:
                self.number = int(input("Bir sayı giriniz:"))

                control = True
                while control:
                        result = self.factorielCalculate(self.number)
                        print("girmiş olduğunuz sayının faktoriyeli ",result," dir.")
                        control = False

            except ValueError:
                print("Lütfen pozitif bir sayı girdiğinize emin olunuz !!")


obj = FactorielCalculation()
obj.showResult()


