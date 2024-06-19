package main

import (
"fmt")



type Foo struct {
_value ST0
}
func __init__[T0 any](self Foo, value T0 any) {
self._value = value}


func __add__[T0 any](self Foo, other T0 any) Foo {
return Foo{_value: (self._value + other._value)}}


func __str__(self Foo) string {
return ("*"*self._value)}



func TestAdding() {
var f1 Foo = Foo{_value: 1}
var f2 Foo = Foo{_value: 2}
fmt.Printf("%v\n",(f1 + f2));}


