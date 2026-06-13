[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qR-atX5d)
# 🐍 [2026-01] 나만의 파이썬 소프트웨어 개발 프로젝트

## 1. 시나리오 제목
* 급등주 포착 단타 시그널 분석기 (Momentum Scalping Signal Scanner)
<br>


## 2. 시나리오 (5~10줄)
이 프로그램은 단타(스캘핑) 투자자를 위해, 입력한 종목의 시세·거래량 데이터를 바탕으로
**"지금 들어갈 만한 급등주인가?"** 를 자동으로 점수화·등급화하는 시그널 분석 시스템이다.

사용자는 **종목명, 현재가, 전일 종가, 당일 거래량, 평소 거래량**을 입력한다. 시스템은
**등락률**과 **거래량 급증 배수**를 계산해 종합 **'급등 점수'** 를 산출하고, 점수 구간에 따라
시그널 등급(**S 강력급등 / A 단타후보 / B 관망 / C 회피**)을 부여한다.

또한 등락률과 거래량이 동시에 폭증하는 복합 조건(예: 등락률 15%↑ **AND** 거래량 3배↑)을
만족하면 **'🚀 단타 진입 시그널'** 뱃지를 부여하고, 목표가·손절가 기준 **모의 수익률**을 계산한다.

최종적으로 사용자는 메뉴를 통해 여러 종목을 **워치리스트(리스트)** 로 관리하고, 급등주만
필터링해 조회할 수 있는 시스템으로 완성하는 것을 목표로 한다.


## 3. 예상 기능 및 메뉴 (최소 5개)
1 --- 종목 시세 입력      (등락률 · 거래량배수 · 급등점수 계산)
2 --- 워치리스트 전체 스캔  (시그널 등급 일괄 판별)
3 --- 급등주만 필터링 출력  (조건별 종목 추출)
4 --- 단타 진입 시그널 확인 (복합조건 뱃지 + 모의 수익률)
5 --- 워치리스트 전체 정보 출력
0 --- 종료

# 🚀 [버전별 개발 일지 & AI 협업 기록]

## 🟦 [1차 과제: V1.0] 시나리오 기획
    
### ✨ V1.0 개발 내용

- 사용자로부터 **종목명(문자열)**, **현재가·전일 종가(실수)**, **당일·평소 거래량(정수)** 을
  입력받는 화면을 구현했다. (변수 5개 이상, 자료형 3종 `str`/`int`/`float` 충족)
- 산술 연산을 활용해 아래 핵심 지표를 계산하고 f-string으로 정렬 출력했다.
  - **등락률(%)** = (현재가 − 전일종가) / 전일종가 × 100
  - **거래량 배수** = 당일 거래량 / 평소 거래량
  - **급등 점수** = 등락률 + (거래량 배수 − 1) × 5
  - **목표가(+5%)** / **손절가(−3%)** = 현재가 × 1.05 / 현재가 × 0.97
- 이번 단계에서는 조건문·반복문 없이 **'변수 선언'과 '입출력·산술'만** 사용했다.

### 🤖 AI 파트너십 과정

**1. 주제 구체화 (관심사 접목형)**
- **프롬프트 요약:** "주식 단타(급등주)에 관심이 많다. '성적 관리 프로그램'이 1차(점수 입력)→
  2차(학점 계산)→3차(메뉴판)→4차(배열 확장)로 발전한 것처럼, 단타 급등주 주제를 4단계
  파이썬 구조에 맞춰 기능 확장 로드맵으로 기획해 달라."
- **적용 내용:** 단순 가격 계산기를 넘어, **'시세 입력(1차) → 시그널 등급 판별(2차) →
  워치리스트 메뉴(3차) → 함수·딕셔너리 관리(4차)'** 로 이어지는 로드맵과 예상 메뉴를 확립함.

**2. 1차 변수·자료형 설계 (세부 설계형)**
- **프롬프트 요약:** "1차 과제 필수 요건(변수 5개 이상, 자료형 3종 이상)을 충족하려면 급등주
  데이터를 어떤 변수와 자료형으로 모델링해야 하나? 조건문 없이 등락률·급등점수를 계산하는
  방법은?"
- **적용 내용:** '시세'를 뭉뚱그린 변수 하나 대신, 데이터 특성에 맞춰 **문자열(종목명),
  실수(가격·등락률), 정수(거래량)** 로 자료형을 명확히 분리. '지난 학기 평균과의 차이'를
  **'전일 종가 대비 등락률'** 로 치환해 1차 산술 연산 요건을 자연스럽게 충족시킴.

### 🔧 Troubleshooting & 기술 회고

1. **문제 1:** `input()`은 항상 문자열을 반환해서, 가격끼리 뺄셈하면 오류가 났다.
   - **해결:** AI에게 질문하여 `float(input(...))`처럼 입력 즉시 형변환해야 한다는 것을 학습,
     가격·거래량 입력부를 모두 형변환하도록 수정.
2. **문제 2:** 등락률·급등 점수의 소수점이 너무 길게 출력됐다.
   - **해결:** f-string 서식 지정자 `{change_rate:+.2f}%`, `{surge_score:.1f}점` 을 적용해
     소수점 자릿수를 정리하고, `{now_price:,.0f}원` 으로 천 단위 콤마를 추가해 가독성을 높임.

### **📁 증빙 자료:**
<img width="1591" height="789" alt="스크린샷 2026-05-25 225440" src="https://github.com/user-attachments/assets/959595a9-9975-4624-a06e-3acc1f597b2d" />
<img width="1660" height="1283" alt="스크린샷 2026-05-25 225424" src="https://github.com/user-attachments/assets/b817eb3c-9ae6-4fed-9cdf-81edfc4ca2b6" />
<img width="995" height="683" alt="스크린샷 2026-05-25 225729" src="https://github.com/user-attachments/assets/f23cb0b5-a5f2-4be4-aedd-d2900b2c4946" />
<img width="1570" height="998" alt="스크린샷 2026-05-25 225552" src="https://github.com/user-attachments/assets/ca66f7dd-d712-4ceb-8171-cb2b6e686d60" />




<br>

## 🟩 [2차 과제: V1.0] 입출력 + 리스트 + 조건문 - 향후 작성 예정
### ✨ V2.0 개발 내용

- 종목을 개별 변수가 아닌 **4개의 병렬 워치리스트**(`names`/`scores`/`grades`/`badges`)에 저장하도록 구조를 바꿨다.
- **`for i in range(n)`** 반복으로 여러 종목의 시세를 연속 입력받고, 1차의 산술 로직(등락률·거래량배수·급등점수)을 그대로 재사용했다.
- **`if-elif-else`** 로 급등 점수를 4단계 시그널 등급으로 판별한다.
  - **S 강력급등**: 점수 ≥ 20  ·  **A 단타후보**: ≥ 10  ·  **B 관망**: ≥ 0  ·  **C 회피**: < 0
- 등락률·거래량이 동시에 폭증하는 **복합 조건(`change_rate >= 15 and volume_ratio >= 3`)** 을 만족하면 `🚀단타진입` 뱃지를 부여했다. (`and`, 관계연산자 `>=`)
- 리스트 관리: **S등급은 `insert(0, …)`** 로 워치리스트 맨 위에 고정, 그 외는 **`append()`** 로 뒤에 추가. 통계는 `len()`·`sum()`·`max()` 로 산출하고, **슬라이싱 복사(`scores[:]`)** 한 사본을 정렬해 원본 입력 순서를 보존한 채 점수 순위를 출력한다. (`not`, `!=`, `+=` 도 통계 집계에 사용)

### 🤖 AI 파트너십 과정

**1. 자료구조 전환 설계 (리스트 모델링)**
- **프롬프트 요약:** "1차에선 종목 하나를 개별 변수로 받았는데, 여러 종목을 다루려면 어떻게 저장하나? 딕셔너리는 아직 안 배웠고 리스트만 써야 한다."
- **적용 내용:** 종목명·점수·등급·뱃지를 **같은 인덱스끼리 대응되는 4개의 병렬 리스트**로 모델링. (4차에서 종목 1개 = `dict` 1개로 묶을 예정임을 미리 메모)

