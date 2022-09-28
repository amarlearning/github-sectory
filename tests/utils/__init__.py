import subprocess
from os import PathLike
from os.path import join
from pathlib import Path


def gh_sectory_cmd(cwd: PathLike, *args):
    return subprocess.run(["github-sectory", *args], cwd=cwd, capture_output=True)


def data_path():
    return join(Path(__file__).parent, "data")
