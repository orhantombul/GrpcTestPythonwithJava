from mytest.MonitorServicePython.com.Model.Container import Container


class ApplicationManager:
    __containerDictionary = {}
    __applicationManager = None

    def __init__(self):
        if ApplicationManager.__applicationManager is not None:
            raise Exception("Application manager was not created !!! ")
        else:
            ApplicationManager.__applicationManager = self

    @staticmethod
    def getApplicationManager():
        if ApplicationManager.__applicationManager is None:
            ApplicationManager()

        return ApplicationManager.__applicationManager

    def getContainer(self, container_ip):
        if container_ip is None:
            return
        return self.__containerDictionary[container_ip]

    def setContainer(self, container_ip, container):
        if container_ip is None or container is None:
            return
        self.__containerDictionary[container_ip] = container

    def createDockerWithContainerIp(self, container_ip):
        if container_ip is None or self.__containerDictionary[container_ip] is not None:
            return

        container = Container()
        container.setIp(container_ip)
        container.setDockerList([])
        self.__containerDictionary[container_ip] = container
        return

    def addDockerByContainerIp(self, container_ip, docker):
        if container_ip is None or docker is None:
            return
        container = self.__containerDictionary[container_ip]

        if container is None:
            self.createDockerWithContainerIp(container_ip)

        docker_list = container.getDockerList()
        docker_list.append(docker)

    def getDocker(self, container_ip, docker_ip):
        if container_ip is None or docker_ip is None:
            return

        container = self.__containerDictionary[container_ip]
        docker_list = container.getDockerList()
        for docker in docker_list:
            if docker.getDockerInfo().getDockerInfoIp() is docker_ip:
                return docker

    def getContainers(self):
        return self.__containerDictionary

    def clearAll(self):
        self.__containerDictionary = {}



