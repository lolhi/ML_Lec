## [Hypothesis Testing](https://mpp.yonsei.ac.kr/courses/course-v1:Microsoft+DAT203.1x+2017_T4/course/#block-v1:Microsoft+DAT203.1x+2017_T4+type@sequential+block@044e71bd5b744e999b4546707e090bcd)

### Introduction to Hypothesis Testing

- 가설검정(Hypothesis testing)
  - 합리적인 의심을 넘어서 정확하게 예 또는 아니오로 대답하는 기술
  - 가설검정을 위해 귀무가설과 대립가설을 설정하고 특정 기준(p-value 등...)을 사용하여 가설을 선택
  - 귀무가설(Null Hypothesis, H0)
    - 현 상태와 아무런 차이가 없음
  - 대립가설(Alternative Hypothesis, H1)
    - 현 상태가 틀렸다는 것을 주장하는 것, 증명 필요
  - p-value
    - probability to observe something as extreme as what you observed, under the null hypothesis
    - 일반적으로 significance level 알파는 5%
  - 만약 p-value가 significance level 보다 작다면 귀무가설을 기각, 크다면 대립가설 기각
  - Assume H0 is true. Does the data contradict the assumption beyond a reasonable doubt?
    - Yes: accept H1, and reject H0
    - No: H0 can't be ruled out as an explanation for the data. in this case we can't accept any hypothesis
    - 대립가설을 기각해도 귀무가설이 옳다는 것은 아님



### Z-Tests, T-Tests, and Other Tests

- Z-Test

  - 평균 및 분산을 이미 알고 있는 경우, 정규분포에 검정을 시행하는 것
  - 입력
    - data, 귀무가설(평균, 표준편차), 대립가설(오른쪽, 왼쪽, 양쪽), significance level
  - 출력
    - 기각 또는 수용, p-value, confidence level, z-score 
  - 언제 사용하는가?
    - data가 정규분포이고, 표준편차를 알때
    - n이 30보다 클떄

- T-Test

  - 정규분포에서 얻은 작은 표본들이 있는 경우 유용

  - 분산을 모름

  - t distribution

    - 정규분포와 유사하지만 끝부분이 조금 넓음(불확실성 때문)

      ![fig1](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%203-Simulation%20and%20Hypothesis/fig1-t_distribution.JPG)

    - 데이터가 많아질 수록 점점 정규분포에 가까워짐

    - 결과적으로 t distribution의 표본 표준편차와 정규분포의 표준편차는 차이가 없게 됨

  - 입력

    - data, 귀무가설(평균), 대립가설(오른쪽, 왼쪽, 양쪽), significance level

  - 출력

    - 기각 또는 수용, p-value, confidence level

  - 언제 사용하는가?

    - n이 30보다 작을 때

- Many other test

  - 비모수 가설검정(Non-parametric hypothesis test, Sign test, Wilcoxon signed rank test)

    - 데이터가 많고, 해당 데이터를 포함한 분포가 무엇인지 모를때 사용
    - 중간값이 특정 값과 동일한지 여부를 검정

  - Test on variance(chi-squared)

    - 분포에 대한 분산이 특정 수보다 크거나 작은지 여부에 대한 검정

  - Test on Proportion(Uses binomial/normal)

    - 모집단의 비율이 특정 값을 넘는다는 가설을 검정

      

### Type 1 and Type 2 Errors

- 1종 오류(Type 1 Error)

  - 검정시 귀무가설이 참이지만 대립가설을 채택했을때 발생
  - 오탐이라고도 함

- 2종 오류(Type 2 Error)

  - 검정시 대립가설이 참이지만 귀무가설을 채택했을때 발생

  - 미탐이라고도 함

    ![fig2](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%203-Simulation%20and%20Hypothesis/fig2-type_1_2_errors.JPG)



### Confidence Intervals

- 이해가 가지 않음..



### Misconceptions About Hypothesis Testing

1. P-values indicate how incompatible data are with a specified model of the world
   - true
2. A p-values measurtes the probability that the null hypothesis is ture.
   - false, p value는 극단적인 일을 관찰 할 가능성을 측정
3. A p-values measures the probability that the data were produxed by random chan alone.
   - false
4. A p-values measures how big an effect is. A small p-value means a large effect.
   - false
5. A p-values tells you how important a result is.
   - false