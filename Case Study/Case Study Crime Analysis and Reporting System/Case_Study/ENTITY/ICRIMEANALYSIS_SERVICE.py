from abc import ABC, abstractmethod


class I_crime_analysis_service:

    @abstractmethod
    def createIncident(self):
        pass

    @abstractmethod
    def updateIncidentStatus(self):
        pass

    @abstractmethod
    def getIncidentsInDateRange(self):
        pass

    @abstractmethod
    def searchIncidents(self):
        pass

    @abstractmethod
    def generateIncidentReport(self):
        pass

    @abstractmethod
    def createCase(self):
        pass

    @abstractmethod
    def getCaseDetails(self):
        pass

    @abstractmethod
    def updateCaseDetails(self):
        pass

    @abstractmethod
    def getAllCases(self):
        pass

