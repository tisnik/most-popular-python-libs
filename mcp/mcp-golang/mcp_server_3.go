// Jednoduchý MCP server s jediným zdrojem

package main

import (
	"strconv"

	mcp_golang "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

type FactorialArguments struct {
	N int `json:"n" jsonschema:"required,description=input value for factorial computation"`
}

func factorialHandler(arguments FactorialArguments) (*mcp_golang.ToolResponse, error) {
	fact := 1
	for i := range arguments.N {
		fact *= 1 + i
	}
	toolResults := mcp_golang.NewTextContent(strconv.Itoa(fact))
	response := mcp_golang.NewToolResponse(toolResults)
	return response, nil
}

func main() {
	done := make(chan struct{})

	server := mcp_golang.NewServer(stdio.NewStdioServerTransport())

	err := server.RegisterTool("factorial", "Výpočet faktoriálu", factorialHandler)
	if err != nil {
		panic(err)
	}

	err = server.Serve()
	if err != nil {
		panic(err)
	}

	<-done
}
