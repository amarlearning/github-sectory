package main

import (
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestUtils_ParseGithubUrl(t *testing.T) {

	testCases := []struct {
		name   string
		input  string
		output []string
		isErr  bool
		error  string
	}{
		{
			name:  "Empty URL",
			input: "",
			isErr: true,
			error: errors.New("empty URL cannot be processed\nCheck docs on how to use Subtory via `subtory --help`").Error(),
		},
		{
			name:  "Invalid URL",
			input: "this is not a 7264782368742368746328^&*^%%$#%$#%$valid url",
			isErr: true,
			error: errors.New("parse \"this is not a 7264782368742368746328^&*^%%$\": invalid URL escape \"%%$\"").Error(),
		},
		{
			name:  "URL of Github User",
			input: "https://github.com/amarlearning",
			isErr: true,
			error: errors.New("url does not have repository and directory path\nCheck docs on how to use Subtory via `subtory --help`").Error(),
		},
		{
			name:  "URL of Github Repository with no directory path",
			input: "https://github.com/amarlearning/github-sectory",
			isErr: true,
			error: errors.New("url point to a Github repository\nUse `git clone` command to get the copy of repository").Error(),
		},
		{
			name:   "URL of Github Repository with directory path",
			input:  "https://github.com/amarlearning/chat-rooms/tree/master/src/main",
			output: []string{"amarlearning", "chat-rooms", "src/main"},
			isErr:  false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			username, repository, path, err := ParseGithubUrl(tc.input)
			if tc.isErr {
				assert.EqualError(t, err, tc.error)
			} else {
				assert.Nil(t, err)
				assert.Equal(t, tc.output, []string{*username, *repository, *path})
			}
		})
	}
}
