"""Main module"""
from python_bill_splitter import (  # type: ignore
    calculate_bill,
    create_friends_dict,
    get_number_of_friends,
    get_random_name,
)


def main() -> None:
    """Main function"""
    number_of_friends = get_number_of_friends()
    if number_of_friends <= 0:
        print("No one is joining for the party")
        return

    friends = create_friends_dict(number_of_friends)
    calculate_bill(friends)

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if choice.lower() == "yes":
        name = get_random_name(friends)
        print(f"{name} is the lucky one!")
    else:
        print("No one is going to be lucky")


if __name__ == "__main__":
    main()
