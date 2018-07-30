import threading
import time
from concurrent import futures

import grpc
from flask import Flask, render_template
from mytest.MonitorServicePython.com import ContainerServer_pb2
from mytest.MonitorServicePython.com import ContainerServer_pb2_grpc
from mytest.MonitorServicePython.com.ApplicationManager import ApplicationManager
from mytest.MonitorServicePython.com.Container import Container
from mytest.MonitorServicePython.com.Docker import Docker
from mytest.MonitorServicePython.com.DockerInfo import DockerInfo
from mytest.MonitorServicePython.com.ContainerServer_pb2 import ContainerList

app = Flask(__name__)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

@app.route('/fill')
def test1():
    application_manager = ApplicationManager.getApplicationManager()
    docker_list = [Docker("hasan", DockerInfo("192.168.1.1", "Fail"))]
    application_manager.setContainer("192.168.2.2", Container("192.168.2.2", docker_list))
    return render_template("robot.html", containerMap=application_manager.getContainers())


@app.route('/list')
def test():
    application_manager = ApplicationManager.getApplicationManager()
    containerMap = application_manager.getContainers()

    return render_template("robot.html", containerMap=containerMap)


class Greeter(ContainerServer_pb2_grpc.SentServiceStatusServicer):

    def contlist(self, request, context):
        application_manager = ApplicationManager.getApplicationManager()
        application_manager.clearAll()
        containerList = request.containerlist
        for grpc_container in containerList:
            container = Container()
            container.setContainerByGrpcContainer(grpc_container)
            application_manager.setContainer(container.getContainerIp(),container)
        return ContainerServer_pb2.Response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ContainerServer_pb2_grpc.add_SentServiceStatusServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5015')
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


threadserving = threading.Thread(name='serve', target=serve)
threadrunning = threading.Thread(name='app.run', target=app.run)

if __name__ == "__main__":
    app.config['SERVER_NAME'] = "127.0.0.1:5555"
    threadserving.start()
    threadrunning.start()
