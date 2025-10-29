# 자연어처리 및 텍스트 파운데이션 모델
## 거대 언어 모델

---

## 목차
1. 텍스트 파운데이션 모델 살펴보기
   - 텍스트 파운데이션 모델 (거대 언어 모델)이란?
   - 거대 언어 모델 예시
2. 거대 언어 모델의 학습
   - 지시 학습
   - 선호 학습
3. 거대 언어 모델의 추론
   - 디코딩
   - 프롬프트 엔지니어링
4. 거대 언어 모델의 평가와 응용
   - 거대 언어 모델의 평가
   - 거대 언어 모델의 응용/한계

---

## 학습 목표
- 텍스트 파운데이션 모델(거대 언어 모델)이 무엇인지 이해합니다.
- 거대 언어 모델의 학습 및 추론 방식을 이해합니다.
- 거대 언어 모델의 응용 및 한계를 파악하고, 실습을 통해 실제 사례에 적용해봅니다.

---

## 0. 학습 시작: 파운데이션 모델

### 파운데이션 모델이란?
- 대량의 데이터를 기반으로 사전 학습된 대규모 AI 모델
- 다양한 작업에 범용적으로 활용할 수 있는 기초(foundation) 역할을 함

### We will learn: 파운데이션 모델의 주요 특징
- 기존 AI 모델과의 차이점
- 3가지 핵심 구성요소

### We will learn: 텍스트 파운데이션 모델 (거대 언어 모델)
- 거대 언어 모델의 특징
- 대표적인 예시

---

## 예시: 텍스트 생성 (ChatGPT)
- ChatGPT를 활용한 텍스트 생성 예시

