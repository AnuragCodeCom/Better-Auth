import bcrypt
import os
import sqlite3


def hash_password(password):
    # Generate a salt
    salt_rounds=12
    salt = bcrypt.gensalt(salt_rounds)
    
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return str(hashed_password.decode('utf-8'))


def verify_password(plain_password, hashed_password):
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

class Auth:
    def __init__(self,db_location='',db_name='database'):
        self.db_path = db_location
        self.db_name = db_name
        if db_location != '': 
            self.auth_db_path = db_location + '/' + 'auth.db'
        else:
            self.auth_db_path ='auth.db'

        # print(self.auth_db_path)
        if os.path.exists(self.auth_db_path) == False:
            self.db_conn = sqlite3.connect(self.auth_db_path)
            self.db_c = self.db_conn.cursor()
            self.db_c.execute(f"""CREATE TABLE usernames (
                        username text
                            )""")
        else:
            self.db_conn = sqlite3.connect(self.auth_db_path)
            self.db_c = self.db_conn.cursor()

        if db_location != '':
            db_path = db_location + '/' + db_name + '.db'
        else:
            db_path = db_location + db_name + ".db"
        # print(db_path)
        if os.path.exists(db_path) == False:
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()
            self.c.execute(f"""CREATE TABLE user_data (
                        username text, 
                        password text
                            )""")
            self.conn.commit()
        else:
            self.conn = sqlite3.connect(db_path)
            self.c = self.conn.cursor()

    def create_user(self,username,password):
        username = str(username).lower()
        if username.startswith("*") == True:
            return("[ERROR] Invalid Character \'*\' In Username")
        self.db_c.execute("""SELECT * FROM usernames""")
        data = []
        for x in self.db_c.fetchall():
            # print(x[0])
            data.append(x[0])
        usernames = data
        if username in usernames:
            return("[ERROR] Username Already Taken")
        self.db_c.execute(f"""INSERT INTO usernames VALUES ('{str(username)}')""")
        self.db_conn.commit()

        password = hash_password(password)

        self.c.execute(f"""INSERT INTO user_data VALUES ('{username}' , '{password}')""")
        self.conn.commit()
        return ("[SUCCESS] User Created Successfully")
    
    def check_username(self,username):
        username = str(username).lower
        self.db_c.execute("""SELECT * FROM usernames""")
        data = []
        for x in self.db_c.fetchall():
            # print(x[0])
            data.append(x[0])
        usernames = data
        if username in usernames:
            return True
        else:
            return False
        
    def verify_user(self,username,password):
        
        username = str(username)
        self.db_c.execute("""SELECT * FROM usernames""")
        data = []
        for x in self.db_c.fetchall():
            # print(x[0])
            data.append(x[0])
        usernames = data

        if username not in usernames:
            return False
        self.c.execute(f"""SELECT password FROM user_data WHERE username = '{username}'""")
        data = []
        for x in self.c.fetchall():
            data.append(x[0])
        hashed_password = data[0]
        if verify_password(password , hashed_password) == True:
            return True
        else:
            return False

        



