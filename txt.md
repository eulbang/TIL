# 딥러닝 및 이미지 파운데이션 모델
## “이미지 파운데이션 모델”

---

## 📘 CONTENTS
1. AI 파운데이션 모델 개념 및 대표 모델  
2. Vision-Language Model (VLM)  
3. Small VLM과 파운데이션 모델들 소개  
4. 개인화, 합성 데이터 활용 사례  

---

## 1차시  
### AI 파운데이션 모델 개념 및 대표 모델

---

## 학습 시작

- 학습데이터와 계산 리소스가 부족한 가난한 AI 서비스 회사(개발자)가  
  멋진 이미지 기반 AI 서비스를 개발하고자 합니다.  
  **어디서부터 시작하면 좋을까요?**

- 기존 이미지 AI 모델은 학습된 도메인과 유사한 데이터에서만 잘 작동했습니다.  
  그러나 실제 사용자 서비스는 전혀 예측하지 못한 데이터가 주어지는 경우도 많습니다.  
  학습하지 않은 상황에서도 동작하는 서비스를 개발하고자 할 때,  
  **어떤 특징을 갖는 이미지 AI 모델이 필요할까요?**

- **실용적인 이미지 AI 모델**을 가지고 어떤 서비스를 만들 수 있을까요?

---

## 학습 목표

- **AI 파운데이션 모델의 개념을 이해하고, 특징을 설명할 수 있다.**  
- **Pre-training, Fine-tuning, Zero/Few-shot 개념을 구분할 수 있다.**  
- **기존 머신러닝 모델과의 차이를 이해할 수 있다.**  
- **대표적 AI 파운데이션 모델 중 하나인 CLIP 모델의 개념과 역량을 알아본다.**

---

## AI 파운데이션 모델의 개념

---

## 1-1. 파운데이션 모델(Foundation model)이란?

### ▍AI 모델
- 함수 또는 프로그램  
- 입출력을 연결해주는 함수 + 데이터로 학습된 함수 +  
  **학습 때 보지 못했던 데이터에 대해서도 작동해야 하는 의무**
- 예시 : 뉴럴넷  
  - 입력 → 뉴럴넷 → 출력  

(이미지: dog/cat 분류를 수행하는 Neural Network 구조)

---

## 1-1. 파운데이션 모델(Foundation model)이란?

### ▍이상적인 AI 모델
- 만약 AI모델이 이 세상에서 발생 가능한 **모든 데이터**와  
  **각 데이터의 설명**을 모두 기억하고 있다면?

(이미지: 로봇이 데이터를 관찰하며 모든 이미지를 기억하는 모습)

### ▍이상적인 AI 모델
- 만약 AI모델이 세상의 모든 데이터와 설명을 기억하고 있다면?  
- 내가 얻고 싶은 답과 유사한 답이 이미 DB에 저장되어 있을 확률이 높음 →  
  **검색 엔진과 유사**
- 예시: 최근접 이웃 탐색 (Nearest Neighbor Search) 알고리즘  
- 그러나, 데이터 확보·저장·탐색은 매우 비용이 크고 현실적이지 않음

(이미지: Database와 Search Engine 구조 예시)

### ▍현실적인 기계학습 모델
- 학습 = AI모델에 데이터를 **패턴화**하여 **압축**  
- 이 과정에서 비슷함과 다름을 파악하게 되고,  
  패턴을 익히면서 새로운 데이터에 대한 **일반화 능력**이 생김  
- → **세상의 수많은 데이터를 최대한 기억할 수 있다면?**

(이미지: Neural Network가 여러 이미지를 압축하며 학습하는 모습)

---

# 1-1. 파운데이션 모델(Foundation model)이란?

▍파운데이션 모델이란?

• 대규모 데이터를 폭넓게 학습한 후, 다양한 문제에 빠르게 적용할 수 있는 범용 대형 AI 모델  
• 미국 스탠포드 대학 사람 중심 AI 연구소에서 2021년 출간된 보고서에서 새로운 범주로 구분을 시작  

▍파운데이션 모델  

• 기존 딥러닝 개발 패러다임 : 아기와 같이 언어, 시각, 청각, 촉각 등 기본적인 것들부터 배워 나가야 함  
• 파운데이션 모델 패러다임 : 거대 모델(커다란 뇌) + 대규모 데이터 학습 (많은 지식과 경험) 기반  
▷ 새로운 일을 처음 접해도 금방 배우고 잘할 수 있음  

▍파운데이션 모델  

• 파운데이션 모델 기반 개발 프로세스  

▍파운데이션 모델의 특징

특징 1 [대규모] : 트랜스포머 모델 + 대규모 언어 데이터 학습  
• 테스트에 상관없이 비슷한 패턴들이 등장하고 있음  
• 주로 비지도학습으로 훈련된 모델들도 많이 등장  
  - 의미하는 바 : 쉬운 데이터 수집 + 대규모 학습  

특징 2 [적응성] : 높은 파인튜닝 성능 (높은 태스크 적용 성능)  
• 믿고 쓸 수 있는 모델  

특징 3 [범용성] : 다양한 작업, 한정되지 않는 출력 지원  
• 예시 - 물체 판별  
  - 기존 : 20여개의 물체 종류 구분  
  - 파운데이션 모델 : 만 개 이상을 물체 종류 구분  
  (또는 자연어 기반의 한정되지 않은 대상에 대한 인식)  

▍파운데이션 모델에 의한 AI 모델 개발의 변화  

• 과거에는 매번 모델을 새로 학습했지만, 이제는 잘 학습된 모델들을 얼마나 잘 활용하느냐가 핵심  
• 파운데이션 모델 하나 확보하는데 투여되는 계산 리소스는 일부 대규모 인프라 이외에 불가  

---

▍적용 활용

활용 되는 기법들: 프롬프트 {엔지니어링, 튜닝}, 전이학습, 적용(Adaptation)학습, 파인튜닝  

- Zero-shot : 처음 보는 문제를 추가 학습 없이 바로 적용 (모델 자체가 가진 배경 지식 활용)  
- Few-shot : 예제 몇 개만 보여주면 바로 적용 가능  
- Fine-tuning : 처음부터 배우지 않아도, 조금만 알려주면 금방 적용  
  (모델 자체를 업데이트. 모델 가중치가 변경 됨)  

---

# 대표적 AI 파운데이션 모델  
- CLIP -

---

# AGI를 향해서

▍Human’s Intelligence (cognition) = perception ∪ higher cognitive processes  

• AI는 사람의 지능과 유사점/차이점 분석을 통해 발전  

▍Human’s Intelligence (cognition) = perception ∪ higher cognitive processes  

• 2022년 11월 이전 : 각 분야별로 지능의 매우 부분적 능력만을 개별적으로 모델링 시도  
• 2022년 11월 (ChatGPT) 이후 : 대규모 언어모델(LLM)이 높은 사고/추론 성능을 보여주기 시작  
  (다양한 인지 능력 벤치마크에서 인간 수준 근접)  

⇒ 그러나 사고 능력과 언어 능력 만으로 현실 세계를 이해하기에 충분할까?  

---

# LLM에 눈을 달아볼까? (시각언어모델)

사용자 : “누가 이 그림을 그렸어?”  
AI : “이 그림은 모나리자로 알려진 여성을 그린 레오나르도 다빈치의 유명한 그림입니다. 여성의 신비로운 미소를 보여주는 초상화로, 세계에서 가장 유명하고 상징적인 예술작품 중 하나가 되었습니다. …”  

입력: “이 이미지를 설명해줘”  
출력: “빨간 스카프를 두르고 있는 고양이 사진이에요.”  

---

# 시각언어모델 예시 - ChatGPT with GPT-4

▍GPT-4 (2023)

• 자연어 입력에 국한된 기존의 거대 언어 모델에서 더 나아가 이미지, 문서, 음성 등  
  멀티모달(multi-modal) 데이터를 처리할 수 있는 모델  
• GPT-4 API를 활용하여 다양한 도메인의 이미지 데이터와 결합한 모델이 개발됨 (예시 : 제조 AI)  

