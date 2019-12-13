class Demo:
    Value = 10;

    def __init__(self, no1, no2):
        self.no1 = no1; #int(input("Please enter no1 :"));
        self.no2 = no2; #int(input("Please enter no2 :"));

    def fun(self):
        print("No1 = ", self.no1);
        print("No2 = ", self.no2);

    def gun(self):
        print("No1 = ", self.no1);
        print("No2 = ", self.no2);

def main():
    no1 = int(input("Please enter no1 :"));
    no2 = int(input("Please enter no2 :"));
    demoobj1 = Demo(no1,no2);
    demoobj1.fun();

    demoobj2 = Demo(51,101);
    demoobj2.gun();

if __name__ == "__main__":
    main();
    