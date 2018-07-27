
class Docker:
    def __init__(self, dname, docker_info):
        self.__dname = dname
        self.__docker_info = docker_info

    def getDockerName(self):
        return self.__dname

    def setDockerName(self, dname):
        self.__dname = dname

    def getDockerInfo(self):
        return self.__docker_info

    def setDockerInfo(self, docker_info):
        self.__docker_info = docker_info
