# AI강의Ⅱ Wrap Up
## 최인호 강사

# AI 강의Ⅱ 챕터 별 리뷰
- AI를 위한 Python과 Math
- EDA
- MLP
- 토큰화 / 임베딩
- 합성데이터와 데이터 증강
- CNN
- RNN / LSTM
- Attention과 Transformer 모델
- Transformer 기반 이미지 모델
- RAG
- PEFT

# AI를 위한 Python과 Math

## 실습: AI를 위한 Python과 Math
- AI를 위한 준비과정  
  1. 파이썬 기본 문법  
  2. 클래스  
  3. Numpy  
  4. Pandas  
  5. Matplot  
  6. Seabon  
  7. 선형회귀  
  8. 로지스틱회귀  
  9. Gradient Decent  

````python
# 깔끔~
def sum1(a, b):
    return a + b

# 파라미터 타입까지 표기
def sum2(a: int, b: int):
    return a + b

# 리턴 타입까지 표현
def sum3(a: int, b: int) -> int:
    return a + b

c = sum1(10, 20)
print(c)
````

## 실습: 실습 자료 공유
- 코드를 직접 실행해보면서 AI강의Ⅱ 에서 배운 내용을 리뷰  
  - 주요 포인트에 대해서  
    어떤 내용을 학습했고  
    왜 이걸 배웠는지 대해 리뷰

# EDA

## 실습: EDA
- EDA를 통해 데이터를 잘 이해한다.  
  - EDA : 데이터를 살펴보는 행동  
  - 데이터 샘플을 확인  
  - 필드 확인  
  - 기본 통계량 확인  
  - 분포 확인  
  - 상관계수 확인  
  - 등등

# MLP (Multi-Layer Perceptron)
- 하나 이상의 은닉층을 가진 신경망  
- 활성화 함수와 함께 복잡한 패턴을 학습하고 분류  
- 딥러닝 학습의 시작점

# 토큰화/임베딩

## 토큰화
- 문장을 토큰 단위로 나누는 과정

## 임베딩
- 각 토큰화된 단어들에게 의미를 부여하는 과정
- 의미공간의 Vector값을 갖게된다.

# 합성 데이터와 데이터 증강

## 합성데이터 (Synthetic Data)
- 실제 세계에 없는 새로운 데이터를 생성하는 것

## 데이터 증강 (Data Augmentation)
- 실제 데이터를 변형하여 데이터 셋을 확보하는 것

# CNN

## CNN (Convolutioonal Neural Network)
- 이미지, 영상에서 시각 데이터의 특징을 기반으로 사물을 인식할 수 있는 딥러닝 알고리즘
- 2012년 AI겨울을 끝내고, CNN 기반의 AlexNet을 통해 AI 시대를 다시 열게 되었음

# RNN / LSTM

## RNN (Recurrent Beural Network)
- AI에서 핵심 딥러닝 알고리즘 중 하나
- 시퀀스 데이터를 학습시키고, 추론시키는데 특화된 딥러닝
- Attention의 필요성을 이해하기 위해 학습했음

## LSTM(Long Short-Term Memory)
- RNN의 가장 큰 단점: 과거 정보를 오래 기억하지 못한다.
  - 과거 정보가 사라지는 이유: 이전 정보를 계속 곱하면서 진행하기 때문(기울기 소실 발생)
- LSTM은 입력/출력/망각 게이트를 통해 중요한 정보는 기억하고 필요 없는 정보는 버림
  - 긴 문맥도 이해할 수 있게 됨
- LSTM의 한계점: 문맥 내 모든 단어 간의 관계를 한 번에 파악하기 어려움

# Attention과 Transformer 모델

## Attention
- 입력데이터에 중요한 부분에 집중할 수 있게 돕는 기술
- 문맥을 이해하는 벡터를 만들어는 역할을 함

## Transformer
- 어텐션을 인코더, 디코더 형태로 활용하여 Foundation Medel 시대를 열게된 딥러닝 모델

## Transformer 기반 이미지 모델
- 트랜스포머는 Text, 이미지, 음성 등 여러 모달을 다루는 모델의 성능을 극대화 시킴

# RAG

