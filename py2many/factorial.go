package main




func Factorial[T0 any](n T0 any) int {
if(n < 0) {
return nil
}
if(n == 0) {
return 1
}
var result int = (n*Factorial((n - 1)))
return result}


