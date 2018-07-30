import time

import grpc
from concurrent import futures
from mytest.MonitorServicePython.com import ContainerServer_pb2_grpc
from mytest.MonitorServicePython.com import ContainerServer_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


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


if __name__ == '__main__':
    serve()
