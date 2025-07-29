def clean_name(name):
    """
    이름의 앞뒤 공백을 제거하고, 첫 글자만 대문자로 바꿉니다.
    (예: "  heLLo " -> "Hello")
    """
    name = name.strip() # 앞뒤 공백 제거
    name = name.capitalize() # 첫 글자 대문자로 변경
    return name # 결과 반환

def make_greeting(name):
    """
    정리된 이름을 받아 "안녕하세요, [이름]님!" 형식의 문자열로 만듭니다.
    (예: "홍길동" -> "안녕하세요, 홍길동님!")
    """
    name = (f"안녕하세요, {name}님!") # f-string 사용하여 문장 수정
    return name # 결과 반환

def process_namelist(name_list):
    """
    전체 이름 리스트를 받아, 비어있지 않은 이름만 골라 인사말로 만들어
    리스트로 반환합니다.
    (이름이 공백으로만 이뤄진 경우는 무시합니다.)
    위에 작성한 함수들을 적절히 활용해야 합니다.
    """
    resultList = []
    for name in name_list:
        name = clean_name(name)
        if name != '' :
            resultList += [make_greeting(name)]
    return resultList
# ----------------------------------------------------
# 아래 코드는 절대 수정하지 마시오.
# ----------------------------------------------------
raw_names = [
    "  홍길동",
    "김싸피 ",
    "   ",
    "lee sunsin"
]
result = process_namelist(raw_names)
print(result)
