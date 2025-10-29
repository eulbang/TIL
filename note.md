# Transformer

## Attention is All You Need
- Transformer는 2017년 Google의 “Attention Is All You Need”라는 논문에서 처음 제안된 아키텍처로,  
  Self-Attention을 핵심 메커니즘으로 하는 신경망 구조이다.

**Attention Is All You Need**

Ashish Vaswani* (Google Brain)  
Noam Shazeer* (Google Brain)  
Niki Parmar* (Google Research)  
Jakob Uszkoreit* (Google Research)  
Llion Jones* (Google Research)  
Aidan N. Gomez† (University of Toronto)  
Łukasz Kaiser* (Google Brain)  
Illia Polosukhin† (개인 이메일)  

Link: Attention Is All You Need (Vaswani et al., 2017)

---

## Transformer
- Transformer는 encoder-decoder 구조로 설계된 신경망 모델이다.
  - **encoder**: 입력 문장을 받아 의미적 표현으로 변환을 수행한다.
  - **decoder**: 인코더의 표현과 지금까지 생성한 단어들을 입력 받아, 다음 단어를 예측한다.
- 이 중 **decoder**가 언어 모델과 같은 방식으로 동작한다.

---

## Multi-Headed Attention
- 문장에서 같은 단어라도 여러 이유(문법적 관계, 의미적 맥락 등)로 다른 단어에 주목할 수 있다.
- 하지만 단일 Self-Attention Head로는 한 가지 관점에서의 단어 간 관계 밖에 파악할 수 없다.
- 따라서 여러 Attention Head를 두어 다양한 관점에서 동시에 정보를 파악한다.

- **Attention Head 1**: 단어의 문맥적 관계에 Attention  
- **Attention Head 2**: 단어의 시제에 Attention  
- **Attention Head 3**: 명사에 Attention  

---

## Multi-Headed Attention (예시)
- Attention head 1: 문법적 의존성 관계 단어들에 주목  
- Attention head 2: 개체에 주목  

---

## Scaled Dot Product
- Query와 Key의 차원이 커질수록, 두 벡터의 내적 값도 자연스럽게 커진다.
- 이 값이 너무 크면 softmax 함수가 출력이 지나치게 뾰족해져, 미세한 변화에도 큰 차이가 발생하고  
  gradient vanishing 문제가 생길 수 있다.

$$
output_l = softmax(X_Q K_l^T X^T) * X V_l
$$

softmax([40, 50, 45]) ≒ [0.000045, **0.99326**, 0.00669]

- 따라서 내적 값을 그대로 사용하지 않고, 나누어 스케일을 조정한다.
- 이렇게 하면 값이 안정적으로 분포되어 학습이 훨씬 더 빠르고 안정적으로 진행된다.

$$
output_l = softmax\left(\frac{X_Q K_l^T X^T}{\sqrt{d/h}}\right) * X V_l
$$

$\sqrt{d/h} = 8$ 로 스케일링  
softmax([5.0, 6.25, 5.625]) ≒ [0.1573, **0.5489**, 0.2938]

---

## Residual Connection
- 깊은 신경망은 층이 깊어질수록 학습이 어려워진다. (Gradient vanishing / exploding)
- 따라서 단순히 Layer의 출력만 사용한다면 정보가 소실되어 layer가 전체를 예측하는 것이 아니라,  
  기존 입력과의 차이만 학습하도록 하는 **residual connection**을 사용한다.

$$
X^{(i)} = X^{(i-1)} + Layer(X^{(i-1)})
$$

---

## Layer Normalization
- 층이 깊어질수록 hidden vector 값들이 커졌다 작아졌다 하면서 학습이 불안정하다.
- Layer Normalization은 각 레이어 단위에서 hidden vector 값을 정규화해,  
  안정적이고 빠른 학습을 돕는다.

---

## Decoder
- Transformer의 decoder는 여러 개의 decoder 블록들을 쌓아 올려서 만든 구조이다.
- 각 블록은 다음으로 구성된다:
  - Masked Self-Attention (Multi-Head)
    - 미래 단어를 보지 않도록 마스크를 씌운 Multi-Head Self-Attention
  - Add & Norm (Residual Connection + Layer Normalization)
  - Feed-Forward Network
    - 각 위치 별 비선형 변환을 수행한다.
  - Add & Norm (Residual Connection + Layer Normalization)

