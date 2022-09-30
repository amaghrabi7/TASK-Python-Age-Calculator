from datetime import date


def get_dob():
    # write code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))
	return date(year, month, day)


def get_age(dob):
    # write code here
	today = date.today()
	difference = today - dob
	return difference.days // 365

# print(get_age(get_dob()))

def main():
	# write code here
	dob = get_dob()
	if dob > date.today():
		print("Invalid birthdate.")
	else:
		print(f"You are {get_age(dob)} years old.")
	


if __name__ == '__main__':
    main()
