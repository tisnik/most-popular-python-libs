package main

import (
	"fmt"
	iter "github.com/hgfischer/go-iter"
)

func A(m int, n int) int {
	if m == 0 {
		return (n + 1)
	}
	if n == 0 {
		return A((m - 1), 1)
	}
	return A((m - 1), A(m, (n-1)))
}

func CheckA() {
	for _, m := range iter.NewIntSeq(iter.Start(0), iter.Stop(4)).All() {
		for _, n := range iter.NewIntSeq(iter.Start(0), iter.Stop(5)).All() {
			fmt.Printf("%v %v %v\n", m, n, A(m, n))
		}
	}
}
