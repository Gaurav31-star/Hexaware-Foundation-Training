from Case_Study.UTIL.DB_CONNECTION import DBConnection


class Cases(DBConnection):
    def __init__(self, case_id=None, description=None, case_date=None, status=None):
        self.case_id = case_id
        self.description = description
        self.case_date = case_date
        self.status = status

    def create_table(self):
        create_query = '''
            create table if not exists Cases(
            case_id int primary key,
            description varchar(150),
            case_date date,
            status varchar(30)
            )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Case table created successfully")

