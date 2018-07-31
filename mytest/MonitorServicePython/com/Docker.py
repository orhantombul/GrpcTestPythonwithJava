from mytest.MonitorServicePython.com.DockerInfo import DockerInfo


class Docker:
    def init(self, name= None, info= None):
        self.__name = name
        self.__info = info

    def getDockerName(self):
        return self.__name

    def setDockerName(self, name):
        self.__name = name

    def getDockerInfo(self):
        return self.__info

    def setDockerInfo(self, info):
        self.__info = info

    def setDockerByGrpcDocker(self, grpcDocker):
        self.setDockerName(grpcDocker.name)
        dockerInfo = DockerInfo()
        dockerInfo.setDockerInfoByGrpcDockerInfo(grpcDocker.info)
        self.setDockerInfo(dockerInfo)
