class Arithmetic:
    Value1 = 0.0;
    Value2 = 0.0;

    def __init__(self):
        self.Value1 = 0.0;
        self.Value2 = 0.0;

    def AcceptData(self):
        Arithmetic.Value1 = int(input("Please enter Value 1 : "));
        Arithmetic.Value2 = int(input("Please enter Value 2 : "));

    def Addition(self):
        result = Arithmetic.Value1 + Arithmetic.Value2;
        print("Addition = ", result);
        return result;
    
    def Subtraction(self):
        subtract = Arithmetic.Value1 - Arithmetic.Value2;
        print("Subtraction = ", subtract);
        return subtract;

    def Multiplication(self):
        multiply_value = Arithmetic.Value1 * Arithmetic.Value2;
        print("Multiplication = ", multiply_value);
        return multiply_value;

    def Division(self):
        division_value = Arithmetic.Value1 / Arithmetic.Value2;
        print("Division = ", division_value);
        return division_value;

def main():
    arithmetic_calc = Arithmetic();
    arithmetic_calc.AcceptData();
    arithmetic_calc.Addition();
    arithmetic_calc.Subtraction();
    arithmetic_calc.Multiplication();
    arithmetic_calc.Division();

if __name__ == "__main__":
    main();
