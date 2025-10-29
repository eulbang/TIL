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

# 2. 거대 언어 모델의 학습

## GPT-3: “거대 언어 모델의 시초”
- 가장 큰 버전의 GPT-3: **1750억 개의 매개변수(Parameters)**  
  → 이전 언어 모델 대비 최소 10배 이상 큰 모델  
- 본격적으로 **인-컨텍스트 학습(In-context learning)** 능력이 나타나기 시작한 언어 모델

출처: https://medium.com/analytics-vidhya/openai-gpt-3-language-models-are-few-shot-learners-82531b3d3122

---

### 학습 방법 및 비용
- **학습 방법:** 다음 토큰 예측 (Next token prediction)  
- **학습 데이터:** 약 3000억 토큰 (4TB 텍스트 데이터 = 인터넷 + 양질의 텍스트북)  
- **학습 비용:** 약 **150억 원 수준**으로 추산  

#### GPT-3 모델 구성 요약
| Model | Parameters | Layers | Hidden Size | Attention Heads |
|--------|-------------|---------|--------------|----------------|
| GPT-3 Small | 125M | 12 | 768 | 12 |
| GPT-3 Medium | 350M | 24 | 1024 | 16 |
| GPT-3 Large | 760M | 24 | 1536 | 16 |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 |
| GPT-3 13B | 13.0B | 40 | 5140 | 40 |
| **GPT-3 175B** | **175.0B** | **96** | **12288** | **96** |

#### 학습 데이터 구성
| Dataset | Quantity (Tokens) | 비중(%) |
|----------|------------------|----------|
| Common Crawl (filtered) | 410B | 60 |
| WebText2 | 19B | 22 |
| Books1 | 12B | 8 |
| Books2 | 55B | 8 |
| Wikipedia | 3B | 3 |

출처: Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020

---

## 다음 토큰 예측 기반 거대 언어 모델의 한계
- 사람의 지시에 대해 **올바르지 않은 응답**을 생성하거나,  
  **유해한 응답**을 생성할 수 있음.

예시:
- GPT-3: 엉뚱한 내용 생성 (문맥 무관한 문장 나열)
- GPT-4: 유해한 지시에 대해 실행 방법을 제시하는 오류 발생

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022  
Wei et al., *Jailbroken: How Does LLM Safety Training Fail?*, NeurIPS 2023

---

## 정렬(Alignment) 학습
> 거대 언어 모델의 출력이 사용자의 **의도와 가치**를 반영하도록 학습

- (1) **지시 학습 (Instruction tuning)**: 주어진 지시에 대해 어떤 응답이 생성되어야 하는지 학습  
- (2) **선호 학습 (Preference learning)**: 상대적으로 어떤 응답이 더 선호되어야 하는지 학습  

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022  
Wei et al., *Jailbroken*, NeurIPS 2023

---

# 2-1. 지시 학습 (Instruction Tuning)

## 지시 학습의 개념
> 주어진 지시에 대해 어떤 응답이 생성되어야 하는지를 학습

- 학습 방법 자체는 기존 언어 모델 (예: BERT) 에서의 **지도 학습(Supervised Fine-Tuning, SFT)** 과 동일  
- 기존 언어 모델은 각 테스크마다 별도의 **추가 학습 및 모델 저장** 필요

예시:
> “전체적으로, 두 시간 동안 영화를 보는 것에서 얻은 가치는 팝콘과 음료의 합계였습니다. 영화는 정말 끔찍했습니다.”  
→ 출력: **0 (부정적)**

---

## 지시 학습 (Instruction tuning): 주어진 지시에 대해 어떤 응답이 생성되어야 하는지
- **Idea:** 모든 자연어 테스크는 텍스트 기반 지시(instruction)와 응답으로 표현할 수 있지 않을까?

예시:
- 감정 분석: “주어진 리뷰 속 유저의 감정이 긍정적이야, 부정적이야?”
- 번역: “주어진 문장을 영어로 번역해줘.”

입력:  
> 지시: “주어진 리뷰 속 유저의 감정이 긍정적이야, 부정적이야?”  
> 리뷰: “전체적으로, 두 시간 동안 영화를 보는 것에서 얻은 가치는 팝콘과 음료의 합계였습니다. 영화는 정말 끔찍했습니다.”  

출력:  
> “부정적으로 보입니다.”

출처: SSAFY 텍스트 파운데이션 모델 강의 슬라이드

