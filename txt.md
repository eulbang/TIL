# 📊 Pandas & 시각화 치트시트 (항목별 표)

---

## 🗂 데이터 로드·저장·기본 확인
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`pd.read_csv(path)`** | CSV 불러오기 | `df = pd.read_csv("data.csv")` |
| `df.to_csv(path, index=False)` | CSV 저장 | `df.to_csv("out.csv", index=False)` |
| **`df.info()`** | 컬럼/타입/결측치 요약 | `df.info()` |
| **`df.describe()`** | 숫자형 요약 통계 | `df.describe()` |
| `df.describe(include="object")` | 범주형 요약 통계 | `df.describe(include="object")` |
| `df.head(n)` | 상위 n행 미리보기 | `df.head(5)` |
| `df.shape` / `df.shape[0]` | (행,열) / 행 수 | `rows = df.shape[0]` |

---

## ❓ 결측치·이상치 처리
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`df.isna().sum()`** | 결측치 개수 | `df.isna().sum()` |
| `df.dropna()` | 결측치 있는 행 제거 | `df = df.dropna()` |
| **`fillna()`** | 결측치 대체 | `df["Age"] = df["Age"].fillna(df["Age"].median())` |
| `quantile(p)` | 분위수(Q1,Q3 등) | `Q1 = s.quantile(0.25)` |
| IQR 경계 | 이상치 범위 | `low=Q1-1.5*IQR; up=Q3+1.5*IQR` |
| `loc[조건,"col"]=값` | 이상치 값 치환 | `df.loc[df["Age"]>up,"Age"]=df["Age"].mean()` |

---

## 🔎 선택·필터링·값 치환
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| `df["col"]`, `df[["A","B"]]` | 컬럼 선택 | `df[["Name","Age"]]` |
| **`df[조건]`** | 불리언 필터링 | `df[df["Survived"]==1]` |
| **괄호+`&`/`\|`** | 다중 조건(괄호 필수) | `df[(df["Age"]>=20) & (df["Sex"]=="female")]` |
| **`isin([...])`** | 집합 포함 필터 | `df[df["Pclass"].isin([2,3])]` |
| `loc[조건,"col"]=값` | 조건부 값 변경 | `df.loc[df["Age"]<=10,"Group"]="Child"` |
| **`replace({old:new})`** | 값 치환 | `df["Gender"]=df["Gender"].replace({0:"Female",1:"Male"})` |
| **`map({})`** | 값 매핑(Series) | `df["G"] = df["G"].map({0:"F",1:"M"})` |
| **`value_counts()`** | 빈도/비율/결측 포함 | `s.value_counts(); s.value_counts(normalize=True); s.value_counts(dropna=False)` |
| `mode()[0]` | 최빈값 | `df["Embarked"].mode()[0]` |

---

## 📊 그룹·집계·정렬·형변환
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`groupby("key")["val"].mean()`** | 그룹 평균 | `df.groupby("Pclass")["Fare"].mean()` |
| `sum()/count()/agg([...])` | 합/개수/다중집계 | `df.groupby("G")["X"].agg(["mean","std"])` |
| **`reset_index()`** | groupby 결과 DF화 | `... .reset_index()` |
| **`sort_values(by=, ascending=)`** | 정렬(오/내림) | `df.sort_values(by="Fare", ascending=False)` |
| **`astype(dtype)`** | 형변환 | `monthly["YearMonth"]=monthly["YearMonth"].astype(str)` |
| **`idxmax()`** | 최대값 행 인덱스 | `best = df.loc[df["Rating"].idxmax()]` |
| **`rename(columns={})`** | 컬럼명 변경 | `df.rename(columns={"Fare":"TicketPrice"}, inplace=True)` |
| **`pd.merge(df1, df2, on=, how=)`** | 병합(inner/left/...) | `pd.merge(df1, df2, on="ID", how="inner")` |

---

## ⏱ 시계열·변동률
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`pd.to_datetime(col, format=)`** | 문자열→날짜 | `df["Date"]=pd.to_datetime(df["Date"], format="%Y-%m")` |
| **`.dt.to_period("M")`** | 연-월 추출 | `df["YM"]=df["Date"].dt.to_period("M")` |
| **`rolling(window).mean()`** | 이동평균 | `df["MA20"]=df["Close"].rolling(20).mean()` |
| **`pct_change()*100`** | 변동률(%) | `df["chg"]=df["Close"].pct_change()*100` |
| 교차점 탐지 | MA 교차(골든/데드) | `df["X"]=df["MA5"]-df["MA20"]; df[(X>0)&(X.shift(1)<0)]` |

