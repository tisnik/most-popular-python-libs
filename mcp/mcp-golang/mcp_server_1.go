// Jednoduchý MCP server s jediným zdrojem

package main

import (
	mcp_golang "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

func resourceHandler() (*mcp_golang.ResourceResponse, error) {
	resource := mcp_golang.NewTextEmbeddedResource(
		"pozdrav://",
		"Hello, dear client",
		"text/plain")
	response := mcp_golang.NewResourceResponse(resource)
	return response, nil
}

func main() {
	done := make(chan struct{})

	server := mcp_golang.NewServer(stdio.NewStdioServerTransport())

	err := server.RegisterResource(
		"pozdrav://",
		"resource_test",
		"This is a test resource", "text/plain", resourceHandler)
	if err != nil {
		panic(err)
	}

	err = server.Serve()
	if err != nil {
		panic(err)
	}

	<-done
}
