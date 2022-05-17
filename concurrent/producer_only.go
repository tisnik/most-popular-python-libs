package main

import (
	"fmt"
)

func producer(channel chan string) {
	for i := 1; i <= 10; i++ {
		message := fmt.Sprintf("message %d", i)
		fmt.Printf("Producer: %s\n", message)
		channel <- message
	}
}

func main() {
	var channel = make(chan string)
	var done = make(chan interface{})
	go producer(channel)
	<-done
}
