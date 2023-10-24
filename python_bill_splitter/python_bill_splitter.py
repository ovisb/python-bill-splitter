import random


def get_number_of_friends() -> int:
    """
    Get number of friends
    """
    try:
        number = int(input("Enter the number of friends joining (including you): "))
    except ValueError as vl:
        print("Only input numbers please!")
        raise vl
    return number


def create_friends_dict(friends_number: int) -> dict:
    """
    @param friends_number: Number of friends to create
    @return: dictionary of friends names
    """
    friends = {}
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(friends_number):
        name = input()
        friends[name] = 0

    return friends


def calculate_bill(friends: dict) -> None:
    """
    Evenly split bill to each friend rounded by two decimal points
    @param friends: friends dict
    """
    bill_value = int(input("Enter the total bill value: "))
    split_bill = round(bill_value / len(friends), 2)
    for name, pay in friends.items():
        friends[name] = split_bill


def get_random_name(friends) -> str:
    """
    Get ra
    @param friends: friends dict
    @return: random name from the friends dict
    """
    return random.choice(list(friends.keys()))
