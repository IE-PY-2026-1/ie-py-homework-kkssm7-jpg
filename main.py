# ============================================
# 대학생 맞춤형 학습 도우미 시스템
# V2.0 - 리스트 + 조건문
# ============================================

print("=" * 52)
print("   📚 대학생 맞춤형 학습 도우미 시스템 V2.0")
print("=" * 52)

# --- 기본 정보 입력 ---
student_name     = input("학생 이름을 입력하시오: ")                        # str
subject_count    = int(input("등록할 과목 수를 입력하시오 (최소 3): "))      # int
last_semester_avg = float(input("지난 학기 평균 점수를 입력하시오: "))       # float

# 변수 초기화
total_score    = 0.0   # float  - 점수 누적용
excellent_count = 0    # int    - 우수 과목 카운터

# 리스트 초기화
subject_names = []
scores        = []
grades        = []

# --- for로 과목 입력 (최소 3개, 'q' 입력 시 break) ---
print(f"\n총 {subject_count}개 과목 정보를 입력하세요. (과목명에 'q' 입력 시 조기 종료)")
for i in range(subject_count):
    print(f"\n  [{i + 1}번째 과목]")
    name = input("    과목명: ")

    if name == "q":                  # break: 조기 종료
        print("    입력을 중단합니다.")
        break

    score = float(input("    현재 점수 (0~100): "))

    # 유효 범위 벗어나면 continue로 재입력 없이 0점 처리
    if score < 0 or score > 100:
        print("    ⚠ 0~100 범위를 벗어났습니다. 0점으로 처리합니다.")
        score = 0.0

    subject_names.append(name)    # 리스트 메소드 ① append
    scores.append(score)           # 리스트 메소드 ② append
    total_score += score           # 복합 대입 연산자 +=

    # 학점 판별 (if~elif~else 연속 조건문)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    grades.append(grade)           # 리스트 메소드 ③ append

    # 우수 과목 판별 — 논리 연산자 and, 관계 연산자 >=
    if score >= 85 and grade != "F":
        excellent_count += 1
        print("    ⭐ 우수 과목으로 선정되었습니다!")

# --- 리스트 조작 (4종) ---
subject_names.insert(0, "★TOP")   # 리스트 메소드 ④ insert (임시 마커)
subject_names.remove("★TOP")      # 리스트 메소드 ⑤ remove (마커 제거)

total_subjects = len(scores)       # 내장 함수 ⑥ len
score_sum      = sum(scores)       # 내장 함수 ⑦ sum
max_score      = max(scores)       # 내장 함수 ⑧ max

# 평균 계산
avg_score  = score_sum / total_subjects
score_diff = avg_score - last_semester_avg

# --- 과목별 상세 출력 ---
print("\n" + "=" * 52)
print(f"   ✅  {student_name} 학생의 과목별 성적")
print("=" * 52)

for i in range(total_subjects):
    badge = ""
    if scores[i] >= 85 and grades[i] != "F":   # 중첩 if (독립 조건)
        badge = " ⭐우수"
    if grades[i] == "F":                         # 독립 if
        badge = " ⚠재수강 권장"

    print(f"  {subject_names[i]:<14} | {scores[i]:5.1f}점 | {grades[i]}학점{badge}")

# --- 학기 전체 요약 ---
print("-" * 52)
print(f"  총 수강 과목  : {total_subjects}개")
print(f"  현재 평균    : {avg_score:.1f}점")
print(f"  지난 학기 대비: {score_diff:+.1f}점")
print(f"  최고 점수    : {max_score:.1f}점")
print(f"  우수 과목 수  : {excellent_count}개")

# --- 종합 판정 (and 연산자) ---
print("=" * 52)
if avg_score >= 90 and excellent_count >= 2:
    print(f"  🏆 {student_name} 학생은 이번 학기 최우수 학습자입니다!")
elif avg_score >= 75:
    print(f"  👍 {student_name} 학생은 양호한 학습 상태입니다.")
elif avg_score >= 60:
    print(f"  📖 {student_name} 학생은 더 많은 노력이 필요합니다.")
else:
    print(f"  ⚠  {student_name} 학생은 학습 지도가 필요합니다.")

# not 연산자 활용
if not excellent_count > 0:
    print("  💡 우수 과목이 없습니다. 더 분발해봅시다!")

print("=" * 52)
