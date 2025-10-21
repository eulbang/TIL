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

