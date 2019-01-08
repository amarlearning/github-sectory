# Github Sectory

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ce49706c9f594d46b127e91cd098f6c7)](https://app.codacy.com/app/amar.om1994/Github-Sectory?utm_source=github.com&utm_medium=referral&utm_content=amarlearning/Github-Sectory&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/amarlearning/Github-Sectory.svg?branch=master)](https://travis-ci.org/amarlearning/Github-Sectory/)
[![PyPI](https://img.shields.io/badge/pypi-v1.1.4-blue.svg)](https://pypi.python.org/pypi/github-sectory)
[![Issues](https://camo.githubusercontent.com/926d8ca67df15de5bd1abac234c0603d94f66c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)](https://github.com/amarlearning/Github-Sectory/issues)
[![HitCount](http://hits.dwyl.io/amarlearning/Github-Sectory.svg)](http://hits.dwyl.io/amarlearning/Github-Sectory)
[![MIT LICENSE](https://img.shields.io/pypi/l/pyzipcode-cli.svg)](http://amarlearning.mit-license.org/)
[![Say Thanks!](https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg)](https://saythanks.io/to/amarlearning)

> CLI for downloading sub-directory of any Github repository using Github Content API!

## Demo
![Demo GitHub Sectory](https://raw.githubusercontent.com/amarlearning/Github-Sectory/master/extras/sreencast.gif)

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

$ github-sectory <github_username> -r <repository name> -d <directory name> [arguments]

Needed:
  -r, -d for repository and directory

Optional:
  -b for branch                              [boolean]
 
Examples:
  $ github-sectory GoogleChrome -r samples -d push-messaging-and-notifications 
  $ github-sectory GoogleChrome -r samples -d push-messaging-and-notifications -b gh-pages
 
```
**Note:** Default branch will be master

***

## Issues

You can report the bugs at the [issue tracker](https://github.com/amarlearning/Github-Sectory/issues)

**OR**

You can [tweet me](https://twitter.com/iamarpandey) if you can't get it to work. In fact, you should tweet me anyway.

***

## License

Built with ♥ by Amar Prakash Pandey([@amarlearning](http://github.com/amarlearning)) under [MIT License](http://amarlearning.mit-license.org/) 

You can find a copy of the License at http://amarlearning.mit-license.org/
