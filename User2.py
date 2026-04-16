"""C'est un fonction qui non permet de crée les nom et prenom de utlisateur"""
import faker
from pathlib import Path 
import logging

fake= faker.Faker()

BASE_DIR=Path(__file__).resolve().parent

logging.basicConfig(
   level=logging.DEBUG,
   filename=BASE_DIR / "respteur.txt", # On met le chemin dans filename
   filemode="w",                       # On met "w" dans filemode
   format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_User():
    logging.info("Generating user.")
    return f" {fake.first_name()},{ fake.last_name()},{fake.free_email()}, {fake.address()}, {fake.password()}"

def get_Users(Nuber_user):
    liste_users=[]
    logging.info(f"Generating a list of {Nuber_user } user.")
    for i in range(Nuber_user):
       liste_users.append(get_User())

    return liste_users

   

if __name__ == '__main__':
  users_list = get_Users(2)
  print(users_list)
