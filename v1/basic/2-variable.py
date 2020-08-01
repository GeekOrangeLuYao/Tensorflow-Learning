import tensorflow as tf

w = tf.Variable(initial_value = tf.random_normal(shape = (1, 4), mean = 100, stddev = 0.35), name = "W")
b = tf.Variable(tf.zeros([4]), name = "b")

# 创建会话
sess = tf.Session()
# 初始化变量
sess.run(tf.global_variables_initializer())
# 执行操作
sess.run([W, b])

# 执行更新变量b的操作
sess.run(tf.assign_add(b, [1, 1, 1, 1])) 
sess.run(b)
## b = [1, 1, 1, 1]

###########################################
"""
Saver 的使用
v1 = tf.Variable(..., name = "v1")
v2 = tf.Variable(..., name = "v2")

saver = tf.train.Saver({ 'v1': v1, 'v2': v2 })
saver = tf.train.Saver([v1, v2])
saver = tf.train.Saver({ v.op.name: v for v in [v1, v2] })
tf.train.saver.save(sess, 'my-model', global_step = 0) # ==> filename: 'my-model-0'
"""

# 保存模型
saver = tf.train.Saver({'W': w, 'b': b})
saver.save(sess, './summary/test.ckpt', global_step = 0)
sess.run(tf.assign_add(b, [1, 1, 1, 1]))
sess.run(b) # ==> b = [2, 2, 2, 2]

saver.restore(sess, './summary/test.ckpt-0')
sess.run(b) # ==> b = [1, 1, 1, 1]

# 对于比较大的情况 tf.train.import_meta_graph
