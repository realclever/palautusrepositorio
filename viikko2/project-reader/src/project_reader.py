from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        as_toml = toml.loads(content)
        dict = as_toml['tool']['poetry']

        name = dict['name']
        description = dict['description']
        dependencies = dict['dependencies']
        dev_dependencies = dict['group']['dev']['dependencies']
        license = dict['license']
        authors = dict['authors']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
