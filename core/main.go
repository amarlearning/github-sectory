package core

import (
	"context"
	"fmt"
	"net/http"
	"os"

	"github.com/amarlearning/subtory/core/client"
	"github.com/amarlearning/subtory/files"
	"github.com/google/go-github/github"
)

func Subtory(directoryUrl string) {
	client := client.Get()
	ctx := context.Background()
	doTheJob(client, ctx, "google", "go-github", "test")
}

func doTheJob(client *github.Client, ctx context.Context, ownerName, reposiotryName, path string) {
	fileContent, directoryContent, resp, err := client.Repositories.GetContents(ctx, ownerName, reposiotryName, path, nil)

	if err != nil {
		os.RemoveAll(path)
		panic(err)
	}

	fmt.Println(resp.Rate.Remaining)

	if fileContent != nil {
		downloadFile(*fileContent.Path, *fileContent.DownloadURL)
	}

	if directoryContent != nil {
		for i := 0; i < len(directoryContent); i++ {
			doTheJob(client, ctx, ownerName, reposiotryName, *directoryContent[i].Path)
		}
	}
}

func downloadFile(filepath, downloadURL string) {

	resp, err := http.Get(downloadURL)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	err = files.Write(filepath, resp.Body)
	if err != nil {
		panic(err)
	}
}
