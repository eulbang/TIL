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

# 3-1. 디코딩 (Decoding) 알고리즘

## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- 학습이 완료된 거대 언어 모델은 어떻게 응답을 생성할까? ⇒ 순차적 추론을 통한 “토큰별 생성”

출처 : https://jalammar.github.io/illustrated-transformer/


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Q. 언제 추론 및 토큰 생성을 멈추고 응답을 제공?  
  A. EOS 토큰 생성 시 종료 or 사전에 정의된 토큰 수 도달 시 종료  
  - E.g. `[SEP]`: BERT에서 사용된 EOS (End Of Sentence) 토큰

1. 원문 텍스트 입력  
   ````python
   text = "Tokenizing text is a core task of NLP."
   encoded_text = tokenizer(text)
   ````

2. 토큰 ID 시퀀스  
   ````python
   {'input_ids': [101, 19204, 6026, 3793, 2003, 1037, 4563, 4708, 1997, 17953, 2361, 1012, 102],}
   ````

3. 토큰 문자열 리스트  
   ````python
   ['[CLS]', 'token', '##izing', 'text', 'is', 'a', 'core', 'task', 'of', 'nl', '##p', '.', '[SEP]']
   ````  
   → 문장 종료 표시 (EOS 토큰)

출처 : https://medium.com/@abdallahashraf90x/tokenization-in-nlp-all-you-need-to-know-45c00cfa2df7


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Goal: 주어진 입력 `x = [x₁, ..., x_L]` 에 대해 다음 토큰 `x_{L+1}` 을 생성  
  - Remark. 거대 언어 모델: 입력 `x`에 대해 다음 토큰에 대한 확률 분포 `p̂(x)`를 제공
- 디코딩(Decoding) 알고리즘: `p̂(x)`로부터 `x_{L+1}`을 생성하는 알고리즘 (다음 단어를 선택하는 방법)

`x = [x₁, x₂, x₃] = [아까, 밥, 먹고]`

단어 목록과 확률 예시  
왔군 - 0.06  
왔어 - 0.5  
왔는데 - 0.2  
왔거든 - 0.1

출처 : https://tilnote.io/books/6480b090e92fe5ef635f54df/6480a73ee92fe5ef635f4d77


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Pytorch 실제 예시

````python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

prompt = "Today I believe we can finally"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# generate up to 30 tokens
outputs = model.generate(input_ids, do_sample=False, max_length=30)
tokenizer.batch_decode(outputs, skip_special_tokens=True)
````

자동회귀 생성 파트  
출처 : https://huggingface.co/blog/introducing-csearch


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Pytorch 실제 예시

디코딩(Decoding) 알고리즘 종류:
- `greedy decoding` by calling `greedy_search()`  
- `contrastive search` by calling `contrastive_search()`  
- `multinomial sampling` by calling `sample()`  
- `beam-search decoding` by calling `beam_search()`  
- `beam-search multinomial sampling` by calling `beam_sample()`  
- `diverse beam-search` by calling `group_beam_search()`  
- `constrained beam-search decoding` by calling `constrained_beam_search()`

출처 : https://docs.pytorch.org/torchtune/0.3/generated/torchtune.generation.generate.html#torchtune.generation.generate


## 디코딩(Decoding) 알고리즘: ① Greedy Decoding
- 핵심 아이디어: 가장 확률이 높은 다음 토큰을 선택  
  - 장점: 사용하기 쉽다.  
  - 단점: 직후만 고려하기 때문에 생성 응답이 최종적으로 최선이 아닐 수 있다.

출처 : https://heidloff.net/article/greedy-beam-sampling/


## 디코딩(Decoding) 알고리즘: ② Beam Search
- 핵심 아이디어: 확률이 높은 k개(beam size)의 후보를 동시에 고려  
  - 고르는 기준: 누적 생성 확률(지금까지 생성된 문장 전체가 나올 확률의 곱)
  - 앞선 Greedy Decoding은 매 시점마다 가장 높은 확률의 선택지 1개만을 선택했지만,  
    Beam Search는 전체 문장 후보들의 누적 확률을 기준으로 상위 k개를 남기는 것

출처 : https://d2l.ai/chapter_recurrent-modern/beam-search.html


