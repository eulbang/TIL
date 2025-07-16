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
    - 잘못 추가했을 경우 git restore --staged filename
    - **git add . : 현재 위치 기준으로 전체 내용 등록 가능**
3. git commit : staging area에 있는 파일들을 Repository에 기록
    - git commit -m "message" : 기록과 함께 메모
4. git config --global user.email "chl984@naver.com"
    - git config --global user.name "Name"
    - 현재 사용자가 누구인지 전역에 설정
        - 필요 시 global 대신 local 가능
    - code ~/.gitconfig 경로에 저장됨
5. git log : commit 과정을 보여줌
    - Author, Date, message
6. git remote add origin https~ : 원격 저장소를 origin 으로 부를 수 있도록 추가함
    - gir remote -v : 추가가 정상적으로 됐는지 확인
7. git push -u origin master : 로컬의 브랜치를 origin 에 master 가 작업한 것을 넣는다
    - 이후부턴 git push 만으로 작동 가능하다
    - **git push origin master 추천**
## Remote Repository
- 원격 저장소
    - 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
1. **GitLab**
    - private 한 공간
    - 수업용
2. GitHub
    - public 한 공간
    - 포폴용
## TIL
- Today I Learned
- GitHub로 관리
---
집에서 하는 숙제 이건 숙제 홈워크
---
- 죄측 Sourse Control 에서 시각적으로 확인 가능