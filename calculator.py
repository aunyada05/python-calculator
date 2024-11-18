class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # Fix: switch a, b

    def multiply(self, a, b):
        result = 0
        is_negative = False

        # Handle negative `b``
        if b < 0:
            is_negative = True
            b = self.subtract(0, b)  

        for _ in range(b):
            result = self.add(result, a)  

        # Handle negative result if b was originally negative
        if is_negative:
            result = self.subtract(0, result) 

        return result

    def divide(self, a, b):
        if b == 0:
            return "Division by zero is not allowed"
        
        result = 0
        is_negative = False

        # Handle negative `a`
        if a < 0:
            is_negative = not is_negative
            a = self.subtract(0, a) 

        # Handle negative `b`
        if b < 0:
            is_negative = not is_negative
            b = self.subtract(0, b) 

        while a >= b:  # Fix: change sign from > to >=
            a = self.subtract(a, b)  
            result = self.add(result, 1)

        # Adjust sign for negative results
        if is_negative:
            result = self.subtract(0, result)  

        return result
    
    def modulo(self, a, b):    
        while a >= b: # Fix: change sign from <= to >=
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))