## 디코딩(Decoding) 알고리즘: ② Beam Search
- 핵심 아이디어: 확률이 높은 여러 후보를 동시에 고려  
  - 장점: 최종적으로 좋은 응답 생성 확률이 높다.  
  - 단점: 계산 비용이 많이 늘어난다(각 후보마다 LLM 추론을 수행).

예시 계산  
“The dog has” = 0.4 * 0.9 = 0.36  
“The nice woman” = 0.5 * 0.4 = 0.20

Greedy 방식의 경우 매번 가장 높은 확률을 계산해 “The nice woman…” 경로를 선택하지만  
Beam Search의 경우 전체 문장 후보의 누적 확률을 고려하여 “The dog has…” 경로를 선택함.

출처 : https://heidloff.net/article/greedy-beam-sampling/


## 디코딩(Decoding) 알고리즘: ③ Sampling
- 핵심 아이디어: 거대 언어 모델이 제공한 확률을 기준으로 랜덤하게 생성  
  - 장점: 다양한 응답을 생성할 수 있음.  
  - 단점: 생성된 응답의 품질이 감소할 수 있음.

단어 사전에 대해 정의된 확률 분포  
모델이 아는 모든 단어에 대해 ‘다음 단어가 될 확률’을 매겨 놓은 것

출처 : https://huyenchip.com/2024/01/16/sampling.html#constraint_sampling

# 3-1. 디코딩 (Decoding) 알고리즘

## 디코딩(Decoding) 알고리즘: ④ Sampling “with Temperature”
- 핵심 아이디어: 하이퍼 파라미터 `T`를 통해 거대 언어 모델이 생성한 확률 분포를 임의로 조작
  - `T > 1`: 확률 분포를 *Smooth*하게 만듦 (더 다양한 응답 생성)
  - `T < 1`: 확률 분포를 *Sharp*하게 만듦 (기존에 확률이 높은 응답에 집중)

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71

- `T < 1`: 확률 분포를 *Sharp*하게 만듦 (기존에 확률이 높은 응답에 집중)
  - 특정 후보(예: 9번 그래프)가 압도적으로 높은 확률을 갖고, 나머지는 매우 낮음
  - → 모델이 항상 비슷한 답(가장 높은 확률의 단어)만 내놓게 됨
  - * 안정적이나 다양성이 떨어짐

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71

- `T > 1`: 확률 분포를 *Smooth*하게 만듦 (더 다양한 응답 생성)
  - 분포가 평평해짐
  - 모든 단어가 거의 비슷한 확률로 선택될 수 있음.
  - → 모델이 예측할 때 다양성이 극대화되지만, 품질은 불안정해짐.
  - * 창의적이나 품질이 떨어질 수 있음.

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71


## 디코딩(Decoding) 알고리즘: ⑤ Top-K Sampling
- 핵심 아이디어: 확률이 높은 `K`개의 토큰들 중에서만 랜덤하게 확률에 따라 샘플링
  - 장점: 품질이 낮은 응답을 생성할 가능성을 줄일 수 있음

출처 : https://sooftware.io/generate/

- 단점: 확률 분포의 모양에 상관 없이 고정된 `K`개의 후보군을 고려

출처 : https://sooftware.io/generate/

- 문맥에 따라 다음 단어의 예측 확률 합이 다르다.
  - `Σ_{w ∈ V_top-K} P(w | “The”) = 0.68`
  - `Σ_{w ∈ V_top-K} P(w | “The”, “car”) = 0.99`

출처 : https://sooftware.io/generate/


## 디코딩(Decoding) 알고리즘: ⑥ Top-P Sampling (or Nucleus Sampling)
- 핵심 아이디어: `K`를 고정하는 대신, 누적 확률(`P`)에 집중하여 `K`를 자동으로 조절
  - 예시: `P = 0.9` → 확률이 높은 응답 후보의 확률을 더했을 때 `0.9`를 처음으로 초과하는 `K`를 사용

출처 : https://sooftware.io/generate/

- 핵심 아이디어: `K`를 고정하는 대신, 누적 확률(`P`)에 집중하여 `K`를 자동으로 조절
- 다양한 평가 지표에서 기존 디코딩 알고리즘들 대비 좋은 성능을 달성