**2. 등급 경계값(임계치) 설계**
- **프롬프트 요약:** "급등 점수를 S/A/B/C로 나누는 `if-elif-else` 경계값을 어떻게 잡아야 직관적일까?"
- **적용 내용:** 거래량이 평소(배수 1)이고 등락률 0이면 점수 0 → **B(관망)** 가 되도록 0을 기준선으로 잡고, 단타후보 10·강력급등 20으로 단계화.

### 🔧 Troubleshooting & 기술 회고

1. **문제 1:** `elif` 를 작은 값부터(`>= 0` 먼저) 써서 모든 종목이 B로만 분류됐다.
   - **해결:** 비교는 **큰 임계치부터** 내려와야 함을 학습, `>= 20 → >= 10 → >= 0 → else` 순으로 재배치.
2. **문제 2:** 통계용으로 점수 리스트를 `.sort()` 했더니 **원본 입력 순서가 깨졌다.**
   - **해결:** `ranking = scores[:]` 로 **슬라이싱 복사**한 사본만 정렬해 원본 워치리스트는 그대로 유지.

### **📁 증빙 자료:**

<img width="1681" height="1030" alt="스크린샷 2026-05-25 225433" src="https://github.com/user-attachments/assets/8ab1572d-3749-4d72-bc3f-97414d67c20c" />
<img width="995" height="683" alt="스크린샷 2026-05-25 225729" src="https://github.com/user-attachments/assets/a821d12c-c5e1-4101-8903-3f9c00a935fb" />


## 🟨 [3차 과제: V3.0] 무한 루프와 메뉴 시스템 (반복문) - 향후 작성 예정

### ✨ V3.0 개발 내용

- **`while True` 무한 반복**으로 메뉴를 계속 띄우고, `0`(종료) 선택 시 **`break`** 로 빠져나가는 대화형 콘솔로 완성했다.
- 메뉴 5종 + 종료로 1·2차 기능을 통합 운영한다.
  - `1` **종목 시세 입력** — 1차 산술 + 2차 등급/뱃지 판별을 수행해 워치리스트에 누적
  - `2` **전체 스캔** — **`for` 순회**로 모든 종목의 등급을 일괄 출력
  - `3` **급등주 필터링** — `for` + 조건(`grades[i] == "S" or grades[i] == "A"`)으로 강력급등·단타후보만 추출
  - `4` **단타 진입 시그널** — `🚀단타진입` 뱃지 종목만 골라 진입가·목표가(+5%)·손절가(−3%) 모의 계산
  - `5` **전체 정보** — 현재가·등락률·거래량배수·점수·등급 표 + 평균/최고 통계
- 빈 워치리스트에서 2~5번을 누르면 안내 문구를 띄우고, **잘못된 메뉴 번호는 `else` 로 방어** 처리했다.
- 함수·딕셔너리·예외처리는 **4차에서 도입 예정**이라, 3차에서는 모든 로직을 메뉴 루프 안에 직접 작성했다.

### 🤖 AI 파트너십 과정

**1. 메뉴 루프 구조 설계**
- **프롬프트 요약:** "입력·조회를 반복하는 메뉴 프로그램을 `while` 로 만들려면 종료는 어떻게 처리하나? 메뉴 분기는 `if-elif` 로 받으면 되나?"
- **적용 내용:** `while True` + `if menu == "0": break` 패턴 확립. `input()` 은 문자열을 반환하므로 **숫자가 아닌 `"0"` 문자열과 비교**하도록 통일.

**2. 데이터 상태 유지(영속성) 설계**
- **프롬프트 요약:** "메뉴를 돌 때마다 입력한 종목이 사라지면 안 된다. 워치리스트를 어떻게 유지하나?"
- **적용 내용:** 리스트들을 **루프 바깥에서 한 번만 선언**하고, 1번 메뉴가 `append()` 로 누적 → 2~5번이 같은 리스트를 계속 조회하도록 설계.

### 🔧 Troubleshooting & 기술 회고

1. **문제 1:** 빈 워치리스트에서 5번(전체 출력)을 누르면 `max([])` 등에서 오류가 났다.
   - **해결:** 각 메뉴 진입부에 **`if len(names) == 0:` 가드**를 넣어 빈 리스트일 때 안내만 출력.
2. **문제 2:** 종료(0)를 눌러도 메뉴가 다시 떴다.
   - **해결:** `if menu == "0":` 분기에서 `break` 가 `while` 루프 자체를 벗어나는지 확인하고, 분기를 루프 맨 앞에 배치.
     
### **📁 증빙 자료:**
<img width="767" height="917" alt="스크린샷 2026-05-25 225901" src="https://github.com/user-attachments/assets/a2beb7e0-3657-4c90-bcf1-60f14c51c3b6" />
<img width="591" height="1141" alt="스크린샷 2026-05-25 225909" src="https://github.com/user-attachments/assets/ea2216b3-15a1-44aa-a9c6-88a6c0714402" />
<img width="1664" height="946" alt="스크린샷 2026-05-25 225457" src="https://github.com/user-attachments/assets/d25103d5-70f8-4b8e-8cde-55a5df3c44a3" />
<img width="1679" height="938" alt="스크린샷 2026-05-25 225448" src="https://github.com/user-attachments/assets/8914510c-00f1-481b-8f5f-ca6cf4467247" />

<br>

### 🟥 [4차 과제: V4.0] 모듈화 및 데이터 확장 (배열과 함수) - 🌟최종 완성 -- 향후 작성 예정
### **✨4차 과제 업데이트 내용:**
 3차까지는 모든 로직을 메뉴 루프 안에 직접 펼쳐 썼지만, 4차에서는 **겉보기 기능은 그대로 두고 속(구조)을 4차 문법으로 재설계**했다.

- **함수 모듈화 (`def` / 매개변수 / 반환값 + `import`)**: 계산 로직을 **외부 파일 `signal_core.py`** 로 분리하고 `import signal_core as sc` 로 가져와 쓴다.
  - `calc_rate()`·`calc_volume_ratio()`·`calc_score()` — 등락률/거래량배수/급등점수 계산
  - `decide_grade(score)` → 등급(S/A/B/C) 반환, `decide_badge(rate, ratio)` → 단타진입 뱃지 반환
  - `make_stock(...)` → 입력값들을 **딕셔너리 한 개**로 묶어 반환, `make_plan(price)` → 진입/목표/손절가 딕셔너리 반환
- **자료구조 고도화 (리스트 → 딕셔너리)**: 3차의 **7개 병렬 리스트**(`names`/`prices`/`rates`/…)를 없애고, **종목 1개 = 딕셔너리 1개**(`{"name":…, "price":…, "score":…, "grade":…, "badge":…}`)로 묶었다. 워치리스트는 이 **딕셔너리들의 리스트** 하나로 관리해 인덱스 어긋남 위험을 없앴다.
- **예외 처리 (`try-except`)**: 잘못된 입력으로 프로그램이 죽지 않도록 방어했다.
  - `ask_float()`/`ask_int()` 입력 도우미 함수에서 **`ValueError`** 를 잡아 숫자가 아니면 다시 입력받음
  - 전일 종가·평소 거래량이 0이면 발생하는 **`ZeroDivisionError`** 를 잡아 해당 종목 입력만 취소
  - 메뉴는 `if-elif-else` 로 분기하고 잘못된 번호는 `else` 로 방어 (3차에서 이어짐)
- **메뉴/기능 구성**: 메뉴 함수(`input_stock`/`scan_all`/`filter_surge`/`show_signals`/`show_all`)로 분리, `main()` 함수에서 `while True` 루프로 호출. `if __name__ == "__main__":` 으로 직접 실행할 때만 `main()` 이 돌게 했다.
    
