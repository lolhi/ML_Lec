# ML_Lec

## Lec 02 - Linear Regression의 Hypothesis와 cost 설명

  - Hypothesis  : H(x) = WX + b
  - Cost        : 1/m∑(H(x^(i)) - y^(i)^2

  -> Cost function인 MSE(Mean Square Error)를 최소화하여 최적의 W와 b를 구함

## Lec 03 - Linear Regression의 cost 최소화 알고리즘 설명

  - Lec02 에서 했었던 값들의 cost 그래프
    ![Lec03-1](./image/Lec03-1.JPG)
  - 이러한 그래프에서 cost값이 최소화된것을 찾아야 함
  - Gradient Descent algorithm(경사하강법) 사용

  ### Gradient Descent algorithm(경사하강법)
  - cost(W,b)가 주어졌을 때 cost를 최소화 하는 W,b를 찾을 수 있음
  - w1,w2...같은 많은 값들이 있는 cost function도 minimize 가능
  - cost function에서 기울기를 계산해 기울기가 가장 작을 때를 찾음(미분을 사용하여 기울기 계산)

  - Gradient Descent algorithm 적용 방법
    ![Lec03-2](./image/Lec03-2.JPG)
  - 미분 결과

  ![Lec03-3](./image/Lec03-3.JPG)

   * 주의사항
     - cost function을 3차원으로 그렸을 때 convex funtion이 아니면 정상동작 하지 않음

     - cost funtion모양이 convex funtion이 아닐경우
     ![Lec03-4](./image/Lec03-4.JPG)
     - cost funtion모양이 convex funtion일 경우
     ![Lec03-5](./image/Lec03-5.JPG)

## Lec 04 - Multi-Variable Linear Regression

  - 한개의 데이터가 아닌 여러개의 데이터일때의 regression
    ![Lec04-1](./image/Lec04-1.JPG)
  - Hypothesis 및 cost funtion
    ![Lec04-2](./image/Lec04-2.JPG)
  - 데이터가 너무 많아지면 표현하기 힘듬
    -> Matrix로 표현하여 Matrix의 곱 사용
    ![Lec04-3](./image/Lec04-3.JPG)
  - Matrix 사용 시 instance갯수가 많아도 한번에 계산 가능

## Lec 05 - Logistic Classfication
  - 이전까지 했던 Regression은 값을 추측하는 것
  - (Binary) Classfication은 정해진 category를 고르는 것
  - 기계적으로 학습하기 위해 0, 1로 encoding 함

  - Linear Regression으로 Classfication 문제를 해결 할 수가 없음
    - Linear Regression을 미리 학습시켜두고 나서 어마어마하게 큰 수가 데이터로 들어오면 기울기가 줄어 정상적인 Classfication 불가
    ![Lec05-1](./image/Lec05-1.JPG)
    - Classfication을 위해 hypothesis의 값이 1이나 0이 나와야 하는데 Linear Regression의 hypothesis(H(x) = Wx + b)는 1보다 크거나 0보다 작은 수가 나올 수 있음

  - 이 문제를 해결하기 위해선 H(x)의 값이 무엇이든 0 ~ 1의 값으로 변환해주어야 함
    - Sigmoid(Logistic) function을 사용
    ![Lec05-2](./image/Lec05-2.JPG)
    ![Lec05-3](./image/Lec05-3.JPG)

  - Logistic funtion의 cost funtion
    - Linear Regression의 cost funtion을 그대로 사용하면 cost funtion의 그래프가 이상하게 그려짐
    ![Lec05-4](./image/Lec05-4.JPG)
      - 중간중간 기울기가 없어지는 부분이 있기 때문에 경사하강법 알고리즘 사용 불가
    - 따라서 다음과 같은 cost funtion을 사용함
    ![Lec05-5](./image/Lec05-5.JPG)
      - y=1 일때 H(x)도 1이면 cost는 0, H(x)가 0이면 cost는 무한대
      - y=0 일때 H(x)도 0이면 cost는 0, H(x)가 1이면 cost는 무한대
      - 프로그래밍에 사용하기 위해 다음과 같이 식을 변경
      ![Lec05-6](./image/Lec05-6.JPG)
    - Gradient Descent algorithm을 사용하기 위해 cost를 미분해야하는데 컴퓨터가 알아서 해줌(복잡함)
    ![Lec05-7](./image/Lec05-7.JPG)

## Lec 06 - Softmax Classfication: Multinomial Classfication

  - Logistic Classfication의 개념을 Multinomial Classfication에 적용
    ![Lec06-1](./image/Lec06-1.JPG)
  - 세개의 독립된 Classfication을 해도 되지만 하나의 벡터 묶어서 하면 바로 계산이 가능하고 독립된것들처럼 동작
    ![Lec06-2](./image/Lec06-2.JPG)
  - 벡터를 계산해서 나온 값들은 0 ~ 1사이의 값들이 아님
    -> Softmax를 사용하여 0 ~ 1로 변환(확률)
    ![Lec06-3](./image/Lec06-3.JPG)
    ![Lec06-4](./image/Lec06-4.JPG)
  - Softmax를 사용하여 구한 확률을 one-hot encoding으로 변환
    ![Lec06-5](./image/Lec06-5.JPG)

  - Softmax Classfication의 cost funtion
    ![Lec06-6](./image/Lec06-6.JPG)
  - Classfication의 예측결과가 틀렸으면 cost는 무한대, 맞았으면 0
    ![Lec06-7](./image/Lec06-7.JPG)

## Lec 07-1 학습 rate, Overfitting, 일반화(Regularization)

  - Learning rate
    - Large Learning rate: Overshooting(Learning rate가 너무 커 cost가 줄어들지 않고 바깥으로 튕겨나감) 유발
    - Small Learning rate: 너무 오래걸려 gradient가 최저값이 아님에도 step이 끝남
    - 이런현상을 방지하기 위해서 cost값을 찍어봐야함

  - Data preprocessing for gradient descent
    - 학습에 사용되는 데이터가 서로 편차가 심히면 튀어나가는 상황이 발생할 수 있음
    - 그래서 데이터를 정규화 해줘야함(Zero-centered data or normalized data)
    - Standardization 방법
    ![Lec07-1](./image/Lec07-1.JPG)

  - Overfitting
    - 학습데이터에 너무 맞는 모델을 만들어 다른 데이터가 들어왔을 때 정상적으로 처리하지 못함
    - 해결 방법은 많은 데이터, 중복된 features 제거 , Regularization
    - Regularization: 너무 큰 Weight 값을 가지게 하지 않는 것
    ![Lec07-2](./image/Lec07-2.JPG)
    - cost funtion에 특정 값을 더해 cost 값 최적화

## Lec 07-2 Traning/ Testing data set

  - data set을 전부 training하는데 사용하면 문제가 발생할 수 있음
    - 시험을 치는데 지난 시험 문제와 똑같은 문제로 시험치는것과 똑같음
  - 모델의 정확성을 높히기 위해서 data set의 70%는 training set으로, 30%는 test set으로 분리
  - test set은 숨겨져 있고 training set으로 학습
    ![Lec07_1-1](./image/Lec07_1-1.JPG)


## Lec 08-1 딥러닝의 기본 개념: 시작과 XOR 문제

  - 인간의 뉴론이 생각보다 단순한 구조로 이루어져 있음
  - activation function
    ![Lec08_1-1](./image/Lec08_1-1.JPG)

  - 그 당시(58년도) 기술로 AND, OR 문제는 해결 가능(Linear separable)
  - 하지만 XOR 문제는 해결 불가능(non linear)
    ![Lec08_1-2](./image/Lec08_1-2.JPG)

  - 한개의 뉴론으로는 해결이 불가능 여러개의 뉴론(MLP)을 사용하면 가능
    - 하지만 뉴론을 학습시킬 수가 없음
    - 해결 방법 : backpropagation
    ![Lec08_1-3](./image/Lec08_1-3.JPG)
    - 해결 방법2 : Convolutional Neural Network
    - 고양이 시신경을 연결해 뉴론 활성 상태를 확인했을 때 이미지에 따라 일부만 활성화
    ![Lec08_1-4](./image/Lec08_1-4.JPG)

  - Big problem
    - backpropagation은 적은 수의 층에서는 잘 동작하나 층수가 많아지면 성능이 떨어짐..
    - Neural Network보다 간단한 알고리즘(SVM 등..)이 잘 동작함

# Lec 08-2 딥러닝의 기본 개념2: Back-propagation 과 2006/2007 '딥'의 출현

  - BreakThrough
    - 2006년: 초기값을 잘못 지정해줘서 W값을 훈련하지 못했다고 논문
    - 2007년: 초기값 문제 확인, neural network를 깊게 구성하면 복잡한 문제 해결 가능

  - ImageNet Classfication 대회
    - 전까진 30%의 오류율을 보였으나 CNN 사용하여 15%로 급감 -> 3%...
