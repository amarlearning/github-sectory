# Github Sectory

[![Build Status](https://travis-ci.org/amarlearning/Github-Sectory.svg?branch=master)](https://travis-ci.org/amarlearning/Github-Sectory/)
[![Downloads](https://pepy.tech/badge/github-sectory)](https://pepy.tech/project/github-sectory)
[![HitCount](http://hits.dwyl.io/amarlearning/Github-Sectory.svg)](http://hits.dwyl.io/amarlearning/Github-Sectory)
[![MIT LICENSE](https://img.shields.io/pypi/l/pyzipcode-cli.svg)](http://amarlearning.mit-license.org/)

> CLI for downloading sub-directory of any Github repository using Github Content API!

## Demo

![Demo GitHub Sectory](https://raw.githubusercontent.com/amarlearning/github-sectory/master/screencast.gif)

## Install

```
$ pip install github-sectory
```

## Usage

### Commands available

```
$ github-sectory <link_to_repo_directory>

Example:
  $ github-sectory https://github.com/amarlearning/PyStalker/tree/master/version01

```

> **OR**

```

Options:
	-r, name of the repository where the folder/directory is present.
	-d, name of the directory that you wish to download.
	-u, username/organisation name of owner of repository.

	-b, branch name of the repository, default is master [OPTIONAL].

Usage:
	1. Pass the directory link as an argument-
		$ github-sectory <github-link-to-directory>

	2. Pass the details as an arguments specified below-
		$ github-sectory -u <username> -r <repository-name> -d <directory-name> -b <branch-name>
```

**Note:** Default branch will be master

---

## Issues

You can report the bugs at the [issue tracker](https://github.com/amarlearning/Github-Sectory/issues)

**OR**

You can [tweet me](https://twitter.com/iamarpandey) if you can't get it to work. In fact, you should tweet me anyway.

---

## License

Built with ♥ by Amar Prakash Pandey([@amarlearning](http://github.com/amarlearning)) under [MIT License](http://amarlearning.mit-license.org/)

You can find a copy of the License at http://amarlearning.mit-license.org/
