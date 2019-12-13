class BankAccount:
    ROI = 10.5;

    def __init__(self):
        self.Name = input("Please Enter Name : ");
        self.Amount = int(input("Please Enter Amount : "));

    def Display(self):
        print("Customer Name : ", self.Name);
        print("Amount : ", self.Amount);

    def Deposit(self):
        value = int(input("Please Enter Amount to Deposit : "));
        self.Amount = self.Amount + value;
        print("Total Amount : ", self.Amount);

    def Withdraw(self):
        value = int(input("Please Enter Amount to Withdraw : "));
        self.Amount = self.Amount - value;
        print("Total Amount : ", self.Amount);

    def CalculateIntrest(self):
        value = self.Amount * (BankAccount.ROI / 100);
        print("Interest Amount : ", value);
        print("Total Amount After Interest : ", self.Amount + value);


def main():
    customer1 = BankAccount();
    customer1.Display();
    customer1.Deposit();
    customer1.Withdraw();
    customer1.CalculateIntrest();

if __name__ == "__main__":
    main();