- 언어 모델처럼 단방향 문맥만 활용

---

## Encoder
- 그에 반해 Transformer의 encoder는 양방향 문맥을 모두 활용할 수 있다.
  - 입력 문장을 의미적 표현으로 변환할 수 있다.
  - 각 단어가 양방향 문맥을 모두 반영한 벡터로 인코딩된다.
- Decoder와의 차이점은 Self-Attention에서 **masking을 제거한 것**뿐이다.

---

## Encoder-Decoder
- 기계 번역에서 Seq2Seq 모델을 사용했던 것처럼, Transformer에서도  
  이해를 위한 encoder와 생성을 위한 decoder로 이루어진 encoder-decoder 구조를 채택한다.
- decoder는 단순 Self-Attention만 하는 것이 아니라, encoder의 출력 표현을 참조하는  
  Cross-Attention을 추가하여 입/출력을 연결한다.

### Cross-Attention
- Cross-Attention을 수행할 때는 Self-Attention과는 다르게  
  Query는 decoder에서, Key와 Value는 encoder에서 가져온다.

# 사전 학습 기반 언어 모델

---

## 목차
1. 사전학습이란?
2. Encoder 모델  
3. Encoder-Decoder 모델  
4. Decoder 모델  
5. In-Context Learning

---

## 학습 목표
- 사전학습(Pretraining)의 개념과 필요성을 설명할 수 있다.  
- Encoder 기반 모델(예: BERT)의 구조와 주요 활용 사례를 이해한다.  
- Encoder-Decoder 기반 모델(예: T5)의 특징과 응용 분야를 설명할 수 있다.  
- Decoder 기반 모델(예: GPT)의 구조와 강점을 이해한다.  
- In-Context Learning(ICL)이 등장하게 된 배경과 그 의미를 설명할 수 있다.  
- ICL 능력을 끌어올리기 위한 대표적인 prompting 기법(CoT, Zero-shot CoT)을 이해한다.

---

## 0. 학습 시작 (오버뷰)

### 사전학습(Pretraining)이란 무엇인가? 왜 중요한가?
- 대규모 데이터 기반의 사전학습 개념과 필요성

### 대표적 모델 유형은 어떻게 구분되는가?
- Encoder 기반, Encoder-Decoder 기반, Decoder 기반

### 각각 어떤 모델이 존재하는가?
- BERT, T5, GPT 등 주요 모델 소개

### In-Context Learning과 발전된 prompting 기법은 무엇인가?
- ICL의 등장 배경과 의미  
- Chain-of-Thought, Zero-shot CoT 등 대표 기법

---

## 1. 사전학습이란?

### 사전학습이란?
- 사전학습이란 대규모 데이터 셋을 이용해,  
  모델이 데이터의 일반적인 특징과 표현을 학습하도록 하는 과정이다.  
- 특히 언어 모델은 인터넷의 방대한 텍스트(웹 문서, 책, 뉴스 등)를 활용해  
  비지도학습 방식으로 학습되어, 일반적인 언어 패턴, 지식, 문맥 이해 능력을 습득한다.

---

## 2. Transformer

### Transformer의 놀라운 결과
- Neural Machine Translation task에서 당시 최고 성능을 달성했을 뿐 아니라,  
  가장 효율적인 학습으로 비용까지 절감할 수 있었다.

| Model | BLEU (EN-DE) | BLEU (EN-FR) | Training Cost (EN-DE) | Training Cost (EN-FR) |
|:--|:--:|:--:|:--:|:--:|
| ByteNet [18] | 23.75 |  |  |  |
| Deep-Att + PosUnk [39] |  | 39.2 |  |  |
| GNMT + RL [38] | 24.6 | 39.92 | 2.3·10¹⁹ | 1.4·10²⁰ |
| ConvS2S [9] | 25.16 | 40.46 | 9.6·10¹⁸ | 1.5·10²⁰ |
| MoE [32] | 26.03 | 40.56 | 2.0·10¹⁹ | 1.2·10²⁰ |
| Deep-Att + PosUnk Ensemble [39] |  | 40.4 |  |  |
| GNMT + RL Ensemble [38] | 26.30 | 41.16 | 1.8·10²⁰ | 1.1·10²¹ |
| ConvS2S Ensemble [9] | 26.36 | 41.29 | 7.7·10¹⁹ | 1.2·10²¹ |
| **Transformer (base model)** | **27.3** | **38.1** | **3.3·10¹⁸** |  |
| **Transformer (big)** | **28.4** | **41.8** |  | **2.3·10¹⁹** |

