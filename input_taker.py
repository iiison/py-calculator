def input_taker(val_count, val = 0):
    message = 'Enter Value {}: '.format(val_count) if val == 0 else 'Enter Value {}({}): '.format(val_count, val)

    value = input(message)
    fmt_value = float(value) if value != '' else val
    print(fmt_value)

    return fmt_value

def addition(val_1, val_2):
    return val_1 + val_2

def subtraction(val_1, val_2):
    return val_1 - val_2

def multiplication(val_1, val_2):
    return val_1 * val_2

def division(val_1, val_2):
    return val_1 / val_2

def operation_selector():
    operation = str(input('Select Operation(+, -, *, /): '))
    operation = '+' if operation == '' else operation

    operation_map = {
        '+' : addition,
        '-' : subtraction,
        '*' : multiplication,
        '/' : division
    }

    return operation_map[operation]