예시) GPT-4V for Generic Anomaly Detection  

유저  
왼쪽 이미지가 결함을 가지고 있는지 판단해줘. 만약 결함이 있다면, 구체적인 이유를 제공해줘.  

GPT-4  
이미지는 병이나 용기의 상단 부분으로 보이는 원형 물체 안으로 끈이나 줄이 통과하고 있는 것처럼 보입니다.  
검토 결과  
1. 원형 물체의 가장자리에 이물질이나 입자가 보입니다.  
2. 가장자리에는 굵은 자국이 보입니다.  
3. 줄에는 헤지거나 마모된 부분처럼 보이는 불규칙한 부분이 있습니다.  

# 시각언어모델 예시 - ChatGPT with GPT-4

▍GPT-4의 시각언어 멀티모달 언어모델로써의 능력 시연 [Sketch-to-web page (HTML)]

---

# 시각언어모델 예시 - Computer use, Claude

▍Claude 기반 Computer use 기능 시연 - 친구와의 여행 플랜 세우기  
• 수많은 컴퓨터 프로그램의 다양한 인터페이스를 이해하기 위해서는 시각 이해도 필요  

---

# 눈으로 어떤 것을 쓸까? CLIP(2021) by OpenAI

▍CLIP(2021) by OpenAI  

• 언어와 이미지의 유사도 학습  

• CLIP 모델 구조  

---

# 1-1. CLIP (2021)

▍CLIP: Contrastive Language-Image Pre-training, by OpenAI  

• AI가 언어와 시각을 통합해서 이해하는 방식을 보여준 패러다임 전환 제시  

• 파운데이션 모델로써의 특징  
  - 입력: 학습하지 않은 새로운 도메인의 입력 데이터에 대해서도 좋은 성능을 발휘 (제로샷 전이)  
  - 출력: 자연어를 이용해 한 번도 본 적 없는 카테고리도 텍스트 설명만으로 출력 정의 가능 (언어 인터페이스)  

▍대조 학습 기반(Contrastive Pre-training)의 언어-이미지 사전 학습  

• 인터넷 데이터를 통한 지도 학습(supervised learning)을 통해 자연어 기반 시각 개념 학습  
• 다양한 이미지-자연어 쌍으로 학습  
  - 인터넷에서 수집된 수억개의 이미지·텍스트 쌍  
  - Alt-text HTML tag, 이미지 캡션, 제목 등을 기반으로 수집  
  - 데이터 정제 과정을 거침 (중복 이미지, 해상도/품질 낮은 이미지, 짧은 텍스트 등)  

• 다양한 이미지-자연어 쌍으로 학습  
  - 텍스트 인코더 : Transformer  
  - 이미지 인코더 : ViT-B (또는 ResNet50)  

---

# 1-2. CLIP 구조 - 텍스트 인코더 (Transformer 기반 Text Encoder)

▍Remind - Transformer  

• 트랜스포머 구조 = 인코더 (Encoder) + 디코더 (Decoder)  
• CLIP에서는 Encoder only 구조 사용  

▍Remind - Transformer  

• 토큰이라는 단위의 입력  
• 입력된 토큰 간의 관계성을 집중하는 Attention 메커니즘으로 구성  
• L 길이의 입력 토큰은 D-차원 특징벡터(임베딩)의 배열로 형태로 입력 (L x D)  

• 자연어 데이터 :  
  Sub-word 단위의 임베딩  

---

# 1-3. CLIP 구조 - 이미지 인코더 (ViT: Vision Transformer, 2020)

▍Remind - Vision Transformer  

• 입력 구성  
  - 텍스트 인코더 (자연어 데이터 입력): Sub-word 단위의 임베딩  
  - 이미지 인코더 (이미지 데이터 입력): 패치 단위의 임베딩  
• ViT: 비전 분야에 트랜스포머를 (최소 수정으로) 적용한 모델  


▍Remind - Vision Transformer

• 이미지를 작은 패치(16x16x3)로 나눔  
• 각 패치를 1D로 Flatten  
• Learnable position embedding 사용  
  - 이미지 내에서 각 패치의 위치 민감 정보 추가  
  - 모델 학습 과정에서 함께 학습됨  
• Transformer encoder : 패치 처리  
• MLP Head를 통해 분류 작업 수행  
  - Head를 수정하여 다른 작업을 위한 transfer learning 활용 가능  
  - CLIP에서는 CLIP 학습법으로 학습됨  

---

# 1-4. CLIP (2021) 학습

▍대조 학습 (Contrastive learning)

• 학습 기준  
  - 목표 이미지(앵커)를 대응하는 텍스트(양성)와 가깝게  
  - 일치하지 않는 여러 텍스트(음성)와는 멀게  

▍대조 학습 (Contrastive learning)

Numpy-like pseudocode  

```
# image_encoder  - ResNet or Vision Transformer
# text_encoder   - CBOW or Text Transformer
# I[n, h, w, c]  - minibatch of aligned images
# T[n, l]        - minibatch of aligned texts
# W_i[d_i, d_e]  - learned proj of image to embed
# W_t[d_t, d_e]  - learned proj of text to embed
# t              - learned temperature parameter

# extract feature representations of each modality
I_f = image_encoder(I)  #[n, d_i]
T_f = text_encoder(T)   #[n, d_t]

# joint multimodal embedding [n, d_e]
I_e = l2_normalize(np.dot(I_f, W_i), axis=1)
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

# scaled pairwise cosine similarities [n, n]
logits = np.dot(I_e, T_e.T) * np.exp(t)

# symmetric loss function
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss   = (loss_i + loss_t) / 2
```

▍대조 학습 (Contrastive learning)

*️⃣ 𝑠ᵢⱼ : i번째 이미지와 j번째 텍스트 임베딩 간의 코사인 유사도  

Softmax 기반 손실 계산  

---

# 1-4. CLIP 간단 응용

▍제로샷 이미지 인식기  

• 텍스트로 원하는 물체 카테고리 리스트 준비  
• 텍스트 기반 카테고리 리스트를 텍스트 임베딩으로 변환하여 Vector DB 준비  
• 쿼리 이미지와 비교해서 가장 높은 점수의 카테고리 반환  

▍생각해보기  
- 검색 시스템과 유사성은 무엇일까?  
- 카테고리 이외에 어떤 것이 가능할까?  
- 카테고리가 정말 많을 경우에 어떻게 효율화할까?  

---

# 강의 정리

▍오늘 공부한 내용 요약 및 정리

• 파운데이션 모델은 대규모 데이터로 사전학습된 범용 모델  
• 파운데이션 모델의 방대한 사전 지식을 이용해 다양한 태스크에 빠르게 적용 가능  
  - 장점: 데이터/리소스 효율적, 범용성, 확장성, 높은 성능  
• 파운데이션 모델은 대규모, 적응성, 범용성의 특징을 가짐  
• 대표 이미지 파운데이션 모델:  
  인터넷 상의 대규모 {텍스트, 이미지} 페어 데이터를 활용한 이미지-언어 연관성을 학습한  
  CLIP 파운데이션 모델과 그 제로샷 이미지 인식기 응용  

---

# 2차시  
Vision-Language Model (VLM)

---

# 학습 시작

• 주어진 이미지와 장면을 분석하고 이해하는 서비스를 만들기 위해  
  지금까지 배운 이미지 인식기, 물체 탐지 모델로 충분할까?  
  인식/탐지 태스크 출력의 제한  

• 세상에 존재하는 수많은 케이스들을 이해하고,  
  사용자의 요구에 맞춰 이미지를 분석할 수 있는 진짜 인텔리전트한 모델은 없을까?  

• 나 대신 어려운 그래프와 문서들을 이해하고 컨설팅 해주는 모델은 어떻게 만들지?  

• 나와 같은 것을 "보고" "대화"를 나눌 수 있는 AI 모델을 구축해보자!  

---

# 학습 목표

