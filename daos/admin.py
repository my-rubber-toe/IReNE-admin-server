from daos.dummy_data.admin import admins
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
class AdminDAO:
    adminList = []

    def __init__(self):
        self.adminList = admins
    
    def get_admin(self, username):
        for admin in self.adminList:
            if (admin.get('username') == username):
                return admin
    
    def check_password(self, password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)