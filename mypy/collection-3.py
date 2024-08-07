#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from typing import List


class Collection[T]():
    def __init__(self) -> None:
        self.collection : List[T] = []

    def append(self, item: T) -> None:
        self.collection.append(item)

    def get_all(self) -> List[T]:
        return self.collection


c = Collection[int]()
c.append(1)
c.append("foo")
