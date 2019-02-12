import tensorflow as tf

# tf.Variable : tensorflow가 사용하는 변수(trainable)
# tf.random_nomal : shape를 결정히고 랜덤한 값으로 초기화
W = tf.Variable(tf.random_normal([1]), name='weigt')

# tf.placeholder : 차후에 feed_dict을 사용하여 값을 변경할 수 있음
x_train = tf.placeholder(tf.float32, shape=[None])
y_train = tf.placeholder(tf.float32, shape=[None])

# H(x) = WX
hypothesis = x_train * W

# cost = 1/m∑(H(x)^(i) - y^(i))^2
# tf.reduce_mean : 값을 평균내줌
# tf.square : 제곱
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Minimize
# Gradient Descent algorithm
# W = W - α*1/m∑(Wx^(i) - y^(i))x^(i)
learning_rate = 0.1
gradient = tf.reduce_mean((W * x_train - y_train) * x_train)
descent = W - learning_rate * gradient
update = W.assign(descent)
# 아래 두줄과 같은 코드
#optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
#train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

#Fit the Line
for step in range(21):
    # 설계한 것들중에 최상위 노드(?) 실행
    #sess.run(train)
    sess.run(update,feed_dict={x_train: [1, 2, 3, 4, 5],
                                y_train: [2, 3, 4, 5, 6]})

    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={x_train: [1, 2, 3, 4, 5],
                                    y_train: [2, 3, 4, 5, 6]}),sess.run(W))
