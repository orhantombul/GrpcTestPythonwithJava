class Container:
    def __init__(self, ip=None, docker_list=None):
        self.__ip = ip
        self.__docker_list = docker_list

    def getContainerIp(self):
        return self.__ip

    def setIp(self, ip):
        self.__ip = ip

    def setDockerList(self, docker_list):
        self.__docker_list = docker_list

    def getDockerList(self):
        return self.__docker_list
