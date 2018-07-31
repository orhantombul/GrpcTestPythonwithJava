import threading
import time
from concurrent import futures

import grpc
from flask import Flask, render_template

from mytest.MonitorServicePython.com import ContainerServer_pb2, ContainerServer_pb2_grpc
from mytest.MonitorServicePython.com.ApplicationManager import ApplicationManager
from mytest.MonitorServicePython.com.Container import Container

app = Flask(__name__)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@app.route('/')
def test():
    application_manager = ApplicationManager.getApplicationManager()
    containerMap = application_manager.getContainers()

    return render_template("robot.html", containerMap=containerMap)


class GetInfoFromGrpc(ContainerServer_pb2_grpc.SendServiceServicer):

    def contlist(self, request, context):
        application_manager = ApplicationManager.getApplicationManager()
        application_manager.clearAll()
        containerList = request.containerlist
        for grpc_container in containerList:
            container = Container()
            container.setContainerByGrpcContainer(grpc_container)
            application_manager.setContainer(container.getContainerIp(), container)
        return ContainerServer_pb2.ContainerListResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ContainerServer_pb2_grpc.add_SendServiceServicer_to_server(GetInfoFromGrpc(), server)
    server.add_insecure_port('[::]:5015')
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


serve_thread = threading.Thread(name='serve', target=serve)
app_thread = threading.Thread(name='app.run', target=app.run)

if __name__ == "__main__":
    app.config['SERVER_NAME'] = "127.0.0.1:5555"
    serve_thread.start()
    app_thread.start()
