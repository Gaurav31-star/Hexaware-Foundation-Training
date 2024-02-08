from Case_Study.UTIL.DB_CONNECTION import DBConnection
from Case_Study.ENTITY.ICRIMEANALYSIS_SERVICE import I_crime_analysis_service
from Case_Study.DAO.INCIDENTS import Incidents
from Case_Study.DAO.REPORTS import Reports
from Case_Study.DAO.CASE import Cases


class crime_analysis_service_impl(Incidents, Reports, Cases, DBConnection, I_crime_analysis_service):
    def __init__(self):
        super(Incidents, self).__init__()

    def createIncident(self):
        incident = Incidents()
        incident.insert_into()

    def updateIncidentStatus(self):
        incident = Incidents()
        incident.update_table()

    def getIncidentsInDateRange(self):
        start_date = input("Enter the start date(yyyy-mm-dd): ")
        end_date = input("Enter the input date(yyyy-mm-dd): ")
        res = [incident for incident in Incidents.incidents if start_date <= incident.incident_date <= end_date]
        for i in res:
            print(i)

    def searchIncidents(self):
        self.incident_id = int(input('Enter the incident id to search the incident details: '))
        search_query = f'select * from Incidents where incident_id = {self.incident_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(search_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Search successfully")

    def generateIncidentReport(self):
        self.incident_id = int(input("Enter the incident id to generate a report: "))
        report_query = f'select * from Reports where incident_id = {self.incident_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(report_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Reports generated successfully")

    def createCase(self):
        self.case_id = int(input("Enter the case id: "))
        self.description = input("Enter the description: ")
        self.case_date = input("Enter the case date: ")
        self.status = input("Enter the status: ")

        query = 'insert into Cases(case_id, description, case_date, status) values(%s,%s,%s,%s)'
        data = [(self.case_id, self.description, self.case_date, self.status)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(query, data)
        DBConnection.connection.commit()
        print("Created case successfully")

    def getCaseDetails(self):
        self.case_id = int(input("Enter the case Id to get details: "))
        get_query = f'select * from Cases where case_id={self.case_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(get_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Case details displayed successfully")

    def updateCaseDetails(self):
        self.case_id = int(input("Enter the case Id to update details: "))
        self.description = input("Enter the description: ")
        self.case_date = input("Enter the case date: ")
        self.status = input("Enter the status: ")
        update_query = f'update Cases set description=%s, case_date=%s, status=%s where case_id=%s'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(update_query)
        print("Case updated successfully")

    def getAllCases(self):
        get_query = f'select * from Cases'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(get_query)
        data = stmt.fetchall()
        for i in data:
            print(i)



# obj = crime_analysis_service_impl()
# obj.generateIncidentReport()
