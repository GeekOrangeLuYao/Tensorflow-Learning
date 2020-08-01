import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print(f"a: {sess.run(a)}") # 2
    print(f"b: {sess.run(b)}") # 3
    print(f"Addition with constants: {sess.run(a + b)}") # 5
    print(f"Multiplication with constants: {sess.run(a * b)}") # 6

x = tf.placeholder(tf.int16, shape = (), name = "x")
y = tf.placeholder(tf.int16, shape = (), name = "y")

add = tf.add(x + y)
mul = tf.multiply(x + y)

with tf.Session() as sess:
    print(f"Addition with variables: {sess.run(add)}")
    print(f"Multiplication with variables: {sess.run(mul)}")

add = tf.add(x, y)
mul = tf.multiply(x, y)

with tf.Session() as sess:
    print(f"Addition with variables: {sess.run(add)}")
    print(f"Multiplication with variables: {sess.run(mul)}")
# Warning: you must feed a value

with tf.Session() as sess:
    print(f"Addition with variables: {sess.run(add, feed_dict = {x: 2, y: 3})}") # 5
    print(f"Muliplication with variables: {sess.run(mul, feed_dict = {x: 2, y: 3})}") # 6

