# ---------------------------------------------
# Product Information System
# Using Different Data Types and Formatting Methods
# ---------------------------------------------

# ----------- Task 1: Take Product Details as Input ------------

# 1. Product ID (int)
product_id = int(input("Enter Product ID: "))

# 2. Product Name (str)
product_name = input("Enter Product Name: ")

# 3. Price (float)
price = float(input("Enter Product Price: "))

# 4. Categories (list)
categories_input = input("Enter Categories (separated by commas): ")
categories = [cat.strip() for cat in categories_input.split(",")]

# 5. Stock Details (tuple)
available_stock = int(input("Enter Available Stock: "))
sold_items = int(input("Enter Sold Items: "))
stock_details = (available_stock, sold_items)

# 6. Discount Percentage (float)
discount = float(input("Enter Discount Percentage: "))

# 7. Product Features (set)
features_input = input("Enter Product Features (separated by commas): ")
product_features = {f.strip() for f in features_input.split(",")}

# 8. Supplier Details (dict)
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# ---------------------------------------------------------------
# ----------- Task 2: Display Using Formatting Methods ----------
# ---------------------------------------------------------------

print("\n" + "-"*50)
print("PRODUCT INFORMATION (Using Comma Separation)")
print("-"*50)

# Comma Separation
print("Product ID:", product_id)
print("Product Name:", product_name)
print("Price:", price)
print("Categories:", categories)
print("Stock Details:", stock_details)
print("Discount:", discount)
print("Features:", product_features)
print("Supplier Details:", supplier_details)

print("\n" + "-"*50)
print("PRODUCT INFORMATION (Using % Formatting)")
print("-"*50)

# Percentage (%) Formatting
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: %.2f" % price)
print("Discount: %.2f%%" % discount)
print("Available Stock: %d, Sold Items: %d" % stock_details)
print("Supplier: %s, Contact: %s, Location: %s" %
      (supplier_details["name"], supplier_details["contact"], supplier_details["location"]))

print("\n" + "-"*50)
print("PRODUCT INFORMATION (Using f-Strings)")
print("-"*50)

# f-strings
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: {price:.2f}")
print(f"Categories: {categories}")
print(f"Stock Details: {stock_details}")
print(f"Discount: {discount}%")
print(f"Features: {product_features}")
print(f"Supplier Details: {supplier_details}")

print("\n" + "-"*50)
print("PRODUCT INFORMATION (Using .format() Method)")
print("-"*50)

# .format() method
print("Product ID: {}".format(product_id))
print("Product Name: {}".format(product_name))
print("Price: {:.2f}".format(price))
print("Categories: {}".format(categories))
print("Stock Details: {}".format(stock_details))
print("Discount: {}%".format(discount))
print("Features: {}".format(product_features))
print("Supplier Details: Name: {name}, Contact: {contact}, Location: {location}".format(
    **supplier_details
))

print("\n" + "-"*50)
print("End of Product Information")
print("-"*50)
