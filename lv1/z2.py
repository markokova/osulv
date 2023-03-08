try:
    number = float(input("Enter a number in interval [0, 1]:"))
    if number < 0 or number > 1:
        print("Number is out of interval.")
    if 0.9 <= number <= 1:
        print('A')
    if 0.8 <= number <= 0.9:
        print('B')
    if 0.7 <= number <= 0.8:
        print('C')
    if 0.6 <= number <= 0.7:
        print('D')
    if 0.6 > number >= 0:
        print('F')
except:
    print("You have to type in a number.")