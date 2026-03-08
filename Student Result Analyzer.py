
def grades(marks):
    if marks>=80:
        return"A"
    elif marks>=60:
        return "B"
    elif marks>=40:
        return "C"
    else:
        return"Fail"

def get_marks(subject):
    while True:
        try:
            marks=int(input(f"Enter the mark you obtained in {subject}:"))
            if 0 <=marks <=100:
                return marks
            else:
                print("Invalid input, choose between 0-100")
        except ValueError:
            print("Invalid input, enter interger number")
while True:
    name= input("Enter your name")
    
    math=get_marks("Maths")
    sci=get_marks("Science")
    eng=get_marks("English")
                    
    math_grade= grades(math)
    sci_grade= grades(sci)
    eng_grade= grades(eng)

    print("Maths:",math_grade)
    print("Science:",sci_grade)
    print("English:",eng_grade)

    total_mark= math+sci+eng
    print("Total marks:",total_mark)

    avg=total_mark/3
    print("Average mark:",avg)

    if total_mark>=240:
        print("Grade: A")
    elif total_mark>=180:
        print("Grade: B")
    elif total_mark>=120:
        print("Grade: C")
    else:
        print("Grade: Fail")

    choice= input("Do you want to add another student?")
    if choice.lower() == "yes":
        continue
    else:
        break
        
        
    
