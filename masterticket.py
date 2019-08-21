TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def caluclate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?   ")
    num_tickets = input("How many tickets would you like, {}?   ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}. Please try again".format(err))
    else:
        amount_due = caluclate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = input("Do you wish to proceed?  Y/N?   ")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyway, {}.".format(name))
print("Sorry, the tickets are all sold out!")