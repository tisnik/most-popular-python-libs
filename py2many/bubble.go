package main

import (
"fmt"
iter "github.com/hgfischer/go-iter")



func BubbleSort[T0 any](size T0 any) {
a := iter.NewIntSeq(iter.Start(0), iter.Stop(size)).All().iter().map(|i| randrange(random, 0, 10000)).collect::<Vec<_>>()
for _, i := range iter.NewIntSeq(iter.Start((size - 1)), iter.Stop(0), iter.Step(-1)).All() {
for _, j := range iter.NewIntSeq(iter.Start(0), iter.Stop(i)).All() {
if(a[j] > a[(j + 1)]) {
{
var __tmp1, __tmp2 = a[(j + 1)], a[j]
a[j] = __tmp1
a[(j + 1)] = __tmp2
}
}
}
}
fmt.Printf("%v\n",a);}


