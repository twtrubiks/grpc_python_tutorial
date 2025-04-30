import grpc
from service_protos import user_pb2
from service_protos import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UsersStub(channel)
        user_request = user_pb2.UserRequest(id=2, name="twtrubiks")

        # test raise NotFound
        # user_request = user_pb2.UserRequest(id=0, name="twtrubiks")

        response = stub.ListUser(user_request)
        print(f"client received: {response}")

if __name__ == '__main__':
    run()
