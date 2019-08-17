month = input("Input your month:").lower()

if month == "january" or month == 'february' or month == 'december':
    print("It's winter")
elif month == 'march' or month == 'april' or month == 'may':
    print("It's spring")
elif month == 'june' or month == 'july' or month == 'august':
    print("It's summer")
elif month == 'september' or month == 'october' or month == 'november':
    print("It's autumn")
else:
    print("Unknown month")