- 점수만 향상한 것이 아니라, 학습 효율도 훨씬 높음.

---

### Transformer와 사전학습(Pretraining)
- Transformer의 등장은 대부분의 최신 모델들이 성능 향상을 위해  
  사전학습(pretraining)을 결합하도록 했다.
- 또한, 뛰어난 병렬 처리 능력 덕분에 대규모 사전학습에 적합하여  
  NLP의 표준 아키텍처로 자리 잡았다.

**예시: GLUE Benchmark**
- 상위권 모델 대부분이 Transformer 기반 + Pretraining 모델이다.

| Rank | Name | Model | Score |
|:--:|:--|:--|:--:|
| 1 | DeBERTa Team - Microsoft | DeBERTa / TuringNLRv4 | 90.8 |
| 2 | HFL iFLYTEK | MacALBERT + DKM | 90.7 |
| 3 | Alibaba DAMO NLP | StructBERT + TAPT | 90.6 |
| 4 | PING-AN Omni-Sinitic | ALBERT + DAAF + NAS | 90.6 |
| 5 | ERNIE Team - Baidu | ERNIE | 90.4 |
| 6 | T5 Team - Google | T5 | 90.3 |

# 1. 사전학습이란?

---

## 사전학습의 관점에서 워드 임베딩 vs. 언어 모델

### 워드 임베딩의 한계
- 워드 임베딩의 경우 사전학습을 통해 단어의 의미를 학습하지만 한계가 존재한다.  
1. **다운스트림 태스크**  
   - 예: 텍스트 분류 등에서는 학습 데이터의 양이 적어,  
     언어의 풍부한 문맥 정보를 충분히 학습하기 어렵다.  
2. **효율성 문제**  
   - 연결된 네트워크가 무작위 초기화되어 학습 효율이 낮고,  
     많은 데이터와 시간이 필요하다.

---

### 언어 모델의 강점
- 언어 모델의 경우 **모델 전체를 사전학습**을 통해 학습하므로,  
  강력한 NLP 모델을 구축하는 데 유리하다.  

1. **언어 표현 학습에 적합**  
2. **파라미터 초기화의 효율성**  
3. **확률 분포 학습을 통한 샘플링·생성 가능**

---

## 언어모델의 사전학습

- 과거 단어들이 주어졌을 때,  
  **다음 단어의 확률분포를 모델링**하는 방법을 배움으로써 사전학습을 수행한다.  
- 인터넷의 대규모 텍스트 코퍼스에서 언어모델링 학습을 수행한 후,  
  학습된 네트워크 파라미터를 저장하여 다양한 다운스트림 태스크에 활용한다.

### 사전학습 → 파인튜닝(Fine-tuning) 패러다임
- 사전학습을 통해 학습한 파라미터로 모델을 초기화하여  
  NLP application 성능을 향상시킨다.

**Step 1:** Pretrain (on language modeling) → 일반적인 언어 패턴 학습  
**Step 2:** Finetune (on your task) → 특정 작업에 맞게 조정

---

## 사전학습 모델들의 역사
- 사전학습 모델은 2018년 이후 급속히 발전하며,  
  BERT, T5, GPT 계열로 대표되는 세 가지 주요 계보를 형성했다.

---

# 2. Encoder 모델

---

## Encoder 모델 개요

- **Encoders**
  - 양방향 문맥을 활용할 수 있다.  
  - 학습을 위한 훈련 방법은?
- **Encoder-Decoders**
  - Encoder와 Decoder의 장점을 모두 결합했다.  
  - 효과적인 사전학습 방법은?
- **Decoders**
  - 전형적인 언어 모델 구조.  
  - 문장 생성에 유용(미래 단어 참조 불가).

---

