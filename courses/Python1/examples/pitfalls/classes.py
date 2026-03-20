# Třídní atributy jsou de facto uloženy ve slovníku
# Ve skutečnosti B a C nemají vlastní hodnoty atributů
# pouze reference do A


class A(object):
    attribute = "foo"


class B(A):
    pass


class C(A):
    pass


print(A.attribute, B.attribute, C.attribute)

A.attribute = "baz"

print(A.attribute, B.attribute, C.attribute)
