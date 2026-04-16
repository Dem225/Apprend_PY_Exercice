"""Module to generate random users"""
import faker
import logging
from pathlib import Path

fake=faker.Faker()
BASE_DIR= Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.DEBUG,
    filename=BASE_DIR / 'logigne.text',
    filemode="w",
    format='%(asctime)s - %(levelname)s - %(message)s'
    
    )
def get_user():
    """_summary_
    Generate a single user
    Returns:
        _type_: User
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(utilisateur_name):
    """Generate a list of users

    Args:
        nombre_utilisateur (int):  Number of user to gener

    Returns:
        list[str]: users
    """
    logging.info(f"Generating a list of {utilisateur_name} user.")
    return [get_user() for _ in range(utilisateur_name)]
    
if __name__ == '__main__':
    user=get_users(5)
    print(user)
    