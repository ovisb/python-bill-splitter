"""Main module"""
from python_bill_splitter import (  # type: ignore
    create_friends_dict,
    get_number_of_friends,
)


def main() -> None:
    """Main function"""
    number_of_friends = get_number_of_friends()
    if number_of_friends <= 0:
        print("No one is joining for the party")
        return

    friends = create_friends_dict(number_of_friends)

    print(friends)


if __name__ == "__main__":
    main()
