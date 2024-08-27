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

# puvodni zpusob pouziti triky KFold

from sklearn.cross_validation import KFold
kf = KFold(20, n_fonds=5, shuffle=False)

# iteration   training set   testing set
for iteration, data in enumerate(kf, start=1):
    print(iteration, data[0], data[1])
