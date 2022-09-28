from utils import gh_sectory_cmd
from utils import data_path
from os import listdir
from os.path import join
from subprocess import CompletedProcess

FILES_IN_DATA = {"different_format.md", "empty_file", "text_file.txt"}
HELP_TEXT = """
        \nCLI for downloading sub-directory of any Github repository.
        \nOptions:
        \t-r, name of the repository where the folder/directory is present.
        \t-d, name of the directory that you wish to download.
        \t-u, username/organisation name of owner of repository.

        \t-b, branch name of the repository, default is master [OPTIONAL].

        \nUsage:
        \t1. Pass the directory link as an argument-
        \t\t$ github-sectory <github-link-to-directory>

        \t2. Pass the details as an arguments specified below-
        \t\t$ github-sectory -u <username> -r <repository-name> -d <directory-name> -b <branch-name>
"""


def check_successful_output(result: CompletedProcess):
    stdout = result.stdout.decode("utf-8")
    assert result.returncode == 0
    assert not result.stderr
    assert "[ Fetching folder content ]" in stdout
    assert "[ Downloading all required files ]" in stdout
    assert "[ Finished ]" in stdout


def check_downloaded_data_files(path: str):
    dirs = listdir(path)
    assert set(dirs) == FILES_IN_DATA
    for file in dirs:
        with open(join(path, "tests", file)) as f:
            downloaded = f.readlines()
        with open(join(data_path(), file)) as f:
            original = f.readlines()
        assert downloaded == original


def test_with_url(tmp_path):
    # Change URL to "https://github.com/amarlearning/github-sectory/tree/master/tests/data"
    res = gh_sectory_cmd(tmp_path, "https://github.com/pytest-dev/pytest/tree/main/changelog")
    assert "[ Validating Input URL ]" in res.stdout.decode("utf-8")
    check_successful_output(res)

    # Replace next 5 lines with commented code once this test is in master
    dirs = listdir(tmp_path)
    assert dirs == ["changelog"]
    dirs = listdir(join(tmp_path, "changelog"))
    assert len(dirs) >= 3
    assert "README.rst" in dirs

    # dirs = listdir(tmp_path)
    # assert dirs == ["tests"]
    # check_downloaded_data_files(join(tmp_path, "tests"))


def test_with_options(tmp_path):
    # Change params to: "-u", "amarlearning", "-r", "github-sectory", "-d", "tests/data"
    res = gh_sectory_cmd(tmp_path, "-u", "pytest-dev", "-r", "pytest", "-d", "changelog")
    assert "[ Validating Input Parameters ]" in res.stdout.decode("utf-8")
    check_successful_output(res)

    # Replace next 5 lines with commented code once this test is in master
    dirs = listdir(tmp_path)
    assert dirs == ["changelog"]
    dirs = listdir(join(tmp_path, "changelog"))
    assert len(dirs) >= 3
    assert "README.rst" in dirs

    # dirs = listdir(tmp_path)
    # assert dirs == ["tests"]
    # check_downloaded_data_files(join(tmp_path, "tests"))


def test_without_params(tmp_path):
    res = gh_sectory_cmd(tmp_path)
    assert res.returncode == 0
    assert not res.stderr
    assert res.stdout.decode("utf-8").strip() == HELP_TEXT.strip()
    assert not listdir(tmp_path)


def test_nested(tmp_path):
    # Change URL to "https://github.com/amarlearning/github-sectory/tree/master/tests"
    res = gh_sectory_cmd(tmp_path, "https://github.com/pytest-dev/pytest/tree/main/.github")
    check_successful_output(res)

    # Replace next 7 lines with commented code once this test is in master
    dirs = listdir(tmp_path)
    assert dirs == [".github"]
    dirs = set(listdir(join(tmp_path, ".github")))
    assert {"workflows", "ISSUE_TEMPLATE", "config.yml"}.issubset(dirs)
    files = listdir(join(tmp_path, ".github", "workflows"))
    assert len(files) >= 3
    assert "deploy.yml" in files

    # dirs = listdir(tmp_path)
    # assert dirs == ["tests"]
    # dirs = set(listdir(join(tmp_path, "tests")))
    # assert {"data", "utils", "test_system.py"}.issubset(dirs)
    # with open(join(tmp_path, "tests", "test_system.py")) as f:
    #     downloaded = f.readlines()
    # assert "def test_nested(tmp_path):\n" in downloaded
    # check_downloaded_data_files(join(tmp_path, "tests", "data"))

