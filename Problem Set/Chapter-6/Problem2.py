m1 = int(input("Enter the marks for subject 1: "))
m2 = int(input("Enter the marks for subject 2: "))
m3 = int(input("Enter the marks for subject 3: "))

total = (m1 + m2 + m3) / 300

if(m1 >= 33 and m2 >= 33 and m3 >= 33):
    if total >= 0.4:
        print("Congratulations! You have passed the exam.")
    else:
        print("Sorry! You have failed the exam as your average percentage is less than 40%.")
else:
    print("Sorry! You failed to score above 33 in one or more subjects. You have failed the exam.")
