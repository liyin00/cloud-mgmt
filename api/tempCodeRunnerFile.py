import hashlib

user_entered_password = 'user1'
salt = "5gz"
db_password = user_entered_password+salt
h = hashlib.md5(db_password.encode())
print(h.hexdigest())
