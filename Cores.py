def cores(x):
    if x == 'red':
        return '\033[31m'
    elif x == 'blue':
        return '\033[34m'
    elif x == 'green':
        return '\033[32m'
    elif x == 'yellow':
        return '\033[33m'
    elif x == 'nula':
        return '\033[0m'
