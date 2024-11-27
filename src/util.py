class UserInputError(Exception):
    pass

def validate_todo(content):
    if len(content) < 5:
        raise UserInputError('Todo content length must be greater than 4')

    if len(content) > 100:
        raise UserInputError('Todo content length must be smaller than 100')

def string_or_empty_string(s):
    if s is None:
        return ''
    
    return s