## Encoder 모델의 사전학습

- Encoder 모델은 **양방향 문맥을 모두 활용**하기 때문에,  
  전통적인 언어 모델과는 차이점이 있다.  
- 입력 단어의 일부를 `[MASK]` 토큰으로 치환하고,  
  모델이 해당 위치의 단어를 예측하도록 학습하는 방식이다.  
- 이를 **Masked Language Model (MLM)** 이라 하며, 대표적인 모델은 **BERT**이다.

---

## BERT

- **BERT**는 2018년 Google에서 공개한 Transformer 기반 모델로,  
  **Masked LM 방법**으로 사전학습을 수행했다.

**논문명**: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding  
**저자**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova  
**기관**: Google AI Language

---

## BERT의 학습 방법 1 - Masked LM

- 학습 방식은 다음과 같다.
  - 입력 토큰의 **15%**를 무작위로 선택.
    - `[MASK]` 토큰으로 치환 (80%)  
    - 랜덤 토큰으로 치환 (10%)  
    - 그대로 유지 (10%)
- 모델은 마스크된 단어에만 집중하지 않고,  
  다양한 문맥 표현을 학습해 **강건한(robust)** 표현을 얻는다.

---

## BERT의 학습 과정 예시

- 입력 토큰 중 일부를 `[MASK]`로 치환한 후,  
  마스크된 위치의 단어를 예측한다.
- 출력 단어 분포에서 가장 높은 확률을 가진 단어를 정답으로 판단한다.

# 2. Encoder 모델

---

## BERT의 학습 방법 2 - Next Sentence Prediction (NSP)

- BERT는 입력을 두 개의 연속된 텍스트로 받아,  
  두 번째 문장이 첫 번째 문장의 실제 다음 문장인지 여부를 예측하는 **Next Sentence Prediction (NSP)** 을 수행한다.

---

### NSP의 목적과 예시

- NSP를 통해 **문장 간 관계를 학습**하여 문맥적 추론 및 문장 수준 이해 태스크에 도움을 주도록 설계되었다.

**예시:**
- 자연어 추론 (Natural Language Inference)
- Paraphrase detection
- 질의응답 (Question Answering)

**입력 예시:**
```
Input = [CLS] the man went to [MASK] store [SEP]
        he bought a gallon [MASK] milk [SEP]
Label = IsNext

Input = [CLS] the man [MASK] to the store [SEP]
        penguin [MASK] are flight ##less birds [SEP]
Label = NotNext
```

---

### NSP 예측 과정

- 두 문장 \(A, B\)의 연속 관계를 예측한다.  
- BERT는 `[CLS]` 토큰의 출력을 FFNN + Softmax에 통과시켜  
  두 문장이 연결되는 확률을 계산한다.

---

## BERT의 다운스트림 태스크

- BERT는 **MLM**과 **NSP** 두 가지 태스크를 동시에 학습한다.  
- `[CLS]` 토큰은 NSP 태스크 용도로 학습되고,  
  다른 토큰들은 MLM 태스크 용도로 학습된다.

---

## BERT의 다운스트림 태스크 - Sentence Level

### ① 두 문장 관계 분류 태스크
- **MNLI**
  - 전제(Premise): 여러 남자들이 뛰고 있는 축구 경기.  
  - 가설(Hypothesis): 몇몇 남자들이 스포츠를 하고 있다.  
  - 분류: {합의(Entailment), 모순(Contradiction), 중립(Neutral)}

- **QQP (Quora Question Pairs)**
  - Q1: 주식 투자 방법은 어디서 배울 수 있나요?  
  - Q2: 주식에 대해 더 배우려면 어떻게 해야 하나요?  
  - 분류: {중복(Duplicate), 비중복(Not Duplicate)}

---

### ② 단일 문장 분류 태스크
- **SST2**
  - 문장: “이 영화에는 재미있는 요소들이 풍부하다.”
  - 분류: {긍정(Positive), 부정(Negative)}

---

## BERT의 다운스트림 태스크 - Token Level

