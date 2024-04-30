# Task 1: Restaurant Menu Update

restaurant_menu = { # Given restaurant menu
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print("Original Menu: {}".format(restaurant_menu)) # print original menu

restaurant_menu["Beverages"] = {"Coke": 2.99, "Wine": 7.99} # add beverages
restaurant_menu["Main Course"]["Steak"] = 17.99 # change steak price
del restaurant_menu["Starters"]["Bruschetta"] # remove bruschetta

print("New Menu: {}".format(restaurant_menu)) # print new menu