from mytest.MonitorServicePython.com.Model.Docker import Docker


class Container:
    def init(self, ip=None, docker_list=None):
        self.__ip = ip
        self.__docker_list = docker_list
        if docker_list is None:
            self.__docker_list = []

    def getContainerIp(self):
        return self.__ip

    def setIp(self, ip):
        self.__ip = ip

    def setDockerList(self, docker_list):
        self.__docker_list = docker_list

    def getDockerList(self):
        return self.__docker_list

    def setContainerByGrpcContainer(self, grpcContainer):
        self.setIp(grpcContainer.ip)
        docker_list = []
        for grpc_docker in grpcContainer.dockerlist:
            docker = Docker()
            docker.setDockerByGrpcDocker(grpc_docker)
            docker_list.append(docker)
        self.setDockerList(docker_list)
