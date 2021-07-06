import tensorflow as tf
# from tensorflow.python.ops.variable_scope import VariableSynchronization
# print(tf.__version__)

# 거의 대부분 우리가 직접 tensor(텐서)를 생성하는 경우는 없다.
# Tensorflow가 tf.io나 tf.data라는 모듈을 기본적으로 가지고 있어서,
# 데이터를 가져와서 자동으로 tensor로 전환(변환)을 해준다.
# 이 변환된 텐서를 나중에 neural network(신경망)에서 사용한다.

# tensor를 이해하기 위해 직접 만들어보기
# tensorflow에서 사용하는 상수(constant)를 생성

# scala 생성(rank가 0인 텐서)
scalar = tf.constant(7)
scalar
# 해당 텐서의 차원 수를 알려줍니다. ndim은 numer of dimension의 약자 해당 텐서의 차원수를 알려준다.
# ndim은 number of dimension의 약자
scalar.ndim
scalar.ndim


# 벡터를 생성(차원이 0보다 큰 것)
vector = tf.constant([10,10])
print(vector)

vector.ndim

# 행렬 (matrix) 생성 (차원)
matrix = tf.constant([
    [10, 7],
    [7, 10]
])
print(matrix)

print(matrix.ndim)

# Tensorflow는 기본적으로 int32나 float32 자료형으로 tensor를 생성한다.

# 새로운 행렬을 생성하고 