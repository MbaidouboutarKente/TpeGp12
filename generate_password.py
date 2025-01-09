import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Vous devez sélectionner au moins une option pour générer un mot de passe.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Demander les préférences de l'utilisateur
length = int(input("Longueur du mot de passe : "))
use_uppercase = input("Utiliser des majuscules (y/n) : ").lower() == 'y'
use_lowercase = input("Utiliser des minuscules (y/n) : ").lower() == 'y'
use_digits = input("Utiliser des chiffres (y/n) : ").lower() == 'y'
use_special = input("Utiliser des caractères spéciaux (y/n) : ").lower() == 'y'

# Générer le mot de passe
password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
print(f"Votre mot de passe généré est : {password}")
