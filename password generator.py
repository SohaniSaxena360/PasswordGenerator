import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','@','#','$','%','%','^','&','*','(',')','_','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to the pypassword Generator!")
nr_letters = int(input("how many letters do you like in your password\n"))
nr_symbols = int(input(f"how many symbols do you like in your password\n"))
nr_numbers = int(input(f"how many numbers do you like in your password\n"))
password_list = []
for char in range(1 ,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1,nr_numbers + 1):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = " "
for char in password_list:
    password += char
print(f"your password is :{password}")