• 고도화된 CLIP 계열인 SigLIP의 등장 배경에 대해서 이해한다.  
• Vision-Language Model의 구조 및 구축 패턴에 대해서 파악한다.  
• LLaVA, Qwen-VL, InternVL 등 최신 시각-언어 파운데이션 모델들의  
  발전 동향에 대해서 설명할 수 있다.  
• (심화) 추가 학습을 요구하지 않는 CLIP계열 멀티모달 정합 모델의 심화 응용 사례를 파악한다.  

# Vision-Language Models

---

## 3-1. AGI를 향해서

▍Human’s Intelligence (cognition)
= perception ∪ higher cognitive processes

- World → Perception(CLIP) → Cognition(LLM) → Interpretation
- 인간의 지능은 인식(Perception)과 고차 인지(Cognition)의 결합으로 이해 가능

---

## 3-1. 멀티모달 언어 모델

▍이미지, 소리, 비디오 등 다양한 모달리티를 함께 이해하고 처리할 수 있는 언어 모델

• 대표적인 모델  
  - ChatGPT, Claude, LLaVA(2023), InstructBLIP, Qwen-VL, InternVL, LLaMA-Vision, smolVLM, Phi, HyperClovaX-SEED-Vision 등  

• 응용 사례  
  - 텍스트와 이미지를 결합한 대화형 AI, 이미지 설명, 문서 이해, 비디오 분석 등 다양한 분야에서 사용  

구조 예시  
```
Image → [Image Encoder] → Feature map  
→ [Linear Projection] (Soft prompt 형성) → [Text Decoder] → “A picture of a dog on a skateboard”
```
(Image Space → Text Space)

---

## 3-2. LLaVA (Large Language and Vision Assistant, 2023)

▍Vision과 Language 모델을 결합한 모델(VLM)로,  
텍스트와 이미지를 동시에 이해

• 주요 특징  
  - 이미지 인식과 텍스트 생성을 결합하여,  
    이미지 설명 생성 또는 시각적 질문 응답 작업에서 뛰어난 성능  
  - 이미지, 명령(Instruction), 답변이 주어진 데이터셋을 구축하여  
    Instruction tuning으로 학습  

• 응용 사례  
  - 이미지 기반 질문 응답(Visual QA), 이미지 설명 생성, 시각적 정보 기반 대화 등  

---

## SigLIP (2023)

▍SigLIP은 softmax 대신 sigmoid 기반 손실함수 사용

• 기존 CLIP의 Contrastive learning 한계  
  - 이미 멀리 배치된 음성 데이터까지 계속 멀게 학습 → 비효율  
• SigLIP은 **일치하지 않는 음성 데이터에만 제한된 영향**을 주는 손실함수 설계  

즉, SigCLIP은 CLIP의 softmax 기반 대조학습을 sigmoid 기반으로 대체하여,  
음성 데이터의 불필요한 분리를 완화함.

---

## SigLIP (2023) - 수식 기반 설명

손실함수:  

\[
L_{SigLIP} = -\frac{1}{N^2} \sum_{i=1}^{N} \sum_{j=1}^{N} \log \frac{1}{1 + e^{-z_{ij}(s_{ij}/τ + b)}}
\]

- \( s_{ij} \): i번째 이미지와 j번째 텍스트 임베딩 간 코사인 유사도  
- \( z_{ij} \): Label (음성 → -1, 양성 → +1)  
  - 음성: \( s \) 작을수록 좋음  
  - 양성: \( s \) 클수록 좋음  
- Sigmoid는 일정 크기 이상이면 gradient가 줄어드는 완만한 형태 → 불필요한 학습 완화

---

## SigLIP (2023) - 성능 비교

▍CLIP 대비 SigLIP은 **잡음이 많은 데이터 환경에서도 더 안정적인 성능**

- Softmax(CLIP) vs Sigmoid(SigLIP) 비교  
- 데이터에 noise가 추가될수록 Sigmoid 모델의 성능 저하가 완만함  
- 최근 SigLIP 2도 공개됨 (VLM 성능 개선 목적)

---

## 멀티모달 정합 응용 (Multi-modal Alignment)

▍서로 다른 두 가지 이상의 모달리티(예: 이미지와 텍스트) 간  
공통된 임베딩 벡터 공간을 구성하는 것

• 서로 다른 모달리티 간 임베딩 유사도(연관성) 비교 가능  

• 대표적 모델  
  - CLIP (OpenAI): 이미지-텍스트 간 Multi-modal Alignment 수행  
  - ImageBind (Meta): 소리, 텍스트, 이미지, 열화상, 깊이맵 등 다양한 모달리티 결합  

→ 멀티모달 정보 간 **공통 컨셉 공간(embedding space)** 형성

---

## 멀티모달 정합 응용 ② — ImageBind

▍ImageBIND: One Embedding Space To Bind Them All  

• 이미지, 비디오, 텍스트, 오디오, 뎁스, 열화상, IMU 데이터를  
  하나의 임베딩 공간으로 결합하여 학습  

**응용 예시**
1. Cross-modal Retrieval:  
   오디오 → 비디오/텍스트 검색  
2. Embedding-space Arithmetic:  
   “새 + 파도 소리 → 바닷가의 새 이미지”  
3. Audio to Image Generation:  
   “엔진 소리 → 트럭 이미지”  
   “빗소리 → 비 오는 장면 생성”  
4. Audio to Segmentation:  
   소리 단서로 객체 위치 파악  

---

## 멀티모달 정합 응용 ③ — VLM의 눈으로 응용

▍VLM 기반 분류

• CLIP 기반 VLM 예시  
  - **BLIP-2** : CLIP + OPT/FlanT5 결합  
  - **InstructBLIP** : BLIP-2의 instruction tuning 버전  
  - **LLaVA** : CLIP + Vicuna  
  - **MiniGPT-4** : CLIP + Vicuna 기반  
  - **mPLUG-Owl** : CLIP 기반 Alibaba VLM  

• SigLIP 기반 VLM 예시  
  - **PaLI-X** : SigLIP + PaLM 결합  
  - **SmolVLM**

→ 최근엔 CLIP, SigLIP의 성공적 구조를 기반으로  
   **Vision Encoder 고도화 모델**들이 활발히 개발되는 추세

# 3-3 최신 공개 VLM 모델들 - Qwen2.5-VL
- 확장 기능
  - 강력한 문서 파싱 기능
    - 다국어 OCR
    - 테이블, 차트, 공식, 악보 이해
    - 필기체 이해
  - 정밀한 객체 그라운딩
    - 객체 탐지, 카운팅 능력 향상
  - 장시간 비디오 이해
    - 초단위 이벤트 세그먼트 추출 가능

# 3-3 최신 공개 VLM 모델들 - Qwen2.5-Omni
- Omni: 라틴어의 접두사. 모든(all), 전부(every), 전체(whole)
- 멀티모달 언어모델 분야에서의 Omni: 읽고, 쓰고, 보고, 듣고, 말하면 Omni

# 3-3 최신 공개 VLM 모델들 - Qwen3-VL
- 25.09.23 일 공개

- 확장된 활용 사례들
  - Omni Recognition
  - Powerful Document Parsing Capabilities
  - Precise Object Grounding Across Formats
  - General OCR and Key Information Extraction
  - Video Understanding
  - Mobile Agent
  - Computer-Use Agent
  - 3D Grounding
  - Thinking with Images
  - MultiModal Coding
  - Long Document Understanding
  - Spatial Understanding

# 3-3 최신 공개 VLM 모델들 - InternVL (2024)
- 상용 VLM에 맞서는 오픈소스 VLM
  - OpenGVLab에서 개발한 멀티모달 언어모델
  - InternVL 1.0부터 시작하여 현재 InternVL 2.5까지 발전
- LLM의 대규모 용량에 맞추어 이미지 모델의 용량을 증대시킴

- 상용 VLM에 맞서는 오픈소스 VLM
- 다양한 종류의 이미지 모델과 언어 모델이 결합되어 오픈소스로 공개됨

- InternVL 전체 구조도

