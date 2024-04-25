from balance import topup_balance

USER_NOT_FOUND = "USER_NOT_FOUND"
NOT_AUTH = "NOT_AUTHORIZED"

db = [
    {"email": "oto@gmail.com", "password": "oto12345"}
]

sign_in_attempts = 0

def find_user_with_email(email):
    for user in db:        
        if user.get("email") == email:
            return user
        
    raise Exception(USER_NOT_FOUND)

def sign_in_user(inputPassword, currentPassword):
    if inputPassword == currentPassword:
        return "TOKEN"
    
    raise Exception(NOT_AUTH)

while True:
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    try:
        user = find_user_with_email(email)
        token = sign_in_user(user.get("password"), password)

    except Exception as e:
        print("e", e)
    
    finally:
        sign_in_attempts +=1
    
    print("sign_in_attempts: ", sign_in_attempts)
