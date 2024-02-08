from Case_Study.UTIL.DB_CONNECTION import DBConnection
from Case_Study.EXCEPTION.INCIDENTNUMBERNOTFOUND import IncidentNumberNotFoundException

class Incidents(DBConnection):
    incidents = []

    def __init__(self, incident_id=None, incident_type=None, incident_date=None, location=None, description=None, status=None, victim_id=None, suspect_id=None):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.incident_date = incident_date
        self.location = location
        self.description = description
        self.status = status
        self.victim_id = victim_id
        self.suspect_id = suspect_id

    def create_table(self):
        create_query = '''
            create table if not exists Incidents(
            incident_id int primary key,
            incident_type varchar(30),
            incident_date date,
            location varchar(30),
            description varchar(100),
            status varchar(30),
            victim_id int,
            suspect_id int
            )
        '''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Incidents table created successfully")

    def insert_into(self):
        self.incident_id = int(input("Enter the incident id: "))
        self.incident_type = input("Enter the incident type: ")
        self.incident_date = input("Enter the incident date: ")
        self.location = input("Enter the location: ")
        self.description = input("Enter the description: ")
        self.status = input("Enter the status: ")
        self.victim_id = int(input("Enter the victim id: "))
        self.suspect_id = int(input("Enter the suspect id: "))

        insert_query = 'insert into Incidents(incident_id, incident_type, incident_date, location, description, status, victim_id, suspect_id) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [(self.incident_id, self.incident_type, self.incident_date, self.location, self.description, self.status, self.victim_id, self.suspect_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Data inserted successfully")
        return 'Incident created successfully'

    def update_table(self):
        try:
            self.incident_id = int(input("Enter the incident id to update the values: "))
            self.incident_type = input("Enter the incident type: ")
            self.incident_date = input("Enter the incident date: ")
            self.location = input("Enter the location: ")
            self.description = input("Enter the description: ")
            self.status = input("Enter the status: ")
            self.victim_id = int(input("Enter the victim id: "))
            self.suspect_id = int(input("Enter the suspect id: "))
            if not self.incident_exists(self.incident_id):
                raise IncidentNumberNotFoundException("Incident id not found")

            update_query = 'update Incidents set incident_type=%s, incident_date=%s, location=%s, description=%s, status=%s, victim_id=%s, suspect_id=%s where incident_id=%s'
            data = [(self.incident_type, self.incident_date, self.location, self.description, self.status, self.victim_id, self.suspect_id, self.incident_id)]
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.executemany(update_query, data)
            DBConnection.connection.commit()
            print("Updated successfully")
            return 'Values updated successfully'

        except IncidentNumberNotFoundException as e:
            print(e)
        except Exception as e:
            print(e)

    def delete_table(self):
        try:
            self.incident_id = int(input("Enter the incident id to delete data: "))
            if not self.incident_exists(self.incident_id):
                raise IncidentNumberNotFoundException("Incident id not found")
            delete_query = f'delete from Incidents where incident_id = {self.incident_id}'
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(delete_query)
            DBConnection.connection.commit()
            print("Deleted successfully")

        except IncidentNumberNotFoundException as e:
            print(e)
        except Exception as e:
            print(e)

    def select_table(self):
        select_query = 'select * from Incidents'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            Incidents.incidents.append(i)
            print(i)
        Incidents.incidents = [list(i) for i in Incidents.incidents]
        print("Values displayed successfully")

    def incident_exists(self, incident_id):
        try:
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            select_query = f'SELECT COUNT(*) FROM Incidents WHERE incident_id = {incident_id}'
            stmt.execute(select_query)
            result = stmt.fetchone()
            if result and result[0] > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error checking incident existence: {e}")
            return False

    def __str__(self):
        return """f'Incident ID: {self.incident_id}', f'Incident Type: {self.incident_type}',f'Incident date: {self.incident_date}',
         f'Location: {self.location}', f'Description: {self.description}',  f'Status: {self.status}', 
          f'Victim ID: {self.victim_id}', f'Suspect ID: {self.suspect_id}' """





