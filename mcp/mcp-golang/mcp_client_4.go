package main

import (
	"context"
	"log"
	"os/exec"

	mcp "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

// Define type-safe arguments
type CalculateArgs struct {
	N int `json:"n"`
}

func main() {
	cmd := exec.Command("go", "run", "./mcp_server_4.go")

	stdin, err := cmd.StdinPipe()
	if err != nil {
		log.Fatalf("Failed to get stdin pipe: %v", err)
	}

	stdout, err := cmd.StdoutPipe()
	if err != nil {
		log.Fatalf("Failed to get stdout pipe: %v", err)
	}

	if err := cmd.Start(); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}

	defer cmd.Process.Kill()

	transport := stdio.NewStdioServerTransportWithIO(stdout, stdin)
	client := mcp.NewClient(transport)

	ctx := context.Background()

	if _, err := client.Initialize(ctx); err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	type Content struct {
		Title       string  `json:"title" jsonschema:"required,description=The title to submit"`
		Description *string `json:"description" jsonschema:"description=The description to submit"`
	}
	content := Content{Title: "Foo"}

	response, err := client.GetPrompt(ctx, "prompt_test", content)
	if err != nil {
		log.Fatalf("Failed to get prompt: %v", err)
	}

	if response != nil {
		messages := response.Messages
		for i, message := range messages {
			text := *message.Content.TextContent
			log.Println(i, text.Text)
		}
	}
}
