import grpc
from typing import Any
from collections.abc import Callable
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException


class ExceptionToStatusInterceptor(ServerInterceptor):

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
        """Override this method to implement a custom interceptor.

         You should call method(request_or_iterator, context) to invoke the
         next handler (either the RPC method implementation, or the
         next interceptor in the list).

         Args:
             method: The next interceptor, or method implementation.
             request_or_iterator: The RPC request, as a protobuf message.
             context: The ServicerContext pass by gRPC to the service.
             method_name: A string of the form
                 "/protobuf.package.Service/Method"

         Returns:
             This should generally return the result of
             method(request_or_iterator, context), which is typically the RPC
             method response, as a protobuf message. The interceptor
             is free to modify this in some way, however.
         """
        try:
            return method(request_or_iterator, context)
        except GrpcException as e:
            context.set_code(e.status_code)
            context.set_details(e.details)
            raise