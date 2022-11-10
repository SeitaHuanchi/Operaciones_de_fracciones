def mcd(m,n):
    while m%n != 0:
        m_old = m
        n_old = n

        m = n_old
        n = m_old%n_old
    return n
	    
class Fraction:
	
	numerator=0 
	denominator=1

	def __init__(self, numerator, denominator):
		self.numerator = int(numerator)
		if denominator ==0:
			raise Exception("No se puede usar 0 en el denominador")
		self.denominator = int(denominator)

	def __str__(self):
		return str(self.numerator)+ "/" + str(self.denominator)
		
	
	def addition (self,otherfrac):
		numerator= self.numerator*otherfrac.denominator + self.denominator*otherfrac.numerator
		denominator= self.denominator* otherfrac.denominator
		comun = mcd(numerator,denominator)
		return Fraction(numerator//comun, denominator//comun)

	def rest (self,otherfrac):
		numerator= self.numerator*otherfrac.denominator - self.denominator*otherfrac.numerator
		denominator= self.denominator* otherfrac.denominator
		comun = mcd(numerator,denominator)
		return Fraction(numerator//comun, denominator//comun)
	
	    
	def multiplication (self,otherfrac):
		numerator= self.numerator * otherfrac.numerator
		denominator= self.denominator * otherfrac.denominator
		return Fraction(numerator,denominator)

	def division (self,otherfrac):
		numerator=self.numerator*otherfrac.denominator
		denominator=self.denominator*otherfrac.numerator
		return Fraction(numerator,denominator)	
		

numerator=int(input("Indique el Valor del 1er numerador: "))
denominator=int(input("Indique el valor del 1er denominador: "))

fract_1=Fraction(numerator,denominator)
print("Primera Fraccion: ",str(fract_1),"\n")

numerator=int(input("Indique el Valodr del 2er numerador: "))
denominator=int(input("Indique el valor del 2er denominador: "))

fract_2=Fraction(numerator,denominator)
print("Segunda Fraccion: ",str(fract_2),"\n")


operation=input("Indique la operacion con simbolos (+, -, *, /): ")

if operation == '+':
		result= fract_1.addition(fract_2)
		print("1era Fraccion + 2da Fraccion = ",str(result))

elif operation == '-':
		result= fract_1.rest(fract_2)
		print("1era Fraccion - 2da Fraccion = ",str(result))

elif operation == '*':
	result= fract_1.multiplication(fract_2)
	print("1era Fraccion * 2da Fraccion = ",str(result))

elif operation == '/':
		result= fract_1.division(fract_2)
		print("1era Fraccion / 2da Fraccion = ",str(result))

else:
	print("Indique una operacion valida")
