- 프로젝트 싸피 = SSAFY GIT
- add, commit 과정 중요하게 생각해야 함
- 과제 하나당 프로젝트 하나
    - 과제 하나당 git 하나이기 때문에 따로 관리 필요
    - git 안에 git 사용 X : SubModule : 별도의 원격 저장소 연결 필요
    - 실수로 넣었을 경우 밖으로 빼고
        - git add .
        - commit -m "delete submodule"
- 커밋 로그 그래프로 보는 법
    - git log --onelint --graph
---
## 커밋 실수
    - git commit
        - 제목 없이 커밋해버릴 경우 vim(메모장)이 열림
        - :q
            - 탈출버튼
        - 커밋 메시지가 없으므로 커밋 할 수 없음
        - 다시 메시지와 함께 커밋하면 됨
## push 가 안되는 경우
    - git push origin master
    - 로컬의 커밋 내역과 서버의 커밋 내역이 다를 경우 오류 출력
    - 현재 로컬이 업데이트 되지 않은 상태
    - git pull : 업데이트 후 재시도
## branch
    - 가지
    - 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git 의 도구
    - 장점
        1. 독립된 개발 환경을 형성하기 때문에 원본에 대해 안전
        2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능
        3. 손쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있음
#### branch 문법
    - git branch
        - 현재 branch 목록을 출력
    - git branch -c viktor/login
        - viktor 가 login 기능을 만들기 위한 branch 를 create 하겠다
    - git switch viktor/login
        - viktor/login 브랜치로 바꾸겠다
        - **브랜치를 바꾸더라도 파일을 볼 수 있다**
    - git merge viktor/login
        - viktor/login 에서 작업된 내용을 현재 위치(master)로 병합한다
        - 브랜치 간 머지 가능
            - git merge master
        - (master|MERGING) : 컨플릭트 상태
    - git branch -d viktor/login
        - viktor/login 브랜치를 삭제한다
    - conflict : 서로 다른 작업자가 동일한 파일을 수정하였을 때 나타나는 충돌현상
        - 결정권자의 수정이 필요함
        - resolve conflict : 없는 버튼
        - resolve locally : 로컬에서 수정
---
1. master 브랜치는 아무도 수정하지 않는다.
2. master 브랜치는 최초 설정 (모든 팀원이 함께 쓸 내용 생성시만 사용)
    - git add . git commit, push 까지 모두 진행
3. develop (혹은 dev) 브랜치를 생성한다.