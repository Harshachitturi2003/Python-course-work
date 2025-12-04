print("-------------MYNTRA-------------")

product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")

price = float(input("Enter Product Price: "))

categories_input = input("Enter Categories: ")
categories = [cat.strip() for cat in categories_input.split(",")]

available_stock = int(input("Enter Available Stock: "))
sold_items = int(input("Enter Sold Items: "))
stock_details = (available_stock, sold_items)

discount = float(input("Enter Discount Percentage: "))

features_input = input("Enter Product Features : ")
product_features = {f.strip() for f in features_input.split(",")}

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}
print("-------------Product Details -----------------")

print("Product ID:", product_id)
print("Product Name:", product_name)
print("Price:", price)
print("Categories:", categories)
print("Stock Details:", stock_details)
print("Discount:", discount)
print("Features:", product_features)
print("Supplier Details:", supplier_details)
print("\n")
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: %.2f" % price)
print("Discount: %.2f%%" % discount)
print("Available Stock: %d, Sold Items: %d" % stock_details)
print("Supplier: %s, Contact: %s, Location: %s" %
      (supplier_details["name"], supplier_details["contact"], supplier_details["location"]))
print("\n")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price: {price:.2f}")
print(f"Categories: {categories}")
print(f"Stock Details: {stock_details}")
print(f"Discount: {discount}%")
print(f"Features: {product_features}")
print(f"Supplier Details: {supplier_details}")
print("\n")
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
