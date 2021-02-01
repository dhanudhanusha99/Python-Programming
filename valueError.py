try:
	n=int(input("Enter the number : "))
	if n<90 or n>120:
		raise ValueError('Number not in range')
except ValueError as ve:
	print('Number entered is not in the range 90-120')
	print(ve)
else:
	print('Number is : ',n)