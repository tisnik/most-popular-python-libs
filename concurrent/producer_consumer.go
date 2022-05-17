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

func consumer(channel chan string) {
	for {
		message := <-channel
		fmt.Printf("Consumer: received %s\n", message)
	}
}

func main() {
	var channel = make(chan string)
	var done = make(chan interface{})
	go producer(channel)
	go consumer(channel)
	<-done
}
