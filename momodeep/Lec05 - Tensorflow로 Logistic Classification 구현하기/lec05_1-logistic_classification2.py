import tensorflow as tf
import numpy as np

# loadtext : text파일을 읽음. delimiter를 사용해 구분가능
xy = np.loadtxt('C:\\Users\\YJ\\Desktop\\workspace\\PythonProject\\ML_Lec\\Lec05 - Tensorflow로 Logistic Classification 구현하기\\data-03-diabetes.csv', delimiter=',', dtype=np.float32)

# [:, 0:-1] : row(행)은 전부 가져오고 column(열)은 마지막 한개(-1)를 제외하고 다 가져온다.
x_data = xy[:, 0:-1]
# [:,[-1]] : row(행)은 전부 가져오고 column(열)은 마지막 한개(-1)만 가져온다
y_data = xy[:,[-1]]

X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([8, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# H(x)= 1/1+e^(-x)
# tf.div(1., 1. + tf.exp(tf.matmul(X, W) + b))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# cost = -1/m∑(ylog(H(x)) + (1 - y)log(1 - H(x)))
cost = -tf.reduce_mean(Y *  tf.log(hypothesis) +
                    (1 - Y) * tf.log(1 - hypothesis))

# minimize
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Accuracy computation
# True if hypothesis>0.5 else False
# True면 1.0, False면 0.0으로 casting
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    #Accuracy Report
    h, c, a = sess.run([hypothesis, predicted, accuracy],
                        feed_dict={X: x_data, Y:y_data})
    print("\nHypothesis: ", h, "\n Correct (Y): ", c, "\nAccuracy: ", a)
