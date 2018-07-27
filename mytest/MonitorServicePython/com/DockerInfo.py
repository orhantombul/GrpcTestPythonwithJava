class DockerInfo:
    def __init__(self, dip, dstatus):
        self.__ip = dip
        self.__status = dstatus

    def getDockerInfoIp(self):
        return self.__ip

    def setDockerInfoIp(self, dip):
        self.__ip = dip

    def getDockerInfoStatus(self):
        return self.__status

    def setDockerInfoStatus(self, dstatus):
        self.__status = dstatus