---

## 🎨 시각화(Matplotlib/Seaborn) — 그래프 생성
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`plt.figure(figsize=(w,h))`** | 도화지 생성 | `plt.figure(figsize=(12,6))` |
| **`sns.countplot(x=, data=)`** | 범주 개수 | `sns.countplot(x="Category", data=df)` |
| **`sns.barplot(x=, y=, data=, estimator=)`** | 막대(평균/합계) | `sns.barplot(x="Category", y="Value", data=df, estimator=sum)` |
| **`sns.histplot(s, bins, kde=True)`** | 히스토그램+KDE | `sns.histplot(df["Age"], bins=30, kde=True)` |
| **`sns.boxplot(x=, y=, data=)`** | 박스플롯 | `sns.boxplot(x="Group", y="Score", data=df)` |
| **`sns.violinplot(x=, y=, data=)`** | 바이올린 | `sns.violinplot(x="Gender", y="Height", data=df)` |
| **`sns.scatterplot(x=, y=, hue=, data=)`** | 산점도 | `sns.scatterplot(x="A", y="B", hue="G", data=df, alpha=0.7)` |
| **`sns.lineplot(x=, y=, hue=, data=, marker="o")`** | 선 그래프 | `sns.lineplot(x="Year", y="GDP", hue="Country", data=df, marker="o")` |
| **`sns.heatmap(df.corr(), annot=True)`** | 상관 히트맵 | `sns.heatmap(df.corr(), annot=True, cmap="coolwarm")` |
| `Series.plot(kind="barh"/"line")` | 시리즈 빠른 플롯 | `weekday_agg.plot(kind="barh")` |

---

## 🛠 시각화(Matplotlib/Seaborn) — 라벨·격자·스케일
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`plt.title(txt, fontsize=)`** | 제목 | `plt.title("월별 매출", fontsize=14)` |
| **`plt.xlabel(txt)` / `plt.ylabel(txt)`** | 축 레이블 | `plt.xlabel("연-월"); plt.ylabel("매출")` |
| **`plt.xticks(rotation=deg)`** | 눈금 라벨 회전 | `plt.xticks(rotation=45)` |
| **`plt.legend(title=, bbox_to_anchor=, loc=)`** | 범례/위치 | `plt.legend(title="Country", bbox_to_anchor=(1.05,1), loc="upper left")` |
| **`plt.grid(True, linestyle="--", alpha=0.6)`** | 격자 | `plt.grid(True, linestyle="--", alpha=0.6)` |
| **`plt.xscale("log")` / `plt.yscale("log")`** | 로그 축 | `plt.xscale("log"); plt.yscale("log")` |
| **`plt.show()`** | 그래프 렌더링 | `plt.show()` |

---

## 🧭 Plotly (대화형 3D·애니메이션)
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`px.scatter_3d(df, x=, y=, z=, color=, size=, hover_name=)`** | 3D 산점도 | `fig = px.scatter_3d(data, x="Population", y="GDP", z="LifeExpectancy", color="Country", size="Population", hover_name="Country")` |
| **`fig.update_traces(marker=dict(size=..), selector=...)`** | 트레이스 속성 업데이트 | `fig.update_traces(marker=dict(size=5), selector=dict(mode="markers"))` |
| **`fig.show()`** | Plotly 그래프 표시 | `fig.show()` |
| `animation_frame=` / `animation_group=` | 프레임/그룹 지정 | `px.scatter_3d(..., animation_frame="Year", animation_group="Country")` |

---

## 🔤 기타 유틸·출력
| 문법/함수 | 설명 | 예제 |
|---|---|---|
| **`astype(str/int/float)`** | 자료형 변환 | `monthly["YM"] = monthly["YM"].astype(str)` |
| **`f-string`** | 포맷 출력 | `print(f"평균: {avg:.2f}")` |
| **`input(prompt)`** | 사용자 입력 받기 | `name = input("이름: ")` |
| `min()/max()/len()` | 최솟값/최댓값/길이 | `len(outliers)` |
