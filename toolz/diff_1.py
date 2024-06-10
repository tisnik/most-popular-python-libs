#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from toolz.itertoolz import diff

seq1 = [1, 2, 3, 4, 5, 6, 7]
seq2 = [1, 0, 3, 4, 9, 9, 0]

print(list(diff(seq1, seq2)))
