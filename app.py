def add_product_to_inventory():
    # Get product details from the user
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    
    # Create or open the inventory file
    with open("inventory.txt", "a") as file:
        # Write the product details to the file
        file.write(f"{product_name}, {product_price}, {product_quantity}\n")
    
    print("Product added successfully!")

# Call the function to add a product
add_product_to_inventory()
