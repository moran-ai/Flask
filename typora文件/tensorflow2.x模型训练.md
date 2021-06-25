# tensorflow2.x模型训练

- **数据加载和预处理**

  tf.data.Dataset.from_tensor_slices()函数  加载数据

  shuffle()  打乱数据

  map()  函数进行预处理

  repeat()  设置是否循环迭代数据集

  

- #### **模型的构建**

  **使用序贯模型构建** Sequential()

  ```python 
  # 导入相应的包，库
  import tensorflow as tf
  from tensorflow.keras import layers, models
  from tensorflow.keras.optimizers import Adam
  
  # 构建模型
  model = models.Sequential()
  
  # 第一个卷积层 filters:滤波器的个数 kelnel_size:卷积核的大小, padding='Same':边界用0进行填充 activation:激活函数 input_shape:输入训练图片的大小和通道数
  model.add(layers.Conv2D(filters=32, kernel_size=(5,5), padding='Same', activation='relu', input_shape=(32, 32, 3)))
  # 第一个池化层 pool_size:池化的大小
  model.add(layers.MaxPooling2D(pool_size=(2, 2)))
  
  # 第二个卷积层 
  model.add(layers.Conv2D(filters=64, kernel_size=(3,3), padding='Same', activation='relu'))
  # 第二个池化层 strides:窗口移动的步长
  model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
  
  # 第三个卷积层
  model.add(layers.Conv2D(filters=96, kernel_size=(3,3), padding='Same', activation='relu'))
  # 第三个池化层
  model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))
  
  # 第四个卷积层
  model.add(layers.Conv2D(filters=96, kernel_size=(3,3), padding='Same', activation='relu'))
  # 第四个池化层
  model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))
  
  # 扁平层 经过卷积之后，不能直接连接全连接层，需要对数据进行压扁
  model.add(layers.Flatten())
  
  # 全连接层
  model.add(layers.Dense(512))  # 全连接输入的数据为512
  # 激活函数
  model.add(layers.Activation('relu'))
  # 全连接层 使用softmax激活函数
  model.add(layers.Dense(10, activation='softmax'))
  # 打印网络结构
  model.summary()
  ```

  

- #### **模型的训练**

  ```python
  # 在模型训练之前，需要对构建好的模型进行编译
  # categorical_crossentropy交叉熵损失函数  优化器：optimizers ；adam  网络评价标准：metrics
  model.compile(loss='categorical_crossentropy', optimizers='adam', metrics=['accuracy'])
  
  # 模型的训练 调用fit()方法
  """
  model.fit(
  	x:输入的数据  如果模型只有一个输入，那么x的类型是numpy array，如果模型有多个输入，那么x的类型应当为list，list的元素是对应于各个输入的numpy array
  	y:标签 numpy array 
  	batch_size：整数，进行每轮梯度下降时的样本数
  	epochs:整数，训练的轮数
  	verbose:日志显示,0为不在标准输出流输出日志信息，1为输出进度条记录，2为每个epoch输出一行记录
  	callbacks：list，其中的元素是keras.callbacks.Callback的对象。这个list中的回调函数将会在训练过程中的适当时机被调用，参考回调函数
  	
  	validation_split：0~1之间的浮点数，用来指定训练集的一定比例数据作为验证集。验证集将不参与训练，并在每个epoch结束后测试的模型的指标，如损失函数、精确度等。注意，validation_split的划分在shuffle之前，因此如果你的数据本身是有序的，需要先手工打乱再指定validation_split，否则可能会出现验证集样本不均匀。
  	
  	validation_data:指定的验证集,形式为(x,y)的元组  此参数将覆盖validation_spilt。
  	shuffle:布尔值或字符串，一般为布尔值，表示是否在训练过程中随机打乱输入样本的顺序。若为字符串“batch”，则是用来处理HDF5数据的特殊情况，它将在batch内部将数据打乱。
  	class_weight：字典，将不同的类别映射为不同的权值，该参数用来在训练过程中调整损失函数（只能用于训练）
      sample_weight：权值的numpy
      array，用于在训练时调整损失函数（仅用于训练）。可以传递一个1D的与样本等长的向量用于对样本进行1对1的加权，或者在面对时序数据时，传递一个的形式为（samples，sequence_length）的矩阵来为每个时间步上的样本赋不同的权。这种情况下请确定在编译模型时添加了sample_weight_mode=’temporal’。
      initial_epoch: 从该参数指定的epoch开始训练，在继续之前的训练时有用。
  )
  """
  history = model.fit(x, y, batch_size=32, epochs=10, verbose=1, validation_data=None)
  ```

  

- #### **模型准确率的验证**

  ```python
  # 模型的验证使用方法evaluate()
  acc, loss = model.evaluate(x_test, y_test)
  print(r'The Accuracy：{acc}')
  print(r'The Loss: {loss}')
  ```

  

- #### **模型的保存**

  ```python
  '''
  path = '模型保存的路径'
  HDF5(.h5, .hdf5)
  HDF 是 Hierarchical Data Format（分层数据格式）的缩写 
  '''
  path = ''
  model.save(path+'.hdf5')
  
  # 读取模型
  from keras.models import load_model
  model_path = '模型保存的路径'
  model = load_model(model_path)
  ```

  

# 损失函数

keras.model.compile(loss='目标函数', optimizer='adam', metrics=['accuracy'])

- **损失函数**

  - mean_squared_error或msg   均方误差 或标准差

  - mean_absolute_error或mae 平均绝对误差

  - mean_absolute_percentage_error或mape 平均绝对百分比误差

  - mean_squared_logarithmic_error或msle 均方对数误差

  - categorical_crossentropy：亦称作多类的对数损失，注意使用该目标函数时，需要将标签转化为形如`(nb_samples, nb_classes)`的二值序列

  - sparse_categorical_crossentrop：如上，但接受稀疏标签。注意，使用该函数时仍然需要你的标签与输出值的维度相同，你可能需要在标签数据上增加一个维度：`np.expand_dims(y,-1)`

  - kullback_leibler_divergence:从预测值概率分布Q到真值概率分布P的信息增益,用以度量两个分布的差异.

    

    

  

# Tensorflow2.x加载图像数据

**tf.io.read_file(filename, name=None)**方法

- **参数解析**
  - filename：一个string类型的张量   A Tensor of type string.
  - name：该操作的名字可选    A name for the operation(optional)
  - 返回值为一个string类型的张量  A Tensor of type string

<https://www.tensorflow.org/api_docs/python/tf/io/read_file>



**tf.io.decode_jpeg(    contents, channels=0, ratio=1, fancy_upscaling=True,    try_recover_truncated=False, acceptable_fraction=1, dct_method='', name=None )**方法

将图像编码转为uint8编码格式

- **参数解析**

  - channels：解码图像所需要的颜色通道数

    - 0:默认使用当前图像格式编码中的通道数
    - 1：输出一张灰度图
    - 3：输出一张RGB的图片

    <https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg>



