# git
- 분산 버전 관리 시스템
#### 버전 관리
- 변경될 때 마다의 과정을 전부 기록하는 것은 불가능하고 비효율적이다.
- 변경사항 + 최종 버전 을 기록하여 관리
#### 분산
- 중앙 vs 분산
    - 중앙 집중식 : 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 작업 후 다시 중앙에 업로드
        - 위험하다
        - 동시에 같은 파일을 수정할 경우 충돌 발생 (원본에서 충동이 일어나므로 원본이 손상됨)
    - 분산식 : 버전을 여러 복제된 저장소에 저장 및 관리
        - 서버 컴퓨터에 수정 사항만 저장해 둔다
        - 동시에 같은 파일을 수정하더라도 원본에 영향이 가지 않음
## git의 3가지 영역
1. Working Directory
    - 실제 작업 중인 영역
    - .git
2. Staging Area
    - 위에서 변경된 파일 중, 다음 버전에 대한 포함 여부를 결정할 수 있는 중간 준비 영역
    - SA 영역에 .temp(임시 파일)
    - Repository 에 등록 시 삭제됨
3. Repository
    - 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨
    - commit : 버전
## git의 동작
1. git init : 로컬 저장소 설정(초기화)
    - 버전을 관리하기 위한 .git(숨김) 폴더 생성
    - 해당 폴더 삭제 시 git 내역 삭제
2. git add : 변경사항이 있는 파일을 staging area에 추가
    - git add 파일의경로 : git의 root 부터 경로(00_startCamp/01_git/markdown.md)
3. git commit : staging area에 있는 파일들을 Repository에 기록
    - git commit -m "message" : 기록과 함께 메모
4. git config --global user.email "chl984@naver.com"
    - git config --global user.name "Name"
    - 현재 사용자가 누구인지 전역에 설정
    - code ~/.gitconfig 경로에 저장됨
5. git log : commit 과정을 보여줌
    - Author, Date, message
- 저장연습
---
- 죄측 Sourse Control 에서 시각적으로 확인 가능