#IDEA
# make a list of groceries
# The user will type in an item in a list of groceries.
#  The output will be a picture of the item
# If the item is not an item in the list ask again 
# if the item is in the list make item picture appear
# or if they say apple and there is an option of green or red ask 
# def 


from PIL import Image
import matplotlib.pyplot as plt
def main():
    # Ask for input from the user
    groceries = ["GreenApple", "RedApple", "WaterBottle"]
    def get_input():
        input_item = input("Enter the name of the grocery item from groceries ")
        if ("apple" in input_item.lower()):
            input_item = input("Enter the color of the apple ")
            if input_item.lower() in groceries:
                return input_item
        if input_item.lower() in groceries:
            
            return input_item
        else:
            print("Please enter a valid item")
            return get_input()
        
    input_item = get_input()

    # Check if the user input is in the list of groceries
    if input_item.lower() in groceries:
        # Get the path of the image file
        image_path = f"{input_item}.jpg"
    # Construct the image file path based on user input

    try:
        # Open the image file
        img = Image.open(image_path)

        # Display the image
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except FileNotFoundError:
        print("Image not found.")

if __name__ == "__main__":
    main()