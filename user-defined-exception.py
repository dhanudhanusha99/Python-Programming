class LogInError(Exception) :pass
try:
	user_name1="abcde"
	password1="A123"
	user_name2=input("Enter the username : ")
	password2=input("Enter the password : ")
	if user_name1==user_name2 and password1==password2:
		print("Successfull login")
	else:
		raise LogInError("Invalid username or password")
except LogInError as e:
	print(e)