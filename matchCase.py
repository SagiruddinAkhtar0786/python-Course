x=int(input("Enter a number: "))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x,"is 90 or 80")
