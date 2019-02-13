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
