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
