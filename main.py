from statics import *


def listen_command():
    return input(get_message)


def say_message(message):
    print(message)


def check_any_set_value_message(set1, message):
    for i in set1:
        if i in message:
            return True
    return False


def do_this_command(message):
    message = message.lower()
    if check_any_set_value_message(greetings, message):
        say_message("Hello!")
    elif check_any_set_value_message(stop_messages, message):
        say_message("Bye!")
        exit()
    else:
        say_message("I don't understand you!")


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
