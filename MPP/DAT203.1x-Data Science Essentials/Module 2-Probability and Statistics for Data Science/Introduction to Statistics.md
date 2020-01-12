## [Introduction to Statistics](https://mpp.yonsei.ac.kr/courses/course-v1:Microsoft+DAT203.1x+2017_T4/course/#block-v1:Microsoft+DAT203.1x+2017_T4+type@sequential+block@1504647a56814b868b8b730f037d51ba)

### Descriptive Statistics

- Histogram
  - 연속형 변수의 값들을 확률로 나타내줌
- Bar chart
  - 범주형 변수의 확률을 나타내줌
- Pareto chart
  - 범주형 변수의 확률을 순서대로 나타내줌
- Scatter plot
  - 변수가 두개 일때 x의 변화에 따른 y의 변화를 보여줌

### Summary Statistics

- 표본 평균(Sample Mean)
  $$
  \bar x = \frac{1}{n}\sum_{i=1}^nx_i
  $$
  

  - 데이터 포인트의 평균
  - mu와 햇갈리지 말것(mu: 전체의 평균)

  - 표본이 크고 n도 충분이 크다면 표본평균은 mu와 비슷한 개념이 됨

-  분위수(Quantiles)/ 백분위수(Percentiles)

  - 오름차순으로 정렬된 데이터를 두 부분으로 나눠줄 포인트를 찾는 것.

  - 예제: 0.55 분위수 찾기

    ![fig1](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig1-quantiles.JPG)

- 표본 중앙값(Sample Median)

  - 정렬된 데이터에서 중앙에 오는 값
  - 0.5 quantiles, 50 percentiles와 동일

- 표본 분산(Sample Variance)
  $$
  s^2=\frac{1}{n-1}\sum_{i=1}^n{(x_i-\bar x)^2}
  $$

  - 모집단의 분산 공식과 다르게 n-1로 나누어 준다.
  - 다음 링크 참조 [왜 표본(샘플)의 분산에서는 n이 아닌 n-1로 나눌까?](https://m.blog.naver.com/sw4r/221021838997)

- 표본 표준편차(Sample Standard deviation)
  $$
  s=\sqrt{s^2}
  $$
  

### Z-Scores

- 각기 다른 기준을 동일한 기준으로 변경하는것...?

- 모집단 Z-Score
  $$
  z=\frac{(x-\mu)}{\sigma}
  $$

- 표본 Z-Score
  $$
  \hat z = \frac{(x-\bar x)}{\sigma}
  $$



### Correlation

- Correlation
  - 두 변수 x,y 간의 관계를 표현한 것.

  - 예제: 대여소에서 바이크를 빌린사람은 자전거를 잘 빌리지 않음.

  - 모집단의 상관계수
    $$
    Corr=E(\frac{X-E(X)}{\sigma_X} \frac{Y-E(Y)}{\sigma_Y})
    $$

  - 표본의 상관계수
    $$
    Corr=\frac{1}{n-1}(\sum_{i=1}^n\frac{x_i-\bar x}{s_x}\frac{y_i-\bar y}{s_y})
    $$

- Covariance

  - 모집단의 공분산
    $$
    Cov(X,Y) = E([X-E(X)]{Y-E(Y)})
    $$

  - 표본의 공분산
    $$
    Cov(x,y)= \frac{1}{n-1}\sum_{i=1}^{n}(x-\bar x)(y-\bar y)
    $$
    

- 표본의 공분산과 상관계수에서 n-1로 나누는 이유는 Summary Statistics의 표본 분산을 구할 때 n-1로 나누는 이유와 같음
- 상관관계와 인과관계는 동일하지 않음



### Simpson's Paradox

- 크기가 작은 데이터셋의 결과가 크기가 큰 데이터셋의 결과와 반대일 때

- 잠복변수가 존재하거나 서로 크기가 맞지 않는 데이터가 합쳐진 경우 발생할 수 있음

- 예시: 항공사별 지연율

  ![fig2](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig2-delay_airline.JPG)

  - 두 항공사의 전체 지연율만 보면 Consolidated Messenger의 지연율이 낮으나 상세 지연율을 보면 Blue Yonder Airline의 모든 도시의 지연율이 낮은것을 확인할 수 있음
  - 이는 데이터의 크기가 맞지 않기 때문인데, Blue Yonder Airline은 대부분의 항공편이 Seattle로 가고 Consolidated Messenger는 대부분 Phoenix로 가는것을 확인할 수 있음
  - Phoenix보단 Seattle이 더 큰 도시이기 때문에 상대적으로 지연율이 높고 Phoenix는 낮기 때문에 전체 지연율은 Consolidated Messenger가 낮게 나옴