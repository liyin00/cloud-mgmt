import hashlib
from datetime import datetime

user_entered_password = 'user1'

db_password = user_entered_password
h = hashlib.md5(db_password.encode())
print(h.hexdigest())


now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
print(dt_string)

