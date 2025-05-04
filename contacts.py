contacts = dict()
def getcity():
    while True:
        allowed_cities = ("Tehran", "Mashhad", "Shiraz")
        print("enter your city (Tehran , Mashhad , Shiraz): ")
        city = input()
        if city in allowed_cities:
            return city
        else:
            print("wrong input \n")
            continue

def addcontact():
    contacts[int(input("enter number: "))] = [input("enter name: ") , getcity()]

def deletcontact():
    name = input("enter the name of the contact you whant to delete: ")
    existance = False
    for contact in contacts:
        if contacts[contact][0] == name:
            existance = True
            assurance = input(f"are you sure you whant to delete {name} : {contact}  y/n?")
            match assurance:
                case "y":
                    contacts.pop(contact)
                    print("contact successfully deleted!\n")
                    break
                case "n":
                    break
                case _:
                    print("wrong input!")
    if existance == False:
        print("contact unavailable")
    

def search():
    print("who do you whant? ")
    name = input()
    existance = False
    for contact in contacts:
        if contacts[contact][0] == name:
            existance = True
            print(f"{name} : {contact} , lives in {contacts[contact][1]}")
    if existance == False:
        print("contact not found!")
    

def showlist():
    for contact in contacts:
        print(f"{contacts[contact][0]} : {contact} , lives in : {contacts[contact][1]}\n")

def quit():
    exit()

while True:
    print(f" enter 1 to add contact \n enter 2 delete by name \n enter 3 to search by name \n enter 4 to show contacts list \n enter 5 to quit\n enter:")
    try:
        action = int(input())
    except:
        print("enter the correct number")
    match action:
        case 1:
            addcontact()
            continue
        case 2:
            if contacts != dict():
                deletcontact()
                continue
            else:
                print("no contacts")
        case 3:
            if contacts != dict():
                search()
                continue
            else:
                print("no contacts")
        case 4:
            if contacts != dict():
                showlist()
                continue
            else:
                print("no contacts")
        case 5:
            quit()
            continue
        case _:
            print("enter number of action.")
            continue