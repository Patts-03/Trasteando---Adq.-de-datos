# Voy a trastear un poco

if __name__=="__main__":
    number = input("Try to match our chosen number: ")

    while int(number) != 15:
        print("Ups, that's not our number")
        number = input("Try again : ")

    print("\n Wow, you made it! \n")
    exit(0)