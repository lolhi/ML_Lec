## [Probability and Random Variables](https://mpp.yonsei.ac.kr/courses/course-v1:Microsoft+DAT203.1x+2017_T4/course/#block-v1:Microsoft+DAT203.1x+2017_T4+type@sequential+block@e9eb955c6691477983b1e5d754f72a52)

### Introduction to Probability

- 확률(Probability)는 데이터 과학자에게 필수적인 기술

- advance probability 이론이 필요하진 않지만 기본 확률 이론에 대한 이해가 필요

- probability is not precisely defined, but it should be, or are you sure this isn't a case of Simpson's paradox, questions like that.

  

  #### Common mistake

  1. 확률의 개념(random variable)에 대해 정의(define)하지 않고 논의를 진행

     - 확률에 대해 이야기 하려면 random variable의 의미를 정의해야 함
     - 확률(probability)이라는 단어 자체는 의미가 없음

  2.  상관관계(Correlation)는 원인(causation)이 아님

  3. 가설검정이 실패하였을때 귀무가설(null hypothesis)이 참이라고 가정하는 것

     

  #### 확률 변수(Random Variable)

  - A random variable assigns a numerical value to each possible outcome of a random experiment. 

  - it's something whose value depends on chance.

  - 확률적 데이터를 대표하는 변수는 나올 수 있는 값이 확률적 분포를 가진다. 즉 특정한 값은 자주 나오고 다른 어떤 값은 드물게 나올 수 있다. 이러한 변수를 확률변수라고 한다(출처: 데이터 사이언스 스쿨)

  - 확률변수는 숫자여야 함.

    ex) 오늘의 날씨 -> x

    ​	  내일의 강수량 -> o

    ​	  랜덤하게 선택한 차의 색상 -> x

    ​	  색상에 숫자를 매긴 차의 랜덤 선택 -> o

    ##### 이산 확률 변수(Discrete Random Variable)

    - A discrete random variable has a number of outcomes that you could count.

    - 확률 변수값이 연속적(continuous)이지 않고 떨어져(discrete) 있는 경우를 이산 확률 변수(discrete random variable)라고 한다.(출처: 데이터 사이언스 스쿨)

      ex) the number of truffles in a box

    ##### 연속 확률 변수(Continuous Random Variable)

    - Now continuous random variables are different in that you can't count the number of possible outcomes.

    - 연속 확률 변수의 값은 실수(real number) 집합처럼 연속적이고 무한개의 경우의 수를 가진다. 이러한 확률 변수를 연속 확률 변수 (continuous random variable)라고 한다.(출처: 데이터 사이언스 스쿨)

      

### 이산 확률 변수(Discrete Random Variables)

- 예제: 주사위의 확률

  ![fig1](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig1-roll_of_a_dice.JPG)

  - X: 확률변수, 주사위를 굴렸을때 나오는 값
  - x: outcome
  - P(X=x): 확률 변수 X가 outcome x를 갖게 될 확률
  - 확률의 총 합은 1
  - 위 표를 확률 질량 함수(Probability Mass Function, PMF)라고 함

  #### Summarizing Distributions

  - Computing the mean

    - 이산 확률 변수의 평균값을 기대값(expected value)라고도 함.

    $$
    \mu = \sum_i x_ip_i = E(X)
    $$

    

  - Computing the Spread 

    - outcome x 와 평균값의 거리에 제곱을 해준것에 확률을 곱함.
      $$
      Var(X) = \sum_ip_i(x_i-\mu_i)^2
      $$

    - 분산은 기존 단위에 제곱을 해주었기때문에 제곱근을 계산하여 원래 단위와 맞춰줄 수 있음
      $$
      \sigma = STD(X) = \sqrt{Var(x)}
      $$

  

### 이산 확률 분포(Discrete Probability Distributions)

- 베르누이 분포(Bernoulli Distribution)

  - 결과가 두가지중 하나만 나오는 시행을 **베르누이 시행**이라고 함

  - 베르누이 시행에 0, 1 같은 숫자를 매긴 것을 **베르누이 확률**라고 함

  - 베르누이 확률을 따르는 분포를 **베르누이 분포** 라고 함(출처: 데이터 사이언스 스쿨)

  - 베르누이 분포의 확률 질량 함수(Probability Mass Function, PMF)는 다음과 같음

    ![fig2](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig2-bernoulli_PMF.JPG)

  - 베르누이 분포는 다음과 같이 나타낼 수 있음
    $$
    X \sim Bernoulli(p)
    $$

  - 예제: 각각의 미국인들이 보험에 들었을 확률

    | Outcome x | Probability p |
    | :-------: | :-----------: |
    |     1     |     0.89      |
    |     0     |     0.11      |

    $$
    X \sim Bernoulli(0.89)
    $$

- 이항 분포(Binomial Distribution)

  - 베르누이 분포의 반복

  - 베르누이 확률을 따르는 표본들이 여러번 반복됬을때의 확률을 구하는 것
    $$
    P(X=x)=\frac{n!}{x!(n-x)!}p^x(1-p)^x
    $$
  
- 예제: 미국인 10명중 3명이 보험에 가입했을 확률은?
    $$
    P(X=3)=\frac{10!}{3!(7)!}0.89^3(0.11)^7 = 1.6485 * 10^{-5}
    $$
  
