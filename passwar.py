# import secrets
# import string

# def generate_password(length=12):
#     # Define the characters that can be used in the password
#     characters = string.ascii_letters + string.digits + string.punctuation
    
#     # Use secrets.choice to generate a random password
#     password = ''.join(secrets.choice(characters) for i in range(length))
    
#     return password

# # Example usage
# if __name__ == "__main__":
#     password_length = 16  # You can change the length as needed
#     print("Generated Password:", generate_password(password_length))
