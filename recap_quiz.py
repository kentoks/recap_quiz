"""Recap quiz for question 17
Created by Kent Nago
February 21st 2022
"""

another = True
fastest = None

race = 0
races = []

while another:
    another += 1
    race = float(input("Enter time: "))
    races.append(race)
    print(f'Okay, {round(race,0)} seconds!') #round to 1dp

    another = int(input("Would you want to enter more? Yes = 1, No = 2 "))
    if another == 1:
        another = True
    else:
        print()
        print('This is what you have entered!!: ')
        for i in races:
            print(f'{i} seconds')
        break

print()
average = sum(races) / len(races)
print("So, The average is", average)


fastest = min(races)
print(f'And the fastest time is {fastest} seconds')
