from Case_Study.UTIL.DB_CONNECTION import DBConnection


class Law_Enforcement_Agencies(DBConnection):
    def __init__(self, agency_id=None, agency_name=None, jurisdiction=None, phone_num=None, officer=None):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.jurisdiction = jurisdiction
        self.phone_num = phone_num
        self.officer = officer

    def create_table(self):
        create_query = '''
            create table Law_Enforcement_Agencies(
            agency_id int primary key,
            agency_name varchar(30),
            jurisdiction varchar(50),
            phone_num varchar(20),
            officer varchar(30)
        )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Law Enforcement Agencies table created successfully")

    def insert_into(self):
        self.agency_id = int(input("Enter the agency id: "))
        self.agency_name = input("Enter the agency name: ")
        self.jurisdiction = input("Enter the jurisdiction: ")
        self.phone_num = input("Enter the phone number: ")
        self.officer = input("Enter the officer: ")

        insert_query = 'insert into Law_Enforcement_Agencies(agency_id, agency_name, jurisdiction, phone_num, officer) values(%s,%s,%s,%s,%s)'
        data = [(self.agency_id, self.agency_name, self.jurisdiction, self.phone_num, self.officer)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        self.agency_id = int(input("Enter the agency id to update the values: "))
        self.agency_name = input("Enter the agency name: ")
        self.jurisdiction = input("Enter the jurisdiction: ")
        self.phone_num = input("Enter the phone number: ")
        self.officer = input("Enter the officer: ")

        update_query = 'update Law_Enforcements_Agencies set agency_name=%s, jurisdiction=%s, phone_num=%s, officer=%s where agency_id=%s'
        data = [(self.agency_name, self.jurisdiction, self.phone_num, self.officer, self.agency_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(update_query, data)
        DBConnection.connection.commit()
        print("Values updated successfully")

    def delete_table(self):
        self.agency_id = int(input("Enter the agency id to delete values: "))
        delete_query = f'delete from Law_Enforcement_Agencies where agency_id={self.agency_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Law_Enforcement_Agencies'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")

