- 생성형 AI의 문제점
  - 오래된 정보 (Outdated information)
  - 도메인 특화 능력 부족
  - 거짓말을 잘한다 (Hallucination)
  - 지식 매개변수화(parameterizing knowledge) 효율성이 낮음

- 실제 우리의 요구사항
  - 도메인별 정확한 답변
  - 빈번한 데이터 업데이트
  - 생성된 콘텐츠의 추적성 및 설명성
  - 데이터의 개인정보 보호

- RAG 이해를 위한 이론  
  - RAG의 장점  
    - 환각 현상 (Hallucination) 감소  
    - 도메인 적용성 개선  
    - Open domain QA 성능 향상  
    - 참고한 Knowledge base가 적절한지 판단 가능  
    - 정보 검색에 강함  

- RAG 이해를 위한 이론  
  - 정보 검색(Retrieval)  
    - 필요한 정보를 검색하는 작업  
    - 데이터베이스, 인터넷, 또는 다른 정보 저장소에서 관련 정보를 찾아내는 과정  
    - 사용자의 쿼리에 가장 잘 맞는 데이터를 식별하고 추출하는 기술과 알고리즘  
    - 웹 검색 엔진, 디지털 도서관, 온라인 데이터베이스, 정보 검색 시스템 등 다양한 분야에서 중요한 역할 수행  

- RAG 이해를 위한 이론  
  - 역색인(Inverted Index)  
    - 색인: 1 -> 1페이지 호출, 100 -> 100페이지 호출  
    - 각 데이터에 빠르게 접근할 수 있도록 도움  
    - 역색인: "학교" -> 3, 49, 100 페이지  
    - 각 단어로 색인 정보를 연결 시켜 놓음으로 단어 기반 검색이 가능하게 함  

- RAG 이해를 위한 이론  
  - BM25  
    - TF-IDF의 정보검색에서의 단점을 보완  
    - Q: 사용자가 입력한 쿼리  
    - D: 대조해보려는 문서  
    - 대부분의 텍스트 기반 검색을 진행할 때 가장 자주 쓰이는 방식  

- RAG (Retrieval-Augmented Generation)
  - Retrieval (검색): 외부 데이터 및 소스를 검색하여 정보 획득
  - Augmented (증강): 사용자의 질문을 보강하여 보다 정확한 문맥 제공
  - Generation (생성): 향상된 정보를 기반으로 더 좋은 답변 생성
  - 답변할 때 확실한 출처를 기반으로 생성하게 됨

- RAG 이해를 위한 이론
  - RAG
    - RAG(Retreival-Augmented-Generation)
    - 정보 검색(retrieval)과 응답 생성(generation)을 결합한 모델
    - 사용자의 질문이 주어지면, Retriever는 관련된 정보나 문서를 데이터베이스에서 검색
    - 검색된 정보로 질문에 대한 답변 생성
    - 보다 풍부하고 정확한 정보를 제공 가능

- LangChain이란?
  - ChatGPT 프로그램 안에서 벗어나 LLM의 기능을 나만의 코드(Javascript/Python)으로 가져와서 이를 자유자재로 사용할 수 있게 해주는 강력한 "프레임워크"
  - LLM으로 하는 모든 것을 LangChain을 통해서 할 수 있음을 의미
    - 프롬프트 엔지니어링
    - RAG(Retrieval Augmented Generation)
    - Agent
    - 외부 LLM API 사용 및 Local LLM 구동
    - Moderation
    - ...

- LLM : 초거대 언어모델로, 생성 모델의 엔진과 같은 역할을 하는 핵심 구성 요소
  - 예시: GPT-4, PALM, LLAMA, Deepseek ...

- Prompts : 초거대 언어모델에게 지시하는 명령문
  - 예시: Prompt Templates, Chat Prompt Template, Example Selectors, Output Parsers

- Index : LLM이 문서를 쉽게 탐색할 수 있도록 구조화 하는 모듈
  - 예시: Document Loaders, Text Splitters, Vectostores, Retrievers

- Memory : 채팅 이력을 기억하도록 하여 이를 기반으로 대화가 가능하도록 하는 모듈
  - 예시: ConversationBufferMemory, Entity Memory, Conversation Knowledge Graph Memory

- Chain : LLM 사슬을 형성하여 연속적인 LLM 호출이 가능하도록 하는 핵심 구성 요소
  - 예시: LLM Chain, Question Answering, Summarization, Retrival Question/Answering

- Agents : LLM이 기존 Prompt Template으로 수행할 수 없는 작업을 가능케 하는 모듈
  - 예시: Custom Agent, Custom MultiAction Agent, Conversation Agent

- LLM 추상화(Abstraction) 제공
  - 추상화(Abstraction)란 사용자에게 불필요한 세부 사항을 숨겨 복잡성을 처리하는 것
  - 사용자는 숨겨진 복잡성을 모두 이해하거나 생각하지 않고 제공된 추상화에서 나만의 로직 구현 가능
  - Language Model + Chain = LangChain
    - 언어모델(Language Model)을 연결(Chain)하여 애플리케이션 구축 가능
    - 모든 LLM 모델을 자세히 공부하지 않고도 간단히 접속을 위한 API 키를 통해 사용 가능

- AI Agent에 대하여
  - AI Agent란?
    - ChatGPT는 AI Agent의 하위 개념 또는 구성 요소로 볼 수 있으며, 단순히 텍스트를 생성하는 언어모델
    - AI Agent는 ChatGPT 같은 LLM을 코어 엔진으로 활용되며, 추가적으로 툴 사용, 계획, 자율적 실행 기능이 결합된 시스템

  - AI agent vs. ChatGPT
    - AI agent
      - 자율성과 상호작용 능력
      - 사용자가 요구한 작업의 완료를 위해 활용 가능한 여러 도구와의 상호작용을 연쇄적으로,
        자율적으로 수행할 수 있는 기술
    - ChatGPT
      - 주로 단일 플러그인을 사용하여 질문에 답변
      - 기본 ChatGPT는 툴과 직접 상호작용하지 않음
