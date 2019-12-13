class Circle:
    PI = 3.1415;
    def __init__(self): #radius, area, circumference
        self.radius = 0.0;
        self.area = 0.0;
        self.circumference = 0.0;

    def Accept(self):
        radius = int(input("Please enter Radius Value: "));
        return radius;

    def CalculateArea(self,rad):
        area = Circle.PI * rad * rad;
        return area;

    def CalculateCircumference(self,rad):
        circumference = 2 * Circle.PI * rad;
        return circumference;

    def Display(self, rad, area, circum):
        print("Radius = ", rad);
        print("Area = ",area);
        print("Circumference = ", circum);

def main():
    #rad = int(input("Please enter"))
    circleobj = Circle();
    rad = circleobj.Accept();
    area1 = circleobj.CalculateArea(rad);
    circum1 =circleobj.CalculateCircumference(rad);
    circleobj.Display(rad, area1,circum1);

if __name__ == "__main__":
    main();
