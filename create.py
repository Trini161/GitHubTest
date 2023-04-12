from PIL import Image
import matplotlib.pyplot as plt

# Define the list of grocery items
groceries = ["GreenApple", "RedApple", "WaterBottle"]

def get_input():
    # Display the list of available grocery items to the user
    print("Available grocery items:")
    for item in groceries:
        print("- " + item)
    input_item = input("Enter the name of the grocery item: ")
    
    if input_item in groceries:
        return input_item
    elif ("apple" in input_item.lower()):
        # If the user entered "apple", prompt for the color
        input_item = input("Enter the color of the apple: ")
        input_item = input_item.capitalize() + "Apple"
    else:
        print("Invalid item.")
        return get_input()

def main():
    # Get input from the user
    input_item = get_input()

    # Construct the path to the image file
    image_path = f"{input_item}.jpg"

    try:
        # Open and display the image file
        img = Image.open(image_path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except FileNotFoundError:
        print("Image not found.")

    # Allow the user to select another item
    choice = input("Do you want to select another item? (y/n) ")
    if choice.lower() == "y":
        main()

if __name__ == "__main__":
    main()
