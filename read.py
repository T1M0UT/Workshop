"""Module made for reading from csv file for tracking program
    """


def read_file(file_path: str) -> dict:
    """function that reads csv file and returns dict \
woth date as key and list with sublists as values

    Args:
        file_path (str): file destination

    Returns:
        dict: dict
    """
    with open(file_path, 'r', encoding='utf_8') as file:
        dates = file.readlines()
        dates.pop(0)
    
    dates_tasks = dict()
    for line in dates:
        elements = line.split(',')
        elements[-1] = elements[-1].rstrip('\n')
        date = elements.pop(0)
        if date in dates_tasks:
            old_tasks = dates_tasks[date]
            tasks = old_tasks + [elements]
            dates_tasks[date] = tasks
        else:
            dates_tasks[date] = [elements]

    return dates_tasks


def write_file(file_path, new_dict):
    """function that writes in file new dict

    Args:
        file_path ([type]): file destination
        new_dict ([type]): new dict with same type of keys and \
values as in read_file
    """
    with open(file_path, 'w', encoding='utf_8') as file:
        first_line = 'DATES,TASK,NUMBER_NEEDED,REAL_NUMBER,PRIORITY,SUCCESS,FAILURE\n'
        file.write(first_line)
        for date in new_dict:
            for value in new_dict[date]:
                values = ''
                for task in value[:-1]:
                    values += task + ','
                values += value[-1]
                line = date + ',' + values
                file.write(line + '\n')



if __name__ == '__main__':
    import doctest