#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.output as out


code = """
# Body Mass Index calculator

print("Mass (kg): ")
mass = int(input())

print("Height (cm): ")
height = int(input())

# předod výšky na metry
height = height / 100.0

# výpočet (bez jakýchkoli kontrol)
bmi = mass / (height * height)

# výpis výsledku
print("BMI = ", bmi)
"""

out.put_code(code, language="python", rows=15)

code2 = r"""
package main

import "fmt"

// I represents a new interface type (in this case empty interface)
type I interface{}

// T represents an user-defined data type
type T struct{}

func main() {
	var t *T
	if t == nil {
		fmt.Println("t is nil")
	} else {
		fmt.Println("t is not nil")
	}
	var i I = t
	if i == nil {
		fmt.Println("i is nil")
	} else {
		fmt.Println("i is not nil")
	}

}
"""

out.put_code(code2, language="go", rows=15)