출처 : Holtzman et al., The Curious Case of Neural Text Degeneration., ICLR 2020


## 디코딩(Decoding) 알고리즘 별 장단점 요약
- Greedy Decoding
  - 장점: 쉬운 사용법
  - 단점: 최적해 보장 `X`
- Beam Search
  - 장점: 좋은 응답 생성 확률 ↑
  - 단점: 큰 계산 비용
- Sampling
  - 장점: 다양한 응답 생성 가능
  - 단점: 품질 불안정
- Sampling with “Temperature”
  - 장점: 창의성/안정성 조절 가능
  - 단점: `T ↑` : 품질 저하 / `T ↓` : 다양성 부족
- Top-K Sampling
  - 장점: 잡음 단어 배제, 품질 향상
  - 단점: `K`값 고정 → 문맥 따라 불균형
- Top-P Sampling (Nucleus)
  - 장점: 확률 누적 기준, 품질·다양성 균형
  - 단점: `P`값 설정 필요 (경우에 따라 랜덤성 여전)

<표3-1_텍스트 파운데이션 모델_거대 언어 모델의 추론_디코딩 알고리즘 별 장단점 요약>

# 3-1. 디코딩(Decoding) 알고리즘
## 디코딩(Decoding) 알고리즘: 실제 예시 with ChatGPT
- **OpenAI Playground / 모델 설정창**
  - 이 값들을 조정하면서 앞서 나온 디코딩 알고리즘 값을 간접적으로 제어할 수 있음.

*출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20*  
<그림3-13_텍스트 파운데이션 모델_거대 언어 모델의 추론_ChatGPT에서 실제로 활용되고 있는 디코딩 알고리즘 및 효과 예시>

---

# 3-2. 프롬프트 엔지니어링
## 입력 프롬프트 = (1) 지시(instruction) + (2) 예시(few-shot examples)
- **지시 (Instruction)**
- **예시 (few-shot examples)**
  - 모델은 학습을 새로 하지 않고 프롬프트 안의 예시를 보고 패턴을 따라 함.

*출처: Brown et al., Language Models are Few-Shot Learners., NeurIPS 2020*  
<그림3-14_텍스트 파운데이션 모델_거대 언어 모델의 추론_인 컨텍스트 학습 (or 퓨샷 프롬프팅) 예시>

---

## 입력 프롬프트의 영향
- 어떻게 지시를 주는지, 어떤 예시를 보여주는지가 거대 언어 모델의 성능에 크게 영향을 미침
- **프롬프트 엔지니어링**: 원하는 답을 얻기 위해 모델에 주어지는 입력(프롬프트)을 설계·조정하는 기법

*출처: Brown et al., Language Models are Few-Shot Learners., NeurIPS 2020*  
<그림3-15_텍스트 파운데이션 모델_프롬프트 엔지니어링_프롬프트에 따른 ChatGPT의 응답 차이>

---

## 프롬프트 엔지니어링: 지시(instruction)
- 감정 분류와 같은 쉬운 문제뿐 아니라 수학, 코딩과 같은 어려운 문제를 거대 언어 모델로 푸는 것에 많은 관심 집중
  - 예시: 수학 질의 응답 (GSM8K → 미국 초등학교 고학년 수준 수학 문제)
    - **질문:** Josh는 쿠키 한 상자를 사려고 돈을 모으고 있어요. 돈을 벌기 위해 팔찌를 만들어 팔기로 했습니다. 팔찌 하나를 만들 때 재료비로 \$1이 들고, 팔찌는 하나당 \$1.5에 판매합니다. Josh가 팔찌를 12개 만들고 쿠키를 산 뒤에도 \$3가 남아있다면, 쿠키 한 상자의 가격은 얼마일까요?
    - **정답:** Josh는 팔찌 하나당 \$1.5 - \$1 = \$0.5의 이익을 얻습니다. Josh가 팔찌를 12개 만들면, 총 이익은 12 * \$0.5 = \$6입니다. 쿠키를 산 뒤에도 \$3가 남아 있으므로, Josh는 \$6 - \$3 = \$3을 쿠키 한 상자에 썼습니다. 따라서 쿠키 한 상자의 가격은 \$3입니다. 정답은 \$3입니다.

