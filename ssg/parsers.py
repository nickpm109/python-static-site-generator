from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        for extensions in self.extensions:
            if extensions == extension:
                return extension

    def parse(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file

    # def write(self, path, dest, content, ext = ".html"):
        # full_path = self.dest / content /
