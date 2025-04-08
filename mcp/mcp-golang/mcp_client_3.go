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
	cmd := exec.Command("go", "run", "./mcp_server_3.go")

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

	for n := range 11 {
		args := CalculateArgs{N: n}
		response, err := client.CallTool(
			context.Background(),
			"factorial",
			args)
		if err != nil {
			log.Fatalf("Failed to call tool: %v", err)
		}

		if response != nil && len(response.Content) > 0 {
			factorial := response.Content[0].TextContent.Text
			log.Printf("%d! = %s", n, factorial)
		}
	}

}
