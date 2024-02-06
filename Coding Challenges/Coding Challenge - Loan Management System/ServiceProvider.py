import mysql.connector as connection

from DBConnection import DBConnection

from Loan import Loan
from Customer import Customer

class LoanRepository(DBConnection):
    def __init__(self):
        pass

    def getCustomerByID(self, cid):
        try:
            self.open()
            self.c.execute(f"Select * From Customer Where customer_id = {cid}")
            cust = self.c.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close()
            return False if cust == None or cust == [] else cust

    def getLoanByID(self, lid):
        try:
            self.open()
            self.c.execute(f"Select * From Loan Where loan_id = {lid}")
        except Exception as e:
            print(e)
        else:
            flag = True
            try:
                if self.c.rowcount == 0:
                    flag = False
                    raise Exception('InvalidLoanException: No such Loan Record found in the database')
            except Exception as e:
                print(e)
            else:
                l = self.c.fetchone()
        finally:
            self.close()
            if flag:
                return Loan(*l)

    def applyLoan(self, loan):
        try:
            print("\nLoan Details are : ")
            loan.display_loan_details()
            conf = input("\nDo you want to continue with the Loan Application?(Y/N) : ").upper()
            if conf == 'Y':
                loan.set_loan_status("Pending")
                loan.insert_new_loan()
                print("\nYou have applied for the Loan Successfully!\nYour Loan Application is 'Pending' from our side.\nIt will be 'Approved' as soon as we Verify your Details.\nThank You...\n")      
            else:
                print('\nLoan Application Cancelled....\n')
        except Exception as e:
            print(e)
    
    def calculateInterest(self, lid):
        try:
            loan = self.getLoanByID(lid)
            loan.display_loan_details()
            interest = (float(loan.principal_amount) * loan.interest_rate * (loan.loan_term/ 12)) / 100
            return interest
        except Exception as e:
            print(e)
            return None
    
    def loanStatus(self, lid):
        try:
            loan = self.getLoanByID(lid)
            loan.display_loan_details()
            cid = loan.get_customer_id()
            c = self.getCustomerByID(cid)
            cscore = Customer(*c).get_credit_score()
            if cscore<=650:
                status = 'Pending'
                print('\nYor Loan Application is "Pending" because you have a Low Credit Score\n')
            else:
                status = 'Approved'
                print('\nYour Loan was Sanctioned andd the Interest Period is Ongoing.\n')
            self.open()
            self.c.execute(f"Update Loan Set loan_status = '{status}' Where loan_id = {lid}")
            self.mydb.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
    
    def calculateEMI(self, lid):
        try:
            loan = self.getLoanByID(lid)
            loan.display_loan_details()
            monthly_interest_rate = (loan.interest_rate / 12) / 100
            emi_numerator = float(loan.principal_amount) * monthly_interest_rate * (pow((1 + monthly_interest_rate), loan.loan_term))
            emi_denominator = pow((1 + monthly_interest_rate), loan.loan_term) - 1
            emi = emi_numerator / emi_denominator
            return emi
        except Exception as e:
            print(e)
    
    def loanRepayment(self, lid, amount):
        try:
            emi = self.calculateEMI(lid)
            num = int(amount//emi)
            if num < 1:
                print('\nSorry...The amount is too low to pay even a Single EMI\n')
            else:
                print(f"\nYou have paid {num} EMIs from the amount {amount} and now - ")
                loan = self.getLoanByID(lid)
                remaining_loan_term = loan.get_loan_term() - num
                remaining_loan_amount = loan.get_principal_amount() - (num*emi)
                self.open()
                self.c.execute(f"Update Loan Set loan_term = {remaining_loan_term}, principal_amount = {remaining_loan_amount} Where loan_id = {lid}")
                self.mydb.commit()
                self.close()
                self.getLoanByID(lid).display_loan_details()
                if remaining_loan_term <= 0 or remaining_loan_amount <= 0:
                    print("\nLoan fully repaid. Congratulations!\n")
        except Exception as e:
            print(e)