## RAG (Retrieval-Augmented Generation)
- LLM이 신뢰성 있는 최신 정보를 참고하여 답변하게 하는 기술
- 환각 현상을 줄일 수 있음

## LangChain 사용방법과 함께 RAG 구현 방법을 실습

# PEFT

## 효율적인 파인튜닝 (PEFT)
- 모든 파라미터를 변경하지 않고, 일부 파라미터만 변경하여 파인듀닝의 효율을 극대화 시킴
- LoRA를 중심적으로 다룸

---
사실상 여기가 끝
---

# 관통 PJT에 AI 적용하기
- AI를 사용하기 위한 구조
- FastAPI 소개
- FastAPI 테스트
- Post 요청 해보기
- 허깅페이스 Local 테스트
- Fast API로 챗봇 만들기

# AI를 사용하기 위한 구조

## 추론 서버를 포함한 아키텍처
### AI를 사용하기 위한 기본 구조
- 추론서버 : AI 추론용 서버를 두고 REST API로 추론
- 백엔드에서 추론 서버를 호출

# FastAPI 소개

## FastAPI를 ML에서 가장 많이 사용되는 Web Framework 입니다.
- REST API 서버 용도로 사용됩니다.
````
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/lunch")
def get_lunch():

  # 이곳에 코드를 넣습니다.

  return {"lunch": "Big-mac"}

# 서버 실행
# uvicorn main:app --reload
````

# FastAPI 테스트

## PyCharm 환경에서 Fast API를 테스트합니다.
- SW역량평가 환경이므로, 모든 PC에 설치되어 있습니다.

# Post 요청 해보기

## FastAPI에서 Post 요청
- Post 요청시 응답을 받아 출력하는 코드를 작성해 봅니다.
  - HTML 파일에서 접근을 위한 CORS 설정이 필요합니다.
  - 우측 Front는 ChatGPT로 생성합니다.

# 허깅페이스 Local 테스트

## 허깅페이스의 Transformer Library 사용
- Qwen3-0.6B 모델을 사용합니다.
- CPU 환경에서 추론이 잘 되는지 테스트합니다.
````
while True:
  prompt = input("입력 : ")
  result = incoke(prompt)
  print(f"AI : {result}\n")
````

# Fast API로 챗봇 만들기

## Fast API로 간단한 챗봇을 만들어봅니다.
- Front
  - ChatGPT로 html 파일을 생성합니다.
  - 전송 버튼을 누를때마다 POST 요청을 합니다.
- Back
  - Fast API로 Local LLM을 동작시킵니다.

# 끝으로
- 관통 PJT 활용 아이디어
- 앞으로의 학습 방향

# 관통 PJT 활용 아이디어 1

## Image to TEXT
- 손글씨, 인쇄된 종이 문서 등 사진으로 부터 Text를 추출해주는 Application 제작

# 관통 PJT 활용 아이디어 2

## Image to Text + Voice to Text
- 영화 이미지와 음성을 Text로 출력해주는 서비스

# 관통 PJT 활용 아이디어 3

## Image to Image
- 이미지와 Mask를 넣어, 다른 이미지로 변경해주는 서비스 제작
- InstantX/Qwen-Image-ControlNet-Inpainting

# 관통 PJT 활용 아이디어 4

## Text to Image
- 나만의 이미지를 생성해주는 Web Application
- https://huggingface.co/stabilityai/stable-diffusion-sl-refiner-1.0

# 관통 PJT 활용 아이디어 5

## Text to Voice
- 텍스트를 음성으로 출력해주는 TTS 서비스
- https://huggingface.co/hexgrad/Kokoro-82M

## 허깅페이스에서 다양한 아이디어를 얻자

## 허깅페이스 모델과 데이터셋
- 다양한 AI Application을 제작할 수 있습니다.

# 앞으로의 학습 방향

## 앞으로의 학습 방향은?

## 이제부터는 프로젝트로 기술을 통합하고, Hugging Face 중심으로 포트폴리오를 만들어야 합니다.

## 추천 학습 방향
- 모달별 모델 사용해서 데모 서비스 만들기
- 모달별 파인튜닝 노하우 습득하기
- 파인튜닝과 RAG 서비스 운영하기
- Local LLM으로 지속적인 학습하기
- 나만의 모델서버 / 추론서버 운영