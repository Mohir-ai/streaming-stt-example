# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from streaming import stt_pb2 as streaming_dot_stt__pb2


class RecognizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecognizeStreaming = channel.stream_stream(
                '/stt.Recognizer/RecognizeStreaming',
                request_serializer=streaming_dot_stt__pb2.StreamingRequest.SerializeToString,
                response_deserializer=streaming_dot_stt__pb2.StreamingResponse.FromString,
                )


class RecognizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RecognizeStreaming(self, request_iterator, context):
        """Bi-directional streaming RPC for recognizing streamed audio.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecognizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RecognizeStreaming': grpc.stream_stream_rpc_method_handler(
                    servicer.RecognizeStreaming,
                    request_deserializer=streaming_dot_stt__pb2.StreamingRequest.FromString,
                    response_serializer=streaming_dot_stt__pb2.StreamingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stt.Recognizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recognizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecognizeStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/stt.Recognizer/RecognizeStreaming',
            streaming_dot_stt__pb2.StreamingRequest.SerializeToString,
            streaming_dot_stt__pb2.StreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
