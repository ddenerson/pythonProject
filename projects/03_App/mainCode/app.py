from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
    1) Add new entry for today.
    2) View entries.
    3) Exit.
 
    Your selection:"""
welcome = "Welcome to the programming diary!"


# receiving data from user
def prompt_new_entry():
    entry_content = input("What have you learned today ?")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)


# showing data
def view_entries(entries):
    for entry in entries:
        print("{}\n{}\n\n".format(entry[0], entry[1]))


print(welcome)
create_table()
user_input = input(menu)

while user_input != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again")

    user_input = input(menu)
