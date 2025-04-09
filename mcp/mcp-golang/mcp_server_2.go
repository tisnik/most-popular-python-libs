// Jednoduchý MCP server s jediným zdrojem

package main

import (
	mcp_golang "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

const resourceURI = "pozdrav://"
const resourceName = "greeting"
const resourceDescription = "Odpověď s pozdravem"
const resourceMimeType = "text/plain"

func resourceHandler() (*mcp_golang.ResourceResponse, error) {
	resource := mcp_golang.NewTextEmbeddedResource(
		resourceURI,
		"Hello, dear client",
		resourceMimeType)
	response := mcp_golang.NewResourceResponse(resource)
	return response, nil
}

func main() {
	done := make(chan struct{})

	server := mcp_golang.NewServer(stdio.NewStdioServerTransport())

	err := server.RegisterResource(
		resourceURI,
		resourceName,
		resourceDescription,
		resourceMimeType,
		resourceHandler)
	if err != nil {
		panic(err)
	}

	err = server.Serve()
	if err != nil {
		panic(err)
	}

	<-done
}