- InternVL 학습 전략
  - (a) 단일 모델 학습 파이프라인
  - (b) LLM을 점점 키워가면서 학습하는 파이프라인

# 3-4 VLM의 성능을 높이는 트릭
- Set of Mark (SoM)
  - 다른 물체 탐지, 세그멘테이션 파운데이션 모델을 활용한 방법
  - VLM 모델들의 부족한 시각 능력을 보완하여 비약적 성능 향상
  - Computer 작동 Agent 모델에 기본적인 비주얼 프롬프팅으로 매우 유용

# 3-4. 도메인 특화 파운데이션 모델들 - 의료
- 의료 이미지(X-Ray, MRI, CT 등)를 입력 받아, 병적 진단 및 원인 설명 등의 태스크 수행
- Contrastive learning을 통해 학습
  - BiomedCLIP 모델 구조

# 심화. CLIP 모델의 고급 응용
---

# 심화 - CLIP 응용 - 멀티모달 정합 손실함수로 활용
## 서로 다른 모달리티(예: 이미지와 텍스트) 간의 변환
- 모달리티 변환을 위한 2가지 디자인
  - 변환(Translating)
  - 정렬(Matching)

## 멀티모달 정합(Multi-modal Alignment)을 활용하는 법
- 서로 다른 두 가지 이상의 모달리티(예: 이미지와 텍스트) 간의 공통된 임베이딩 벡터 공간을 구성하는 것
- 이 연관성을 거꾸로 활용하는 방법은 없을까?
- 멀티모달 정보 간 공통 컨셉 공간(Embedding space)

## 정합(Matching)을 통한 크로스모달 변환
- 멀티모달 정합 손실 함수(Multi-modal alignment loss)
  - Multi-modal 데이터(예시: 이미지와 텍스트) 사이의 정렬된 정도를 측정
  - 대표적인 텍스트·이미지 손실함수: **CLIP loss**, **Score Distillation Sampling(SDS) loss**
- **CLIP loss [Radford21]**
  - 사전학습된 CLIP 활용
- **SDS loss [Poole23]**
  - 사전학습된 text-to-image diffusion model 활용

## CLIP loss 예시
- 텍스트-이미지 간 정렬 정도 측정 (손실함수로 사용됨)

---

# 3-4. 도메인 특화 파운데이션 모델들 - 의료
## MedCLIP (2022)
- 의료 텍스트와 이미지 임베딩을 정합시킨 의료용 CLIP 모델
- 텍스트 입력으로부터 이미지 상의 질병을 탐지하거나 특정 종류의 의료 이미지를 검색하는 방식 등으로 활용 가능

## LLaVA-Med (2023)
- LLaVA를 의료 데이터에 파인튜닝한 의료 특화 모델
- 의료 이미지를 포함한 지시문 데이터(visual instruction-following data)를 통해  
  의료 이미지 기반 챗봇 대화가 가능한 멀티모달 모델

---

# 3-4. 도메인 특화 파운데이션 모델들 - 의료 (사례)
- 입력: 흉부 X-ray 이미지
- 출력: 폐렴 진단 및 설명 예시 (LLaVA-Med 대화 기반 진단 결과)
- 실제 예시:
  - 폐렴 소견 감지
  - 삽입된 장치 유무 확인 등

---

# 3-4. 도메인 특화 파운데이션 모델들 - 제조업
## AnomalyGPT (2023)
- 제조업 환경에서 발생하는 결함이나 불량을 탐지(anomaly detection)하기 위한 모델
- 챗봇 형식으로 이미지 상 결함에 대해 텍스트로 질의응답을 주고받을 수 있음
- ImageBind의 이미지 인코더와 Vicuna를 언어 모델로 활용하여 제조업 데이터에 파인튜닝

---

# 3-4. 도메인 특화 파운데이션 모델들 - 3D 언어 모델
- 3차원 표현(예: point-cloud)과 자연어의 관계를 학습한 파운데이션 모델
- **3D LLM 모델 구조**
  - 3차원 질문-대답 생성
  - 3차원 공간 네비게이션
  - 로봇팔 동작 생성

---

# 3-4. 도메인 특화 파운데이션 모델들 - 로봇 행동 모델
- 입력: 사람의 텍스트 명령 + 로봇 시점 영상
- 출력: 로봇 행동 (위치 변화, 관절 움직임 등)
- 텍스트 명령 기반 로봇 동작 예시
- 응용 사례: **PaLM-E** (다중 모달 명령 → 로봇 행동 변환 모델)

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 정합(Matching)을 통한 크로스모달 변환
- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

“정면을 향해 걷고 있는 앨런 튜링”  
“춤추고 있는 프레디 머큐리”

Text-to-X  
(예시 : Text-to-3D)

- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

### 다양한 활용 예시
- 이미지 캡셔닝  
- 텍스트 입력을 통한 이미지 스타일 변환  
- Text-to-image 생성  
- Text-to-motion 생성  
- Text-to-3D 물체 생성  
- 텍스트 입력을 통한 이미지/비디오 검색  
…  
(지난 4년 동안 약 4만편 이상 인용)

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - ZeroCLIP
- 입력: 이미지 / 출력: 캡션  
- 다양하고 구체적인 텍스트 생성, 제한된 OCR (글자인식) 능력

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - StyleCLIP
- 입력: 텍스트 명령, 원본 이미지 / 출력: 편집된 이미지

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - CLIP-Actor
- 입력: 텍스트 설명 / 출력: 3D 애니메이팅 아바타

---

# 강의 정리

## 오늘 공부한 내용 요약 및 정리
- CLIP의 학습 디자인 한계를 간파한 SigLIP  
- VLM = Vision-Language Encoder (예: CLIP/SigLIP) + Language Model  
  - 비전 입력은 눈에 해당하는 지각 기능,  
    언어 기반의 LLM은 뇌의 사고에 해당하는 중추 역할 수행  
- 기존 언어모델은 텍스트만, CV 모델은 이미지만 처리하기 때문에  
  이를 융합하면 수많은 문제들을 하나의 모델로 해결 가능  
  - 이미지 인식, 탐지, 카운트, Visual Q&A, 추론, 글자 인식(OCR), 번역, 추론, etc.  
  - 도메인 특화 VLM 사례들  
- 심화 CLIP 응용으로 추가 데이터 및 학습 없이  
  새로운 응용 모델을 만드는 디자인 패턴 (역전파 응용)

---

# 3차시  
## Small VLM과 파운데이션 모델들 소개

---

# 학습 시작
- VLM 모델이 유용하긴 한데, 서버는 너무 비싸다.  
  내 개인 컴퓨터나 스마트폰에서 실행되는 모델은 없을까?  
  엄청 성능이 좋을 필요는 없는데  
- 사진 속 특정 대상을 자동으로 분리하거나,  
  내가 딱 원하는 고품질 이미지를 빨리 찾고 싶은데  
  어떤 프로그램을 사용하는 게 좋을까?

---

# 학습 목표
- 경량화 VLM 모델들이 어떤 것들이 있는지 살펴보고,  
  디자인 패턴과 특징을 이해한다.  
- 한국어 VLM의 별도 개발 필요성을 이해한다.  
- Segment Anything, Grounding DINO를 비롯한  
  이미지/비디오 생성 모델, 3D 복원 모델들의 기능과 입출력, 활용을 설명할 수 있다.  
- 이미지/영상 파운데이션 모델들의 산업에 미치는 영향을 상상할 수 있다.

# Small Vision-Language Models (sVLM)

---

## 1-1. OpenVLM  
**VLM 성능 리더보드**

