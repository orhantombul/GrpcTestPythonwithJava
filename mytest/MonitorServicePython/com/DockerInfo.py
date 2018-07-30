class DockerInfo:

    def init(self):
        pass

    def getDockerInfoIp(self):
        return self.__ip

    def setDockerInfoIp(self, dip):
        self.__ip = dip

    def getDockerInfoStatus(self):
        return self.__status

    def setDockerInfoStatus(self, dstatus):
        self.__status = dstatus

    def setDockerInfoByGrpcDockerInfo(self, grpcDockerInfo):
        self.setDockerInfoIp(grpcDockerInfo.dockerip)
        self.setDockerInfoStatus(grpcDockerInfo.dockerstatus)
