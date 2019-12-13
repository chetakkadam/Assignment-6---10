class Numbers:
    Value = 0.0;

    def __init__(self):
        self.num = int(input("Please Enter Number : "));

    def ChkPrime(self):
        chk = False;
        if self.num > 1 :
            for i in range(2, self.num//2):
                if self.num % 2 == 0 :
                    print(self.num, " is not Prime Number.");
                    return chk;
                    break;
            else:
                chk = True;
                print(self.num, " is Prime Number.");
        else:
            chk = True; 
            return chk;

    def ChkPerfect(self):
        sum = 0;
        chkresult = False;
        for i in range(1, self.num):
            if self.num % i == 0:
                sum = sum + i;
        if sum == self.num:
            chkresult = True;
            print("%d is a perfect number" %self.num);
        else:
            chkresult = False;
            print(" %d is not perfect number" %self.num);
        return chkresult;

    def Chkfactor(self):
        self.lst = [];
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                self.lst.append(i);
        print("List of Factor Numbers : ", self.lst);
        return self.lst;

    def SumfactorNum(self):
        sum = 0;
        for i in range(0, len(self.lst)):
            sum = sum + self.lst[i];
        print("Addition of Factorial Number : ", sum);
        return sum;

def main():
    num1 = Numbers();
    num1.ChkPrime();
    num1.ChkPerfect();
    lst = num1.Chkfactor();
    num1.SumfactorNum();

   
if __name__ == "__main__":
    main();
                
            


