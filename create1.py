# Write a program that asks the user how many teeth they have.

# create a list with all teeth names in adults
AllTeethNames = ["left central incisor", "left lateral incisor", "left canine", "left first molar", "left second molar", "left third molar", "left first premolar", "left second premolar", "right central incisor", "right lateral incisor", "right canine", "right first molar", "right second molar", "right third molar", "right first premolar", "right second premolar"]
# Welcome the user to the Dentist Office
numMissingTeeth = "0"
MissingTooth = "null"
implant = "null"
print("Welcome to the Dentist Office")

def getTeeth():
    numTeeth = int(input("How many teeth do you have? "))
    if numTeeth == 32:
        print("You have a full set of teeth for an adult")
    elif numTeeth == 20:
            print("You have a full set of teeth for a child")
    elif numTeeth > 32 or numTeeth < 0:
        print("Invalid number of teeth")
        numTeeth = input("How many teeth do you have ")
    else :
        print("you are missing " + str(32 - int(numTeeth)) + " teeth")
        numMissingTeeth = str(32 - int(numTeeth))
        # Ask the user what tooth they are missing
        print(AllTeethNames)
        MissingTooth = input( "What tooth are you missing? ").lower()


  

def procedure(AllTeethNames):
    for i in AllTeethNames:
        if i == MissingTooth:
            print("You are missing the " + i)
            implant = input("Would you like a " + i + " implant? Yes or No ").lower()
            return implant
procedure(AllTeethNames)
if implant == "yes":
    print("It will cost $500")

    
getTeeth()
procedure(AllTeethNames)
