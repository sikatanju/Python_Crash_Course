def get_formatted_name(first, last, middle=''):
    if middle:
        return f'{first.title()} {middle.title()} {last.title()}'
    else:
        return f'{first.title()} {last.title()}'

