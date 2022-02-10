from task2 import numerals, response


def numeral():
    while (digit := input("numeral> ")).isdigit():
        # Fill in here


def language():
    # Write a line to obtain a list of languages
    print("Available languages:")
    for l in languages:
        print(l)
    while (l := input("language> ").upper()) not in languages:
        print(f"Language {l} is not available")
    # Write a line to set the language


if __name__ == "__main__":

    print("Available commands are:\n language\n numeral")
    print("Press Enter to exit")
    while (command := input("command> ").lower()):
        if command == "numeral":
            numeral()
        elif command == "language":
            language()
        else:
            print("Invalid command")
