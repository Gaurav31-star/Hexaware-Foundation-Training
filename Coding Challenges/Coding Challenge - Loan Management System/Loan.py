
class Loan():
    def __init__(self, loan_id=None, customer_id=None, principal_amount=None, interest_rate=12, loan_term=None, loan_type=None, loan_status='Pending'):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = float(principal_amount)
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    def get_loan_id(self):
        return self.loan_id

    def get_customer_id(self):
        return self.customer_id

    def get_principal_amount(self):
        return float(self.principal_amount)

    def get_interest_rate(self):
        return self.interest_rate

    def get_loan_term(self):
        return self.loan_term

    def get_loan_type(self):
        return self.loan_type

    def get_loan_status(self):
        return self.loan_status

    def set_loan_id(self, loan_id):
        self.loan_id = loan_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_principal_amount(self, principal_amount):
        self.principal_amount = float(principal_amount)

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def set_loan_term(self, loan_term):
        self.loan_term = loan_term

    def set_loan_type(self, loan_type):
        self.loan_type = loan_type

    def set_loan_status(self, loan_status):
        self.loan_status = loan_status

    def display_loan_details(self):
        print(f'\nThe Current details of your {self.loan_type} with',end=" " )
        print(f"Loan ID: {self.loan_id} are - ")
        print(f"Customer ID: {self.customer_id}")
        print(f"Principal Amount: {self.principal_amount}")
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Loan Term: {self.loan_term} months")
        print(f"Loan Type: {self.loan_type}")
        print(f"Loan Status: {self.loan_status}")
        print()

    def insert_new_loan(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status) VALUES ({self.customer_id}, {self.principal_amount}, {self.interest_rate}, {self.loan_term}, '{self.loan_type}', '{self.loan_status}')")
            self.mydb.commit()
            self.loan_id = self.c.lastrowid
            print(f"\nLoan record added to the database with ID: {self.loan_id}\n")
        except Exception as e:
            print(e)
        finally:
            self.close()