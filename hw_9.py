def index_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Please try again! Enter the contact name and phone number with a space!"
    return wrapper


def key_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "There is name no such! Check the contact name and try again!"
    return wrapper


phone_book = {}
hello = lambda *args: f"How can I help you?"    #  функція привітання

@key_error
def print_phone(*args):         # виводить вказани номер телефону для існуючого контакту
    name = args[0]
    return f"{phone_book[name]}"

def show_all(*args):  # принтує всі існуючі номери телефонів
    if not phone_book:
        return "The phone book has no contacts"
    result = ""
    for name, phone in phone_book.items():
        result += f"{name}: {phone}\n"
    return result

@index_error
def change_contact(*args):
    name, phone = args[0], args[1]
    if phone_book.get(name):
        phone_book[name] = phone
        return phone_book
    else:
        return f"The phone number has not been changed. Check the typed name '{name}', and try again!"

@index_error
def add(*args):
    name, phone = args[0], args[1]
    phone_book.update({name: phone})
    return f"This is contact {name}: {phone}, add in phone_book!"
    # phone_book.update({args[0]: args[1]})
    # return f"This is contact {args[0]}: {args[1]}, add in phone_book!"

COMMANDS = {add: "add",
            hello: "hello",
            change_contact: "change",
            print_phone: "phone",
            show_all: "show all"}

def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")
    return None, None

def main():
    while True:
        user_input = input(">>> ").lower()
        # user_input = user_input.lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        command, data = command_parser(user_input)
        if not command:
            print("Sorry, unknown command")
        else:
            print(command(*data))

if __name__ == "__main__":
    main()
