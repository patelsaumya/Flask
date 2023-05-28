from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

hashed_pass = bcrypt.generate_password_hash('mypassword')
print(hashed_pass)
wrong_check = bcrypt.check_password_hash(hashed_pass, 'wrongpass')
print(wrong_check)
right_check = bcrypt.check_password_hash(hashed_pass, 'mypassword')
print(right_check)

from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)
wrong_check = check_password_hash(hashed_pass,'wrong')
print(wrong_check)
right_check = check_password_hash(hashed_pass,'mypassword')
print(right_check)