### **🤖 AI 파트너십 과정**
**1. 함수 분리 & 모듈화 설계**
- **프롬프트 요약:** "3차까지 메뉴 루프 안에 계산식을 다 적었더니 중복이 많다. 4차에서 함수로 빼고 외부 파일로 모듈화(`import`)하려면 어떤 단위로 나눠야 하나?"
- **적용 내용:** '계산'(등락률·점수·등급)과 '화면/메뉴'를 분리. 계산 함수들은 `signal_core.py` 로 모으고 `main.py` 는 입력·메뉴·출력만 담당하도록 역할을 나눴다.

**2. 리스트 → 딕셔너리 전환**
- **프롬프트 요약:** "지금은 종목 정보가 7개 병렬 리스트에 흩어져 있어서 `scores[i]`, `grades[i]` 처럼 인덱스로 맞춰 써. 딕셔너리로 바꾸면 뭐가 좋아지고, 어떻게 묶어야 해?"
- **적용 내용:** 같은 인덱스끼리 흩어져 있던 값을 **종목 1개 = `dict` 1개**로 묶어 `stock["grade"]` 처럼 **이름(키)으로 접근**. 인덱스 어긋남 버그가 원천 차단되고 가독성이 올라갔다.

**3. 예외 처리(try-except)로 입력 방어**
- **프롬프트 요약:** "사용자가 가격에 글자를 넣거나 전일 종가에 0을 넣으면 프로그램이 그냥 죽어버려. 죽지 않고 다시 입력받게 하려면?"
- **적용 내용:** `ValueError`(숫자 변환 실패)는 `while True` + `try-except` 로 다시 묻고, `ZeroDivisionError`(0으로 나누기)는 그 종목 입력만 건너뛰도록 했다.
    
### **🛠️ Troubleshooting & 기술 회고:**
 **문제 1:** `import signal_core` 가 `ModuleNotFoundError` 로 안 됐다.
   * **원인:** `signal_core.py` 가 `main.py` 와 **같은 폴더**에 없었음.
   * **해결:** 두 파일을 같은 폴더에 두면 `import` 가 됨을 학습. 실행도 그 폴더에서 `python main.py` 로.
2. **문제 2:** 리스트를 딕셔너리로 바꾼 뒤 `scores[i]` 같은 옛 코드가 `KeyError`/타입 오류를 냈다.
   * **원인:** 인덱스 접근(`[i]`)과 키 접근(`["score"]`)이 섞여 있었음.
   * **해결:** 종목을 꺼낼 땐 `s = watchlist[i]`, 값은 `s["score"]` 처럼 **키 접근으로 통일**.
3. **문제 3:** 숫자 입력 칸에 글자를 넣으면 프로그램이 즉시 종료됐다.
   * **원인:** `float(input())` 이 변환 실패 시 `ValueError` 를 던지고 잡는 곳이 없었음.
   * **해결:** `ask_float`/`ask_int` 도우미 함수에서 `try-except ValueError` 로 잡아 재입력 유도.
     
### **📁 증빙 자료:**
<img width="420" height="953" alt="스크린샷 2026-06-13 155220" src="https://github.com/user-attachments/assets/31ef9fe0-5b66-4878-9524-8e88416b5921" />
<img width="490" height="1011" alt="스크린샷 2026-06-13 155234" src="https://github.com/user-attachments/assets/50194b01-5d0c-4cc7-9966-b026264406f5" />
<img width="1698" height="1177" alt="스크린샷 2026-06-13 155300" src="https://github.com/user-attachments/assets/d702854e-a715-43e7-b2a5-672d9bc285c0" />
<img width="1625" height="1206" alt="스크린샷 2026-06-13 155308" src="https://github.com/user-attachments/assets/0c03d0cc-ccf0-42e9-b45e-d109af9c4882" />
<img width="1607" height="1205" alt="스크린샷 2026-06-13 155313" src="https://github.com/user-attachments/assets/a6c64cd1-2c78-4690-8e70-1aa3bd4897ca" />
<img width="1671" height="1173" alt="스크린샷 2026-06-13 155321" src="https://github.com/user-attachments/assets/5313ad86-238a-4775-ba55-22591af4286d" />
<img width="1673" height="1217" alt="스크린샷 2026-06-13 155329" src="https://github.com/user-attachments/assets/12b671f4-ec8c-4c82-b84d-38c23354893c" />
<img width="1691" height="1194" alt="스크린샷 2026-06-13 155338" src="https://github.com/user-attachments/assets/d7dd2512-ad6d-40bc-97a6-0214ec9e2376" />
<img width="1709" height="721" alt="스크린샷 2026-06-13 155352" src="https://github.com/user-attachments/assets/674aba98-290c-4845-9c32-f0183937531f" />

<br>

# 🎮 [추가 확장 버전] 단타 시그널 엔진으로 만든 웹 모의주식 게임

> 파일: **`급등주_단타게임.html`** · 실행: **파일 더블클릭** (브라우저만 있으면 됨, 설치·서버·인터넷 불필요)

### 🕹️ 왜 게임으로 만들었나 (기획 배경)

나는 **2019년 GIGDC(글로벌 인디 게임 개발 경진대회)에 Unity 기반 게임을 출품해 입상**한 경험이 있다.
그때의 게임 개발 경험을 살려, 이번 학기 1~4차에 걸쳐 만든 **급등주 단타 시그널 분석기의 핵심 로직을
'직접 플레이하며 체감하는 게임'으로 확장**해 보고 싶었다.

콘솔 분석기는 "이 종목이 급등주인가?"를 점수·등급으로 알려주지만, **그 신호가 실제로 돈이 되는지**는
보여주지 못한다. 그래서 *"분석기를 켠 채 매매할 때 vs 끄고 감으로만 매매할 때"* 의 결과 차이를
직접 비교하는 게임으로 만들어, **내가 설계한 시그널 로직의 효용을 눈으로 증명**하는 것을 목표로 했다.

### ✨ 게임 내용

- **시그널 엔진 재사용:** 콘솔 `signal_core.py` 의 계산 공식(등락률·거래량배수·급등점수·등급·🚀뱃지)을
  **그대로** 자바스크립트로 옮겨 게임에 탑재했다. (같은 로직 = 같은 판단)
- **두 가지 모드로 '단타 시그널의 위력' 체험:**
  - 🟢 **일반 모드 (분석기 ON):** 종목마다 급등점수·등급(S/A/B/C)·🚀단타진입 뱃지가 그래프 위에 표시
  - 🔴 **하드코어 모드 (분석기 OFF):** 등급·뱃지가 전부 숨겨지고, 오직 가격 그래프만 보고 매매
- **공정한 비교 + 효과 증명:** 시드 기반 난수로 *'같은 시장'* 을 두 모드로 플레이할 수 있고,
  게임 종료 시 같은 시장에서 봇을 돌려 비교한다. (200개 시드 검증 결과
  **🚀시그널봇 평균 +47% vs 🎲랜덤봇 평균 +11%, 승률 ≈100%**)
- **게임 플레이:** 시드머니 100만원으로 20일간 단타 투자. 10개 가상 종목을 클릭해 '진입(상세)' 화면에서
  가격 그래프를 보며 수량 단위로 매수/매도. 📈 +5% 익절 / −3% 손절 규칙으로 굴리면 수익이 쌓인다.

### 🛠️ 기술 포인트 (이해한 범위 내에서 직접 구현)

- **외부 라이브러리 0개 · 단일 HTML 파일** — CSS/JS를 전부 한 파일에 담아 오프라인·무설치로 실행
- **그래프를 SVG로 직접 그림** — 차트 라이브러리 없이 좌표를 계산해 선그래프/영역/🚀마커를 렌더링
- **'상장한 지 오래된 종목' 느낌** — 게임 시작 전 과거 30일치 시세를 미리 생성해 그래프에 함께 표시
- **펌프 앤 덤프 시장 모델** — 평소엔 잔잔하다가 가끔 급등(거래량 폭증 → 🚀뱃지) 후 하락하는 패턴으로,
  "뱃지 보고 사서 익절, 오래 들면 물림"이라는 단타의 본질을 단순화해 재현

> ⚠️ 이 게임은 **4차 본 과제와는 별개의 추가 도전작**이다.
> 4차 필수 문법(함수·딕셔너리·예외처리)을 충족하는 본 과제는 콘솔 버전(`main.py` + `signal_core.py`)이며,
> 본 게임은 그 로직을 응용한 확장 결과물이다. (교육용 가상 게임 · 실제 투자 권유 아님)

