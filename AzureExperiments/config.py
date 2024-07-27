import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r'/Users/xiao/Projects/git/AnalysisProjects/AzureExperiments/config.ini')

        self.SUBSCIRPTION_ID = self.config.get('DEFAULT', 'SUBSCIRPTION_ID')
        self.RESOURCE_GROUP = self.config.get('DEFAULT', 'RESOURCE_GROUP')
        self.WORKSPACE_NAME = self.config.get('DEFAULT', 'WORKSPACE_NAME')
