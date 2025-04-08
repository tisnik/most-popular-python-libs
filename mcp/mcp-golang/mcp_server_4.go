// Jednoduchý MCP server s jediným zdrojem

package main

import (
	"fmt"

	mcp_golang "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

type Content struct {
	Title       string `json:"title" jsonschema:"required,description=The title to submit"`
	Description string `json:"description" jsonschema:"description=The description to submit"`
}

func promptHandler(arguments Content) (*mcp_golang.PromptResponse, error) {
	text := mcp_golang.NewTextContent(fmt.Sprintf("Hello, %s!", arguments.Title))
	message := mcp_golang.NewPromptMessage(text, mcp_golang.RoleUser)
	response := mcp_golang.NewPromptResponse("description", message)
	return response, nil

}

func main() {
	done := make(chan struct{})

	server := mcp_golang.NewServer(stdio.NewStdioServerTransport())

	err := server.RegisterPrompt("prompt_test", "This is a test prompt", promptHandler)

	err = server.Serve()
	if err != nil {
		panic(err)
	}

	<-done
}
