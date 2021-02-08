## 캐글 및 데이터 분석에 대한 메모입니다.(캐글 데이터분석캠프 영상 참고 후 메모와 개인 학습내용 정리 합본)

### 용어 정리
competition : 대회, Dataset : 데이터 셋, NoteBook : 코드 공유, 듀토리얼 공유, Discussion : Text로 의견공유, 팀원모집, 솔루션공유등

### 목표
공부, 메달, 상금, 성취감

### 티어 와 메달
티어 : 초록-> 하늘 ->보라(Expert) -> 주황(Master) -> 금색(GrandMaster)
메달 : 동 -> 은 -> 금

### 기타
현업에 깔끔한 데이터가 없다, 앙상블 위주의 접근, 그냥문제풀이 아니냐 등의 부정적 측면 말고
본인이 얻고 싶은것을 명확히 하기 ( 다양한 도메인 지식, 우승 솔루션을통한 전체적인 프로세스 공략, 정지된 데이터 모델링 초점, 고전적인 방법부터
최신 논문까지 활용 가능)

### Competitions

대회타입 
* Featrued : 스코어 대회
* Analytics : 분석 대회
* Research : 연구 대회
* Getting Started : 듀토리얼
* Play ground : 재미용 대회

제출 방식
* Simple Competition : 제출 파일만 제출
* code competition : 코드로 제출

### 대회 세부 확인
* 대회가 어떤 주제인지 Description 확인
* Data의 종류와 분량 확인(EDA)
* Evaluation 확인 + 리더보드 대략 확인(이미 사람들이 정확도 최고를 찍었는데 내가 한다고 얻을 수 있는게 있을까?? 등등)
* 기존에 논의된 Discussion 살펴보기
* Upvote 많은 Notebook 살펴보기
* Leaderboard : public = 대회 중간 score, private = 대회 최종 score / 제출한 Test Data의 33% public 나머지 priavate
* Notebook 퀄리티 높히기 : 마크업, 링크, 설명 등등


### 머신러닝

입력 -> EDA -> 전처리 -> 모델 -> 결과
      
입력->EDA(데이터에서 인사이트 찾기) -> 전처리(모델에 적합하게 수정, Feature Engineer/Selection, 도메인지식활용) -> 모델 -> 결과
결과 -> 모델 ( Hyperparameter개선, 여러모델 시도, 모델 합치기(앙상블)
결과 -> EDA(새로운 인사이트)

### 입력
CSV파일, 판다스 라이브러리 (일반 크기의 파일)

Dask, Datable, Rapids (큰 데이터)

### EDA
Pandas, Matplot, seaborn, plotly

##### 실제 이 단계에서 봐야할 것
* 어떤 문제를 해결하려고 하는가
* 어떤 종류의 데이터가 있고 어떻게 처리할까??(어떤데이터 이니까 어떻게 인코딩 해야겠다)
* 데이터의 누락값이 무엇이고, 이를 어떻게 처리할까?
* 특이 값(outlier)은 어디에 있으며 이를 어떻게 처리할까?
* 데이터를 최대한 활용하기 위해 어떻게 새로운 피쳐를 만들까

##### 데이터 살피기
* 어떤 데이터 인지, 모델에 넣을수 있는 데이터 인지
* numerical / categorical
* numerical : 이산형(정수로 나누어 지는것)/ 연속형(연속적인값, 예를들면 나이)
* categorical : 명목형(순서 상관x)/ 순서형(순서가 있는것)
* feature들을 적어보고 숫자 데이터 간의 관계 확인, 숫자와 categorical데이터 간의 관계 확인, categorical 데이터들 간의 관계 확인

##### ML 
* 머신러닝의 기본은 통계 
* 시각화를 하는 이유는 : 이해
* What would you like to show?? : 구성(comparison), 분포(distribution,나이분포등..), 관계(Relation, 데이터들의 관계), 데이터간의 차이

### 전처리
* Feature Engineering : 어떻게 새롭게 만들것인가, 조합할것인가
* Feature Seletion : 어떻게 Feature를 선택할 것인가.
* 도메인 지시고가 모델의 특성에 맞게

### 모델
* ml모델
* 부스팅 모델
* 스태킹, 앙상블 등등

### 결과
* score이해
* overfitting 과의 싸움
* Hyperparameter 바꿔가며 실험
* 다시 돌아가며 EDA 부터 

### 머신 러닝 적용 3 요소

#### 개념적이해
* 모델이 어떤 아이디어를 가지고 있을까?
* 기존 모델이 어떤 점을개선했을까?
* 이 모델의 장단점
* 무엇을 계산하고 있는 걸까?

#### 프로그래밍 스킬
* 라이브러리 사용법
* 모델을 직접 구현하는 방법
* 구현된 모델을 커스텀 하는 방법
* 시간과 컴퓨팅 코스트를 어떻게 줄일까
* 재사용성과 가독성을 어떻게 늘릴까

#### 수학 + 도메인
* 모델 내부에는 어떤 과정?
* 데이터는 어떻게 살펴볼 수 있을까?
* 데이터에 따른 전처리 방법
* 데이터에 노이즈 확인
* 가정을 어떻게 검증할까.

### 데이터 별 인코딩

* Categorical 데이터 에는 Norminal(명목형) 데이터 와 Ordinal(순서형) 데이터로 나뉘어 진다.
* Norminal 데이터는 순서가 없는 즉, 셩별 종류 등의 데이터 이며
* Ordinal 데이터는 순서가 있는 것 즉, 수능의 등급이나, 좌석등급, 순위 등이 이에 속한다.
* 현재까지 내가 알고 있는 인코딩은 map함수를 이용하여 지정해주는것, one-hot 인코딩, LabelEncoder()함수를 불러오는것 이렇게 세가지 이다.
* 순서가 없는 데이터 즉 Norminal데이터 를 LabelEncoder()를 통해서 인코딩을 하게되면 관계가 발생하게 된다.
* 예를 들면 A형: 1 , B형: 2, c형: 3 일때 A형 + B형 = C형 이라는 관계가 생기게 된다.
* 따라서 이러한 Norminal 데이터는 one-hot 인코딩을 사용해주고
* Ordinal 데이터는 순서가 있기 때문에 LabelEncoder()를 사용해도 무방하다.
