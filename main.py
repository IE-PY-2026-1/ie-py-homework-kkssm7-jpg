# =====================================================
#  [2026-01] 급등주 포착 단타 시그널 분석기
#  V4.0 - 함수 모듈화(def/import) + 딕셔너리 전환 + 예외처리(try-except)
#  ※ 1차(입출력·산술)+2차(리스트·조건문)+3차(메뉴·반복문) 누적
#  ※ 4차 추가: 기능별 함수 분리 / 외부 모듈 signal_core.py import /
#     종목 1개 = 딕셔너리 1개 / 입력 오류 try-except 방어
#  ※ 교육용 콘솔 시뮬레이션 (실제 매매/투자 권유 아님)
# =====================================================

import signal_core as sc   # 외부 파일(모듈)로 분리한 핵심 계산 함수들을 가져온다


# ----- 입력 도우미 함수: 예외처리(try-except)로 잘못된 입력 방어 -----
def ask_float(prompt):
    """실수를 입력받되, 숫자가 아니면 다시 묻는다. (ValueError 예외처리)"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("    ⚠ 숫자(실수)로 입력하세요. 예: 12500")


def ask_int(prompt):
    """정수를 입력받되, 숫자가 아니면 다시 묻는다. (ValueError 예외처리)"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("    ⚠ 숫자(정수)로 입력하세요. 예: 30000")


# ----- 메뉴 1: 종목 시세 입력 -> 딕셔너리로 만들어 워치리스트에 추가 -----
def input_stock(watchlist):
    name         = input("  종목명          : ")
    now_price    = ask_float("  현재가(원)       : ")
    prev_close   = ask_float("  전일 종가(원)    : ")
    today_volume = ask_int("  당일 거래량(주)  : ")
    avg_volume   = ask_int("  평소 거래량(주)  : ")

    # 전일종가/평소거래량이 0이면 0으로 나누기 오류 -> try-except로 방어
    try:
        stock = sc.make_stock(name, now_price, prev_close, today_volume, avg_volume)
    except ZeroDivisionError:
        print("    ⚠ 전일 종가와 평소 거래량은 0이 될 수 없습니다. 입력을 취소합니다.")
        return

    watchlist.append(stock)
    print(f"  -> [{stock['name']}] 등락률 {stock['rate']:+.2f}% / 거래량 {stock['ratio']:.2f}배")
    print(f"     급등점수 {stock['score']:.1f}점 / 등급 {stock['grade']} / {stock['badge']}  (워치리스트 추가 완료)")


# ----- 메뉴 2: 워치리스트 전체 스캔 (for 순회) -----
def scan_all(watchlist):
    if len(watchlist) == 0:
        print("  워치리스트가 비어 있습니다. 먼저 1번으로 종목을 입력하세요.")
        return
    print("  [ 워치리스트 전체 스캔 ]")
    for i in range(len(watchlist)):
        s = watchlist[i]
        print(f"   {i + 1:>2}. {s['name']:<10} 급등점수 {s['score']:>6.1f}점  등급 {s['grade']}  {s['badge']}")


# ----- 메뉴 3: 급등주 필터링 (S·A 등급만) -----
def filter_surge(watchlist):
    if len(watchlist) == 0:
        print("  워치리스트가 비어 있습니다.")
        return
    print("  [ 급등주 필터 : S(강력급등) · A(단타후보) 등급만 ]")
    hit = 0
    for i in range(len(watchlist)):
        s = watchlist[i]
        if s["grade"] == "S" or s["grade"] == "A":
            hit += 1
            print(f"   ⭐ {s['name']:<10} 급등점수 {s['score']:>6.1f}점  등급 {s['grade']}")
    if hit == 0:
        print("   조건을 만족하는 급등주가 없습니다.")
    else:
        print(f"   => 총 {hit}종목이 급등주 후보입니다.")


# ----- 메뉴 4: 단타 진입 시그널 (복합조건 뱃지 + 모의 손익) -----
def show_signals(watchlist):
    if len(watchlist) == 0:
        print("  워치리스트가 비어 있습니다.")
        return
    print("  [ 단타 진입 시그널 : 복합조건(등락률 15%↑ AND 거래량 3배↑) 통과 종목 ]")
    hit = 0
    for i in range(len(watchlist)):
        s = watchlist[i]
        if s["badge"] == "🚀단타진입":
            hit += 1
            plan = sc.make_plan(s["price"])   # 진입가/목표가/손절가 딕셔너리
            print(f"   🚀 {s['name']} (등락률 {s['rate']:+.2f}%, 거래량 {s['ratio']:.2f}배)")
            print(f"      진입 {plan['entry']:,.0f}원 / 목표 {plan['target']:,.0f}원(+5%) / 손절 {plan['stop']:,.0f}원(-3%)")
    if hit == 0:
        print("   복합조건을 만족하는 종목이 아직 없습니다.")


# ----- 메뉴 5: 워치리스트 전체 정보 + 통계 -----
def show_all(watchlist):
    if len(watchlist) == 0:
        print("  워치리스트가 비어 있습니다.")
        return
    print("  [ 워치리스트 전체 정보 ]")
    total_score = 0.0
    best_score  = watchlist[0]["score"]
    for i in range(len(watchlist)):
        s = watchlist[i]
        print(f"   {s['name']:<10} {s['price']:>9,.0f}원  {s['rate']:>+7.2f}%  "
              f"{s['ratio']:>5.2f}배  {s['score']:>6.1f}점  {s['grade']}  {s['badge']}")
        total_score += s["score"]
        if s["score"] > best_score:
            best_score = s["score"]
    avg_score = total_score / len(watchlist)
    print("  " + "-" * 46)
    print(f"   총 {len(watchlist)}종목 | 평균 급등점수 {avg_score:.1f}점 | 최고점 {best_score:.1f}점")


# ----- 메뉴판 출력 함수 -----
def print_menu():
    print()
    print("=" * 50)
    print(" [ 메뉴 ]")
    print("  1 --- 종목 시세 입력   (등락률·점수·등급 자동 계산)")
    print("  2 --- 워치리스트 스캔  (전체 등급 일괄 출력)")
    print("  3 --- 급등주 필터링    (S·A 등급만 추출)")
    print("  4 --- 단타 진입 시그널 (복합조건 뱃지 + 모의 손익)")
    print("  5 --- 워치리스트 전체 정보")
    print("  0 --- 종료")
    print("=" * 50)


# ----- 메인 함수: 메뉴 루프 -----
def main():
    print("=" * 50)
    print("        급등주 포착 단타 시그널 분석기  V4.0")
    print("      (함수 모듈화 + 딕셔너리 + 예외처리 도입)")
    print("=" * 50)

    watchlist = []   # 종목 딕셔너리들을 담는 리스트 (루프 바깥에서 한 번만 선언)

    while True:
        print_menu()
        menu = input(" 메뉴 번호를 선택하세요 : ")

        if menu == "0":
            print(" 프로그램을 종료합니다. 성투하세요! 📈")
            break
        elif menu == "1":
            input_stock(watchlist)
        elif menu == "2":
            scan_all(watchlist)
        elif menu == "3":
            filter_surge(watchlist)
        elif menu == "4":
            show_signals(watchlist)
        elif menu == "5":
            show_all(watchlist)
        else:
            print("  잘못된 메뉴입니다. 0~5 사이 숫자를 입력하세요.")


# 이 파일을 직접 실행할 때만 main() 호출 (import 될 때는 실행되지 않음)
if __name__ == "__main__":
    main()
