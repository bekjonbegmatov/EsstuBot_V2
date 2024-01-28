import sqlite3
import json 

 # The class of users 
class Users:

    # Initithaliating of class Users 
    def __init__(self) -> None:
        """ CONECTING INTO THE DATABASE """
        self.conn = sqlite3.connect(database='esstu_bot_db.sqlite3')
        self.cursor = self.conn.cursor()

    # The method for creating a new Users
    def create_user(self, user_id:int, usename:str, degre:str, course:int, grup:str) -> bool:
        # try :
            # Creating a new user 
        self.cursor.execute('INSERT INTO Users (user_id, usename, degre, course, grup) VALUES (?, ?, ?, ?, ?)', (user_id, usename, degre, course, grup,))
        self.conn.commit()
        return True
        # If anything isn't ok 
        # except : return False 
    # The method for a getting all users
    def get_all_users(self):
        data = self.cursor.execute('SELECT * FROM Users').fetchall()
        return data
    
    def chaeck_users(self, user_id:int) -> bool:
        '''The method for cheking users into the database'''
        user = self.cursor.execute('SELECT * FROM Users WHERE user_id == ?', (user_id,)).fetchall()
        if len(user) == 0 : return False
        return user[0]

    # The method for exporting users to json file 
    def export_to_json(self) -> bool:
        query = 'SELECT * from Users'
        data = self.cursor.execute(query).fetchall()
        with open("Users.json", "w") as f:
            json.dump(data, f)
            
 # The class of admins
class Admin:

    # Initithaliating of class Admins
    def __init__(self) -> None:
        """ CONECTING INTO THE DATABASE """
        self.conn = sqlite3.connect(database='db.sqlite3')
        self.cursor = self.conn.cursor()

    # The method for creating a new admin
    def create_admin() -> bool:
        pass

    # The method for remowing an admin
    def remove_admin() -> bool:
        pass
    
    # The method for getting all admin
    def get_all_admins():
        pass


# Users().create_user(user_id=13123, usename='behruz', degre='bakalavr', course=1, grup='B743' )