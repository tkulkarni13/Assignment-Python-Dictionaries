# Task 1: Customer Service Ticket Tracker

service_tickets = { # Initial service tickest
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}

def newTicket(customer, issue): # Function to add a new ticket
    if (len(service_tickets) == 0):
        service_tickets["Ticket001"] = {"Customer": customer, "Issue": issue, "Status": "open"} # Create first ticket if dictionary is empty
    else:
        currentTicket = list(service_tickets.keys())[-1] # Find name of most recent ticket
        newTicketNum = int(currentTicket[-3:]) + 1 # Use previous ticket's number and add 1 for new ticket
        newTicketName = "Ticket" + "{:03d}".format(newTicketNum)

        service_tickets[newTicketName] = {"Customer": customer, "Issue": issue, "Status": "open"} # Create new ticket in the dictionary with new name

def updateTicket(ticket_name): # Function to update a ticket from open -> closed
    if (ticket_name not in service_tickets.keys()):
        print("No such service ticket has been made") # Notify user if provided ticket doesn't exist
    else:
        if (service_tickets[ticket_name]["Status"] == "closed"):
            print("{} is already closed".format(ticket_name)) # Notify user if a service ticket has already been closed
        else:
            service_tickets[ticket_name]["Status"] = "closed" # Set status of specified ticked to closed

def displayAllTickets(): # Function to diplay all service tickets
    for ticket in service_tickets.items(): # Loop through the dictionary and print each one
        print(ticket)

def displayOpenTickets(): # Function to display open tickets
    for ticket in service_tickets.keys():
        if (service_tickets[ticket]["Status"] == "open"): # Loop through dictionary and print those with status 'open'
            print(service_tickets[ticket])

def displayClosedTickets(): # Function to display closed tickets
    for ticket in service_tickets.keys():
        if (service_tickets[ticket]["Status"] == "closed"): # Loop through dictionary and print those with status 'closed'
            print(service_tickets[ticket])

# Testing
displayAllTickets()
newTicket("Santa", "Shipping")
updateTicket("Ticket002")
updateTicket("Ticket003")
displayAllTickets()
print()
print("Open Tickets:")
displayOpenTickets()
print ("Closed Tickets")
displayClosedTickets()