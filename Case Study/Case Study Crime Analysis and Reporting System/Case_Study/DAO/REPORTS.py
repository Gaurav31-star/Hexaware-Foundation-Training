from Case_Study.UTIL.DB_CONNECTION import DBConnection


class Reports(DBConnection):
    def __init__(self, report_id=None, incident_id=None, reporting_officer=None, report_date=None, report_details=None, status=None):
        self.report_id = report_id
        self.incident_id = incident_id
        self.reporting_officer = reporting_officer
        self.report_date = report_date
        self.report_details = report_details
        self.status = status

    def create_table(self):
        create_query = '''
        create table if not exists Reports(
        report_id int primary key,
        incident_id int,
        reporting_officer varchar(30),
        report_date date,
        report_details varchar(150),
        status varchar(20)
        )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Reports table successfully created")

    def insert_into(self):
        self.report_id = int(input("Enter the report id: "))
        self.incident_id = input("Enter the incident id: ")
        self.reporting_officer = input("Enter the reporting officer: ")
        self.report_date = input("Enter the report date: ")
        self.report_details = input("Enter the report details: ")
        self.status = input("Enter the status: ")

        insert_query = 'insert into Reports(report_id, incident_id, reporting_officer, report_date, report_details, status) values(%s,%s,%s,%s,%s,%s)'
        data = [(self.report_id, self.incident_id, self.reporting_officer, self.report_date, self.report_details, self.status)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        self.report_id = int(input("Enter the report id: "))
        self.incident_id = input("Enter the incident id: ")
        self.reporting_officer = input("Enter the reporting officer: ")
        self.report_date = input("Enter the report date: ")
        self.report_details = input("Enter the report details: ")
        self.status = input("Enter the status: ")

        update_query = 'update Reports set incident_id=%s, reporting_officer=%s, report_date=%s, report_details=%s, status=%s where report_id=%s'
        data = [(self.incident_id, self.reporting_officer, self.report_date, self.report_details, self.status, self.report_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(update_query, data)
        DBConnection.connection.commit()
        print("Values updated successfully")

    def delete_table(self):
        self.report_id = int(input("Enter the report id to delete values: "))
        delete_query = f'delete from Reports where report_id={self.report_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Reports'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")