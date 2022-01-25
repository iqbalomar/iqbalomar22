print("Hello to my first game here :p")
name=str(input("What's your name? "))
#print(name)
age=int(input("What's your age? "))
#print(age)
if age>=18:
    print("You are old enough to play :p")
    ques = str(input("Do you wanna play? "))
    if ques == "yes":
        print("Let's play")
        print("We will start with 10 rounds")
        choice = str(input(" Choose ... left/right? ..."))
        if choice == "left":
            path = str(input("Great!, now you're infront of a lack would you go across or swim?"))
            if path =="swim":
                print("Sorry!, try another option")
            else:
                other = str(input("You managed to get across, but we're bit by a fish and lost 5 healths. You notice a house and a river, which one you choose?"))
                if other =="river":
                    print("You fell in the river and lost")
                else:
                    print("You win ")
                    print("Welcome Home")
        else:
            print("You lost!!")



else:
    print("You are still a baby, come back when you are older :p")

