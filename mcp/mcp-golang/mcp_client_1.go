package main

import (
	"context"
	"log"
	"os/exec"

	mcp "github.com/metoro-io/mcp-golang"
	"github.com/metoro-io/mcp-golang/transport/stdio"
)

func main() {
	cmd := exec.Command("go", "run", "./mcp_server_1.go")

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

	if _, err := client.Initialize(context.Background()); err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	resource, err := client.ReadResource(context.Background(), "pozdrav://")
	if err != nil {
		log.Printf("Failed to read resource: %v", err)
	}

	if resource != nil {
		log.Printf("Resource content: %s", resource)
	}
}
