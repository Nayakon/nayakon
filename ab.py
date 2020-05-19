"""
this example shows how to open a file for text,write and read
and shows how to parse our data into text and back from text
"""
x,y = 0,0
FILENAME = "big_data.txt"

while 1:

   # #print("x = {}; y = {}".format(x,y))
    print("x = %d; y = %d" % (x,y))

    print("""
            MENU X&Y
    set (X)
    set (Y)
    (S)ave
    (L)oad
    (Q)uit
    
    """)

    option = input("Option: ").upper()

    if option == "X":
        x = int(input("enter new value for X:"))

    elif option == "Y":
        y = int(input("enter new value for Y:"))

    elif option == "S":
        f = open(FILENAME, "w")
        f.write("{}\n{}\n".format(x,y))
        f.close()

    elif option == "L":
        f = open(FILENAME, "r")
        a = int(f.readline())
        b = int(f.readline())
        f.close()

    elif option == "Q":
        break

    else:
        print("\ninvalid option!\n")





