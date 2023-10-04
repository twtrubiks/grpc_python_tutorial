import concurrent.futures
import grpc
from service_protos import user_pb2
from service_protos import user_pb2_grpc
from interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

class UsersServicer(user_pb2_grpc.UsersServicer):
    def ListUser(self, request, context):
        if request.id == 0:
            raise NotFound("Sorry, id is not allowed 0")

        details = [
            {
                "id": request.id,
                "value" : request.name
            },
            {
                "id": request.id,
                "value" : request.name
            },
        ]
        return user_pb2.UserResponse(details=details)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        concurrent.futures.ThreadPoolExecutor(max_workers=10),
        # interceptors=interceptors
        )
    user_pb2_grpc.add_UsersServicer_to_server(
        UsersServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
