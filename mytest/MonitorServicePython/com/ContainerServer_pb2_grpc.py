# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from mytest.MonitorServicePython.com import ContainerServer_pb2 as ContainerServer__pb2


class SendServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.contlist = channel.unary_unary(
        '/tr.com.argela.grpcserver.SendService/contlist',
        request_serializer=ContainerServer__pb2.ContainerListRequest.SerializeToString,
        response_deserializer=ContainerServer__pb2.ContainerListResponse.FromString,
        )


class SendServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def contlist(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'contlist': grpc.unary_unary_rpc_method_handler(
          servicer.contlist,
          request_deserializer=ContainerServer__pb2.ContainerListRequest.FromString,
          response_serializer=ContainerServer__pb2.ContainerListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tr.com.argela.grpcserver.SendService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
