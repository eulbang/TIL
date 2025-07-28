# JaveScript
### History of JavaScript
#### ECMAScript
- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
  - 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공
- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행됨
  - ECMAScript는 JavaScript의 표준이며, JavaScript는 ECMAScript 표준을 따르는 구체적인 프로그래밍 언어
  - ECMAScript는 언어의 핵심을 정의하고, JavaScript는 ECMAScript 표준을 따라 구현된 언어로 사용됨
#### ECMAScript의 역사
- ECMAScript 5(ES5)에서 안정성과 생산성을 크게 높임(2009)
- ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가됨(2015)
### 변수
- 식별자(변수명) 작성 규칙
  - 반드시 문자, 달러('$') 또는 밑줄('_')로 시작
  - 대소문자를 구분
  - 예약어 사용 불가
- 식별자(변수명) Naming case
  - 카멜 케이스(camelCase)
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스(PascalCase)
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수에 사용
- 변수 선언 키워드 3가지
  1. let
    - 블록 스코프(block scope)를 갖는 지역 변수를 선언
    - 재할당 가능
    - 재선언 불가능
    - ES6에서 추가
  2. const
    - 블록 스코프(block scope)를 갖는 지역 변수를 선언
    - 재할당 불가능 (선언 시 반드시 초기값 설정 필요)
    - 재선언 불가능
    - ES6에서 추가
  3. var
  - 블록 스코프 (block scope)
    - if, for, 함수 등의 **'중괄호({}) 내부'**를 가리킴
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
  - 기본적으로 const 사용을 권장
  - 재할당이 필요하다면 그때 let으로 변경해서 사용
### 데이터 타입
- 원시 자료형 : 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
  - Number
    - 정수 또는 실수형 숫자를 표현하는 자료형
  - String
    - 텍스트 데이터를 표현하는 자료형
    - '+' 연산자를 사용해 문자열끼리 결합
    - 뺄셈, 곱셈, 나눗셈 불가능
    - Template Literals (템플릿 리터럴)
      - 내장된 표현식을 허용하는 문자열 작성 방식
      - Backtick('')을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
      - 표현식은 '$'와 중괄호(${expression})로 표기
  - Boolean
  - null : 값이 없음
    - null 의 타입이 object 로 출력 - 버그
  - undefined : 할당조차 안됐음
- 참조 자료형 : 객체의 주소가 저장되는 자료형(가변, 주소가 복사)
  - Objects(Object, Array, Function)
### 연산자
- 할당 연산자
- 증감 연산자
- 비교 연산자
- 동등 연산자
  - '암묵적 타입 변환' 통해 타입을 일치시킨 후 같은 값인지 비교
- 일치 연산자 (===) : 주로 사용
- 논리 연산자
### 제어문
#### 조건문
- if
  - else if
  - else
- 삼항 연산자
  - condition ? expression1 : expression2
#### 반복문
- while
- for
- for...in
  - 객체의 열거 가능한 속성에 대해 반복
  - 키 반복
- for...of
  - 반복 가능한 객체(배열, 문자열 등)에 대해 반복
  - 값 반복
## DOM
- document 객체
- 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
- DOM API
  - 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공
- DOM 특징
  - DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
  - 모두 document 객체의 하위 객체로 구성됨
- DOM tree
  - 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화
    - 객체 간 상속 구조가 존재
### DOM 선택
- 선택 메서드
- document.querySelector()
  - 요소 한 개 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element를 선택
- document.querySelectorAll()
  - 요소 여러 개 선택
  - 제공한 CSS selector를 만족하는 NodeList를 반환
### DOM 조작
- 속성 조작
  - 클래스 속성 조작
  - 'classList' property : 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
    - element.classList.add()
      - 지정한 클래스 값을 추가
    - element.classList.remove()
      - 지정한 클래스 값을 제거
    - element.classList.toglle()
      - 클래스가 존재한다면 제거하고 false를 반환
      - 클래스가 존재하지 않으면 추가하고 true를 반환
  - 일반 속성 조작
    - Element.getAttribute()
      - 해당 요소에 지정된 값을 반환 (조회)
    - Element.setAttribute(name, value)
      - 지정된 요소의 속성 값을 설정
      - 속성이 이미 있으면 기존 값을 갱신
        - 그렇지 않으면 지정된 이름과 값으로 새 속성이 추가
    - Element.removeAttribute()
      - 요소에서 지정된 이름을 가진 속성 제거
- HTML 콘텐츠 조작
- DOM 요소 조작
  - document.createElement(tagName)
    - 작성한 tagName의 HTML요소를 생성하여 반환
  - Node.appenChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 추가된 Node 객체를 반환
  - Node.removeChile()
    - DOM에서 자식 Node를 제거
    - 제거된 Node를 반환
- style 조작
### 함수
- Function : 참조 자료형에 속하며 모든 함수는 Function object
- 함수 정의
  - function name ([param],..) {return value}
  - return 값이 없다면 undefined를 반환
  - 선언식/표현식
  - 함수 표현식 특징
    - 함수 이름이 없는 '익명 함수'를 사용할 수 있음
    - 선언식과 달리 표현식으로 정의한 함수는 **호이스팅** 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음
- 매개변수
  1. 기본 함수 매개변수
  2. 나머지 매개변수
    - 임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타내는 방법
  - 매개변수 > 인자
    - 누락된 인자는 undefined로 할당
  - 매개변수 < 인자
    - 초과 입력된 인자는 사용하지 않음
- Spread syntax : '...' : 전개 구문
  - 전개 구문 활용처
    1. 함수와의 사용
      - 함수 호출 시 인자 확장
      - 나머지 매개변수(압축)
    2. 객체와의 사용
    3. 배열과의 사용
- 화살표 함수 : 함수 표현식의 간결한 표현법
  - function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
  - const arrow = name => 'hello, ${name}'
  - **object를 다룰 때 신경 쓸 부분이 줄어든다**
#### 세미콜론 (semicolon)
- 자바스크립트는 문장 마지막 세미콜론(';')을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
- JavaScript를 만든 Brendam Eich 또한 세미콜론 작성을 반대
### 이벤트
- 무언가 일어났다는 신호, 사건
- 웹에서의 모든 동작은 이벤트 발생과 함께 한다.
- 'event' object
  - DOM 에서 이벤트가 발생했을 때 생성되는 객체
  - mouse, input, keyboard, touch ...
- .addEventListener()
  - 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
  - EventTarget.addEventListener(type, handler)
    - type
      - 수신할 이벤트 이름
      - 문자열로 작성
    - handler
      - 발생한 이벤트 객체를 수신하는 콜백 함수
      - 콜백 함수는 발생한 event object를 유일한 매개변수로 받음
- event handler
  - 이벤트가 발생했을 때 발생하는 함수
  - 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것
- 버블링
  - 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러 뿐만 아니라 부모 요소의 핸들러가 동작하는 현상
  - 반대 : 캡처링
### enevt handler 활용
### 이벤트 기본 동작 취소
- HTML의 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되어 기본 동작을 취소할 필요가 있음
- .preventDefault() : 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정