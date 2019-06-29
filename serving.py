import numpy as np

# Communication to TensorFlow server via gRPC
import grpc

# TensorFlow serving stuff to send messages
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow.contrib.util import make_tensor_proto

timeout = 60.0

channel = grpc.insecure_channel('localhost:8501')
# channel = grpc.insecure_channel('10.150.0.10:8501')
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
request = predict_pb2.PredictRequest()

request.model_spec.name = '5'
request.model_spec.signature_name = 'serving_default'


def generate_tokens(input_tokens):
    input_data = np.array([[2061, 318, 428, 30]], dtype='int32')
    input_data = np.array([input_tokens], dtype='int32')
    request.inputs['input'].CopyFrom(make_tensor_proto(input_data,
                                                       shape=input_data.shape))
    response = stub.Predict(request, timeout)
    tensor = response.outputs['output']

    return [tensor.int_val]
