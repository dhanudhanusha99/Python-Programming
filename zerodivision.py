try:
	a=int(input("Enter the numerator : "))
	b=int(input("Enter the denominator : "))
	print("Result after division : "%(a/b))
except(ZeroDivisionError,ValueError) as er:
	print(er)
else:
	print("Successfully Executed ")
finally:
	print("Executed")