#def mifuncion(texto):
#    print(texto)
#print("chau")      
#mifuncion("Hola como estas")
#el programa primero llama a al funcion pero como en este caso esta mal idententado primero 
# imprime chau y despues hola como estas 
#para recorrer se debe utilizar while para saber si es un numero primo o no diviendo por diferentes numeros

import unittest        

def is_primo(value ):
    if  value <= 2:  # Los números menores o iguales a 1 no son primos
        return True
    for i in range(2, int(value**0.5) + 1):  # Iteramos desde 2 hasta la raíz cuadrada de 'numero'
        if value % i == 0:  # Si 'numero' es divisible por 'i', entonces no es primo
            return False
    return True 

class Testprimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True) 
    
    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)
    
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(9)
        self.assertEqual(result, False)

unittest.main()

#no se modifican las reglas(test) solamente se modifica la funcion
#para que funcionen todos los test 

