import tensorflow as tf

# X and Y data
#x_train = [1, 2, 3]
#y_train = [1, 2, 3]

# tf.Variable : tensorflow가 사용하는 변수(trainable)
# tf.random_nomal : shape를 결정히고 랜덤한 값으로 초기화
W = tf.Variable(tf.random_normal([1]), name='weigt')
b = tf.Variable(tf.random_normal([1]), name='bias')

# tf.placeholder : 차후에 feed_dict을 사용하여 값을 변경할 수 있음
x_train = tf.placeholder(tf.float32, shape=[None])
y_train = tf.placeholder(tf.float32, shape=[None])

# H(x) = WX + b
hypothesis = x_train * W + b

# cost = 1/m∑(H(x)^(i) - y^(i))^2
# tf.reduce_mean : 값을 평균내줌
# tf.square : 제곱
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Minimize
# tf.train.GradientDescentOptimizer : 경사하강법 사용
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()
# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

#Fit the Line
for step in range(2001):
    # 설계한 것들중에 최상위 노드(?) 실행
    #sess.run(train)
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
        feed_dict={x_train: [1, 2, 3, 4, 5],
                    y_train: [2.1, 3.1, 4.1, 5.1, 6.1]})

    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)
