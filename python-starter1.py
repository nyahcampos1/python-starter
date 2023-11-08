import random

def ex1():
    Array = []
    for number in range(10):
        Array.append(random.randint(0, 100))
    sum = 0
    for num in Array:
         sum += num
    print(Array)
    print(f"The sum is: {sum}")

def ex2():
    width = input("Enter width: ")
    width = int(width)
    height = input("Enter height: ")
    height = int(height)
    length = input("Enter length: ")
    length = int(length)

    volume = width * length * height
    print(f"Volume is: {volume}")

def ex3():
    arr = [int(x) for x in input().split(",")]
    print(arr[0] == arr[-1]) #

def ex4():
    text = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    Array = [x for x in text.split()]
    count = 0
    for word in Array:
        if word == "Python":
            count += 1
    print(count)

def ex5():
    myList = [1,2,3]
    mySet = {3,4,5}
    listToSet = set(myList)

    newSet = listToSet.union(mySet)
    print(newSet)

def ex6():
    Array = [11, 100, 101, 999, 1001]
    print(list(reversed(Array)))

def ex7():
    number = random.randint(0,100)

    while (True):
        guess = int(input("Guess? "))
        if guess < 10:
            print("You lose.")
        elif guess > 10 and guess < 50:
            print("Try again.")
        elif guess > 50:
            print("You win!")
            break

def ex8():
    myList = [6,2,7,3,77,7,1]
    smallest = myList[0]

    for num in range(1, len(myList)):
        if myList[num] < smallest:
            smallest = myList[num]

    print(smallest)

def ex9():
    string = input("Enter string: ")
    if (string == string.upper()):
        print("True")
    else:
        print("False")

def ex10():
    Vs = 0
    Cs = 0
    string = input("Enter string: ")

    Vs = ["A" , "E" , "I" , "O" , "U"]

    for c in string:
        if c.upper() in Vs:
            vowels +=1
        else:
            consonants +=1
    print("Vowels: " + str(vowels))
    print("Consonants: " + str(consonants))

def ex11():
    today = date.today()
    with open('output.txt', 'w') as f:
        f.write(f"Today's date is {today:%d/%m/%Y}.")
    f.close()

def ex12():
    number = input("Enter integer: ")
    if ("." in number):
        print("Error")
    else:
        print(-1 *int(number))

def ex13():
    while (True):
        first = input("Enter first integer: ")
        if (first == "exit"):
            break
        second = input("Enter second integer: ")
        if (second == "exit"):
            break
        print(int(first) + int(second))