- 이항분포의 평균값(기대값)
    $$
    E(X)=np
    $$
  
- 이항분포의 분산
    $$
    Var(X)=np(1-p)
    $$
    



### Binomial Distribution Examples

- 예제1: 동전 20개를 무작위로 던졌을때 10개가 앞면이 나올 확률

  - 조건: 각각의 동전이 앞면이 나올 확률은 0.5

  $$
  X \sim Bernoulli(0.5)
  $$

  - 다음과 같이 구할 수 있다.

$$
  Binomial\,Distribution의\,확률\\
  P(X=x)=\frac{n!}{x!(n-x)!}p^x(1-p)^{n-x}\\
  P(X=10)=\frac{20!}{10!10!}0.5^{10}0.5^{10}\\
  =0.176197052001953125
$$

- 예제2: 동전 20개를 무작위로 던졌을때 10개 이하가 앞면이 나올 확률
  $$
  P(X\leq10)=P(X=0)+P(X=1)+\,...+P(X=10)\\
  = 0.5881
  $$
  
  - 위와같은 문제는 PMF를 플롯으로 그려서 푸는게 편함
  
- 예제3: 룰렛에 18개의 검은칸, 18개의 빨간칸, 2개의 초록칸이 있다고 할때 룰렛을 10번 돌리고 검은칸에 10번 다 배팅하면 적어도 4판 이길 확률은?

  - 검은칸에 걸었을 때 이길 수 있는 확률은 다음과 같다

    | Outcome x | Probability p |
    | :-------: | :-----------: |
    |     1     |    약 0.47    |
    |     0     |    약 0.53    |

  - 이는 베르누이 확률 변수이기 때문에 다음과 같이 표현할 수 있다.
    $$
    X \sim Bernoulli(0.47)
    $$
    
- 따라서 이항분포를 이용하여 다음과 같이 풀 수 있다.
  
$$
  P(X\geq4)=P(X=4)+P(X=5)+P(X=6)+P(X=7)+P(X=8)+P(X=9)+P(X=10)\\
  = 0.2271 + 0.2417 + 0.1786 + 0.0905 + 0.0301 + 0.0059 + 0.0005\\
  = 0.7744‬
  $$
  


### Poisson Distributions

- 이항분포의 극한 버전

- 사건의 발생횟수가 많아 질 수록 성공확률은 작아짐(동일 비율로)

- 포아송 분포에서는 np는 람다로 변경

- 따라서 다음과 같이 PMF 공식이 변경된다.
  $$
  P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}, x=0.1.2,...
  $$

- 포아송 분포의 기대값과 분산은 다음과 같다
  $$
  E(X) =\lambda, Var(X)=\lambda
  $$

- 람다의 의미는 단위 시간 당 평균 발생 횟수를 의미한다(출처: https://danbi-ncsoft.github.io/study/2019/07/15/poisson.html)

### Continuous Probability Distributions

- 테이블에서 나올 값들을 셀 수 없기 때문에 연속확률 변수의 확률을 나타낼 수 있는 테이블을 만들 수 없음

- 연속확률 변수를 나타낼 수 있는 곡선은 그릴 수 있음

- 특정 값을 놓고 확률을 묻는다면 해당 값의 구간은 0의 확률을 가지지만 값의 범위를 지정하고 확률을 물으면 0이 될수 없음

  ![fig3](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig3-continuous_probability_distributuion.JPG)

- 위와 같은 함수를 **확률 밀도 함수(Probability density function)** 이라고 함

![fig4](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig4-uniform_distribution.JPG)

- 위와 같이 특정 구간의 확률이 동일한 분포를 **균등 분포(Uniform Distribution)** 이라고 함

- 특정 구간의 확률을 구하기 위해서 다음과 같이 계산

  ![fig5](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig5-calculate_continuous_distribution_probability.JPG)



### Cumulative Distribution Functions

- CDF(Cumulative Distribution Functions)는 확률변수 X가 특정 값 이하에 해당한다는 의미

- PDF가 주어졌을때 다음과 같이 표현
  $$
  F(x)=P(X\leq x)
  $$

  - 위 식에서 leq를 le로 바꿔도 무방

- fig5의 식을 CDF를 사용하여 다음과 같이 나타낼 수 있음
  $$
  P(10 \leq X \leq 14) = F(14)-F(10)
  $$
  
- F(x)값을 구하였을때 다음과 같이 그래프로 나타낼 수 있음

![fig6](https://github.com/lolhi/ML_Lec/blob/master/MPP/DAT203.1x-Data%20Science%20Essentials/Module%202-Probability%20and%20Statistics%20for%20Data%20Science/fig6-cdf.JPG)



### Central Limit Theorem

- 정규 분포(Nomal Distribution)

  - 공식
    $$
    f(t)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(t-\mu)^2}{2\sigma^2}}
    $$

  - 표준편차의 값이 작아지면 뽀족한 정규분포가 만들어지고, 값이 커지면 넓은 정규분포가 만들어짐

- 중심극한정리(Central Limit Theorem)

  - 독립 확률 변수의 숫자가 크고, 그 숫자를 모두 더해준다면, 정규분포에 가까워짐
  - n이 커질수록 정규분포에 가까워짐
  - 이항분포도 n이 커진다면 정규분포에 가까워짐(사건이 독립이기 때문에)
