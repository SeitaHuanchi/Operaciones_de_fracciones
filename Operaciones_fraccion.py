def mcd(m,n):
    while m%n != 0:
        mViejo = m
        nViejo = n

        m = nViejo
        n = mViejo%nViejo
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
		
	
	def addition (self,other):
		numerator= self.numerator*other.denominator + self.denominator*other.numerator
		denominator= self.denominator* other.denominator
		comun = mcd(numerator,denominator)
		return Fraction(numerator//comun, denominator//comun)

	def rest (self,other):
		numerator= self.numerator*other.denominator - self.denominator*other.numerator
		denominator= self.denominator* other.denominator
		comun = mcd(numerator,denominator)
		return Fraction(numerator//comun, denominator//comun)
	
	    
	def multiplication (self,other):
		numerator= self.numerator * other.numerator
		denominator= self.denominator * other.denominator
		return Fraction(numerator,denominator)

	def division (self,other):
		numerator=self.numerator*other.denominator
		denominator=self.denominator*other.numerator
		return Fraction(numerator,denominator)	
		
while True:
	numerator=int(input("Indique el Valor del 1er numerador: "))
	denominator=int(input("Indique el valor del 1er denominador: "))

	a=Fraction(numerator,denominator)
	print("Primera Fraccion: ",str(a),"\n")

	numerator=int(input("Indique el Valodr del 2er numerador: "))
	denominator=int(input("Indique el valor del 2er denominador: "))

	b=Fraction(numerator,denominator)
	print("Segunda Fraccion: ",str(b),"\n")


	operation=input("Indique la operacion con simbolos (+, -, *, /): ")

	if operation == '+':
		result= a.addition(b)
		print("1era Fraccion + 2da Fraccion = ",str(result))

	elif operation == '-':
		result= a.rest(b)
		print("1era Fraccion - 2da Fraccion = ",str(result))

	elif operation == '*':
		result= a.multiplication(b)
		print("1era Fraccion * 2da Fraccion = ",str(result))

	elif operation == '/':
		result= a.division(b)
		print("1era Fraccion / 2da Fraccion = ",str(result))

	else:
		print("Indique una operacion valida")

	if input("\nOtra operacion? s/n : \n") == 'n':
		break
