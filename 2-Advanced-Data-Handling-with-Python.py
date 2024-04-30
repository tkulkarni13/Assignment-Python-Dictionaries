# Task 1: Hotel Room Booking Tracker

hotel_rooms = { # original hotel composition
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def bookRoom (room_num, customer): # function to book a room for a customer
    try:
        room = hotel_rooms.get(room_num)
    except KeyError:
        print("Room doesn't exit") # Inform user if they try to book of a room that doesn't exist
    else:
        if (room["status"] == "available"):
            room["status"] = "booked" # Set room status to 'booked'
            room["customer"] = customer # Add customer to dictionary
        else:
            print("That room is currently booked") # Inform user if the try to book and already booked room

def checkOut(room_num): # Function to checkout of a room
    try:
        room = hotel_rooms.get(room_num)
    except KeyError:
        print("Room doesn't exit") # Inform user if they try to checkout of a room that doesn't exist
    else:
        if (room["status"] == "booked"):
            room["status"] = "available" # Set room status to 'available'
            room["customer"] = "" # Remove customer from dictionary
        else:
            print("That room is currently available") # Inform user they can't checkout of an empty room

def displayHotelStatus(): # Function to display what rooms are available and not
    for room_num, value in hotel_rooms.items(): # Loop to iterate through all rooms
        print(f"{room_num}: {value["status"]}") # Print status of each room

displayHotelStatus() # original hotel status
bookRoom("101", "Santa Claus") # book room 101 for santa claus
checkOut("102") # check out john doe from room 102
print()
displayHotelStatus() # new hotel status