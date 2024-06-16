package main

import (
	iter "github.com/hgfischer/go-iter"
)

func FillInList(size int) None {
	var l List = []None{}
	for _, i := range iter.NewIntSeq(iter.Start(0), iter.Stop(size)).All() {
		l = append(l, (i + 1))
	}
	return None(l)
}
