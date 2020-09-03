from database import add_entry, get_entry


menu = """Please select one of the following options:
(1) Add new entry for today
(2) View entries
(3) Exit

Your selection: """

welcome_mess = "Welcome to your daily journals"

def prompt_new_entry():
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entry(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

print(welcome_mess)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entry(get_entry())        
    else:
        print("Invalid option, please tyr again")


    user_input = input(menu)