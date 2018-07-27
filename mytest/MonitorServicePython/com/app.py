from concurrent import futures
from flask import Flask, render_template
from ApplicationManager import ApplicationManager
from DockerInfo import DockerInfo
from Container import Container
from Docker import Docker
import time
import grpc
import ContainerServer_pb2_grpc
import ContainerServer_pb2

app = Flask(__name__)

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@app.route('/fill')
def test1():
    applicationManager = ApplicationManager.getApplicationManager()
    dockerList = [Docker("hasan", DockerInfo("192.168.1.1", "Fail"))]
    applicationManager.setContainer("192.168.2.2", Container("192.168.2.2", dockerList))
    return render_template("robot.html", containerMap=applicationManager.getContainers())


@app.route('/list')
def test():
    applicationManager = ApplicationManager.getApplicationManager()
    containerMap = applicationManager.getContainers()

    return render_template("robot.html", containerMap=containerMap)

class Greeter(ContainerServer_pb2_grpc.SentServiceStatusServicer):

    def contlist(self, request, context):
        print(request)
        return ContainerServer_pb2.Response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ContainerServer_pb2_grpc.add_SentServiceStatusServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5013')
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == "__main__":
    app.run(debug=True)
    serve()