# 2-1. 지시 학습

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 학습 방법: 주어진 입력을 받아서 이에 대한 응답을 따라 하도록 지도 추가 학습 (Supervised Fine-Tuning, SFT)
- (A) Pretrain–finetune (BERT, T5)
  - Typically requires many task-specific examples
  - One specialized model for each task
- (B) Prompting (GPT-3)
  - Improve performance via few-shot prompting or prompt engineering
- (C) Instruction tuning (FLAN)
  - Model learns to perform many tasks via natural language instructions
  - Inference on unseen task
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 학습 데이터의 다양성 증대를 위해, 각 테스크를 다양한 지시(템플릿)로 표현할 수 있음
- Premise  
  `Russian cosmonaut Valery Polyakov set the record for the longest continuous amount of time spent in space, a staggering 438 days, between 1994 and 1995.`
- Hypothesis  
  `Russians hold the record for the longest stay in space.`
- Target  
  `Options: - yes  - no`
- Template 예시
  - Template 1: Based on the paragraph above, can we conclude that `<hypothesis>`?
  - Template 2: Can we infer the following? `<hypothesis>`
  - Template 3: Read the following and determine if the hypothesis can be inferred from the premise  
    Premise: `<premise>`  
    Hypothesis: `<hypothesis>`  
    `<options>`
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 기존 NLP 테스크 데이터를 지시 학습을 위한 데이터로 수정하여 학습 및 테스트에 활용
- 학습시에 보지 못한 지시에 대한 일반화 성능 평가를 위해, 관련 없는 테스크들을 테스트에 별도로 활용
  - 예시: 요약(`summarization`)을 테스트 때의 테스크로 활용하기 위해, 학습 시에는 제거
- 주요 데이터셋
  - Natural language inference (7): ANLI(R1-R3), CB, MNLI, QNLI, RTE, SNLI, WNLI  
  - Commonsense (4): CoPA, HellaSwag, PiQA, StoryCloze  
  - Sentiment (4): IMDB, Sent140, SST-2, Yelp  
  - Paraphrase (4): MRPC, QQP, PAWS, STS-B  
  - Closed-book QA (3): ARC(easy/chal.), NQ, TQA  
  - Struct to text (4): CommonGen, DART, E2ENLG, WEBNLG  
  - Translation (8): ParaCrawl EN/DE, EN/ES, EN/FR, WMT-16 EN/CS, EN/DE, EN/FI, EN/RO, EN/RU, EN/TR  
  - Reading comp. (5): BoolQ, DROP, MultiRC, OBQA, SQuAD  
  - Read. comp. w/ commonsense (2): CosmosQA, ReCoRD  
  - Coreference (3): DPR, Winogrande, WSC273  
  - Misc. (7): CoQA, QuAC, WIC, Math, Fix Punctuation(NLG), TREC, CoLA  
  - Summarization (11): AESLC, AG News, CNN-DM, Gigaword, Multi-News, Newsroom, SamSum, Wiki Lingua EN, XSum, Opin-Abs: iDebate, Opin-Abs: Movie
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 실험 결과: 예시 없이도 (`0-shot`) 새로운 지시에 대해 올바른 응답을 내놓는 성능이 크게 증가!
- `LaMDA-PT 137B`는 구글의 당시 기준 `SOTA` 텍스트 파운데이션 모델을 추가 학습
- 주요 비교 대상: FLAN 137B, LaMDA-PT137B, GPT-3 175B, GLAM 64B/64E, Supervised model
- Natural language inference: ANLI R1-R3, CB, RTE  
- Reading comprehension: MultiRC, OBQA, BoolQ  
- Closed-book QA: NQ, ARC-C, TQA, ARC-e  
- Translation: EN↔RO, EN↔DE, EN↔FR  
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 파운데이션 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN or T0)
- 실험 결과: 성능 향상을 위한 핵심 요소는 다음과 같음
  1. 학습 테스크의 개수: 다양한 종류의 지시를 학습할수록 보지 못한 지시에 대한 일반화 성능이 좋아짐
  2. 추가 학습하는 모델의 크기: 특정 규모 이하에서는 지시 학습의 효과성이 떨어짐 → 지시를 이해하고 응답하는 것도 창발성의 하나
  3. 지시를 주는 방법: 자연어 지시로 사람에게 대화하듯 지시하는 것이 가장 효과적
