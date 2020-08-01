# Tensor 张量

## 1. 基本定义

张量，一般就是多维向量，Tensorflow中表示相同数据类型的多维数据，用户通过执行操作来创建或者计算张量，张量的形状是可以推断的。
一般是这几个操作：
```python
tf.constant() # 常量
tf.placeholder() # 占位符，需要后续填充
tf.Variable() # 变量
```

也可以通过某些函数直接生成：
```python
tf.zeros([64, 1, 100, 30])
```