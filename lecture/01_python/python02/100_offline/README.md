# 온라인 실습실을 활용한 원격 저장소 사용하기

1. git clone을 통해서 원격 저장소의 내용을 로컬 PC에 내려받기
  - 실습을 위해 생성된 원격 저장소란?
    - 우리가 일반적으로 직접 생성한 원격 저장소랑 완전히 동일하다.
    - 그런데, 사용하는데 있어서 헷갈리는 이유는 뭐냐?
      - git init 명령어는 이제 뭐하는 용도인지 알 것 같다.
      - local에 만든 폴더에서 명령창에 git init을 작성하면 이제 그곳이 git으로 관리되는 곳이 되니까!
      - 원격 저장소... (내가 만든거 아님!) -> git으로 관리가 되고 있는것인가?
        - 이 부분이 안보임!
  - 원격 저장소는
    - git으로 관리되고 있는 폴더 통째로 드라이브에 업로드 한 것.
    - 따라서, 현재 폴더 `lectures/01_python/python02/100_offline` 위치에서 
      - git clone {원격 저장소 주소} 명령어를 입력한다는 것은
      - 그 원격 저장소에서 git으로 관리하고 있는 폴더를 `현재 위치`에 다운로드 받는것.
      - 다운 받은 순간의 그 폴더명은 무엇으로 정해지는가?
        - 원격 저장소 repository (project)의 이름이 폴더 이름이 된다.

2. 과제를 완료하고 난 후에, 이 완료된 정보를 원격 저장소에 업로드 해야한다.
  - 그렇다면, 이때 git add, git commit을 해야하는 위치는 어디인가?
  1. lectures(혹은 study or TIL, 또는 다양한 이름의 내 공부용 원격 저장소) 폴더 위치
  2. ws_a 폴더 이냐 -> 어.. 당연히 ws_a 위치에서 해야하는 것!!!
    ???: 2번이요! 
  - 잘 알고있지만, 우리는 실수를 하기 마련이다. 무슨 실수를 하느냐?
    - 작업 위치를 확인하지 않고 git add, git commit 하게 된다.
    - 왜 그런가? 하니... 현재 작업 위치를 보자면...
      ` ~/Desktop/lectures/01_python/python02/100_offline (master)`
    -  어? `(master)` 달려있네? git으로 관리중이네...? 이곳에서 git add ... 어쩌구...
    - 과제 제출용 원격 저장소가 아닌 lectures에 업로드하게 된다.
  3. 문제 상황 발생
    - lecture 위치에서 git add 를 하고나서 생각하니, 과제 제출위치가 아니다.
    - 부랴부랴 과제 제출 위치로 옮겨가서 git commit 했지만 안된다.
    - 왜 안되냐?
      - 과제 폴더를 담당하고 있는 git에는 add 한 적이 없다.
      - 따라서, 과제 폴더 담당 git은 commit을 할 수가 없다.

3. 올바른 위치 (과제 담당 폴더에서) git add, commit, push를 완료하고 난 후에 `.git`을 삭제한다.
  - 이때는 과제를 올바른 위치에 제출을 마쳤으니,
  - 내 컴퓨터에 있는 `.git` 폴더는 삭제해도 된다.
    - 물론, 일반적인 상황은 절대 아님! 
    - 일반적으로 이 `.git`을 지울일은 없습니다. 프로젝트 자체를 지웠으면 지웠지...
  - 그럼 일반적이지 않은 이 행위를 우리는 왜 해야 하는까?
  - 지금 공부하고 있는 이 폴더 (TIL or Study, lecutres 등)을 나의 다른 원격 저장소에 업로드하기 위해서
    - 과제 폴더 담당 `.git` 을 제거하지 않으면, submodule이 되어서,
    - 내 공부 폴더의 담당자 `.git` 은 과제 폴더 내의 수정 사항을, 과제 폴더 담당 .git에게 맡긴다.

4. 내 공부용 폴더 담당 `.git` 에게도 현재의 변동사항을 알려주고, add, commit, push