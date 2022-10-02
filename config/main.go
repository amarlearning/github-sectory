package config

import (
	"fmt"
	"os"

	"github.com/joho/godotenv"
)

func LoadEnvVariables() {
	err := godotenv.Load(".env")

	if err != nil {
		fmt.Println("Application error - unable to load necessary env variables")
		os.Exit(1)
	}
}