*출처: https://huggingface.co/datasets/openai/gsm8k*  
<그림3-16_텍스트 파운데이션 모델_프롬프트 엔지니어링_GSM8K 수학 문제 예시와 거대 언어 모델의 생성한 풀이 예시>

---

## 프롬프트 엔지니어링: 성능 비교
- 감정 분류와 같은 쉬운 문제뿐 아니라 수학, 코딩과 같은 어려운 문제를 거대 언어 모델로 푸는 것에 많은 관심 집중
  - Claude 3, GPT-4, Gemini 등 최신 모델들의 벤치마크 비교 (Grade School Math, MATH 등)

*출처: https://www.anthropic.com/news/claude-3-family*  
<그림3-17_텍스트 파운데이션 모델_프롬프트 엔지니어링_다양한 벤치마크에서의 최신 SOTA 거대 언어 모델들 간의 성능 비교>

---

## Chain-of-Thought (CoT) 프롬프팅
- **아이디어:** 단순히 질문과 응답만을 예시로 활용하는 것이 아니라, **추론(Reasoning)** 과정도 예시에 포함
  - 이를 통해 테스트 질문에 대해 추론을 생성하고 응답하도록 유도함으로써, 더 정확한 정답 생성을 기대할 수 있음
  - 질문에 대한 정답을 바로 제시 → 틀림
  - 질문에 대한 정답이 나오는 추론 과정을 함께 제시 → 정답률 상승

*출처: Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Model., NeurIPS 2022*  
<그림3-18_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 추론 기반 응답 예시>

---

## CoT 프롬프팅의 효과
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴
  - *PaLM*: 당시 구글에서 사용했던 가장 큰 거대 언어 모델 (PaLM 540B vs. GPT-3 175B)
- **CoT로 인한 성능 향상은 모델 크기가 커질수록 더 확대됨**  
  (추론 ~= 창발성?)
  - *창발성:* 모델 크기가 커지면 갑자기 새로운 능력이 나타나는 현상을 의미  
    (*PaLM의 창발적 능력이 발현되었을 수 있음*)

*출처: Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Model., NeurIPS 2022*  
<그림3-19_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 복잡한 추론 테스크에 대한 성능 향상 예시: GSM8K>

# 3-2. 프롬프트 엔지니어링
## Chain-of-Thought (CoT) 프롬프팅
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴  
- **다른 추론 테스크:** 마지막 단어 연결  
  - In-domain: 예시도 2 단어, 테스트도 2 단어  
  - Out-of-domain: 예시는 2 단어, 테스트는 4 단어  
  - 마지막 글자 이어붙이기 문제 → 단계적 추론이 필요함

<그림3-20_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 복잡한 추론 테스크에 대한 성능 향상 예시: 마지막 단어 연결>  
출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴  
- **다른 추론 테스크:** 마지막 단어 연결  
  - In-domain: 예시도 2 단어, 테스트도 2 단어  
  - Out-of-domain: 예시는 2 단어, 테스트는 4 단어  

- **2 letters**
  - 두 모델 다 꾸준히 증가  
  - 모델 크기가 클수록 성능이 좋아짐  
- **4 letters**
  - 학습 예시와 다른 일반화된 문제(out of domain)  
  - CoT를 썼을 때 향상됨

➡ CoT는 추론 테스크에서 성능을 크게 높일 뿐 아니라 훈련에 없던 더 어려운 문제도 효과적으로 대응할 수 있게 함

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- 예시 기반 CoT는 강력하지만, 예시를 위한 추론 과정을 수집해야 하는 문제가 있음  
- **Q. 예시 없이도(0-shot) 거대 언어 모델의 추론 성능을 강화할 수 있을까? (i.e., 0-shot CoT)**  
  - 단계별 사고 과정을 예시로 제공하여 LLM의 추론 능력을 향상시킴

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- 예시 기반 CoT는 강력하지만, 예시를 위한 추론 과정을 수집해야 하는 문제가 있음  
- **Q. 예시 없이도(0-shot) 거대 언어 모델의 추론 성능을 강화할 수 있을까? (i.e., 0-shot CoT)**  
  - “Let’s think step by step.”이라는 문구 추가로 예시 없이 LLM 성능 향상

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **1. 유인 문장을 통한 추론 생성** (e.g. “Let’s think step by step”)

