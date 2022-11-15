import rich

a_list = [1, 2, 3, 4, 5]
rich.print(a_list)

a_tuple = (1, 2, 3, 4, 5)
rich.print(a_tuple)

a_dict = {'list': a_list, 'tuple': a_tuple, 'nil': None}
rich.print(a_dict)

other_list = [True, False, None]
rich.print(other_list)

