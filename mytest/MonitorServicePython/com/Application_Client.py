from __future__ import print_function
import grpc
import ContainerServer_pb2
import ContainerServer_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:5013')
    stub = ContainerServer_pb2_grpc.SentServiceStatusStub(channel)

    response = stub.contlist(ContainerServer_pb2.ContainerList())

    print("List client received: " + response.docker_name)


if __name__ == '__main__':
    run()
