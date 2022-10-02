package main

import (
	"errors"
	"net/url"
	"regexp"
	"strings"
)

func ParseGithubUrl(furl string) (*string, *string, *string, error) {

	u, err := url.Parse(furl)
	if err != nil {
		return nil, nil, nil, err
	}

	fields := strings.FieldsFunc(u.RequestURI(), func(c rune) bool {
		return c == '/'
	})

	err = validateFeilds(fields)
	if err != nil {
		return nil, nil, nil, err
	}

	re := regexp.MustCompile(`\/(?P<USERNAME>[\w]+)\/(?P<REPOSITORY>[\w\d-]+)\/tree\/[\w]+\/(?P<PATH>[\w-]+\/.+)`)
	githubDetails := re.FindStringSubmatch(u.RequestURI())

	return &githubDetails[1], &githubDetails[2], &githubDetails[3], nil

}

func validateFeilds(fields []string) error {
	if len(fields) == 0 {
		return errors.New("empty URL cannot be processed\nCheck docs on how to use Subtory via `subtory --help`")
	}

	if len(fields) == 1 {
		return errors.New("url does not have repository and directory path\nCheck docs on how to use Subtory via `subtory --help`")
	}

	if len(fields) == 2 {
		return errors.New("url point to a Github repository\nUse `git clone` command to get the copy of repository")
	}
	return nil
}
