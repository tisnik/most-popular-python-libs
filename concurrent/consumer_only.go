package main

import (
	"fmt"
)

func consumer(channel chan string) {
	for {
		message := <-channel
		fmt.Printf("Consumer: received %s\n", message)
	}
}

func main() {
	var channel = make(chan string)
	var done = make(chan interface{})
	go consumer(channel)
	<-done
}
