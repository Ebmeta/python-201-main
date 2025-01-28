# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
num_set = set()
points = 5
item = 10
while points >= 0 and item >= 0:
    if points == 0 :
        print("Game over")
        break
    if item == 0 :
        print("You win .Then typing numbers, you never dublicated " , num_set)
        break

    num = int(input(f'Typing a number that you have not entered before. You have {points} attempt :'))
    if num in num_set :
        print("The number was already in the set . TRy again")
        points -= 1
        continue
    num_set.add(num)
    item -= 1

