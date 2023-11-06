
Marks_str=input("Enter your marks-")
try :
    Marks=int(Marks_str)

            #75<A
    if 75 <= Marks :
        print("A")
            #60<B<75
    elif 60 <= Marks < 75 :
        print("B")
            #40<B<60
    elif 40 <= Marks < 60 :
        print("C")
    else :
        print("Fail")

except ValueError :
    print("Type the valid number")

