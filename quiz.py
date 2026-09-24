score = 0 
answer1 = input("What is the largest planet in our solar system?")

if answer1 == "Jupiter":
    print("Correct")
    score = score + 1
else:
    print("Wrong, the answer is Jupiter.")
answer2 = input("How many sides does a hexagon have?")
if answer2 == "6":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 6!")
answer3 = input("What program are you learning?")
if answer3 == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is python!")
    
print("Your score is", score)
if score == 3:
    print("Perfect score!")
elif score == 2:
    print("Eh.")
elif score == 1:
    print("Damn that's bad, lol.")
else:
    print("Dumbass.")