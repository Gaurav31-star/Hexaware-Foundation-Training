from Case_Study.UTIL.DB_CONNECTION import DBConnection


class Suspects(DBConnection):
    def __init__(self, suspect_id=None, first_name=None, last_name=None, dob=None, gender=None, address=None, phone_num=None):
        self.suspect_id = suspect_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.phone_num = phone_num

    def create_table(self):
        create_query = '''
            create table if not exists Suspects(
            suspect_id int primary key,
            first_name varchar(30),
            last_name varchar(30),
            dob date,
            gender char,
            address varchar(30),
            phone_num varchar(20))
            '''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Suspects table created successfully")

    def insert_into(self):
        self.suspect_id = int(input("Enter the suspect id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.dob = input("Enter the date of birth: ")
        self.gender = input("Enter the gender: ")
        self.address = input("Enter the address: ")
        self.phone_num = input("Enter the phone number: ")

        insert_query = 'insert into Suspects(suspect_id, first_name, last_name, dob, gender, address, phone_num) values(%s,%s,%s,%s,%s,%s,%s)'
        data = [(self.suspect_id, self.first_name, self.last_name, self.dob, self.gender, self.address, self.phone_num)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        self.suspect_id = int(input("Enter the suspect id to update the values: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.dob = input("Enter the date of birth: ")
        self.gender = input("Enter the gender: ")
        self.address = input("Enter the address: ")
        self.phone_num = input("Enter the phone number: ")

        update_query = 'update Suspects set first_name=%s, last_name=%s, dob=%s, gender=%s, address=%s, phone_num=%s where suspect_id=%s'
        data = [(self.first_name, self.last_name, self.dob, self.gender, self.address, self.phone_num, self.suspect_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(update_query, data)
        DBConnection.connection.commit()
        print("Values updated successfully")

    def delete_table(self):
        self.suspect_id = int(input("Enter the suspect id to delete values: "))
        delete_query = f'delete from Suspects where suspect_id={self.suspect_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Suspects'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")

