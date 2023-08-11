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

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, major, minor):
        self._major = major
        self._minor = minor

    def _is_valid_version(self, other):
        return (hasattr(other, "_major") and
                hasattr(other, "_major"))

    def __eq__(self, other):
        if not self._is_valid_version(other):
            return NotImplemented
        return (self._major, self._minor) == \
               (other._major, other._minor)

    def __lt__(self, other):
        if not self._is_valid_version(other):
            return NotImplemented
        return (self._major, self._minor) < \
               (other._major, other._minor)


v1 = Version(1, 0)
v2 = Version(1, 2)
v3 = Version(1, 2)
v4 = Version(2, 1)

print(v1==v2)
print(v2==v3)

print()

print(v1<v2)
print(v1<v4)
print(v2<v4)

print()

print(v1>v2)
print(v1>v4)
print(v2>v4)
