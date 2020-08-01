# Optimizer 优化器

Tensorflow 训练机制
典型的机器学习和深度学习问题，包含以下3个部分：

1. 模型：$y = f(x) = wx + b$
2. 损失函数：$loss = L(y, \hat{y})$
3. 优化算法：利用$loss$计算模型参数的更新

Tensorflow 优化器
一次典型的迭代优化应该分为以下3个步骤：
1. 计算梯度：调用`compute_gradients`方法
2. 处理梯度：用户按照自己需求处理梯度值，如梯度裁剪和梯度加权等
3. 应用梯度：调用`apply_gradients`方法，将处理后的梯度值应用到模型参数。

```python
optimizer = tf.train.GrdientDescentOptimizer(learning_rate = 0.01)
grads_and_vars = optimizer.compute_gradients(loss, var_list, ...)
clip_grads_and_vars = [(tf.clip_by_value(grad, -1.0, 1.0), var) for grad, var in grads_and_vars]
train_op = optimizer.apply_gradients(clip_grads_and_vars)

```

```python
optimizer = tf.train.GrdientDescentOptimizer(learning_rate = 0.01)
global_step = tf.Variable(0, name = "global_step", trainable = False)
train_op = optimizer.minimize(loss, global_step = global_step)
```