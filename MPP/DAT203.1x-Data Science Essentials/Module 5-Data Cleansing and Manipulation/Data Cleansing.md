## [Data Cleansing](https://mpp.yonsei.ac.kr/courses/course-v1:Microsoft+DAT203.1x+2017_T4/course/#block-v1:Microsoft+DAT203.1x+2017_T4+type@sequential+block@8d3a8fe1a77f40088b770a03c700aee6)

### Missing and Repeated Values

- 결측치(Missing values)

  - 대부분의 머신러닝 알고리즘은 누락된 값을 처리할 수 없음

  - 결측치로 인해 의도하지 않은 이상한 방향으로 수렴할 수도 있음

    ex)

    ![fig1](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%205-Data%20Cleansing%20and%20Manipulation/fig1-missing_values.JPG)

  - 해결법

    1. 행 제거
    2. 특정한 값으로 대체
    3. Interpolate values
    4. forward fill
    5. backward fill
    6. Impute

- 반복값(Repeated values)

  - 여러 반복되는 값을 가지고 있을 경우 편향 유발

    ex)

    ![fig2](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%205-Data%20Cleansing%20and%20Manipulation/fig2-repeated_values.JPG)

  - 해결법
    1. 중복 행 제거
       - DataFrame.drop_duplicates()
       - 주의할것



### Feature Engineering

- 머신러닝 기법을 사용할 때 좋은 성능을 얻기 위해 데이터를 변형하는 것

  ![fig3](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%205-Data%20Cleansing%20and%20Manipulation/fig3-automoblie_pairplot.JPG)

  ex) Automobile 데이터에 price와 city.mpg, curb.weight, engine.size 간 pairplot에서 곡선이 보였는데 price에 log를 해주니 곡선이 완화되었음



### Outliers and Errors

- 이상치(Outliers)
  - 이상치를처리하지 않으면 모델에 편향이 생길 수 있음
  - 따라서 관측값이 이상치인지 흥미로운 값인지 구분할 수 있어야 함

- 발견법

  - 일반적으로 요약통계량과 시각화를 통해 발견

    - scatter plot

      ![fig4](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%205-Data%20Cleansing%20and%20Manipulation/fig4-outliers.JPG)

    - histogram

      ![fig5](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%205-Data%20Cleansing%20and%20Manipulation/fig5-outliers.JPG)

- 해결법

  1. Censor
     - 의심스러운 행을 지움
  2. Trim
     - 범위를 벗어난 값을 제거
  3. Interpolate
     - 시계열이나 연속적값인 경우 사용
  4. Substitute
     - 대체



### Introduction to Data Scaling

- Scaling
  - Numeric Variable은 비슷한 스케일을 가져야 함
  - 방식
    1. Z-Scaling
       - 평균 0, 분산 1으로 스케일링
    2. de trend
       - 시계열 데이터에서 나타날 수 있는 trend 제거
    3. Min-Max Scaling
       - 최소값을 0, 최대값을 1로 스케일링
  - scaling은 이상치 제거 후 진행