[급등주_단타게임.html](https://github.com/user-attachments/files/28908696/_.html)

<img width="958" height="862" alt="스크린샷 2026-06-13 161504" src="https://github.com/user-attachments/assets/c661552e-96a9-4414-8b30-44fab87aa911" />
<img width="953" height="973" alt="스크린샷 2026-06-13 161510" src="https://github.com/user-attachments/assets/3338caf1-e4db-4d4e-b8b7-b649da444027" />
<img width="619" height="446" alt="스크린샷 2026-06-13 161521" src="https://github.com/user-attachments/assets/e25db978-9db0-4078-9281-1b02f1fafaae" />
<img width="1684" height="674" alt="스크린샷 2026-06-13 160915" src="https://github.com/user-attachments/assets/5dbefe97-5156-40db-b96a-1c76713f47f7" />

<!DOCTYPE html>
<!--
=========================================================================
 급등주 단타 시그널 게임  (모의 주식 투자 게임)
 - 4차 과제 "급등주 포착 단타 시그널 분석기"의 기합/도전 버전 (별도 쇼케이스)
 - signal_core.py 와 '똑같은 시그널 공식'을 자바스크립트로 옮겨 웹 게임에 탑재했다.
 - 종목을 클릭해 '진입(상세)' 화면으로 들어가면 가격 그래프를 보며 매매한다.
 - 두 가지 모드로 '단타 시그널 분석기'의 위력을 직접 체험한다.
     · 일반 모드   : 종목마다 급등점수 / 등급(S·A·B·C) / 🚀단타진입 뱃지가 보인다.
     · 하드코어 모드: 분석기 OFF. 가격 그래프만 보고 감으로 매매한다.
 - 서버/설치 필요 없음. 이 파일을 더블클릭하면 브라우저에서 바로 실행된다.
 - 교육용 게임이며 실제 투자 권유가 아니다. 종목명도 전부 가상이다.
=========================================================================
-->
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>급등주 단타 시그널 게임</title>
<style>
  /* ============ 다크 네온 트레이딩 터미널 테마 ============ */
  :root{
    --up:#ff4d5e;        /* 상승: 빨강 */
    --down:#38bdf8;      /* 하락: 파랑 */
    --cyan:#22d3ee; --magenta:#e879f9; --gold:#fbbf24;
    --panel:rgba(255,255,255,.04); --line:rgba(255,255,255,.10);
    --txt:#e8edf7; --dim:#8b97ad;
  }
  *{ box-sizing:border-box; }
  body{
    margin:0; padding:0; min-height:100vh; color:var(--txt);
    font-family:"맑은 고딕","Malgun Gothic",sans-serif;
    background:
      radial-gradient(1200px 600px at 80% -10%, rgba(232,121,249,.12), transparent 60%),
      radial-gradient(1000px 500px at -10% 10%, rgba(34,211,238,.12), transparent 55%),
      linear-gradient(180deg,#070b16 0%,#0a1020 100%);
    background-attachment:fixed;
  }
  /* 은은하게 흐르는 격자 배경 */
  body::before{
    content:""; position:fixed; inset:0; z-index:0; pointer-events:none; opacity:.35;
    background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),
                     linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
    background-size:40px 40px; mask-image:linear-gradient(180deg,#000,transparent 80%);
  }
  .wrap{ position:relative; z-index:1; max-width:900px; margin:0 auto; padding:18px; }
  .mono{ font-family:ui-monospace,"Consolas",monospace; }
  .up{ color:var(--up); } .down{ color:var(--down); } .flat{ color:var(--dim); }

  /* ============ 시작 화면 ============ */
  /* 상단 흐르는 시세 티커 */
  .ticker{ overflow:hidden; white-space:nowrap; border-top:1px solid var(--line);
    border-bottom:1px solid var(--line); padding:8px 0; margin-bottom:28px; background:rgba(0,0,0,.25); }
  .ticker span{ display:inline-block; padding:0 22px; font-size:13px; }
  .ticker .track{ display:inline-block; animation:scroll 22s linear infinite; }
  @keyframes scroll{ from{transform:translateX(0)} to{transform:translateX(-50%)} }

  .hero{ text-align:center; padding:14px 0 30px; }
  .badge-top{ display:inline-block; font-size:12px; letter-spacing:3px; color:var(--cyan);
    border:1px solid rgba(34,211,238,.4); border-radius:999px; padding:5px 14px; margin-bottom:18px; }
  .title{ font-size:46px; font-weight:900; line-height:1.1; margin:0;
    background:linear-gradient(90deg,#fff,var(--cyan) 60%,var(--magenta));
    -webkit-background-clip:text; background-clip:text; color:transparent;
    text-shadow:0 0 40px rgba(34,211,238,.25); }
  .title .rocket{ -webkit-text-fill-color:initial; filter:drop-shadow(0 0 12px rgba(251,191,36,.6)); }
  .tagline{ color:var(--dim); margin-top:14px; font-size:15px; }

  .modes{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:8px; }
  @media(max-width:640px){ .modes{ grid-template-columns:1fr; } .title{ font-size:34px; } }
  .modecard{ position:relative; text-align:left; cursor:pointer; padding:22px; border-radius:18px;
    background:var(--panel); border:1px solid var(--line); color:var(--txt);
    transition:transform .18s, box-shadow .18s, border-color .18s; overflow:hidden; }
  .modecard:hover{ transform:translateY(-5px); border-color:rgba(34,211,238,.6);
    box-shadow:0 14px 40px rgba(34,211,238,.18); }
  .modecard.hard:hover{ border-color:rgba(255,77,94,.6); box-shadow:0 14px 40px rgba(255,77,94,.18); }
  .modecard .ic{ font-size:34px; }
  .modecard .mt{ font-size:19px; font-weight:800; margin:10px 0 6px; }
  .modecard .md{ color:var(--dim); font-size:13px; line-height:1.55; }
  .modecard .go{ margin-top:14px; font-weight:800; color:var(--cyan); }
  .modecard.hard .go{ color:var(--up); }
  .tipbar{ margin-top:22px; text-align:center; color:var(--dim); font-size:13px; }
  .tipbar b{ color:var(--gold); }

  /* ============ 게임 화면 공통 ============ */
  .topbar{ display:flex; flex-wrap:wrap; gap:8px; padding:14px 16px; border-radius:16px;
    background:var(--panel); border:1px solid var(--line); margin-bottom:14px; backdrop-filter:blur(6px); }
  .topbar .cell{ flex:1; min-width:96px; }
  .topbar .label{ font-size:11px; color:var(--dim); letter-spacing:1px; }
  .topbar .value{ font-size:18px; font-weight:800; }

  .card{ background:var(--panel); border:1px solid var(--line); border-radius:16px; }

  /* 종목 목록 */
  .stockrow{ display:flex; align-items:center; gap:14px; padding:14px 16px; cursor:pointer;
    border-bottom:1px solid var(--line); transition:background .15s; }
  .stockrow:last-child{ border-bottom:none; }
  .stockrow:hover{ background:rgba(34,211,238,.06); }
  .stockrow .nm{ flex:1; }
  .stockrow .nm b{ font-size:16px; } .stockrow .nm .code{ color:var(--dim); font-size:11px; margin-left:6px; }
  .stockrow .nm .own{ display:inline-block; margin-top:3px; font-size:11px; color:var(--gold);
    border:1px solid rgba(251,191,36,.4); border-radius:6px; padding:1px 6px; }
  .stockrow .spark{ width:120px; height:38px; }
  .stockrow .sig{ min-width:88px; text-align:center; }
  .stockrow .sigbadge{ font-size:11px; color:var(--up); font-weight:800; margin-top:4px; text-shadow:0 0 10px rgba(255,77,94,.5); }
  .stockrow.hot{ background:rgba(255,77,94,.08); box-shadow:inset 3px 0 0 var(--up); }
  .stockrow.hot:hover{ background:rgba(255,77,94,.13); }
  .stockrow .pr{ text-align:right; min-width:120px; }
  .stockrow .pr .px{ font-size:16px; font-weight:800; }
  .stockrow .pr .ch{ font-size:13px; }
  .stockrow .enter{ color:var(--dim); font-size:20px; }

  /* 상세(진입) 화면 */
  .detail-head{ display:flex; align-items:center; gap:12px; padding:14px 16px; border-bottom:1px solid var(--line); }
  .back{ background:rgba(255,255,255,.06); color:var(--txt); border:1px solid var(--line);
    border-radius:10px; padding:8px 12px; cursor:pointer; font-weight:700; }
  .back:hover{ border-color:var(--cyan); }
  .detail-head .dn{ flex:1; } .detail-head .dn b{ font-size:20px; } .detail-head .dn .code{ color:var(--dim); font-size:12px; margin-left:6px; }
  .detail-head .dp{ text-align:right; } .detail-head .dp .px{ font-size:22px; font-weight:900; }
  .chartbox{ padding:10px 8px 0; }
  .chartbox svg{ width:100%; height:auto; display:block; }
  .chart-x{ display:flex; justify-content:space-between; color:var(--dim); font-size:11px; padding:2px 12px 12px; }

  /* 분석기 패널 */
  .signal{ display:flex; flex-wrap:wrap; gap:10px; padding:14px 16px; border-top:1px solid var(--line); }
  .chip{ flex:1; min-width:120px; background:rgba(255,255,255,.03); border:1px solid var(--line);
    border-radius:12px; padding:10px 12px; }
  .chip .l{ font-size:11px; color:var(--dim); } .chip .v{ font-size:17px; font-weight:800; }
  .grade{ font-weight:900; padding:1px 10px; border-radius:999px; color:#06101f; }
  .gS{ background:var(--up); color:#fff; } .gA{ background:var(--gold); } .gB{ background:#34d399; } .gC{ background:#94a3b8; }
  .badge-on{ color:var(--up); font-weight:900; text-shadow:0 0 14px rgba(255,77,94,.5); }
  .locked{ flex:1; text-align:center; color:var(--dim); padding:18px; border-top:1px solid var(--line); }
  .locked .big{ font-size:22px; }

  /* 매매 패널 */
  .trade{ padding:16px; border-top:1px solid var(--line); }
  .holdinfo{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px; }
  .holdinfo .h{ flex:1; min-width:110px; background:rgba(255,255,255,.03); border:1px solid var(--line);
    border-radius:10px; padding:8px 10px; }
  .holdinfo .h .l{ font-size:11px; color:var(--dim); } .holdinfo .h .v{ font-size:16px; font-weight:800; }
  .qtybar{ display:flex; align-items:center; gap:8px; margin-bottom:12px; }
  .qtybar input{ flex:1; text-align:center; font-size:18px; font-weight:800; padding:10px;
    background:#0a1424; color:var(--txt); border:1px solid var(--line); border-radius:10px; }
  .step{ background:rgba(255,255,255,.06); color:var(--txt); border:1px solid var(--line);
    border-radius:10px; padding:10px 12px; cursor:pointer; font-weight:800; min-width:46px; }
  .step:hover{ border-color:var(--cyan); }
  .maxbtn{ background:rgba(251,191,36,.15); color:var(--gold); border:1px solid rgba(251,191,36,.4); }
  .orderbtns{ display:flex; gap:10px; }
  .orderbtns button{ flex:1; padding:14px; font-size:16px; font-weight:900; border:none; border-radius:12px; cursor:pointer; }
  .b-buy{ background:linear-gradient(180deg,#ff6470,#e23a4a); color:#fff; box-shadow:0 8px 24px rgba(226,58,74,.35); }
  .b-sell{ background:linear-gradient(180deg,#54c6ff,#2b9be0); color:#04121f; box-shadow:0 8px 24px rgba(43,155,224,.3); }
  .b-sellall{ background:rgba(255,255,255,.06); color:var(--txt); border:1px solid var(--line)!important; }
  .orderbtns button:disabled{ filter:grayscale(.7) brightness(.6); cursor:not-allowed; box-shadow:none; }
  .msg{ min-height:20px; margin-top:10px; font-size:13px; color:var(--gold); text-align:center; }

  /* 다음날 버튼 */
  .next{ display:block; width:100%; margin-top:16px; padding:16px; font-size:17px; font-weight:900;
    border:none; border-radius:14px; cursor:pointer; color:#04121f;
    background:linear-gradient(90deg,var(--cyan),var(--magenta)); box-shadow:0 10px 30px rgba(34,211,238,.25); }
  .next:hover{ filter:brightness(1.08); }

  /* 결과 모달 */
  .overlay{ position:fixed; inset:0; z-index:5; background:rgba(2,6,16,.72); backdrop-filter:blur(4px);
    display:none; align-items:center; justify-content:center; padding:16px; }
  .overlay.show{ display:flex; }
  .result{ background:linear-gradient(180deg,#0d1730,#0a1020); border:1px solid var(--line);
    border-radius:20px; padding:26px; max-width:540px; width:100%; box-shadow:0 30px 80px rgba(0,0,0,.6); }
  .result h2{ margin:0 0 6px; }
  .rrow{ display:flex; justify-content:space-between; align-items:center; padding:11px 0; border-bottom:1px solid var(--line); }
  .rrow .v{ font-weight:900; font-size:18px; }
  .verdict{ margin-top:16px; padding:14px; border-radius:12px; background:rgba(34,211,238,.07);
    border:1px solid rgba(34,211,238,.25); font-size:14px; line-height:1.6; }
  .resbtns{ display:flex; gap:10px; margin-top:18px; }
  .resbtns button{ flex:1; }
  .hidden{ display:none; }
  .disclaimer{ text-align:center; color:var(--dim); font-size:11px; margin-top:26px; }
</style>
</head>
<body>
<div class="wrap">

  <!-- ===================== 시작 화면 ===================== -->
  <div id="startScreen">
    <div class="ticker">
      <div class="track" id="tickerTrack"></div>
    </div>

    <div class="hero">
      <div class="badge-top">M J U · SCALPING ARCADE</div>
      <h1 class="title"><span class="rocket">🚀</span> 급등주 단타 시그널</h1>
      <div class="tagline">시드머니 <b>100만원</b> · 20일 · 내가 만든 시그널 엔진으로 급등주를 잡아라</div>
    </div>

    <div class="modes">
      <button class="modecard" onclick="startGame('normal')">
        <div class="ic">🟢</div>
        <div class="mt">일반 모드</div>
        <div class="md">단타 분석기 <b style="color:var(--cyan)">ON</b>. 종목마다 급등점수·등급(S/A/B/C)·🚀단타진입 뱃지가 그래프 위에 표시된다. 신호를 보고 매매!</div>
        <div class="go">분석기 켜고 시작 ▶</div>
      </button>
      <button class="modecard hard" onclick="startGame('hardcore')">
        <div class="ic">🔴</div>
        <div class="mt">하드코어 모드</div>
        <div class="md">단타 분석기 <b style="color:var(--up)">OFF</b>. 등급·뱃지가 전부 숨겨진다. 오직 가격 그래프만 보고 감으로 승부한다.</div>
        <div class="go">맨몸으로 시작 ▶</div>
      </button>
    </div>

    <div class="tipbar">💡 <b>공략:</b> 🚀단타진입 뱃지가 뜬 종목을 사고, <b>+5% 익절 / −3% 손절</b> 규칙으로 다음날 정리하면 수익이 쌓인다.</div>
    <div class="disclaimer">※ 교육용 가상 게임입니다. 모든 종목명은 허구이며 실제 투자 권유가 아닙니다.</div>
  </div>

  <!-- ===================== 게임 화면 ===================== -->
  <div id="gameScreen" class="hidden">
    <div class="topbar">
      <div class="cell"><div class="label">진행</div><div class="value" id="dayInfo">Day 1 / 20</div></div>
      <div class="cell"><div class="label">모드</div><div class="value" id="modeInfo">일반</div></div>
      <div class="cell"><div class="label">현금</div><div class="value mono" id="cashInfo">1,000,000</div></div>
      <div class="cell"><div class="label">총자산</div><div class="value mono" id="assetInfo">1,000,000</div></div>
      <div class="cell"><div class="label">수익률</div><div class="value mono" id="rateInfo">0.0%</div></div>
    </div>

    <div id="viewArea"></div>
    <button class="next" id="nextBtn" onclick="nextDay()">다음 날 ▶</button>
  </div>
</div>

<!-- ===================== 결과 모달 ===================== -->
<div class="overlay" id="overlay">
  <div class="result">
    <h2>📊 20일 투자 결과</h2>
    <div class="rrow"><span id="meLabel">나의 최종 수익률</span><span class="v" id="meResult"></span></div>
    <div class="rrow"><span>🚀 시그널봇 (S/🚀 신호만 매매)</span><span class="v" id="sigResult"></span></div>
    <div class="rrow"><span>🎲 랜덤봇 (무작위 매매)</span><span class="v" id="rndResult"></span></div>
    <div class="verdict" id="verdict"></div>
    <div class="resbtns">
      <button class="next" style="margin:0; background:linear-gradient(90deg,#54c6ff,#2b9be0);" onclick="replaySameMarket()">🔄 같은 장 다시</button>
      <button class="next" style="margin:0;" onclick="newMarket()">🆕 새 장 시작</button>
    </div>
  </div>
</div>

<script>
/* =====================================================================
   0. 시드 기반 난수 발생기 (mulberry32)
      같은 seed → 항상 같은 난수 → '같은 장'을 두 모드로 공정 비교 가능.
   ===================================================================== */
function makeRandom(seed){
  return function(){
    seed |= 0; seed = seed + 0x6D2B79F5 | 0;
    let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

/* =====================================================================
   1. 시그널 엔진  ★ signal_core.py 와 똑같은 공식 ★
   ===================================================================== */
const calcRate   = (now, prev)    => (now - prev) / prev * 100;   // 등락률(%)
const calcRatio  = (todayV, avgV) => todayV / avgV;              // 거래량 배수
const calcScore  = (rate, ratio)  => rate + (ratio - 1) * 5;     // 급등 점수
const decideGrade = (s) => s >= 20 ? "S" : s >= 10 ? "A" : s >= 0 ? "B" : "C";
const decideBadge = (rate, ratio) => (rate >= 15 && ratio >= 3); // 복합조건 단타진입

/* =====================================================================
   2. 게임 설정 / 상태
   ===================================================================== */
const TOTAL_DAYS = 20;
const PREHIST    = 30;        // 게임 시작 전 '이미 상장돼 거래되던' 과거 일수 (그래프에 미리 표시)
const SEED_MONEY = 1000000;
const STOCKS = [
  {name:"떡상전자",   code:"TTSANG"},
  {name:"가즈아바이오", code:"GAZUA"},
  {name:"존버컴퍼니",  code:"JONBR"},
  {name:"우주방위산업", code:"SPACE"},
  {name:"코인티슈",    code:"COINT"},
  {name:"라면로보틱스", code:"RAMEN"},
  {name:"불기둥에너지", code:"BBUL"},
  {name:"따상제약",    code:"DDSANG"},
  {name:"무지성홀딩스", code:"MUZI"},
  {name:"천슬라모터스", code:"CHEON"},
];

let rawPrices = [];    // 종목별 전체 가격 배열 (과거 PREHIST일 + 게임 TOTAL_DAYS일)
let marketPath = [];   // 게임 20일치 시세 (각 날짜 = 종목 10개 스냅샷)
let currentDay = 0;    // 0~19
let cash = 0;
let holdings = {};     // { 종목명: {shares, avgBuy} }
let mode = "normal";
let curSeed = 1;
let view = "list";     // "list"(목록) 또는 "detail"(진입)
let selected = 0;      // 진입한 종목 인덱스

/* =====================================================================
   3. 시장 생성 (평소 잔잔 → 가끔 급등(펌프) → 덤프(폭락))
   ===================================================================== */
function genStockPath(rng){
  let base   = Math.round((5000 + rng() * 75000) / 100) * 100;
  let avgVol = Math.round(50000 + rng() * 200000);
  let prices = [base], volumes = [avgVol];
  let state = "normal", left = 0;
  // 과거 PREHIST일 + 게임 TOTAL_DAYS일을 한 번에 생성 (같은 변동 로직)
  for(let d = 1; d <= PREHIST + TOTAL_DAYS; d++){
    let prev = prices[d-1], pct, vm;
    if(state === "pump"){
      pct = 0.06 + rng()*0.06; vm = 2.5 + rng()*2; left--;
      if(left <= 0){ state = "dump"; left = 1 + Math.floor(rng()*2); }
    } else if(state === "dump"){
      pct = -(0.07 + rng()*0.07); vm = 1.5 + rng()*1.5; left--;
      if(left <= 0) state = "normal";
    } else {
      pct = -0.03 + rng()*0.07; vm = 0.6 + rng()*0.9;
      if(rng() < 0.14){ state="pump"; left=1+Math.floor(rng()*2);
        pct = 0.16 + rng()*0.07; vm = 4 + rng()*3; }   // 급등 시작 → 🚀뱃지 점등
    }
    let next = Math.max(100, Math.round(prev*(1+pct)/10)*10);
    prices.push(next); volumes.push(Math.round(avgVol*vm));
  }
  return { avgVol, prices, volumes };
}
function buildMarket(seed){
  const rng = makeRandom(seed);
  const paths = STOCKS.map(() => genStockPath(rng));
  rawPrices = paths.map(p => p.prices);          // 그래프용 전체 가격 보관
  const days = [];
  for(let d = 1; d <= TOTAL_DAYS; d++){
    const snap = paths.map((s, i) => {
      const idx = PREHIST + d;                    // 게임 d일째는 전체 배열의 PREHIST+d 위치
      const price = s.prices[idx], prev = s.prices[idx-1], vol = s.volumes[idx];
      const rate = calcRate(price, prev), ratio = calcRatio(vol, s.avgVol);
      const score = calcScore(rate, ratio);
      return { ...STOCKS[i], price, prev, volume:vol, avgVol:s.avgVol, rate, ratio, score,
               grade:decideGrade(score), badge:decideBadge(rate, ratio) };
    });
    days.push(snap);
  }
  return days;
}

/* =====================================================================
   4. 시작 / 화면 전환
   ===================================================================== */
function startGame(selectedMode){
  mode = selectedMode;
  marketPath = buildMarket(curSeed);
  currentDay = 0; cash = SEED_MONEY; holdings = {}; view = "list";
  document.getElementById("startScreen").classList.add("hidden");
  document.getElementById("gameScreen").classList.remove("hidden");
  document.getElementById("overlay").classList.remove("show");
  document.getElementById("modeInfo").textContent = (mode==="normal") ? "일반(ON)" : "하드코어(OFF)";
  render();
}

// 한 종목의 '오늘까지 공개된' 가격/뱃지 이력 (과거 PREHIST일 포함, 미래는 안 보여줌)
function history(i){
  const full = rawPrices[i];
  const upto = PREHIST + currentDay + 1;          // 오늘 종가까지의 인덱스
  const prices = full.slice(0, upto + 1);         // 과거 + 오늘까지
  const badges = prices.map((_, idx) => {
    const gameDay = idx - PREHIST;                // 1~ 이 게임 거래일, 그 이하는 과거
    return (gameDay >= 1 && gameDay <= currentDay + 1) ? marketPath[gameDay-1][i].badge : false;
  });
  return { prices, badges };                      // 게임 시작선(거래시작)은 인덱스 PREHIST 위치
}

/* =====================================================================
   5. 렌더링 (목록 / 상세)
   ===================================================================== */
function render(){
  // --- 상단 정보 ---
  const snap = marketPath[currentDay];
  let stockValue = 0;
  for(const s of snap) if(holdings[s.name]) stockValue += holdings[s.name].shares * s.price;
  const asset = cash + stockValue, totRate = (asset/SEED_MONEY - 1) * 100;
  document.getElementById("dayInfo").textContent   = `Day ${currentDay+1} / ${TOTAL_DAYS}`;
  document.getElementById("cashInfo").textContent  = num(cash);
  document.getElementById("assetInfo").textContent = num(asset);
  const rEl = document.getElementById("rateInfo");
  rEl.textContent = signed(totRate)+"%"; rEl.className = "value mono " + cls(totRate);

  document.getElementById("viewArea").innerHTML = (view === "list") ? renderList() : renderDetail();
  const btn = document.getElementById("nextBtn");
  btn.textContent = (currentDay >= TOTAL_DAYS-1) ? "투자 종료하고 결과 보기 🏁" : "다음 날 ▶";
}

// 종목 목록 (클릭하면 진입)
function renderList(){
  const snap = marketPath[currentDay];
  let html = `<div class="card">`;
  for(let i = 0; i < snap.length; i++){
    const s = snap[i], h = history(i);
    const own = holdings[s.name];
    // 일반 모드: 목록에서도 등급/뱃지를 바로 보여준다 (하드코어는 자물쇠로 가림)
    const hot = (mode === "normal" && s.badge) ? " hot" : "";
    const sig = (mode === "normal")
      ? `<div class="sig"><span class="grade g${s.grade}">${s.grade}</span>${s.badge ? `<div class="sigbadge">🚀단타진입</div>` : ``}</div>`
      : `<div class="sig flat">🔒</div>`;
    html += `<div class="stockrow${hot}" onclick="enter(${i})">
      <div class="nm"><b>${s.name}</b><span class="code">${s.code}</span>
        ${own ? `<div class="own">보유 ${own.shares.toLocaleString()}주</div>` : ``}</div>
      <div class="spark">${sparkline(h.prices, i)}</div>
      ${sig}
      <div class="pr">
        <div class="px mono">${num(s.price)}</div>
        <div class="ch mono ${cls(s.rate)}">${signed(s.rate)}%</div>
      </div>
      <div class="enter">›</div>
    </div>`;
  }
  html += `</div>`;
  return html;
}

// 진입(상세) 화면: 큰 그래프 + 분석기 + 매매 패널
function renderDetail(){
  const s = marketPath[currentDay][selected];
  const h = history(selected);
  const own = holdings[s.name];
  const shares = own ? own.shares : 0;
  const pl = own ? (s.price - own.avgBuy) * shares : 0;
  const maxBuyable = Math.floor(cash / s.price);

  // 분석기 패널 (모드에 따라)
  let analysis;
  if(mode === "normal"){
    analysis = `<div class="signal">
      <div class="chip"><div class="l">급등점수</div><div class="v mono">${s.score.toFixed(1)}점</div></div>
      <div class="chip"><div class="l">시그널 등급</div><div class="v"><span class="grade g${s.grade}">${s.grade}</span></div></div>
      <div class="chip"><div class="l">거래량 배수</div><div class="v mono">${s.ratio.toFixed(2)}배</div></div>
      <div class="chip"><div class="l">단타 시그널</div><div class="v">${s.badge ? `<span class="badge-on">🚀단타진입</span>` : `<span class="flat">관망</span>`}</div></div>
    </div>`;
  } else {
    analysis = `<div class="locked"><div class="big">🔒 분석기 OFF</div>가격 그래프만 보고 직접 판단하세요</div>`;
  }

  return `<div class="card">
    <div class="detail-head">
      <button class="back" onclick="back()">← 목록</button>
      <div class="dn"><b>${s.name}</b><span class="code">${s.code}</span></div>
      <div class="dp"><div class="px mono ${cls(s.rate)}">${num(s.price)}</div>
        <div class="mono ${cls(s.rate)}">${signed(s.rate)}%</div></div>
    </div>
    <div class="chartbox">${bigChart(h.prices, h.badges)}</div>
    <div class="chart-x"><span>← 상장 후 과거 ${PREHIST}일</span><span>Day ${currentDay+1} · 오늘</span></div>
    ${analysis}
    <div class="trade">
      <div class="holdinfo">
        <div class="h"><div class="l">보유 수량</div><div class="v mono">${shares.toLocaleString()}주</div></div>
        <div class="h"><div class="l">평균 단가</div><div class="v mono">${own ? num(own.avgBuy) : "-"}</div></div>
        <div class="h"><div class="l">평가손익</div><div class="v mono ${cls(pl)}">${own ? signed2(pl) : "-"}</div></div>
      </div>
      <div class="qtybar">
        <button class="step" onclick="stepQty(-10)">−10</button>
        <button class="step" onclick="stepQty(-1)">−1</button>
        <input id="qty" type="number" min="1" value="${Math.max(1, Math.min(maxBuyable||1, 10))}">
        <button class="step" onclick="stepQty(1)">+1</button>
        <button class="step" onclick="stepQty(10)">+10</button>
        <button class="step maxbtn" onclick="maxQty()">최대 ${maxBuyable}주</button>
      </div>
      <div class="orderbtns">
        <button class="b-buy"  onclick="doBuy()"  ${maxBuyable<1?"disabled":""}>매수</button>
        <button class="b-sell" onclick="doSell()" ${shares<1?"disabled":""}>매도</button>
        <button class="b-sellall" onclick="sellAll()" ${shares<1?"disabled":""}>전량매도</button>
      </div>
      <div class="msg" id="msg"></div>
    </div>
  </div>`;
}

/* =====================================================================
   6. 그래프 (SVG 직접 그리기 — 라이브러리 없음)
   ===================================================================== */
function chartSVG(prices, badges, W, H, idSuffix, showMarks, dividerIdx){
  const padX = 14, padTop = 22, padBot = 14;
  const min = Math.min(...prices), max = Math.max(...prices), span = (max-min) || 1;
  const n = prices.length;
  const X = i => padX + (W - 2*padX) * (n===1 ? 0.5 : i/(n-1));
  const Y = v => padTop + (H - padTop - padBot) * (1 - (v-min)/span);
  const pts = prices.map((p,i) => `${X(i).toFixed(1)},${Y(p).toFixed(1)}`).join(" ");
  const area = `${X(0).toFixed(1)},${H-padBot} ${pts} ${X(n-1).toFixed(1)},${H-padBot}`;
  const up = prices[n-1] >= prices[0];
  const color = up ? "#ff4d5e" : "#38bdf8";
  let marks = "";
  if(showMarks){
    badges.forEach((b,i) => { if(b) marks += `<text x="${X(i).toFixed(1)}" y="${(Y(prices[i])-9).toFixed(1)}" font-size="14" text-anchor="middle">🚀</text>`; });
  }
  // 과거(상장 후)와 게임 거래 구간을 나누는 점선
  let divider = "";
  if(dividerIdx != null && dividerIdx > 0 && dividerIdx < n){
    const dx = X(dividerIdx).toFixed(1);
    divider = `<line x1="${dx}" y1="${padTop}" x2="${dx}" y2="${H-padBot}" stroke="rgba(255,255,255,.22)" stroke-width="1" stroke-dasharray="4 4"/>
      <text x="${dx}" y="${padTop-7}" font-size="10" fill="#8b97ad" text-anchor="middle">거래시작</text>`;
  }
  return `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
    <defs><linearGradient id="grad${idSuffix}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="${color}" stop-opacity="0.35"/>
      <stop offset="1" stop-color="${color}" stop-opacity="0"/></linearGradient></defs>
    <polygon points="${area}" fill="url(#grad${idSuffix})"/>
    ${divider}
    <polyline points="${pts}" fill="none" stroke="${color}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${X(n-1).toFixed(1)}" cy="${Y(prices[n-1]).toFixed(1)}" r="4" fill="${color}"/>
    ${marks}
  </svg>`;
}
function sparkline(prices, i){ return chartSVG(prices, null, 120, 38, "sp"+i, false); }                  // 목록용(구분선 없음)
function bigChart(prices, badges){ return chartSVG(prices, badges, 640, 240, "big", mode==="normal", PREHIST); } // 상세용(거래시작 구분선)

/* =====================================================================
   7. 매매 (수량 기반 — 비싼 종목도 1주씩 살 수 있음)
   ===================================================================== */
function enter(i){ selected = i; view = "detail"; render(); }
function back(){ view = "list"; render(); }
function qtyVal(){ return Math.max(1, parseInt(document.getElementById("qty").value) || 1); }
function stepQty(d){ const el = document.getElementById("qty"); el.value = Math.max(1, (parseInt(el.value)||0) + d); }
function maxQty(){ const s = marketPath[currentDay][selected]; document.getElementById("qty").value = Math.max(1, Math.floor(cash/s.price)); }

function doBuy(){
  const s = marketPath[currentDay][selected], qty = qtyVal(), cost = qty * s.price;
  if(cash < cost){ msg(`현금이 부족합니다. (필요 ${num(cost)} / 보유 ${num(cash)})`); return; }
  cash -= cost;
  if(holdings[s.name]){
    const hd = holdings[s.name], tot = hd.shares + qty;
    hd.avgBuy = (hd.avgBuy*hd.shares + cost) / tot; hd.shares = tot;
  } else holdings[s.name] = { shares: qty, avgBuy: s.price };
  msg(`✅ ${s.name} ${qty.toLocaleString()}주 매수 (${num(cost)})`);
  render();
}
function doSell(){
  const s = marketPath[currentDay][selected], hd = holdings[s.name];
  if(!hd) return;
  const qty = Math.min(qtyVal(), hd.shares), gain = (s.price - hd.avgBuy) * qty;
  cash += qty * s.price; hd.shares -= qty; if(hd.shares <= 0) delete holdings[s.name];
  msg(`💰 ${s.name} ${qty.toLocaleString()}주 매도 (손익 ${signed2(gain)})`);
  render();
}
function sellAll(){
  const s = marketPath[currentDay][selected], hd = holdings[s.name];
  if(!hd) return;
  const gain = (s.price - hd.avgBuy) * hd.shares;
  cash += hd.shares * s.price; delete holdings[s.name];
  msg(`💰 ${s.name} 전량 매도 (손익 ${signed2(gain)})`);
  render();
}
function msg(t){ const el = document.getElementById("msg"); if(el) el.textContent = t; }

function nextDay(){
  if(currentDay >= TOTAL_DAYS-1){ endGame(); return; }
  currentDay++; render();
}

/* =====================================================================
   8. 게임 종료 + 봇 비교 (단타 시그널의 '위력' 증명)
   ===================================================================== */
function endGame(){
  const last = marketPath[TOTAL_DAYS-1];
  let myAsset = cash;
  for(const s of last) if(holdings[s.name]) myAsset += holdings[s.name].shares * s.price;
  const myRate  = (myAsset/SEED_MONEY - 1) * 100;
  const sigRate = (signalBot(marketPath)/SEED_MONEY - 1) * 100;
  const rndRate = (randomBot(marketPath, curSeed)/SEED_MONEY - 1) * 100;

  document.getElementById("meLabel").textContent = (mode==="normal" ? "나 (일반 모드)" : "나 (하드코어 모드)") + " 최종 수익률";
  setRes("meResult", myRate); setRes("sigResult", sigRate); setRes("rndResult", rndRate);

  let v;
  if(mode === "hardcore"){
    v = `분석기 없이 감으로만 매매한 결과입니다. 같은 시장에서 단타 시그널봇은 <b class="up">${signed(sigRate)}%</b>를 벌었어요. ` +
        `🚀 신호가 보였다면 어땠을까요? '같은 장 다시'로 일반 모드에 도전해 보세요!`;
  } else if(myRate >= sigRate){
    v = `🎉 시그널봇(<b class="up">${signed(sigRate)}%</b>)보다 잘하셨습니다! 단타 신호를 완벽하게 활용했네요.`;
  } else {
    v = `단타 시그널봇 <b class="up">${signed(sigRate)}%</b> vs 무작위 매매(랜덤봇) <b>${signed(rndRate)}%</b>. ` +
        `🚀뱃지를 그대로 따라가는 것만으로도 무작위보다 훨씬 높은 수익이 납니다 — 이것이 <b class="up">단타 시그널 분석기의 위력</b>입니다.`;
  }
  document.getElementById("verdict").innerHTML = v;
  document.getElementById("overlay").classList.add("show");
}

// 🚀 시그널봇: 매일 🚀뱃지(점수 최고) 매수, +5%/−3%면 매도
function signalBot(days){
  let bcash = SEED_MONEY; const hold = {};
  for(let d = 0; d < days.length; d++){
    const snap = days[d];
    for(const s of snap) if(hold[s.name]){
      const g = (s.price - hold[s.name].buy) / hold[s.name].buy;
      if(g >= 0.05 || g <= -0.03){ bcash += hold[s.name].shares * s.price; delete hold[s.name]; }
    }
    const c = snap.filter(s => s.badge && !hold[s.name]).sort((a,b)=>b.score-a.score)[0];
    if(c && bcash > c.price){ const qty = Math.floor((bcash*0.5)/c.price);
      if(qty > 0){ bcash -= qty*c.price; hold[c.name] = {shares:qty, buy:c.price}; } }
  }
  return liquidate(bcash, hold, days[days.length-1]);
}
// 🎲 랜덤봇: 무작위 매매
function randomBot(days, seed){
  const rng = makeRandom(seed*7+13); let bcash = SEED_MONEY; const hold = {};
  for(let d = 0; d < days.length; d++){
    const snap = days[d];
    if(rng() < 0.5){ const held = snap.filter(s => hold[s.name]);
      if(held.length){ const s = held[Math.floor(rng()*held.length)]; bcash += hold[s.name].shares*s.price; delete hold[s.name]; } }
    if(rng() < 0.5){ const s = snap[Math.floor(rng()*snap.length)];
      if(!hold[s.name] && bcash > s.price){ const qty = Math.floor((bcash*0.3)/s.price);
        if(qty > 0){ bcash -= qty*s.price; hold[s.name] = {shares:qty, buy:s.price}; } } }
  }
  return liquidate(bcash, hold, days[days.length-1]);
}
function liquidate(bcash, hold, lastSnap){
  let a = bcash; for(const s of lastSnap) if(hold[s.name]) a += hold[s.name].shares*s.price; return a;
}

/* =====================================================================
   9. 다시하기
   ===================================================================== */
function replaySameMarket(){ mode = (mode==="normal") ? "hardcore" : "normal"; startGame(mode); }
function newMarket(){
  curSeed = Date.now() % 100000;
  document.getElementById("overlay").classList.remove("show");
  document.getElementById("gameScreen").classList.add("hidden");
  document.getElementById("startScreen").classList.remove("hidden");
}

/* =====================================================================
   10. 출력 보조 + 시작화면 티커 꾸미기
   ===================================================================== */
function num(n){ return Math.round(n).toLocaleString(); }
function signed(n){ return (n>0?"+":n<0?"−":"") + Math.abs(n).toFixed(1); }       // 퍼센트용
function signed2(n){ return (n>0?"+":n<0?"−":"") + Math.abs(Math.round(n)).toLocaleString() + "원"; } // 금액용
function cls(n){ return n>0 ? "up" : n<0 ? "down" : "flat"; }
function setRes(id, r){ const el = document.getElementById(id); el.textContent = signed(r)+"%"; el.className = "v mono " + cls(r); }

// 시작화면 상단 흐르는 티커 (장식용, 가상 시세)
(function(){
  const rng = makeRandom(777);
  let one = "";
  for(const s of STOCKS){
    const ch = (rng()*30 - 8);
    const c = ch >= 0 ? "up" : "down";
    one += `<span><b>${s.name}</b> <span class="mono ${c}">${(rng()*60000+3000|0).toLocaleString()} <span class="${c}">${ch>=0?"▲":"▼"}${Math.abs(ch).toFixed(1)}%</span></span></span>`;
  }
  document.getElementById("tickerTrack").innerHTML = one + one;  // 두 번 이어붙여 끊김없이 스크롤
})();
</script>
</body>
</html>
