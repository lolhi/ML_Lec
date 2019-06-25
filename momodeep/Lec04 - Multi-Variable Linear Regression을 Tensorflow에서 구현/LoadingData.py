import tensorflow as tf
import numpy as np

# loadtext : text파일을 읽음. delimiter를 사용해 구분가능
xy = np.loadtxt('C:\\Users\\YJ\\Desktop\\workspace\\PythonProject\\ML_Lec\\Lec04 - Multi-Variable Linear Regression을 Tensorflow에서 구현\\data-01-test-score.csv', delimiter=',', dtype=np.float32)

# [:, 0:-1] : row(행)은 전부 가져오고 column(열)은 마지막 한개(-1)를 제외하고 다 가져온다.
x_data = xy[:, 0:-1]
# [:,[-1]] : row(행)은 전부 가져오고 column(열)은 마지막 한개(-1)만 가져온다
y_data = xy[:,[-1]]

print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)

X = tf.placeholder(tf.float32, shape=[None,3])
Y = tf.placeholder(tf.float32, shape=[None,1])

W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X,W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train],
        feed_dict={X: x_data, Y: y_data})

    if step % 10 == 0:
        print(step, "Cost : ", cost_val, "\n hypothesis :\n", hy_val)

#Ask my score
print("Your score will be ", sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