### ① QA 태스크 (Question Answering)
- **SQuAD Dataset**
  - 질문: 뉴욕 자이언츠와 뉴욕 제츠는 뉴욕시의 어느 경기장에서 경기를 하나요?  
  - 문맥: 두 팀은 뉴저지 이스트 러더퍼드에 있는 Metlife Stadium에서 홈 경기를 한다.  
  - 정답: **Metlife Stadium**

---

### ② 개체명 인식 (Named Entity Recognition, NER)
- **CoNLL 2003 NER**
  - 문장: `John Smith lives in New York`  
  - 라벨:
    - John → B-PER (사람 이름의 첫 단어)  
    - Smith → I-PER (사람 이름의 나머지 단어)  
    - lives → O (개체명이 아닌 단어)  
    - in → O (개체명이 아닌 단어)  
    - New → B-LOC (장소 이름의 첫 단어)  
    - York → I-LOC (장소 이름의 나머지 단어)

---

## BERT의 결과

- BERT는 다양한 태스크에 적용 가능한 **범용성**을 보여주었으며,  
  Fine-tuning을 통해 여러 NLP 과제에서 **SOTA (최첨단 성능)** 을 달성하였다.

| System | MNLI-(m/mm) | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE | Average |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Pre-OpenAI SOTA | 80.6 / 80.1 | 66.1 | 82.3 | 93.2 | 35.0 | 81.0 | 86.0 | 61.7 | 74.0 |
| BiLSTM + ELMo + Attn | 76.4 / 76.1 | 64.8 | 79.8 | 90.4 | 36.0 | 73.3 | 84.9 | 56.8 | 71.0 |
| OpenAI GPT | 82.1 / 81.4 | 70.3 | 87.4 | 91.3 | 45.4 | 80.0 | 82.3 | 56.0 | 75.1 |
| **BERT_BASE** | **84.6 / 83.4** | **71.2** | **90.5** | **93.5** | **52.1** | **85.8** | **88.9** | **66.4** | **79.6** |
| **BERT_LARGE** | **86.7 / 85.9** | **72.1** | **92.7** | **94.9** | **60.5** | **86.5** | **89.3** | **70.1** | **82.1** |

- 대표적 평가 태스크:
  - **QQP:** 문장 중복 탐지  
  - **QNLI:** 자연어 추론  
  - **SST-2:** 감정 분석  
  - **CoLA:** 문법적 적절성 판단  
  - **STS-B:** 문장 의미 유사도  
  - **MRPC:** 문장 패러프레이즈  
  - **RTE:** 자연어 추론(소규모 데이터)

## 2. Encoder 모델

### 📘 BERT의 결과
- Layer의 수, hidden state의 크기, attention head의 수가 클수록 성능이 향상되는 경향을 보였다.

| Hyperparams | Dev Set Accuracy |
|--------------|------------------|
| #L | #H | #A | LM (ppl) | MNLI-m | MRPC | SST-2 |
| 3 | 768 | 12 | 5.84 | 77.9 | 79.8 | 88.4 |
| 6 | 768 | 3 | 5.24 | 80.6 | 82.2 | 90.7 |
| 6 | 768 | 12 | 4.68 | 81.9 | 84.8 | 91.3 |
| 12 | 768 | 12 | 3.99 | 84.4 | 86.7 | 92.9 |
| 12 | 1024 | 16 | 3.54 | 85.7 | 86.9 | 93.3 |
| 24 | 1024 | 16 | 3.23 | 86.6 | 87.8 | 93.7 |

---

### 📘 BERT의 한계
- 인코더 기반 모델인 **BERT**는 주어진 입력을 잘 이해하도록 학습되지만, 시퀀스를 생성해야 하는 태스크에는 적합하지 않다.  
  (예시: 기계 번역, 텍스트 생성 등)
- 생성 태스크에서는 **autoregessive**하게, 즉 한 번에 한 단어씩 생성해야 하는데,  
  이를 자연스럽게 수행하지 못하기 때문에 생성 태스크에는 **디코더 기반 모델**을 주로 사용한다.

---

## 3. Encoder-Decoder 모델

### 📗 인코더-디코더 모델
- **Encoders**
  - 양방향 문맥을 활용할 수 있다.
  - 학습하기 위한 훈련 방법은?
- **Encoder-Decoders**
  - Encoder와 Decoder의 장점을 모두 결합했다.
  - 효과적인 사전학습 방법은?