- 성능 비교  
  - Held-out clusters: CommonSense / Average NLI / Closed-book QA  
  - FT: instruction / Eval: instruction (FLAN) → `55.2`  
  - FT: dataset name / Eval: instruction → `46.6`  
  - FT: dataset name / Eval: dataset name → `47.0`  
  - FT: no instruction → `37.3`
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

# 2-2. 선호 학습 (Preference Learning)

## 지시 학습의 한계: 주어진 입력에 대해 적절한 하나의 응답이 있다고 가정
- 이는 정답이 정해져 있는 객관적 테스트 (e.g. 수학) 에서는 자연스러움  
  - `Question`: 양의 정수 m과 n의 최대공약수는 6이고, 최소공배수는 126이다. 이때 m + n의 가능한 최소값은 얼마인가?  
  - `Answer`: 60
- 출처: Cobbe et al., *Training Verifiers to Solve Math Word Problems*, OpenAI

## 지시 학습의 한계: 주어진 입력에 대해 적절한 하나의 응답이 있다고 가정
- 이는 정답이 정해져 있는 객관적 테스트 (e.g. 수학)에서는 자연스러움
- 그러나, 정답이 정해져 있지 않은 개방형(Open-ended) 테스트 (e.g. 번역)에서는 한계가 있음
  - Goal: 단순히 복수 정답을 허락하는 대신, 더 좋은(선호되는) 응답을 생성하도록 하고 싶음
- 예시 (번역)
  - 입력:  
    `When I am down and, oh my soul, so weary  
    When troubles come and my heart burdened be  
    Then, I am still and wait here in the silence  
    Until you come and still awhile with me`
  - 출력 1:  
    `내가 우울하고, 아, 내 영혼이 너무 지쳤을 때  
    고난이 닥치고 내 마음이 무거워질 때  
    그때, 나는 조용히 기다리며 이 침묵 속에 머물러 있네  
    당신이 오셔서 나와 함께 잠시 머물러 주실 때까지`
  - 출력 2:  
    `내 마음이 지치고 영혼마저 무거울 때  
    근심이 찾아와 가슴이 짓눌릴 때  
    나는 잠잠히 이곳에서 기다리네  
    그대가 와서 잠시 곁에 머물러 주기를`
- 출처: Cobbe et al., *Training Verifiers to Solve Math Word Problems*, OpenAI

## 선호 학습 (Preference Learning)
- 다양한 응답 중 사람이 더 선호하는 응답을 생성하도록 추가학습
- 다양한 응답은 모델이 생성, 응답 간의 선호도는 사람이 제공
- ChatGPT를 만들기 위한 핵심 알고리즘!
  - 공식 문서는 공개되어 있지 않지만, 아래와 같은 힌트가 공식 블로그에 제공되어 있음
- 인용:
```
We trained this model using Reinforcement Learning from Human Feedback (RLHF),
using the same methods as InstructGPT,
but with slight differences in the data collection setup.
We trained an initial model using supervised fine-tuning:
human AI trainers provided conversations in which they played both sides—the user and an AI assistant.
We gave the trainers access to model-written suggestions to help them compose their responses.
We mixed this new dialogue dataset with the InstructGPT dataset,
which we transformed into a dialogue format.
```
- 출처: https://openai.com/index/chatgpt/

# 2-2. 선호 학습

## 선호 학습 (Preference Learning): 다양한 응답 중 사람이 더 선호하는 응답을 생성하도록 추가학습
- InstructGPT의 핵심 아이디어:
  - 사람의 피드백을 통한 강화학습 (Reinforcement Learning from Human Feedback, RLHF)
  - 사람의 피드백 := 응답에 대한 선호도
- Step 1: Collect demonstration data, and train a supervised policy.
- Step 2: Collect comparison data, and train a reward model.
- Step 3: Optimize a policy against the reward model using reinforcement learning.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 1. 지시 학습을 통한 텍스트 파운데이션모델(e.g. GPT-3)의 추가 학습
- 실제 유저로부터 다양한 지시 입력을 수집하고, 해당 입력에 대해 훈련된 사람 주석자들이 정답 데이터를 생성
- Step 1: Collect demonstration data, and train a supervised policy.
  - A prompt is sampled from our prompt dataset.
  - A labeler demonstrates the desired output behavior.
  - This data is used to fine-tune GPT-3 with supervised learning.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 2. 사람의 선호 데이터를 수집하여, 보상 모델(Reward model, RM)을 학습
- 주어진 입력에 대한 선택지는 모델이 생성, 다양한 선택지에 대한 선호도는 사람이 생성
- 사람과 일치한 선호도를 출력할 수 있도록 보상 모델을 지도 학습
  - 사람이 선호하는 응답이 입력으로 주어짐 → 높은 보상을 출력
