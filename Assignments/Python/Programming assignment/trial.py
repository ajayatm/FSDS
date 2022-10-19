from xml.etree.ElementTree import C14NWriterTarget


def calculator_welcome():
    print('Calculator provides following options:')
    print('1. Add two numbers')
    print('2. Substract two numbers')
    print('3. Multiply two numbers')
    print('4. Divide two numbers')
    return None

def get_option():
    try:
        a = int(input('Please select an option: '))
        if a < 1 or a > 4:
            print('Invalid option, please try again')
            get_option()
        return a
    except:
        print('Invalid option, please try again')
        get_option()

def get_first_operand(option):
    try:
        a = float(input('Please select first operand: '))
        return a
    except:
        print('Invalid first operand, please try again')
        get_first_operand()

def get_second_operand(option):
    try:
        b = float(input('Please select second operand: '))
        if option == 4 and b == 0:
            print('Division by zero not allowed')
            c = get_second_operand(option)
            return c
        return b
    except:
        print('Invalid second operand, please try again')
        get_second_operand(option)

def process_calculator():
    try:
        calculator_welcome()
        option = get_option()
        x = get_first_operand(option)
        y = get_second_operand(option)
        if option == 1:
            print('Sum of operands:', x + y)
        if option == 2:
            print('Difference of operands:', x - y)
        if option == 3:
            print('Product of operands:', x*y)
        if option == 4:
            print('Division of operands:', x/y)
    except Exception as msg:
        print(msg)


process_calculator()