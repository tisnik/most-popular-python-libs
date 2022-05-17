package main

import (
	"fmt"
)

const (
	num_producers = 5
	num_consumers = 20
)

func producer(id int, channel chan string, done chan interface{}) {
	for i := 1; i <= 10; i++ {
		message := fmt.Sprintf("message %d", i)
		fmt.Printf("Producer %d: %s\n", id, message)
		channel <- message
	}
	done <- struct{}{}
}

func consumer(id int, channel chan string) {
	for {
		message := <-channel
		fmt.Printf("Consumer %d: received %s\n", id, message)
	}
}

func main() {
	var channel = make(chan string)
	var done = make(chan interface{})
	for i := 0; i < num_producers; i++ {
		go producer(i, channel, done)
	}
	for i := 0; i < num_consumers; i++ {
		go consumer(i, channel)
	}
	for i := 0; i < num_producers; i++ {
		<-done
	}
}