- Step 2: Collect comparison data, and train a reward model.
  - A prompt and several model outputs are sampled.
  - A labeler ranks the outputs from best to worst.
  - This data is used to train our reward model.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 2. 사람의 선호 데이터를 수집하여, 보상 모델(Reward model, RM)을 학습
- 주어진 입력에 대한 선택지는 모델이 생성, 다양한 선택지에 대한 선호도는 사람이 생성
- 사람과 일치한 선호도를 출력할 수 있도록 보상 모델을 지도 학습
  - 사람이 선호하는 응답이 입력으로 주어짐 → 높은 보상을 출력
- 예시
  - 선택지 A: Explain gravity... → Reward: `-5`
  - 선택지 D: People went to the moon... → Reward: `100`
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 3. 보상이 높은 응답을 생성하도록 강화 학습을 통해 추가 학습
- 핵심: Step 1 & 2에서 보지 못한 질문에 대해 사람의 추가적인 개입 없이 학습된 모델들을 통해 추가 학습이 진행
- 지시 학습된 모델을 보상 모델 기반 강화 학습을 통해 한 번 더 추가 학습
- Step 3: Optimize a policy against the reward model using reinforcement learning.
  - A new prompt is sampled from the dataset.
  - The policy generates an output.
  - The reward model calculates a reward for the output.
  - The reward is used to update the policy using PPO.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 결과: 유저의 지시를 얼마나 잘 수행하는지를 사람이 직접 평가
- 단순 프롬프팅이나 지시 학습에 비해 발전된 지시 수행능력을 보여줌
  - InstructGPT: Likert score 5점대
  - Supervised Fine-Tuning: 4점대
  - GPT (prompted): 3점대
  - GPT: 2점대
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 결과: 얼마나 안전한 응답을 생성하는지 평가
- 기존 대비, InstructGPT는 해로운 응답(RealToxicity)과 거짓말(TruthfulQA, Hallucinations)을 덜 생성
  - RealToxicity  
    GPT: `0.233`  
    SFT: `0.199`  
    InstructGPT: `0.196`
  - TruthfulQA  
    GPT: `0.224`  
    SFT: `0.206`  
    InstructGPT: `0.413`
  - Hallucinations  
    GPT: `0.414`  
    SFT: `0.078`  
    InstructGPT: `0.172`
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## LLaMA2
- InstructGPT와 비슷하게 RLHF와 대화 데이터를 활용한 LLaMA2 Chat 모델을 공개
  - LLaMA1 때에는 사전 학습된 모델만 공개
- 구성
  - Human feedback: Human preference data → Helpful & Safety Reward Model 생성
  - Fine-tuning: RLHF, Rejection Sampling, Proximal Policy Optimization
  - Pretraining: Self-supervised learning 기반 LLaMA2 학습
  - 최종 모델: LLaMA-2-chat
- 출처: Touvron et al., *Llama 2: Open Foundation and Fine-Tuned Chat Models*, Meta AI

## LLaMA2
- InstructGPT와 비슷하게 RLHF와 대화 데이터를 활용한 LLaMA2 Chat 모델을 공개
- 당시 대화형 타입 개방형 거대 언어 모델 중 가장 우수한 성능을 보여줌
- 성능 비교 (% Win Rate)
  - LLaMA-2-70b-chat vs ChatGPT-0301 → Win: `35.9`, Tie: `31.5`, Loss: `32.5`
  - LLaMA-2-70b-chat vs PaLM-Bison → Win: `53.0`, Tie: `24.6`, Loss: `22.4`
  - LLaMA-2-34b-chat vs Falcon-40b-instruct → Win: `76.3`, Tie: `14.6`, Loss: `9.1`
  - LLaMA-2-34b-chat vs Vicuna-33b-v1.3 → Win: `37.2`, Tie: `31.2`, Loss: `31.2`
  - LLaMA-2-13b-chat vs Vicuna-13b-v1.1 → Win: `45.4`, Tie: `29.8`, Loss: `24.9`
  - LLaMA-2-7b-chat vs MPT-7b-chat → Win: `61.1`, Tie: `20.9`, Loss: `18.0`
- 출처: Touvron et al., *Llama 2: Open Foundation and Fine-Tuned Chat Models*, Meta AI

# 3. 거대 언어 모델의 추론

57p 부터