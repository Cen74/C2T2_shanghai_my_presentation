# coding=utf-8

def pick_keys_from_dict(mydict):
    """return keys containing 'A' from mydict

    Arg:
        mydict (dict)

    Return: 
        A list
    """
    mylist = []
    for k in mydict:
        if k.startswith('A'):
            mylist.append(k)
    return mylist

def test1():
    """test for pick_keys_from_dict

    """
    print pick_keys_from_dict({'A1':1,'B2':2,'C3':3})
    print pick_keys_from_dict({'A1':1,'B2':2,'C3':3,'A4':4})
    # assert pick_keys_from_dict({'A1':1,'B2':2,'C3':3}) == ['A1']

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
    sorted_list = sorted(mylist, key=lambda x: int(x[1:]))
    return sorted_list

def test2():
    """test for sorted_list_by_number_inside

    """
    print sorted_list_by_number_inside(['A5', 'A3', 'A2'])
    # print sorted_list_by_number_inside(['A5', 'A20', 'A10'])
    # print sorted_list_by_number_inside(['A2', 'A5', 'A3'])
    # print sorted_list_by_number_inside(['A1', 'A11', 'A10'])
    # print sorted_list_by_number_inside(['AB5', 'AB3', 'AB2'])

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
        result.append(mydict[k])
    return result

def test3():
    """test for pick_values_from_dict

    """
    print pick_values_from_dict({'a':1,'b':2,'c':3}, ['a','b'])
    print pick_values_from_dict({'a':1,'b':2,'c':3}, ['a','b','d'])

def main():
    adict = {'A1': 41, 'A3': 23, 'A9': 39, 'A10': 10, 
             'B1': -1, 'B2': -2, 'C5': '5', 'C8': '8'}
    keys_A_list = pick_keys_from_dict(adict)
    ordered_keys_A_list = sorted_list_by_number_inside(key_A_list)
    values_A_list = pick_values_from_dict(adict, ordered_keys_A_list)
    print values_A_list

if __name__ == '__main__':
    # main()
    # test1()
    # test2()
    test3()