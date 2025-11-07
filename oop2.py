class Calculator:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        while True:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                if len(self.numbers) < 2:
                    print("Please enter at least 2 numbers!")
                    self.numbers = []
                    continue
                break
            try:
                self.numbers.append(float(num))
            except ValueError:
                print("Please enter a valid number!")

    def add(self):
        result = sum(self.numbers)
        print(f'Sum of {self.numbers} is: {result}')

    def minus(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        print(f'Subtraction result of {self.numbers} is: {result}')

    def multi(self):
        result = 1
        for num in self.numbers:
            result *= num
        print(f'Multiplication of {self.numbers} is: {result}')

    def div(self):
        result = self.numbers[0]
        try:
            for num in self.numbers[1:]:
                if num == 0:
                    raise ZeroDivisionError
                result /= num
            print(f'Division result of {self.numbers} is: {result}')
        except ZeroDivisionError:
            print('Cannot divide by zero!')

    def menu(self):
        while True:
            user_input = input("""
            1-add multiple numbers
            2-minus multiple numbers
            3-multiply multiple numbers
            4-divide multiple numbers
            5-exit
            Your choice: """)
            
            if user_input in ['1', '2', '3', '4']:
                self.numbers = []  # Reset numbers list
                self.get_numbers()
                if user_input == '1':
                    self.add()
                elif user_input == '2':
                    self.minus()
                elif user_input == '3':
                    self.multi()
                elif user_input == '4':
                    self.div()
            elif user_input == '5':
                print('Goodbye!')
                break
            else:
                print('Invalid choice! Try again.')

calc = Calculator()
calc.menu()