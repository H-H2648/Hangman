import turtle
import random




def draw(hanger, check):
    if check == 0:
        hanger.left(90)
        hanger.forward(200)
        hanger.right(90)
        hanger.forward(50)
        hanger.right(90)
        hanger.forward(10)
    if check == 1:
        hanger.right(90)
        hanger.circle(30)
        hanger.penup()
        hanger.circle(30, 180)
        hanger.pendown()
    if check == 2:
        hanger.right(90)
        hanger.forward(70)
    if check == 3:
        hanger.backward(45)
        hanger.left(30)
        hanger.forward(50)
    if check == 4:
        hanger.backward(50)
        hanger.right(60)
        hanger.forward(50)
    if check == 5:
        hanger.backward(50)
        hanger.left(30)
        hanger.forward(50)
        hanger.left(30)
        hanger.forward(45)
    if check == 6:
        hanger.backward(45)
        hanger.right(60)
        hanger.forward(45)


def start_game():
    decide = input("Play game? (Anything other than a 'no' is considered a yes)")
    if decide == "no":
        return False
    else:
        return True


def play_game():
    decide = start_game()
    hanger = turtle.Turtle()
    hanger.hideturtle()
    while decide:
        value = random.randint(0, 4096)
        count = 0
        complete = False
        dictionary = open("dictionary.txt", "r")
        lines = dictionary.readlines()
        word = lines[value]
        mystery_word = ""
        lst = []
        for i in range(len(word) - 1):
            mystery_word = mystery_word + "_"
        draw(hanger, count)
        while count < 6 and not complete:
            print("Your word now looks like this: " + mystery_word)
            guess = input("Make your guess! (Please guess one letter at a time): ")
            if guess in lst:
                print("You already made this guess")
            elif len(guess) != 1:
                print("Please read the instruction.")
                continue
            elif guess in word:
                print("You made a correct guess")
                lst.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        mystery_word = mystery_word[:i] + guess + mystery_word[i + 1:]
                if "_" not in mystery_word:
                    complete = True
                    print(complete)
            elif guess not in word:
                print("You made an incorrect guess")
                lst.append(guess)
                count += 1
                print("You now have " + str(6 - count) + " guesses left.")
                draw(hanger, count)
        if complete:
            print("You won!")
            print("The word was " + word)
            decide = start_game()
        elif count == 6:
            print("You lost!")
            print("The word was " + word)
            decide = start_game()


play_game()
