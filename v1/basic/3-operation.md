# Operation 操作

根据前面的说明，数据流图由节点和有向边组成，每个节点均对应一个具体的操作。因此，操作是模型功能的实际载体。
数据流图中的节点按照功能不同可以分为3种：

* **存储节点**：有状态的变量操作，存储模型参数
* **计算节点**：无状态的计算或控制操作，主要负责算法逻辑表达或流程控制
* **数据节点**：数据的占位符操作，用于描述图外输入数据的属性
操作的输入和输出都是张量或者是操作（函数式编程）

|    操作类型    |                           典型操作                           |
| :------------: | :----------------------------------------------------------: |
|    基础算术    |          add/multipy/mod/sqrt/sin/trace/fft/argmin           |
|    数组运算    |        size/rank/split/reverse/cast/one_hot/quantize         |
|    梯度裁剪    |        clip_by_value/clip_by_norm/clip_by_global_norm        |
| 逻辑控制和调试 |       identity/logical_and/equal/less/is_finite/is_nan       |
|   数据流控制   |          enqueue/dequeue/size/take_grad/apply_grad/          |
|   初始化操作   | zeors_initializer/random_normal_initializer/orthogonal_initializer |
|  神经网络运算  |     convolution/pool/bias_add/softmax/dropout/erosion2d      |
|    随机运算    |    random_normal/random_shuffle/multinomial/random_gamma     |
|   字符串与暖   |    string_to_hash_bucket/reduce_join/substr/encode_base64    |
|  图像处理运算  |    encode_png/resize_images/rot90/hsv_to_rgb/adjust_gamma    |



占位符操作

Tensorflow使用占位符操作表示图外输入的数据，如训练和测试数据

Tensorflow数据流图描述了算法模型的计算拓扑，其中的各个操作（节点）都是抽象的函数映射或数学表达式。

换句话说，数据流图本身是一个具有计算拓扑和内部结构的“壳”。在用户向数据流图填充数据前，途中并没有真正执行任何计算。