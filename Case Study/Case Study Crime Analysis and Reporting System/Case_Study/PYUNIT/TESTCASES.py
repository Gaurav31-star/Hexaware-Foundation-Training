import unittest
from Case_Study.DAO.INCIDENTS import Incidents


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.incident = Incidents()

    # testing whether an incident is created or not
    def test_incident(self):
        print("Create a new incident with incident id = 5")
        result = self.incident.insert_into()
        self.assertEqual('Incident created successfully', result)

    # testing whether incident status updated or not
    def test_update(self):
        print("Updating the status of incident. Set status = Investigation ")
        result = self.incident.update_table()
        self.assertEqual('Values updated successfully', result)


if __name__ == '__main__':
    unittest.main()
