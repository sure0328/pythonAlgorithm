age = int(input("Enter your age:"))
if age < 0:
    print("Error")
elif age >= 0 and age<7:
	print("Free")
elif (age >= 7 and age < 14) or age >= 60:
	print("Half price")
else:
	print("Full price")