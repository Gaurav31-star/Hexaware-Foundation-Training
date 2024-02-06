import mysql.connector as connection

from Loan import Loan
from Customer import Customer

from ServiceProvider import LoanRepository

class MainModule():
    def main():
        lp = LoanRepository()
        while True:
            print("\n----------Main Menu----------")
            print("Press-1 to Apply for a Loan")
            print("Press-2 to Check Loan Status")
            print("Press-3 to Calculate Interest")
            print("Press-4 to Calculate EMI")
            print("Press-5 to Loan Repayment")
            print("Press-6 to Exit")
            ch = int(input())
            if ch == 1:
                c = int(input('\nEnter Your Customer ID :'))
                cust = lp.getCustomerByID(c)
                if not cust:
                    n = input('Enter Your Name : ')
                    eml = input('Enter Your Email Address : ')
                    pno = input("Enter Your Phone Number : ")
                    add = input('Enter Your Address : ')
                    cscore = int(input('Enter Your Credit Score : '))
                    c = Customer(name=n, email_address=eml, phone_number=pno, address=add, credit_score=cscore).insert_new_customer()
                pa = int(input('Enter the Principal Amount : '))
                ltm = int(input('Enter the Loan Term in Months : '))
                lty = input('Enter the Loan Type (CarLoan/HomeLoan) : ')
                loan = Loan(customer_id=c, principal_amount=pa, loan_term=ltm, loan_type=lty)
                lp.applyLoan(loan)
            elif ch == 2:
                lid = int(input('\nEnter Your Loan ID : '))
                lp.loanStatus(lid)
            elif ch == 3:
                lid = int(input('\nEnter Your Loan ID : '))
                print(f"Total Interest of this Loan Amounts to : {lp.calculateInterest(lid)}")
            elif ch == 4:
                lid = int(input('\nEnter Your Loan ID : '))
                print(f"The EMI amounts to : {lp.calculateEMI(lid)}")
            elif ch == 5:
                lid = int(input('\nEnter Your Loan ID : '))
                am = int(input('Enter Your Total Amount : '))
                lp.loanRepayment(lid, am)
            elif ch == 6:
                print("\n----------Thank You----------\n")
                break
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n')


if __name__ == "__main__":
    MainModule.main()