- **Decoders**
  - 전형적인 언어 모델 구조
  - 문장 생성에 유용 (미래 단어 참조 불가)

---

### 📗 T5 (Text-to-Text Transfer Transformer)
- **T5**는 2019년 Google Research에서 공개한 모델로 Transformer Encoder-Decoder 구조 기반의 모델이다.
- 모든 태스크를 **Text-to-Text** 포맷으로 변환해 하나의 모델로 학습한다.

📄 예시 논문: *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (Raffel et al., 2019)*

---

### 📗 T5의 학습 방법 – Span Corruption
- Encoder-Decoder 구조에서는 Encoder가 입력 문장을 모두 보고, 그 정보를 바탕으로 Decoder가 출력을 생성한다.
- 따라서 학습을 위해 **Span Corruption**이라는 과정을 수행한다.

📌 과정:
- 입력 문장에서 연속된 토큰을 무작위로 선택해 제거  
- 제거된 부분을 특수 placeholder 토큰으로 치환 (예: `<X>`, `<Y>`)  
- 디코더는 이 placeholder에 해당하는 원래 span을 복원하도록 학습  

👉 이를 통해 **언어 모델링처럼 훈련**을 수행할 수 있다.

---

### 📗 T5의 다운스트림 태스크
- T5는 **NLU (GLUE, SuperGLUE)**, **QA (SQuAD)**, **요약 (CNN/DM)**, **번역 (En→De, En→Fr, En→Ro)** 등의 태스크에서 모두 좋은 성능을 보여  
  **범용적으로 활용될 수 있는 모델임을 입증**하였다.

| Architecture | Objective | Params | Cost | GLUE | CNNDM | SQuAD | SGLUE | EnDe | EnFr | EnRo |
|---------------|------------|---------|------|-------|--------|--------|--------|-------|-------|-------|
| Encoder-decoder | Denoising | 2P | M | 83.28 | 19.24 | 80.88 | 71.36 | 26.98 | 39.82 | 27.65 |

---

## 4. Decoder 모델

### 📘 Decoder 모델
- **Encoders**
  - 양방향 문맥을 활용할 수 있다.
  - 학습하기 위한 훈련 방법은?
- **Encoder-Decoders**
  - Encoder와 Decoder의 장점을 모두 결합했다.
  - 효과적인 사전학습 방법은?
- **Decoders**
  - 전형적인 언어 모델 구조
  - 문장 생성에 유용 (미래 단어 참조 불가)

---

### 📘 Finetuning Decoder
- Transformer의 Decoder는 사전학습 단계에서 **다음 단어 예측 (Next Token Prediction)** 을 학습한다.

#### ✅ 생성 태스크에 활용할 때:
- 사전학습 때와 동일하게 **다음 단어 예측 방식**으로 fine-tuning한다.  
- 따라서 decoder는 대화나 요약 태스크 등 **출력이 시퀀스인 태스크에 자연스럽게 적합**하다.

#### ✅ 분류 태스크에 활용할 때:
- 마지막 hidden state 위에 새로운 **linear layer**를 연결해 **classifier**로 사용한다.  
- 이때, linear layer는 아예 처음부터 다시 학습해야 하며,  
  fine-tuning 시 gradient가 decoder 전체로 전파된다.

## 4. Decoder 모델

### GPT-1
- GPT-1은 2018년 OpenAI에서 공개한 Transformer 기반의 Decoder 모델이다.
- Autoregressive LM (왼쪽 → 오른쪽 단어 예측) 방식으로 사전학습 되었다.

---

### GPT-1의 fine-tuning 방법 (분류 태스크)
- GPT-1은 다음 단어 예측이라는 언어모델의 학습 목표를 최대한 유지하면서, fine-tuning을 수행했다.

- NLI (두 문장을 입력 받아 관계를 함의(entailment) / 모순(contradiction) / 중립(neutral) 중 하나로 분류):
  - 전제(Premise): The man is in the doorway.
  - 가설(Hypothesis): The person is near the door.
  - ➜ Entailment

- 입력 토큰에 특수한 토큰([START], [DELIM], [EXTRACT])을 붙여 분류 문제를 처리했고,  
  [EXTRACT] 위치의 hidden state에 classifier를 연결해 사용했다.

