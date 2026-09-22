            #VALIDADOR DE NOTAS CON PROMEDIO
#Bosquejo
    #Notas a cargar: -60, 80, 40, 200

    #¿-60 válida?  -60 < 0        → NO
    #¿80 válida?   0 ≤ 80 ≤ 100   → SÍ  → notas = [80]
    #¿40 válida?   0 ≤ 40 ≤ 100   → SÍ  → notas = [80, 40]
    #¿200 válida?  200 > 100      → NO

    #Lista final: [80, 40]
    #Promedio: (80 + 40) / 2 = 60.0

class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-30,60,20,120))
print(cal.promedio())