출처: [https://openai.com/chatgpt/](https://openai.com/chatgpt/)
- <그림0-1_텍스트 파운데이션 모델_파운데이션 모델_ChatGPT사용 예시>

---

## 예시: 비디오 생성 (SORA)
- 텍스트 기반 비디오 생성 예시

출처: [https://openai.com/index/sora/](https://openai.com/index/sora/)
- <그림0-2_텍스트 파운데이션 모델_파운데이션 모델_SORA를 통한 텍스트 기반 비디오 생성 예시>

---

## 예시: 멀티모달 입력과 출력 (GPT-4o)
- 멀티모달: 이미지, 비디오, 오디오, 텍스트

출처: [https://openai.com/index/hello-gpt-4o/](https://openai.com/index/hello-gpt-4o/)
- <그림0-3_텍스트 파운데이션 모델_파운데이션 모델_GPT-4o를 통한 실시간 질의 응답 예시>

---

## 파운데이션 모델 이전
- 새로운 테스크를 해결하려면 해당 테스크에 대한 “별도의 학습” 필요

예시:
- Early days [features] → 0/1  
- AlexNet (2012) → ship  
- BERT (2018) → "i love this movie" → pos/neg

출처: [https://cs231n.stanford.edu/](https://cs231n.stanford.edu/)
- <그림0-4_텍스트 파운데이션 모델_파운데이션 모델_AI 모델을 학습하기 위한 이전 방법론들에 대한 예시>

---

## 파운데이션 모델의 등장
- 새로운 테스크를 해결하려면 “자세한 설명(프롬프트)”을 입력해주는 것으로 충분
- ChatGPT: 텍스트 파운데이션 모델  
  (a.k.a 거대 언어 모델 or Large Language Model or LLM)

출처: [https://www.gotai.co.kr/](https://www.gotai.co.kr/)
- <그림0-5_텍스트 파운데이션 모델_파운데이션 모델_텍스트 파운데이션 모델(ChatGPT)을 통한 새로운 테스크(4행시) 해결 예시>

# 0. 학습 시작: 파운데이션 모델

## 파운데이션 모델
- 새로운 테스크를 해결하려면 “자세한 설명(프롬프트)”을 입력해주는 것으로 충분 😊  
  - SORA: 비디오 파운데이션 모델

> “세련된 여성이 따뜻하게 빛나는 네온과 움직이는 도시 간판으로 가득한 도쿄 거리를 걸어 내려온다.  
> 그녀는 검은 가죽 재킷, 긴 빨간 드레스, 검은 부츠를 착용하고 검은 가방을 들고 있다.  
> 그녀는 선글라스를 쓰고 빨간 립스틱을 바르고 있다. 그녀는…”

출처: https://openai.com/index/sora/

---

## 파운데이션 모델의 3가지 구성요소

### (1) 빅데이터
- 인터넷에 존재하는 데이터 수가 기하급수적으로 증가

출처: https://medium.com/@koshwemoethu.blacknet/the-era-of-big-data-863e87f0515d

---

### (1) 빅데이터 (심화)
- 딥러닝 기반 AI 모델은 학습 데이터가 늘어날수록 성능이 증가

출처: https://epochai.org/blog/trends-in-training-dataset-sizes

---

### (2) 자가 학습(Self-supervised Learning)
- 사람이 정답을 알려줄 필요 없음
- 예시: **다음 토큰 예측(Next token prediction)** 을 통한 텍스트 파운데이션 모델(거대 언어 모델) 학습

  - 인터넷에서 데이터 추출 → “아까 밥 먹고 왔어”
  - 학습 데이터 생성  
    - 입력: 아까 밥 먹고  
    - 정답: 왔어  

출처: https://tilnote.io/books/6480b090e92fe5ef635f54df/6480a73ee92fe5ef635f4d77

---

### (3) 어텐션(Attention) 기반 트랜스포머(Transformer) 모델
- 더 많은 데이터를 학습할 수 있는 인공신경망 구조  
  - **어텐션(Attention)**: 입력 데이터에서 중요한 부분에 주의를 집중하는 메커니즘  
  - **트랜스포머(Transformer)**: 어텐션 메커니즘을 기반으로 한 신경망 구조  

출처: https://www.researchgate.net/figure/Decoder-only-Transformer-architecture-The-input-to-the-decoder-is-tokenized-text-and_fig3_373183262

---

# 1. 텍스트 파운데이션 모델 살펴보기

## 1-1. 텍스트 파운데이션 모델이란?

### 파운데이션 모델의 3가지 구성 요소 in 언어 모델 (Language Model)
- GPT-1, BERT와 같은 언어 모델에도 3가지 구성 요소가 이미 포함되어 있음  
  - 그러나 파운데이션 모델과 같은 능력을 보여주지 못함 → **어떤 차이 때문일까?**

출처: Delvin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*, NAACL 2019

---

### GPT-2: 추가 학습 없이 새로운 테스크 수행 가능
- 언어 모델이 추가 학습 없이도 텍스트 지시를 통해 새로운 테스크를 “어느 정도” 수행할 수 있음을 확인

출처: Radford et al., *Language Models are Unsupervised Multitask Learners*, OpenAI 2019

# 1-1. 텍스트 파운데이션 모델이란?

## 파운데이션 모델의 3가지 구성 요소 in 언어 모델 (Language Model)
- GPT-2: 언어 모델이 추가 학습 없이도 텍스트 지시를 통해 새로운 테스크를 “어느 정도” 수행할 수 있음을 확인  
  - 가장 큰 GPT-2 모델조차도 *underfitting*된 결과를 보여줌 → **모델 크기를 더 늘렸을 때 성능이 개선될 여지가 있음**

$$
Perplexity = \sqrt[N]{\frac{1}{P(w_1, w_2, \ldots, w_N)}} = \sqrt[N]{\prod_{i=1}^{N} \frac{1}{P(w_i|w_1, w_2, \ldots, w_{i-1})}}
$$

출처: Radford et al., *Language Models are Unsupervised Multitask Learners*, OpenAI 2019

---

## 텍스트 파운데이션 모델(거대 언어 모델)의 특이점

### (1) 규모의 법칙 (Scaling Law)
- 더 많은 데이터, 큰 모델, 긴 학습 → 더 좋은 성능

출처: Kaplan et al., *Scaling Laws for Neural Language Models*, arXiv:20.01

---

### (2) 창발성 (Emergent Property)
- 특정 규모를 넘어서면 갑자기 모델에서 발현되는 성질  
  - **예시 #1. 인-컨텍스트 학습 (In-context Learning)**  
    주어진 설명과 예시만으로 새로운 테스크를 수행  
  - **예시 #2. 추론 (Reasoning)** 능력  

출처: Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020

---

# 1-2. 거대 언어 모델 예시

## 텍스트 파운데이션 모델 (or 거대 언어 모델, LLM)
- 기존 대비  
  1. 더 큰 모델(>7B)  
  2. 더 많은 데이터(>1T)에서 학습되어 창발성이 나타나기 시작한 언어 모델  
- 일반적으로 거대 언어모델은 GPT와 같이 다음 토큰 예측을 통해 많은 텍스트 데이터에서 사전 학습된 트랜스포머 기반 모델을 의미  

| 구분 | 대표 모델 |
|------|------------|
| **폐쇄형 거대언어 모델** | ChatGPT, Claude 3, Gemini |
| **개방형 거대언어 모델** | LLaMA 2, DeepSeek, Mistral AI |

출처: SSAFY 텍스트 파운데이션 모델 슬라이드

---

## 폐쇄형 (Closed) 거대 언어 모델
- 예시: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google)
- **장점:** 일반적으로 더 우수한 성능 및 최신 기능을 갖고 있으며 사용하기 쉬움  
- **단점:**  
  1. 사용 시마다 비용이 발생  
  2. 모델이나 출력에 대한 정보가 제한적으로 제공됨  

출처: https://platform.openai.com/docs/guides/text?lang=python  
https://openai.com/ko-KR/api/pricing/

27부터