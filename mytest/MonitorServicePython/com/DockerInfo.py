class DockerInfo:

    def init(self,ip=None,status=None):
        self.__ip = ip
        self.__status = status
        pass

    def getDockerInfoIp(self):
        return self.__ip

    def setDockerInfoIp(self, ip):
        self.__ip = ip

    def getDockerInfoStatus(self):
        return self.__status

    def setDockerInfoStatus(self, status):
        self.__status = status

    def setDockerInfoByGrpcDockerInfo(self, grpcDockerInfo):
        self.setDockerInfoIp(grpcDockerInfo.ip)
        self.setDockerInfoStatus(grpcDockerInfo.status)