[START] The man is in the doorway [DELIM] The person is near the door [EXTRACT]

---

### GPT-1의 fine-tuning 방법 (분류 태스크)
Classification: Start – Text – Extract → Transformer → Linear  
Entailment: Start – Premise – Delim – Hypothesis – Extract → Transformer → Linear  
Similarity: Start – Text1 – Delim – Text2 – Extract (또는 반대) → Transformer → Linear  
Multiple Choice: Start – Context – Delim – AnswerN – Extract → Transformer → Linear

---

### GPT-1의 결과
- GPT-1은 생성 태스크를 잘 수행했을 뿐만 아니라,  
  태스크 별 fine-tuning을 통해 분류/추론 등 이해 중심 태스크에서도 우수한 성능을 보였다.

| Method | MNLI-m | MNLI-mm | SNLI | SciTail | QNLI | RTE |
|---------|---------|----------|------|----------|------|------|
| ESIM + ELMo | - | - | 89.3 | - | - | - |
| CAFE | 80.2 | 79.0 | 89.3 | - | - | - |
| SAN | 80.6 | 80.1 | - | - | - | - |
| CAFE | 78.7 | 77.9 | 88.5 | 83.3 | - | - |
| GenSen | 71.4 | 71.3 | - | - | 82.3 | 59.2 |
| Multi-task BiLSTM + Attn | 72.2 | 72.1 | - | - | 82.1 | 61.7 |
| Finetuned Transformer LM (ours) | 82.1 | 81.4 | 89.9 | 88.3 | 88.1 | 56.0 |

---

### GPT-2
- GPT-2는 GPT-1의 확장 버전으로 2019년 OpenAI에서 공개된 모델이다.
- GPT-1에 비해 더 많은 데이터와 더 큰 parameter size로 학습되었으며,
  이를 통해 더 자연스러운 텍스트 생성 능력을 보여주었다.

---

## 5. In-Context Learning

### GPT-3
- GPT-3는 2020년 OpenAI에서 공개한 모델로,
  GPT-2에서 모델의 parameter size를 키워 (1750억 개),
  별도의 파인튜닝 없이 컨텍스트 안의 예시만 보고도 새로운 태스크를 수행할 수 있게 되었다.
- 이런 능력을 In-Context Learning이라고 한다.

---

### GPT-3 - In-Context Learning
- 모델에 예시와 함께 어떤 태스크를 할 지 지정해주면,
  모델이 그 패턴을 따라가는 식으로 동작하면서, 완벽하지 않지만 그럴듯하게 태스크를 수행하는 모습을 보인다.

입력:
"thanks → merci  
hello → bonjour  
mint → menthe  
otter →"

출력:
"loutre..."

---

### GPT-3 - In-Context Learning
#### Zero-shot
The model predicts the answer given only a natural language description of the task.  
No gradient updates are performed.

Translate English to French:  
cheese =>

#### One-shot
In addition to the task description, the model sees a single example of the task.  
No gradient updates are performed.

Translate English to French:  
sea otter => loutre de mer  
cheese =>

#### Few-shot
In addition to the task description, the model sees a few examples of the task.  
No gradient updates are performed.

Translate English to French:  
sea otter => loutre de mer  
peppermint => menthe poivrée  
plush giraffe => girafe peluche  
cheese =>

---

### GPT-3 - In-Context Learning
- 이러한 능력은 모델의 크기, 즉 parameter size가 커질수록 더 강력하게 나타났으며,
  zero-shot, one-shot, few-shot 모두에서 일관된 성능 개선이 관찰되었다.

## 5. In-Context Learning

### GPT-3 - In-Context Learning
- 또한, 모든 parameter size의 모델에서, shot의 수가 많을수록 태스크 수행 성능이 향상되었다.
- Zero-shot < One-shot < Few-shot

---

### Chain-of-Thought prompting
- In-Context Learning의 발견으로 인해, Prompt의 중요성이 대두되었다.
- 하지만 단순한 Few-shot prompting만으로는 여러 스텝을 거쳐야 하는 문제들을 풀기 어려웠는데, 이를 해결하기 위해 Chain-of-Thought (CoT) prompting 방식이 등장했다.
- CoT prompting은 모델이 문제 해결 과정에서 논리적인 사고 단계를 거쳐 최종 답을 도출하도록 유도하는 prompting 기법이다.

