package cmd

import (
	"os"

	"github.com/amarlearning/subtory/config"
	"github.com/amarlearning/subtory/core"
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "subtory",
	Short: "A CLI for downloading sub-directory of any GitHub repository",
	Run: func(cmd *cobra.Command, args []string) {
		core.Subtory(args[1])
	},
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	config.LoadEnvVariables()
}
