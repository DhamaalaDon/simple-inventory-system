def add_product_to_inventory():
    # Get product details from the user
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    
    # Create or open the inventory file in append mode
    with open("inventory.txt", "a") as file:
        # Write the product details to the file
        file.write(f"{product_name}, {product_price}, {product_quantity}\n")
    
    print("Product added successfully!")

def view_inventory():
    print("Current Inventory:")
    try:
        # Open the inventory file in read mode
        with open("inventory.txt", "r") as file:
            contents = file.readlines()
            if not contents:
                print("Inventory is empty.")
            else:
                # Print each line in the inventory
                for line in contents:
                    print(line.strip())
    except FileNotFoundError:
        print("No inventory file found.")

def delete_product():
    product_name_to_delete = input("Enter the product name to delete: ")
    
    try:
        # Read all the lines from the inventory file
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        
        # Filter out the line with the product to delete
        updated_lines = [line for line in lines if not line.lower().startswith(product_name_to_delete.lower())]
        
        if len(updated_lines) == len(lines):
            print("Product not found!")
        else:
            # Rewrite the file with the updated inventory
            with open("inventory.txt", "w") as file:
                file.writelines(updated_lines)
            print(f"Product '{product_name_to_delete}' deleted successfully!")
    
    except FileNotFoundError:
        print("No inventory file found.")

# Main menu to choose an operation
def main_menu():
    while True:
        print("\nInventory System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Delete Product")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product_to_inventory()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
main_menu()
