import random


def get_number(message: str = "") -> int:
    """
    Get number of friends
    :param message: Message for the user
    :return: number
    """
    try:
        number = int(input(message))
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


def calculate_bill(friends: dict, total_bill: int, winner: str = "") -> None:
    """
    Evenly split bill to each friend rounded by two decimal points

    @param friends: friends dict
    @param total_bill: total bill to calculate split
    @param winner: if passed winner does not pay
    """
    minus = 1 if winner else 0
    split_bill = round(total_bill / (len(friends) - minus), 2)
    for name, pay in friends.items():
        friends[name] = 0 if winner and name == winner else split_bill


def get_random_name(friends) -> str:
    """
    Get random name
    @param friends: friends dict
    @return: random name from the friends dict
    """
    return random.choice(list(friends.keys()))
