import tensorflow as tf
from tensorflow.python.ops.gen_math_ops import square

mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.1415926, tf.float64)
its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)

mystr = tf.Variable(["Hello", "world"], tf.string)
cool_numbers = tf.Variable([3.1415, 2.71828], tf.float32)
first_numbers = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)

mymat = tf.Variable([[7], [11]], tf.int16)
myxor = tf.Variable([[False, True], [True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)

my_image = tf.zeros([64, 1, 100, 30])