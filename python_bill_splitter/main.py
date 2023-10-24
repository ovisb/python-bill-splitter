"""Main module"""
from python_bill_splitter import (  # type: ignore
    calculate_bill,
    create_friends_dict,
    get_number,
    get_random_name,
)


def main() -> None:
    """Main function"""
    while True:
        try:
            number_of_friends = get_number(
                "Enter the number of friends joining (including you): "
            )
        except ValueError:
            continue
        except EOFError:
            print("Exit program..")
            return
        break

    if number_of_friends <= 0:
        print("No one is joining for the party")
        return

    print()
    friends = create_friends_dict(number_of_friends)

    total_bill = get_number("Enter the total bill value: ")
    print()

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    print()

    if choice.lower() == "yes":
        name = get_random_name(friends)
        print(f"{name} is the lucky one!\n")
        calculate_bill(friends, total_bill, name)
    else:
        calculate_bill(friends, total_bill)
        print("No one is going to be lucky")

    print(friends)


if __name__ == "__main__":
    main()
