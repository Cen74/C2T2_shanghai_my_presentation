# coding=utf-8

def pick_keys_from_dict(mydict, startswith='A'):
    """return keys starts with startswith from mydict

    Arg:
        mydict (dict)

    Return: 
        A list
    """
    mylist = []
    for k in mydict:
        if k.startswith(startswith):
            mylist.append(k)
    return mylist

def sorted_list_by_number_inside(mylist):
    """return a list sorted by the number inside the list element

    Arg:
        mylist (list)

    Return:
        A list

    Example:
        >>> sorted_list_by_number_inside(['A2', 'A5', 'A3'])
        ['A2', 'A3', 'A5']
    """
    import re
    sorted_list = sorted(mylist, key=lambda x: int(re.findall(r'\d+', x)[0]))
    return sorted_list

def pick_values_from_dict(mydict, mylist):
    """return a list of values of mydict according to keys in mylist

    Args:
        mydict (dict)
        mylist (list): A list of keys
    
    return:
        A list
    """
    result = []
    for k in mylist:
        if k in mydict:
            result.append(mydict[k])
    return result

def main():
    adict = {'A1': 41, 'A3': 23, 'A9': 39, 'A10': 10, 
             'B1': -1, 'B2': -2, 'C5': '5', 'C8': '8'}
    keys_A_list = pick_keys_from_dict(adict)
    ordered_keys_A_list = sorted_list_by_number_inside(keys_A_list)
    values_A_list = pick_values_from_dict(adict, ordered_keys_A_list)
    print values_A_list

if __name__ == '__main__':
    main()