# 학생들의 이름과 점수를 딕셔너리에 저장하시오.
#    "Alice" = 85,
#    "Bob" = 78,
#    "Charlie" = 92,
#    "David" = 88,
#    "Eve" = 95
# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.

# '''
# 학생 점수 정보
#    "Alice" = 85,
#    "Bob" = 78,
#    "Charlie" = 92,
#    "David" = 88,
#    "Eve" = 95
# '''

# 아래에 코드를 작성하시오.

score = {'Alice':85, 'Bob':78, 'Charlie':92, 'David':88, 'Eve':95}

def avg(score):
    av = 0
    for i in score:
        av += score.get(i)
    return av/len(score)

av = avg(score)
print(f"평균 점수 : {av}")
highscr = list(i for i in score if score.get(i)>=80)
print(f"80점 이상 받은 학생 : {highscr}")
srt = dict(sorted(score.items(), key=lambda item: item[1], reverse=True))
print(f"점수 내림차순 : {list(srt.values())}")
gap = max(score.values()) - min(score.values())
print(f"최고 점수차 : {gap}")
gdjb = {}
for i in score:
    if score[i] > av:
        gdjb[i] = score[i]
result = ', '.join(f"{name}: {score}" for name, score in gdjb.items())
print(f"80점 이상 점수자: {result}")