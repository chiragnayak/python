# Function
def validate_mobile_number(mobile):
    status = 'invalid'

    '''
    Should be 10 Digits
    First digit should be between 6 and 9
    '''
    if len(mobile) == 10 and mobile.isdigit() and int(mobile[0]) in range(6, 10):
        status = 'valid'

    return status

# Lambda Expression
sqr = lambda max_num: [num ** 2 for num in range(1, max_num + 1)]

# User defined exception to handle the invalid number
class InvalidNumber(Exception):
    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg

    def display_err_msg(self):
        return f'An Error has Occurred: {self.err_msg}'