<그림3-22_텍스트 파운데이션 모델_거대 언어 모델의 추론_0-shot CoT 프롬프팅 개요도>  
출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **1. 추론 문장을 통한 추론 생성** (e.g. “Let’s think step by step”)  
- **2. 주어진 질문과 생성된 추론을 통한 정답 생성** (e.g. “Therefore, the answer is”)

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **결과:** 0-shot CoT는 기존 0-shot 프롬프팅보다 훨씬 높은 추론 성능을 달성  
- 또한, 0-shot CoT는 모델 크기가 임계점을 넘어서야 효과성이 발휘됨  
  - 따라서, 추론 능력은 거대 언어 모델의 창발성 결과라고 볼 수 있음

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **Q. 추론 문장의 중요성?**
  - 단순한 문구 하나가 성능을 크게 향상시킴
  - 적절하지 못한 문구를 제시했을 때 성능을 떨어뜨리거나 역효과가 남

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

# 4. 거대 언어 모델의 평가와 응용

---

# 4-1. 거대 언어 모델의 평가

## 평가 (Evaluation): 구축한 시스템(e.g. 코드 or 앱)이 실제로 잘 동작하는지를 확인하는 단계

- 평가의 3가지 요소
  1) 목표: 시스템으로 무엇을 달성하고자 하는지  
  2) 평가 방법: 어떤 방법으로 평가할 것인지  
  3) 평가 지표: 어떻게 성공 여부를 판단할 것인지

> 출처: https://www.ytn.co.kr/_ln/0102_202404130800061445

- 예시: 배달 어플
  1) 목표: 음식을 음식점으로부터 유저에게까지 배달하는 것  
  2) 평가 방법: 배달 시간을 측정  
  3) 평가 지표: 전체 유저 배달 건수에 대한 평균 배달 시간

> 출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20

## AI 모델의 평가: “테스트 데이터”

- 핵심 가정: 학습 단계에서 본 적이 없고, 질문과 정답을 알고 있음
- 예시: 감정 분류  
  1) 목표: 주어진 입력 텍스트의 감정을 올바르게 예측하는 것  
  2) 평가 방법: AI 모델의 예측 감정과 사람이 작성한 정답을 비교하는 것  
  3) 평가 지표: 테스트 데이터 셋에서의 평균 정확도  

“총평하자면, 두 시간 동안 영화를 보고 얻은 건 팝콘과 음료 뿐입니다. 영화는 정말 형편없었어요.”

데이터 입력 → 추가 학습된 언어 모델 → 예측과 정답 비교  
예측 감정: 0 (부정적) = 정답 감정: 0 (부정적)

<그림 4-1. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_AI 모델의 테스트 데이터 기반 평가 예시>

출처: Delvin et al., BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, NAACL 2019

## 거대 언어 모델 평가의 특징

- 특정 테스트에서 학습된 기존 AI 모델들과 달리, 거대 언어 모델은 다양한 테스트에 대해 동시에 학습됨  
  - 따라서, 거대 언어 모델의 성능을 올바르게 평가하기 위해서는 많은 테스트에서의 성능을 종합적으로 판단해야 함  
  - 또한, 디코딩 알고리즘, 입력 프롬프트에 따라 같은 질문에 대해서도 예측이 바뀌므로, 공평한 비교를 위해서는 해당 부분도 고려해야 함

<그림 4-2. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델간의 성능 비교 예시>

출처: OpenAI, GPT-4 Technical Report

- 특정 테스트에서 학습된 기존 AI 모델들과 달리, 거대 언어 모델은 다양한 테스트에 대해 동시에 학습됨  
  - 따라서, 거대 언어 모델의 성능을 올바르게 평가하기 위해서는 많은 테스트에서의 성능을 종합적으로 판단해야 함  
  - 또한, 디코딩 알고리즘, 입력 프롬프트에 따라 같은 질문에 대해서도 예측이 바뀌므로, 공평한 비교를 위해서는 해당 부분도 고려해야 함

<그림 4-2. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델간의 성능 비교 예시>

출처: OpenAI, GPT-4 Technical Report

102p~