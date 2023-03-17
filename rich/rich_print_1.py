#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from rich import print

a_list = [1, 2, 3, 4, 5]
print(a_list)

a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)

a_dict = {"list": a_list, "tuple": a_tuple, "nil": None}
print(a_dict)

other_list = [True, False, None]
print(other_list)
