
class Calculator:

   

    def __init__(self):
        pass
    # Dekorátor, ami a metódust a Calculator osztályhoz köti
    @classmethod
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

def test_calculator():
    a = 54
    b = 43

    # Statikus metódus meghívása, példányosítás nélkül is hívható a dekorátor miatt
    print(Calculator.add(a, b))

    calc = Calculator()
    print(calc.add(a, b))
    print(calc.subtract(a, b))
    print(calc.multiply(a, b))
    print(calc.divide(a, b))

if __name__ == "__main__":
    test_calculator()
