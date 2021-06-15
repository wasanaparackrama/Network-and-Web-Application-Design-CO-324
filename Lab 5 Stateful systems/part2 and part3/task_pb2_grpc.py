# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import task_pb2 as task__pb2


class TaskapiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addTask = channel.unary_unary(
                '/Taskapi/addTask',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=task__pb2.Task.FromString,
                )
        self.delTask = channel.unary_unary(
                '/Taskapi/delTask',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.UInt64Value.SerializeToString,
                response_deserializer=task__pb2.Task.FromString,
                )
        self.editTask = channel.unary_unary(
                '/Taskapi/editTask',
                request_serializer=task__pb2.Task.SerializeToString,
                response_deserializer=task__pb2.Task.FromString,
                )
        self.listTasks = channel.unary_unary(
                '/Taskapi/listTasks',
                request_serializer=task__pb2.TaskQuery.SerializeToString,
                response_deserializer=task__pb2.Tasks.FromString,
                )


class TaskapiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addTask(self, request, context):
        """Add a new task and return its id

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delTask(self, request, context):
        """Delete a task by id

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editTask(self, request, context):
        """Edit an existing task (ignoring write conflicts)

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listTasks(self, request, context):
        """List all tasks in the given states

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskapiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addTask': grpc.unary_unary_rpc_method_handler(
                    servicer.addTask,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=task__pb2.Task.SerializeToString,
            ),
            'delTask': grpc.unary_unary_rpc_method_handler(
                    servicer.delTask,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.UInt64Value.FromString,
                    response_serializer=task__pb2.Task.SerializeToString,
            ),
            'editTask': grpc.unary_unary_rpc_method_handler(
                    servicer.editTask,
                    request_deserializer=task__pb2.Task.FromString,
                    response_serializer=task__pb2.Task.SerializeToString,
            ),
            'listTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.listTasks,
                    request_deserializer=task__pb2.TaskQuery.FromString,
                    response_serializer=task__pb2.Tasks.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Taskapi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Taskapi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Taskapi/addTask',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            task__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Taskapi/delTask',
            google_dot_protobuf_dot_wrappers__pb2.UInt64Value.SerializeToString,
            task__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def editTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Taskapi/editTask',
            task__pb2.Task.SerializeToString,
            task__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Taskapi/listTasks',
            task__pb2.TaskQuery.SerializeToString,
            task__pb2.Tasks.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
