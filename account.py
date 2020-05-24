import os


class Account:
    def __init__(self, name):
        self.name = name
        self.filename = self.get_pathname()
        self.username_entry()

    def username_entry(self):
        confirmed = False
        filename = None
        while not confirmed:
            if os.path.exists(self.filename):
                confirmed = True
            else:
                create = input("User doesn't exist. Create? y/n")
                if create == 'y':
                    self.create_user_file(filename)
        return filename

    def get_pathname(self):
        filename = os.path.abspath(os.path.join('.', 'users/', self.name + '.mxg'))
        return filename

    def create_user_file(self, filename):
        password = input("Username: {}\nPassword: ".format(self.name))
        with open(filename, 'w') as fout:
            fout.write(password)
        print("User created.")

    def password_entry(self):
        with open(self.filename) as fin:
            user_pass = fin.read()
        password = input("Password: ")
        if password == user_pass:
            return True
        else:
            return False
