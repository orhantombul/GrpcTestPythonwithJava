from mytest.MonitorServicePython.com.DockerInfo import DockerInfo


class Docker:
    def init(self, dname=None, docker_info=None):
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

    def setDockerByGrpcDocker(self, grpcDocker):
        self.setDockerName(grpcDocker.dockername)
        dockerInfo = DockerInfo()
        dockerInfo.setDockerInfoByGrpcDockerInfo(grpcDocker.dockerinfo)
        self.setDockerInfo(dockerInfo)