- OpenVLM Leaderboard (https://huggingface.co/spaces/opencompass/open_vlm_leaderboard)
- 상위권 모델의 공통점 → 너무 무겁다!
- 예시:
  - InternVL 3-78B : 78.4B 파라미터
  - InternVL 3-38B : 38.4B 파라미터
  - Ovis2-34B : 34.9B 파라미터
- 대부분 30B~70B 이상으로, 실사용에는 과도하게 큼

---

## 1-2. sVLM  
**다양한 온디바이스 모델 실경량화된 소형 VLM을 만들기 위한 시도들**

- sLLM에서 이루어진 경량화 시도들이 VLM에서도 이어지고 있음  
- VLM → sLLM → sVLM 순으로 발전 중
  1. **VLM**: 멀티모달 데이터 처리를 위한 비전언어모델 개발  
  2. **sLLM**: 대규모 언어모델을 경량화하기 위한 시도  
  3. **sVLM**: 효율적인 소형 VLM 개발  
- 목표: 성능은 유지하면서도 **cheaper/faster**  
- 예시 모델: SmolVLM, MiniCPM-V2, PaliGemma 3B, InternVL2 2B, Qwen2-VL 2B, Idefics3 8B 등

---

## 1-3. SmolVLM  
**Huggingface가 개발한 sVLM**

- Vision Encoder: **SigLIP**  
- Language Model: **Llama 3.1 8B → SmolLM2 1.7B**  
- 구조:
  - Vision Encoder → Modality Projection + Pooling → LLM
  - Hidden States를 통해 이미지 특징을 텍스트로 전달  
- 설계 목표: 효율적인 Vision-Language 연동, 낮은 메모리 사용량

---

## 1-3. SmolVLM (성능 비교)

- Inference GPU memory needs (Batch Size=1)
  | Model | 1 image (GB) | 2 images (GB) |
  |--------|---------------|---------------|
  | SmolVLM (ours) | 5.02 | 5.70 |
  | PaliGemma 3B | 6.72 | 7.76 |
  | InternVL2 2B | 10.52 | 16.51 |
  | Qwen2-VL-2B | 13.70 | 23.12 |

- → SmolVLM이 가장 가볍고 효율적임  
(출처: https://huggingface.co/blog/smolvlm)

---

## 1-4. Moondream 0.5B  
**모바일 기기나 엣지 디바이스에서의 실시간 실행을 염두에 두고 개발**

- 2억 개의 파라미터, 8비트 양자화 시 다운로드 크기 479MB  
- 실행 메모리 약 996MB 수준으로 매우 작음  
- 4비트 양자화 시에는 다운로드 375MB, 메모리 816MB까지 감소  

### 제공 기능
- Image Captioning  
- Visual Question Answering  
- Object Detection  
- Pointing (x, y)  
- Gaze Detection  
- OCR & Document Understanding  

(출처: https://moondream.ai/c/playground)

---

## 1-4. Moondream 0.5B - Demo  
- 시각 질의(Visual Query)를 입력해 이미지 기반 질의응답, 캡션, 포인팅, 탐지 수행  
- Playground 링크: https://moondream.ai/c/playground  

---

## 1-4. Moondream 0.5B - 손쉬운 사용법  

````python
pip install moondream==0.0.5

import moondream as md
from PIL import Image

# Initialize with local model path
model = md.vl(model="path/to/moondream-0_5b-int4.mf")

# Load and process image
image = Image.open("path/to/image.jpg")
encoded_image = model.encode_image(image)

# Generate caption
caption = model.caption(encoded_image)["caption"]
print("Caption:", caption)

# Ask questions
answer = model.query(encoded_image, "What's in this image?")["answer"]
print("Answer:", answer)

## 1-5. Gemini Nano  
**온 디바이스용 경량 Gemini**

- 18억 및 32.5억 개 파라미터의 두 가지 변형 (Nano-1, Nano-2)으로 구성되어  
  스마트폰 등 디바이스 내부에서 직접 실행될 수 있도록 설계

- 2024년 출시된 픽셀 9 시리즈에는 이 Gemini Nano 모델이 탑재되어,  
  녹음 앱에서 녹음 중 실시간으로 이미지/오디오 내용을 인식하고 요약하는 기능이 구현

- 사용자가 카메라로 보이는 자료를 녹음과 함께 입력하면,  
  기기가 내부 AI를 통해 해당 이미지를 이해하고 관련 텍스트를 생성

출처: [https://github.com/vikhyat/moondream?tab=readme-ov-file](https://github.com/vikhyat/moondream?tab=readme-ov-file)

## 1-6. 갤럭시 온디바이스 AI  
**모바일 NPU로 이미지, 언어, 오디오, 영상 작업을 기기 내에서 직접 생성형 AI 실행**

- 텍스트 기반 이미지 생성  
- 인페인팅 & 아웃페인팅  
- 어조 변환 및 문법 교정  
- 자연어 기반 사진 촬영 (예: “스케이트보드 탈 때 찍어줘”)  

출처: https://github.com/vikhyat/moondream?tab=readme-ov-file

---

## 1-7. LMDeploy  
**LMDeploy를 이용한 InternVL 배포**

- LMDeploy는 LLM의 효율적 압축, 배포, 서빙을 지원하는 오픈소스 툴킷  

### 특징
- 효율적인 추론: 지속적 배치, 병렬화, 고성능 CUDA 커널 등으로 최대 1.8배 높은 처리량  
- 효과적인 양자화: 4비트 양자화 등 방식을 통해 2.4배 빠른 추론  
- 분산 서빙: 여러 머신과 GPU에서 다중 모델 서비스 배포  
- 대화형 추론: 대화 이력 재처리를 줄이는 방식으로 효율적인 대화형 추론  
- 높은 호환성: 다양한 기능을 동시에 사용 가능  

출처: https://lmdeploy.readthedocs.io/en/latest/

---

## 1-7. 실습 - LMDeploy  
**InternVL, Qwen, DeepSeek, Phi 등 다양한 VLM 제공**

### 지원 모델 목록
- LLaVA(1.5, 1.6) (7B~34B)  
- InternLM-XComposer2 (7B, 4khd-7B)  
- InternLM-XComposer2.5 (7B)  
- Qwen-VL (7B)  
- Qwen2-VL (2B, 7B, 72B)  
- Qwen2.5-VL (3B, 7B, 72B)  
- DeepSeek-VL (7B)  
- DeepSeek-VL2 (3B, 16B, 27B)  
- InternVL-Chat (v1.1~v1.5)  
- InternVL2 (1B~76B)  
- InternVL2.5(MPO) (1B~78B)  
- InternVL3 (1B~78B)  
- Phi-3-vision (4.2B)  
- Phi-3.5-vision (4.2B)  
- GLM-4V (9B)  
- Llama3.2-vision (11B, 90B)  
- Molmo (7B-D, 72B)  
- Gemma3 (1B~27B)  
- Llama4 (Scout, Maverick)  

출처: https://github.com/InternLM/lmdeploy

---

## 1-7. 실습 - LMDeploy - InternVL  
**LMDeploy를 이용한 InternVL 배포**

- LMDeploy는 LLM의 효율적 압축, 배포, 서빙을 지원하는 오픈소스 툴킷  

### 오프라인 배포
```python
from lmdeploy import pipeline
from lmdeploy.vl import load_image

pipe = pipeline('OpenGVLab/InternVL2-8B')

image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe((f'describe this image', image))
print(response)
```

### 온라인 배포
```
lmdeploy serve api_server OpenGVLab/InternVL2-8B
```

출처: https://lmdeploy.readthedocs.io/en/latest/

---

## 1-8. 기타 sVLM  
**최신 sVLM**

- **Qwen 2.5-VL 3B**  
  - 다양한 크기의 이미지와 장시간 영상 처리 가능  
  - 표, 악보, 화학식 등 다양한 형태의 데이터 및 JSON 형식 등 처리 가능  

- **Phi-3.5 Vision Instruct 4.2B**  
  - OCR, 차트 분석, 비디오 용약 등에 특화된 경량 멀티모달 모델  

- **DeepSeek-VL2 1B**  
  - 중국 AI 스타트업으로 저비용 오픈소스 LLM 및 VLM 개발  

- **Gemma 3 1B**  
  - Google의 멀티모달 오픈소스 모델  
  - 1B ~ 27B의 다양한 크기 모델 제공  

출처:  
https://github.com/QwenLM/Qwen2.5-VL  
https://huggingface.co/microsoft/Phi-3.5-vision-instruct

---

## 2. 한국어 sVLM  

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**언어별 토큰 길이 격차 (토큰 정보밀도 차이)**

- 언어에 따라 동일한 문장이라도 토큰화 후 길이에 큰 차이 발생  
- 영어 중심 토크나이저는  
  - 영어가 일부 언어보다 최대 2.5배 높은 정보 밀도를 보여, 같은 토큰 길이에 더 많은 내용을 담을 수 있음  
  - 비영어권 언어는 컨텍스트 활용 효율이 낮고 토큰 낭비가 발생하는 “구조적” 불이익 존재  
  - (언어 자체 한계가 아닌, 토큰화 방법의 효율성 차이)

예시 (Tokens / Characters 비교)  
- 영어: 4 / 23  
- 한국어: 7 / 13  
- 중국어: 4 / 7  
- 일본어: 9 / 12  

출처: https://huggingface.co/blog/royswastik/transformer-tokenization-vocabulary-creation

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**토크나이저의 언어 편중 이슈**

- 주요 빈도가 높은 표현 위주로 설계되어, 사용 빈도가 적거나 형태가 설계 언어와 다른 언어는 비효율적으로 긴 토큰 시퀀스가 생성  

**형태소가 복잡한 언어의 토큰화**
- 핀란드어, 독일어의 경우, 하나의 단어가 매우 길거나 여러 의미를 접합해 표현하므로, 서브워드 단위로 쪼개지는 토큰 수가 크게 증가  

출처:  
Ali, Mehdi, et al. “Tokenizer choice for llm training: Negligible or crucial?” Findings of the Association for Computational Linguistics: NAACL, 2024.  
https://medium.com/@geosar/the-importance-of-tokenizers-for-multilingual-llms-a-case-study-on-greek-af5301b0bacf

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**토큰을 줄이려는 시도 – 한국어**

예시 문장:  
이번 방학 때 뭐해? (What is your plan for this vacation?)

- 기본(Base): 19 Tokens  
- 확장(Extended): 8 Tokens  

→ 한국어 맞춤형 토크나이저를 통해 동일 문장의 토큰 수를 절반 이하로 감소 가능

출처:  
Seo, Jean, et al. “How does a Language-Specific Tokenizer affect LLMs?” arXiv preprint arXiv:2502.12560 (2025)

---

## 2-2. 한국어 sVLM 모델  
**한국어 sVLM 모델**

- HyperCLOVAX-SEED-Vision-Instruct-3B는 NAVER가 개발한 한국어 특화 멀티모달 모델로, 텍스트와 이미지를 동시에 이해하고 텍스트를 생성  

출처: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B

- HyperCLOVAX-SEED-Vision-Instruct-3B는 NAVER가 개발한 한국어 특화 멀티모달 모델로,  
  텍스트와 이미지를 동시에 이해하고 텍스트를 생성  

### HyperCLOVA X Vision의 정량 지표

**Public Benchmarks**

| Model | SEEDv1 (image) | MMMU (val) | TextVQA (val) | DocVQA (test) | ChartQA (test) | InfographicVQA (test) | MathVista (testmini) | VQAv2 | Average |
|--------|----------------|-------------|----------------|----------------|----------------|-----------------------|----------------------|--------|----------|
| GPT-4V | 69.1 | 56.8 | 78 | 88.4 | 78.5 | 75.1 | 49.9 | 77.2 | 71.63 |
| HCX-VLM | 75.6 | 45.1 | 77.9 | 89.8 | 81 | 65.2 | 57.1 | 81 | 71.59 |

달성률(%) 99.94  

**K-GED (한국 초·중·고 검정고시) 성능**

| Model | Correct Answers |
|--------|----------------|
| GPT-4o | 1152 / 1480 (77.8 %) |
| HCX-VLM | 1240 / 1480 (83.8 %) |

---

### 예시 1 : 안내문 요약  
> 이 사진에 있는 안내판에는 일본어 문장이 쓰여 있습니다. 요약 결과 :  
> - 1952년 졸업생들이 기증한 조각  
> - 아사쿠라 호우미의 작품으로 일본 제협회 출품작  
> - 제목은 “평화가 오다”, 1957년 학생들의 염원을 담아 기증  
> - 안내문은 작품의 제작자와 의도를 설명  

---

### 예시 2 : 요리 절차 추론  
> 재료 : 소고기, 양파, 토마토, 햄버거 빵 → 함께 햄버거 만드는 순서 예측 결과  
> 1. 햄버거 빵 준비  
> 2. 패티 형성 및 양념  
> 3. 팬에 기름 두르고 패티 굽기  
> 4. 토마토·양파 슬라이스  
> 5. 햄버거 조립 및 치즈 추가  

---

### 예시 3 : 그래프 해석  
> 원그래프에 따르면 Company A 점유율이 50%로 가장 높고,  
> Company B 25%, C 15%, D 10% → A가 최대 시장 점유율 보유  

---

## HuggingFace를 통한 한국어 sVLM 모델 사용  

1. HuggingFace 로그인 및 모델 다운로드  
2. 커스텀 모델 등록 및 불러오기  
3. 대화 데이터 구성 및 입력 생성  
4. 텍스트 생성  

---

### 1️⃣ HuggingFace 로그인 및 모델 다운로드
```python
from huggingface_hub import login
# 1. 토큰 로그인 (토큰은 https://huggingface.co/settings/tokens 에서 생성)
login(token="token_id")

from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B",
    local_dir="./hyperclovax_vision_3b",
    local_dir_use_symlinks=False
)
```

---

### 2️⃣ 커스텀 모델 등록 및 불러오기
```python
from transformers import AutoTokenizer, AutoProcessor, AutoConfig, AutoModelForCausalLM
from hyperclovax_vision_3b.modeling_hyperclovax import HCXVisionForCausalLM, HCXVisionConfig

# 1. 커스텀 등록
AutoConfig.register("hyperclovax_vlm", HCXVisionConfig)
AutoModelForCausalLM.register(HCXVisionConfig, HCXVisionForCausalLM)

# 2. 모델 로드
model_path = "./hyperclovax_vision_3b"

tokenizer = AutoTokenizer.from_pretrained(model_path)
processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to("cpu")
```

---

### 3️⃣ 텍스트 생성
```python
chat = [
    {"role": "system", "content": "당신은 친절한 한국어 AI 비서입니다."},
    {"role": "user", "content": "안녕?"},
    {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"},
    {"role": "user", "content": "너는 무슨 음식 좋아해?"}
]

input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt", tokenize=True)
input_ids = input_ids.to(device="cpu")

output_ids = model.generate(
    input_ids,
    max_new_tokens=64,
    do_sample=True,
    top_p=0.6,
    temperature=0.5,
    repetition_penalty=1.0
)
print("="*80)
print("LLM EXAMPLE")
print(tokenizer.batch_decode(output_ids)[0])
print("="*80)
```

---

### 4️⃣ 텍스트 + 이미지 프롬프트
```python
vlm_chat = [
    {"role": "system", "content": {"type": "text", "text": "System Prompt"}},
    {"role": "user", "content": {"type": "text", "text": "User Text 1"}},
    {
        "role": "user",
        "content": {
            "type": "image",
            "filename": "tradeoff_sota.png",
            "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff_sota.png?raw=true",
            "ocr": "List the words in the image in raster order...",
            "lens_keywords": "Gucci Ophidia, cross bag, Supreme shoulder bag",
            "lens_local_keywords": "[0.07, 0.21, 0.92, 0.90] Gucci Ophidia"
        }
    }
]
```

---

### 5️⃣ 텍스트 생성 (이미지 입력 포함)
```python
new_vlm_chat, all_images, is_video_list = processor.load_images_videos(vlm_chat)
preprocessed = processor(all_images, is_video_list=is_video_list)

input_ids = tokenizer.apply_chat_template(
    new_vlm_chat,
    return_tensors="pt",
    tokenize=True,
    add_generation_prompt=True,
)

output_ids = model.generate(
    input_ids=input_ids.to(device="cpu"),
    max_new_tokens=8192,
    do_sample=True,
    top_p=0.6,
    temperature=0.5,
    repetition_penalty=1.0,
    **preprocessed,
)
print(tokenizer.batch_decode(output_ids)[0])
```

## 2-2. 한국어 sVLM 모델  
**한국어 sVLM 모델**

- Kanana-1.5-v-3b-instruct는 Kakao가 개발한 한국어 특화 멀티모달 모델

| 모델 비교 | 전체 평균 | 영어 이미지 이해 | 한국어 이미지 이해 | 영어/한국어 멀티모달 지시 이해 |
|-------------|------------|------------------|------------------|------------------------------|
| kanana-1.5-v-3b-instruct (3.62B) | 약 70 | 약 75 | 약 60 | 약 70 |
| HCX-SEED-Vision-3B (3.72B) | 약 68 | 약 70 | 약 58 | 약 65 |
| Phi-3-Vision (4.15B) | 약 65 | 약 68 | 약 55 | 약 60 |
| Qwen2.5-VL-3B (3.75B) | 약 72 | 약 75 | 약 62 | 약 70 |
| InternVL2.5-4B (3.94B) | 약 68 | 약 70 | 약 56 | 약 66 |

출처: https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct

---

# 다른 이미지 파운데이션 모델들 소개

---

## Remind – VLM의 성능을 높이는 트릭  
**Set of Mark (SoM)**

- 세그멘테이션을 위해 서로 다른 모델들을 결합하여 사용  
- SEEM, Semantic-SAM, SAM, MaskDINO 등 활용  

### 예시 비교  
- 입력: 이미지  
- 입력 + SoM  
→ 세밀한 객체 인식 및 위치 정확도 향상

> GPT-4V 기본 입력 → “컵”으로 오답  
> GPT-4V + SoM → “램프(12번)”으로 정답 인식  
> 위치 기반 질의(창가 좌석 등) 정확도 상승

출처: Yang et al., *Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V*, arXiv 2023

---

## 2-1. 이미지 파운데이션 모델  
**영상 파운데이션 모델 개요**

- 컴퓨터 비전(CV)에서 방대한 데이터를 학습한 모델들  
- 분할(Segmentation), 탐지(Detection), 3D 및 깊이 예측(3D & Depth) 등 다양한 작업 수행 가능  

### 영상 파운데이션 모델의 예시  
- 이미지-텍스트 유사도 측정  
- 비전-언어 모델  
- 멀티모달 융합  
- 3D LLM 구조 (Perceiver + LLM 기반 3D Feature 학습)

---

## 2-2. 이미지 세그멘테이션 모델  
**Segment Anything (SAM, 2023; SAM2, 2024) – Meta**

- 컴퓨터 비전에서도 방대한 양의 데이터로 Foundation 모델을 구축 가능함을 증명  
- 클릭, 박스, 부분 세그먼트, 텍스트 등의 유저 입력을 받아 원하는 영역 마스크를 추출  
- 약 1,100만 개 이미지 (약 10억 개의 마스크) 학습  

출처:  
Ravi et al., *SAM 2: Segment Anything in Images and Videos*, arXiv 2024  
Kirillov et al., *Segment Anything*, ICCV 2023  

---

## 2-2. 이미지 내 물체 탐지 모델  
**Grounding DINO (2023) – IDEA Research**

- 텍스트 입력을 통해 이미지 내 물체를 탐지  
- 대규모 데이터 기반으로 다양한 물체에 대한 높은 일반화 성능 확보  
- 객체 탐지 분야 Foundation 모델로 우수한 성능 달성  

**응용**  
- 이미지 검색, 탐지, 분류 작업  

출처:  
Liu, Shilong, et al. *Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection.* arXiv:2303.05499 (2023)

---

## 2-2. 이미지 내 인스턴스 탐지 및 세그멘테이션 모델  
**Grounded SAM (2024) – IDEA Research**

- Grounding DINO + SAM 결합 모델  
- 텍스트 입력으로 객체 탐지뿐 아니라 분할까지 수행 가능  
- Grounding DINO의 박스를 SAM의 입력으로 활용해 개별 물체 분할  

예시  
- 텍스트 입력: “말, 구름, 풀, 하늘, 언덕”  
- Grounding DINO: 모든 물체 탐지  
- Grounded SAM: 모든 물체를 탐지 및 분할 가능  

출처:  
https://github.com/IDEA-Research/Grounded-Segment-Anything

---

## 2-2. 비디오 내 인스턴스 탐지 및 세그멘테이션 모델  
**SAMURAI (2024) – Univ. Washington**

- 비주얼 물체 트래킹 분야 최신 (State-of-the-art, 2025.05 기준)  
- SAM2 기반 응용 모델  
- 응용 사례: 비디오 편집, 물체 제거기, 이상행동 감지, CCTV 자동 분석, 스포츠 중계 등  

출처:  
Yang et al., *SAMURAI: Adapting Segment Anything – Motion-Aware Memory*, arXiv 2024

---

## 2-3. 영상 생성 파운데이션 모델들  
**이미지 생성 (Image Generation)**

- 대규모 이미지 학습을 통해 텍스트 설명으로 새로운 이미지를 생성  

### 응용 사례 1
- 텍스트 외 조건(자세, 환경, 스타일 등)을 입력받아 이미지 생성  

### 응용 사례 2
- 텍스트 기반 3D 객체 생성  

출처:  
Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*, CVPR 2022  
Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, CVPR 2023  
Poole et al., *DreamFusion: Text-to-3D using 2D Diffusion*, ICLR 2023  
Youwang et al., *Paint-it: Text-to-Texture Synthesis via Deep Convolutional Networks*, CVPR 2024  

---

## 2-3. Closed 이미지 생성 모델  
**DALL·E 3 (OpenAI)**

- 출시 시기: 2023년 10월 (ChatGPT 통합 출시)  
- ChatGPT 및 Bing Image Creator에서 사용 가능  
- 대화형 프롬프트 개선 및 이미지 생성 지원  
- ChatGPT 내장형 서비스  
- 복잡한 프롬프트를 정교하게 반영하며 안전장치 강화  

예시 Prompt: **“우울한 아보카도”**

출처: https://openai.com/index/dall-e-3/

## 2-3. Closed 이미지 생성 모델 – DALL·E 예시

### DALL·E 2 vs DALL·E 3 비교
- **Prompt**: *An expressive oil painting of a basketball player dunking, depicted as an explosion of a nebula.*

| 모델 | 예시 설명 |
|------|------------|
| DALL·E 2 | 색채 표현은 강렬하나, 세부 묘사 및 공간 표현이 다소 거칠음 |
| DALL·E 3 | 섬세한 질감 표현, 배경(성운)의 입체감과 조명 효과 향상 |

출처: https://openai.com/index/dall-e-3/

---

### DALL·E 3 추가 예시

| 유형 | 설명 |
|------|------|
| **스티커 이모지** | 인물 사진을 기반으로 캐릭터 스티커 생성 |
| **지브리 스타일** | “원본 구조를 유지한 채로, 지브리 스타일로 만들어줘” 프롬프트를 적용한 사례 |

출처: https://openai.com/index/dall-e-3/

---

## 2-3. Closed 이미지 생성 모델 – Midjourney v7

**Midjourney v7 (Midjourney Inc.)**
- 출시 시기: 2025년 4월 알파 버전 공개  
- 모든 이미지에서 세부 묘사(높은 품질), 프롬프트 해석 정확도 향상  
- 손/신체 표현의 일관성 개선  
- 긴 프롬프트 이해, 세밀한 스타일 조정(색상·음영 등) 가능  
- 텍스트 포함 이미지 생성  

출처: https://updates.midjourney.com/v7-alpha/

---

### Midjourney v7 예시  
- 실제 같은 촬영 질감과 조명 효과  
- 영화적 분위기, 캐릭터 묘사 정확도 향상  
- 다양한 예술 스타일을 정밀하게 재현 가능  

출처: https://updates.midjourney.com/v7-alpha/

---

## 2-3. Open Source 이미지 생성 모델  
**Stable Diffusion 3 / 3.5 (Stability AI)**

- 출시 시기: 2024년 2월, 10월 공개  
- 오픈소스 가중치 공개 (HuggingFace에서 다운로드 가능)  
- Diffusion Transformer 아키텍처 도입 → 이미지 품질 및 다중 객체 표현 개선  
- 텍스트 및 글자 표현 향상 → 이미지 내 문구 생성 정확도 상승  
- 다양한 크기의 모델 제공 (800M~8B 파라미터)  

**Prompt:** *Photo studio shot of a chameleon*

출처:  
https://huggingface.co/spaces/stabilityai/stable-diffusion-3-5-large  
https://petapixel.com/2024/02/23/stability-ai-preview-next-gen-ai-image-generator-stable-diffusion-3/

---

## 2-3. Open Source 이미지 생성 모델  
**FLUX (Flux.1) – Black Forest Labs**

- 출시 시기: 2024년 8월 공개  
- 일부 상용(Pro) 버전 존재하나 Dev/Schnell은 오픈소스 제공  
- 12억 파라미터 Rectified Flow Transformer 기반 최신 모델  
- 프롬프트 준수, 스타일 다양성, 복잡한 장면 생성에 강점  
- 텍스트 이미지화 성능 우수 → 이미지 안의 글자·숫자 표현 가능  

**모델 변형**
- Pro: 최고 성능 (API 유료)  
- Dev: 오픈 가중치, 연구용(비상업)  
- Schnell: 경량·고속, 오픈소스/상업용 허용  

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

### FLUX (Flux.1) 예시  
- 다양한 예술 스타일, 현실적 조명, 고해상도 묘사 가능  
- 인물, 동물, 건축물, 제품 등 다중 카테고리 표현에 강점  

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

### FLUX (Flux.1) 텍스트 표현 예시
**Prompt:**  
*Latte art in a rich, creamy coffee, with "Stablecog" beautifully inscribed in intricate white foam.*

→ 실제 라떼 거품 위에 정교하게 문구가 새겨진 모습 구현

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

## 2-3. 이미지 생성모델 응용 – 파인튜닝으로 용도 변경  
**ControlNet (2023)**

- 컨트롤 조건 입력을 기반으로 사용자가 원하는 이미지를 생성  
- 커뮤니티 중심으로 매우 활발히 응용되고 있음  
- 입력 예시: Sketch, Normal map, Depth map, Canny edge, Human pose 등  
- 출력 예시: 동일 구조의 다양한 스타일 이미지 생성 가능  

출처: Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, ICCV 2023  

---

### ControlNet 응용 예시 2
- Edge 이미지 + 텍스트 조건을 함께 입력  
- 예시 프롬프트: “a high-quality and extremely detailed image”  
- 다양한 모델(SD 1.5, Comic Diffusion, Protogen 3.4 등)로 각기 다른 스타일 생성  

출처: Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, ICCV 2023

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 노블-뷰 생성 모델 - Zero123XL(콜롬비아 대학; 2023) : 2D에서 3D로 변환
- 2D 이미지를 입력으로 받아 해당 물체를 특정 위치의 카메라 뷰로 바라보았을 때의 모습을 생성하는 모델  
- 추가로 2D 이미지 입력만으로 해당 물체의 3D 전체 모습을 재현할 수 있음  
- 응용 : 3D 모델링, 가상현실(VR) 및 증강현실(AR) 콘텐츠 생성에 사용  

**입력(Input)**  
**합성(Synthesized)**  

Down 30°  Left: 90°

입력 이미지  
3D 영상  

Liu, Ruoshi, et al. "Zero-1-to-3: Zero-shot one image to 3d object." ICCV. 2023.

---

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 정교한 3D Depth map 추정 – Marigold (2024)
- 단안 깊이 추정(monocular depth estimation)을 위해 이미지 생성 Diffusion 모델을 합성데이터에 파인튜닝  

(상단: 원본 이미지 / 하단: 예측된 깊이맵 / 하단부: 3D 복원 결과)

---

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 이미지 & 3D 동시 생성 모델 - JointDiT(Microsoft, POSTECH)
- 출시 시기: 2025년 5월  
- 기능: 이미지와 3D 깊이 맵 동시 생성, 입력 이미지의 3D 추정, 3D 기반 이미지 생성 등 다양한 기능 지원  
- 물리적으로 더욱 그럴듯한 장면 생성  

Byung-Ki et al., JointDiT: Enhancing RGB-Depth Joint Modeling with Diffusion Transformers, arXiv, 2025, https://byungki-k.github.io/JointDiT/

---

# 2-4. 3D 파운데이션 모델

## Depth Anything v2(HKU, TikTok; 2024)
- SAM 이후 연구된 많은 vision foundation 모델 중 깊이맵(depth map) 예측을 위한 모델  
- SAM과 마찬가지로 약 150만 개의 방대한 데이터로 학습됨  
- 이때 약 6,200만개의 라벨링 되지 않은 데이터를 추가로 활용하여 성능 극대화  
- 응용 : 자율주행, 로봇 비전, 3D 복원 등 다양한 작업에서 사용  

입력 영상  
Depth Anything으로 예측한 깊이맵  

출처: https://depth-anything.github.io  

---

# 2-4. 3D 파운데이션 모델

## 사람 중심 모델 - Sapiens(Meta; 2024)
- 인간 형태 인식을 위해 3000만 개의 이미지로 학습된 파운데이션 모델  
- 사람 중심 태스크들  

    - 2D Pose Estimation : 인간의 자세를 예측함  
    - Body-part Segmentation : 신체부위를 구분함  
    - Depth Estimation : 카메라와의 거리를 예측함  
    - Surface Normal Prediction : 3D 모델링을 위해 표면의 법선 방향을 예측함  

Image | Pose | Segmentation | Depth | Normal  

출처: https://github.com/facebookresearch/sapiens  

---

# 2-5. Closed 비디오 생성 모델

## Sora (OpenAI)
- 출시 시기: 2024년 12월 ChatGPT Pro (월 $200) 플랜에 공개. 웹 플랫폼 sora.com을 통해 제공  
  - ChatGPT Plus 사용자는 제한적으로 720p 이용 가능.  
- 텍스트 → 비디오 생성 및 이미지/동영상 → 비디오 확장 모두 지원  
- 최대 1080p, 20초 길이 영상 생성 (Pro 구독 시)  
- ChatGPT와 통합된 대화형 편집·사용자 피드백으로 반복 개선 가능  
- 물리적인 이해를 보여줌 (월드 모델로의 가능성을 보임)  

출처: Brooks et al., “Video generation models as world simulators,” Technical report 2024  

---

# 2-5. Closed 비디오 생성 모델

## Veo 2 (Google Gemini)
- 출시 시기: 2025년 4월 Gemini Advanced 구독자에게 공개  
  - Google AI Studio(Gemini)에 통합  
- 8초 길이, 720p 해상도의 와이드스크린 비디오 생성  
- 생성 영상에는 워터마크가 포함되어 합성 비디오 식별 가능  
- Whisk Animate 기능으로 정적 이미지를 비디오로 변환 가능  
- TikTok, YouTube 등에 바로 공유 가능 편의성 제공  

Prompt: *An animated shot of a tiny mouse with oversized glasses, reading a book by the light of a glowing mushroom in a cozy forest den.*

출처: https://techcrunch.com/2025/04/15/googles-veo-2-video-generator-comes-to-gemini/

---

# 2-5. Closed 비디오 생성 모델

## Veo 3 (Google Gemini)
- 자연스럽게 싱크된 소리까지 같이 생성  

(속보입니다.)

[유튜버 딸깍 디자이너 제공.]

---

# 2-5. Closed 비디오 생성 모델

## 비디오 편집 모델
- Modify Video (Luma Labs)  

(좌: 원본 영상 / 우: 편집 후 영상 예시)

