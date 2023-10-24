def move_forward():
    print("moving forward\n")

def turn(direction):
    print(f"turning {direction}\n")

def start_engine():
    print("starting engine\n")

def stop_engine():
    print("stopping engine\n")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout\n")

def menu():
    option=9
    while option not in [0,1,2,3,4,5,6,7]:
        print ("1. Library")
        print ("2. Tech Park")
        print ("3. Hospital")
        print ("4. Mall")
        print ("5. Airport")
        print ("6. University")
        print ("7. Stadium")
        print ("0. Exit")
        option = int(input("Please introduce your destination: "))
        if option not in [0,1,2,3,4,5,6,7]:
            print ("\nWrong option. Try again.\n")
    return option

destination = menu()

start_engine()

if destination == 1: #library
    move_forward()
    turn("left")

if destination == 2: #Tech park
    move_forward()
    turn("right")

if destination>= 3 and destination<=7:
    move_forward()
    print ("Entering rondabout\n")
    if destination == 3:
        follow_roundabout(1)
    if destination == 4:
        follow_roundabout(2)
    if destination == 5:
        follow_roundabout(3)
    if destination == 6:
        follow_roundabout(4)
        turn("left")
    if destination == 7:
        follow_roundabout(5)
        turn("right")

print("\nYou've arrived to your destination.\n")

stop_engine()