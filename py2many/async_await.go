package main

import (
"fmt")



#[async]
func task() {
fmt.Printf("%v\n","task started");
await!(asyncio.sleep(5));
fmt.Printf("%v\n","task finished");}


func Main() {
task1 := asyncio.create_task(task())
fmt.Printf("%v\n","task created");
await!(task1);
fmt.Printf("%v\n","done");}


