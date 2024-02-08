from Case_Study.UTIL.DB_CONNECTION import DBConnection


class Officers(DBConnection):
    def __init__(self, officer_id=None, first_name=None, last_name=None, badge_no=None, officer_rank=None, phone_num=None, agency_id=None):
        self.officer_id = officer_id
        self.first_name = first_name
        self.last_name = last_name
        self.badge_no = badge_no
        self.officer_rank = officer_rank
        self.phone_num = phone_num
        self.agency_id = agency_id

    def create_table(self):
        create_query = ''' create table if not exists Officers(
            officer_id int primary key,
            first_name varchar(30),
            last_name varchar(30),
            badge_no varchar(10),
            officer_rank varchar(30),
            phone_num varchar(20),
            agency_id int
        )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Officers table created successfully")

    def insert_into(self):
        self.officer_id = int(input("Enter the officer id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.badge_no = input("Enter the badge number: ")
        self.officer_rank = input("Enter the rank: ")
        self.phone_num = input("Enter the phone number: ")
        self.agency_id = input("Enter the agency id: ")

        insert_query = 'insert into Officers(officer_id, first_name, last_name, badge_no, officer_rank, phone_num, agency_id) values(%s,%s,%s,%s,%s,%s,%s)'
        data = [(self.officer_id, self.first_name, self.last_name, self.badge_no, self.officer_rank, self.phone_num, self.agency_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        self.officer_id = int(input("Enter the officer id to update values: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.badge_no = input("Enter the badge number: ")
        self.officer_rank = input("Enter the rank: ")
        self.phone_num = input("Enter the phone number: ")
        self.agency_id = input("Enter the agency id: ")

        update_query = 'update Officers set first_name=%s, last_name=%s, badge_no=%s, officer_rank=%s, phone_num=%s, agency_id=%s where officer_id=%s'
        data = [(self.first_name, self.last_name, self.badge_no, self.officer_rank, self.phone_num, self.agency_id, self.officer_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(update_query, data)
        DBConnection.connection.commit()
        print("Values updated successfully")

    def delete_table(self):
        self.officer_id = int(input("Enter the officer id to delete values: "))
        delete_query = f'delete from Officers where officer_id={self.officer_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Officers'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")
