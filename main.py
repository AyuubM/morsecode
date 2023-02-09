from data import morse_code


user_ans = input("What would you like translate to Morse Code?: ")


for char in user_ans:
    for i in morse_code.keys():
        if char.upper() == i:
            print(morse_code.get(i), end="/")

