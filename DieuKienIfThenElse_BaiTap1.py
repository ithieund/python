score = input("Enter your score: ")
score = int(score)

# Basic solution - nested
if score >= 90:
    print('grade is A')
else:
    if score >= 80:
        print('grade is B')
    else:
        if score >= 70:
            print('grade is C')
        else:
            if score >= 60:
                print('grade is D')
            else:
                print('grade is F')

# Advanced solution
if score >= 90:
    print('grade is A')
elif score >= 80:
    print('grade is B')
elif score >= 70:
    print('grade is C')
elif score >= 60:
    print('grade is D')
else:
    print('grade is F')