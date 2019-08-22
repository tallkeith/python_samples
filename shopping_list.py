shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'LIST' to show shopping list.
Enter 'HELP' for this help.
""")


def add_to_list(item):
    shopping_list.append(item)
    print("{} added to shopping list. There are ".format(item) + str(len(shopping_list)) + " items in your list")


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'LIST':
        show_list()
        continue
    
    add_to_list(new_item)