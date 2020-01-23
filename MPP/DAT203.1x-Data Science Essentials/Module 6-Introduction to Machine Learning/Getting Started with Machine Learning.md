## [Getting Started with Machine Learning](https://mpp.yonsei.ac.kr/courses/course-v1:Microsoft+DAT203.1x+2017_T4/course/#block-v1:Microsoft+DAT203.1x+2017_T4+type@sequential+block@15670c4ad58c43b38c8f0e82c0b37e99)

### Introduction to Machine Learning

- 다음과 같이 분류할 수 있음

  1. Classification

     - Predict answers to Yes/No questions

  2. Regression

     - Predict real values

  3. Clustering

     - Find patterns of similar objects

       

  #### 1. Classification

  - 예제를 엄청 많이 제공하여 훈련시키고 새로운 데이터가 있을 때 대상이 맞는지  아닌지 분류 하는 기술

  - classification을 위해 데이터를 training set, test set으로 나누어서 진행

    ex) 2016년 맨홀 화재 예측

    ![fig1](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%206-Introduction%20to%20Machine%20Learning/fig1-classification.JPG)

    - 위의 그래프처럼 화재 발생(+)과 화재 미발생(-)을 구분할 수 있는 **결정경계 f(x)**를 찾는 문제를 classification 이라고 함

  - Common algorithms

    1. Logistic Regression(with L1 or L2 regularization)
    2. Decision Trees / Classification Trees / CART / C4.5 / C5.0
    3. AdaBoost(Boosted Decision Trees)
    4. Support Vector Machines
    5. Random Forests
    6. Neural Networks
    7.  etc...

  - Evaluation

    - Confusion Matrix

      ![fig2](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%206-Introduction%20to%20Machine%20Learning/fig2-confusion_matrix.JPG)

      1. True Positive
         - 실제 레이블도 true이고 예측도 true 인 경우
      2. False Positive(Type 1 Error)
         - 실제 레이블은 false이나 true로 예측한 경우
      3. False Negative(Type 2 Error)
         - 실제 레이블은 true이나 false로 예측한 경우
      4. True Negative
         - 실제 레이블도 false이고 예측도 false 인 경우

    - Misclassification error
      $$
      \frac{FP+FN}{n}=\frac{1}{n}\sum_{i=0}^n1_{[y_i\neq \hat y_i]}
      $$
      

    - Accuracy
      $$
      1-missclassification\,error=\frac{1}{n}\sum_{i=0}^n1_{[y_i= \hat y_i]}=\frac{TP+TF}{n}
      $$

    - 모델의 평가는 test set을 사용하여 진행되어야 함.

      

  #### 2. Regression

  - For prediction real-valued outcomes

    ex) Businessweek 클릭 수 데이터를 활용하여 수입 예측

    ​	![fig3](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%206-Introduction%20to%20Machine%20Learning/fig3-regression.JPG)

    - 위와 같이 x와 y 사이의 관계를 나타내는 일반화 된 함수를 찾는 것

  - Evaluation

    - Mean Absolute Error(MAE)
      $$
      MAE=\sum_{i=0}^n|y_i-f(x_i)|
      $$

    - Mean Squared Error(MSE)/Sum of Squared Error(SSE)
      $$
      MSE=\sum_{i=0}^n(y_i-f(x_i))^2
      $$

    - Root Mean Squared Error(RMSE)
      $$
      RMSE=\sqrt{\sum_{i=0}^n(y_i-f(x_i))^2}
      $$

    - R-Squared

      - 회귀식이 얼마나 데이터를 잘 설명하고 있는지 설명하는 지표(1에 가까울 수록 좋음)
        $$
        SSE=\sum_{i=0}^n(y_i-f(x_i))^2\\
        SSR=\sum_{i=0}^n(\bar y-f(x_i))^2\\
        SST=\sum_{i=0}^n(\bar y-y_i)^2
        $$

        $$
        R^2=1-\frac{SSE}{SST}
        $$

    - 모델의 평가는 test set을 사용하여 진행되어야 함.

      

  #### 3. Clustering

  - 대표적인 Unsupervised Learning
    - Supervised learning과 다르게 label이 없음
  - 비슷한 것들끼리 묶는 것
  - label이 없기때문에 평가하기 어려움
  - K-means 알고리즘이 대표적
    1. 클러스터 갯수 입력
    2. 클러스터 중심 초기화
    3. 모든 점들을 가까운 클러스터 중심에 지정
    4. 지속적으로 클러스터 중심을 변경하여 최적의 클러스터 중심 계산