질문: 민지는 4월에 친구 48명에게 연필을 팔았고, 5월에는 그 절반만큼의 연필을 팔았다.  
민지가 4월과 5월에 모두 판매한 연필은 몇 자루인가?

---

### Chain-of-Thought prompting 예시
#### Standard Prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls.  
How many tennis balls does he have now?  
A: The answer is 11.

Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more,  
how many apples do they have?  
A: The answer is 27. ❌

#### Chain-of-Thought Prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls.  
How many tennis balls does he have now?  
A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls.  
5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more,  
how many apples do they have?  
A: The cafeteria had 23 apples originally. They used 20 to make lunch,  
so they had 23 - 20 = 3. They bought 6 more apples,  
so they have 3 + 6 = 9. The answer is 9. ✅

---

### Chain-of-Thought prompting 결과
- CoT prompting은 일반적인 prompt 방식보다 훨씬 우수한 성능을 보이며,  
  새로운 SOTA(State-Of-The-Art) 성과를 달성하였다.
- 심지어, fine-tuning을 수행한 모델들보다도 더 좋은 성능을 보였다.

| 모델 | 방식 | Solve Rate (%) |
|------|------|----------------|
| Finetuned GPT-3 175B | - | 33 |
| Prior best | - | 55 |
| PaLM 540B | standard prompting | 18 |
| PaLM 540B | chain-of-thought prompting | 57 |

---

### Zero-Shot Chain-of-Thought prompting
- 하지만 기존 CoT Prompting은 few-shot 예시가 필요하다.  
  예시가 없을 경우, 추론 과정이 나타나지 않아 성능 저하가 발생하게 된다.
- 이를 보완하기 위해, 질문 뒤에 “Let’s think step by step”이라는 문장을 추가해  
  모델이 스스로 추론 단계를 생성하도록 유도하는 Zero-Shot CoT prompting 방법이 등장했다.

Q: A juggler can juggle 16 balls. Half of the balls are golf balls,  
and half of the golf balls are blue. How many blue golf balls are there?  
A: Let’s think step by step.  
(Output) There are 16 balls in total. Half of the balls are golf balls.  
That means there are 8 golf balls. Half of the golf balls are blue.  
That means there are 4 blue golf balls. ✅

---

### Zero-Shot Chain-of-Thought prompting 성능 비교
- Zero-Shot CoT prompting을 통해, 별도의 예시 없이도  
  Few-Shot CoT에 견줄 만한 성능을 달성하였다.

| Model / Method | MultiArith | GSM8K |
|----------------|-------------|--------|
| Zero-Shot | 17.7 | 10.4 |
| Few-Shot (2 samples) | 33.7 | 15.6 |
| Few-Shot (8 samples) | 33.8 | 15.6 |
| Zero-Shot-CoT | 78.7 | 40.7 |
| Few-Shot-CoT (2 samples) | 84.8 | 41.3 |
| Few-Shot-CoT (4 samples : First) | 89.2 | - |
| Few-Shot-CoT (4 samples : Second) | 90.5 | - |
| Few-Shot-CoT (8 samples) | 93.0 | 48.7 |
| Zero-Plus-Few-Shot-CoT (8 samples) | 92.8 | 51.5 |
| Finetuned GPT-3 175B [Wei et al., 2022] | - | 33 |
| Finetuned GPT-3 175B + verifier [Wei et al., 2022] | - | 55 |
| PaLM 540B: Zero-Shot | 25.5 | 12.5 |
| PaLM 540B: Zero-Shot-CoT | 66.1 | 43.0 |
| PaLM 540B: Zero-Shot-CoT + self consistency | 89.0 | 70.1 |
| PaLM 540B: Few-Shot [Wei et al., 2022] | - | 17.9 |
| PaLM 540B: Few-Shot-CoT [Wei et al., 2022] | - | 56.9 |
| PaLM 540B: Few-Shot-CoT + self consistency [Wang et al., 2022] | - | 74.4 |

---

### 마무리
**감사합니다.**