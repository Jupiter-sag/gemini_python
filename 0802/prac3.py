"""
學生成績管理系統
功能：新增學生、輸入成績、查詢成績、計算統計、排名、刪除學生
"""

# ── 資料儲存（以字典為主結構）────────────────────────────
# 格式：{ 學號: { "姓名": str, "成績": { 科目: 分數, ... } } }
students = {}


# ══════════════════════════════════════════════════════
# 1. 新增學生
# ══════════════════════════════════════════════════════
def add_student():
    print("\n【新增學生】")
    student_id = input("輸入學號：").strip()
    if student_id in students:
        print(f"⚠️  學號 {student_id} 已存在。")
        return
    name = input("輸入姓名：").strip()
    students[student_id] = {"姓名": name, "成績": {}}
    print(f"✅ 已新增學生：{name}（{student_id}）")


# ══════════════════════════════════════════════════════
# 2. 輸入 / 更新成績
# ══════════════════════════════════════════════════════
def input_score():
    print("\n【輸入成績】")
    student_id = input("輸入學號：").strip()
    if student_id not in students:
        print("⚠️  找不到該學號，請先新增學生。")
        return

    subject = input("輸入科目名稱：").strip()
    while True:
        try:
            score = float(input(f"輸入 {subject} 分數（0-100）："))
            if 0 <= score <= 100:
                break
            print("⚠️  分數須介於 0 到 100 之間。")
        except ValueError:
            print("⚠️  請輸入有效的數字。")

    students[student_id]["成績"][subject] = score
    print(f"✅ {students[student_id]['姓名']} 的 {subject} 成績已設定為 {score}")


# ══════════════════════════════════════════════════════
# 3. 查詢單一學生成績
# ══════════════════════════════════════════════════════
def query_student():
    print("\n【查詢學生成績】")
    student_id = input("輸入學號：").strip()
    if student_id not in students:
        print("⚠️  找不到該學號。")
        return

    info = students[student_id]
    print(f"\n  學號：{student_id}")
    print(f"  姓名：{info['姓名']}")

    scores = info["成績"]
    if not scores:
        print("  尚未輸入任何成績。")
        return

    print("  ┌──────────────┬────────┐")
    print("  │ 科目         │  分數  │")
    print("  ├──────────────┼────────┤")
    for subject, score in scores.items():
        print(f"  │ {subject:<12} │ {score:>6.1f} │")
    print("  └──────────────┴────────┘")

    avg = sum(scores.values()) / len(scores)
    print(f"  平均分數：{avg:.2f}")
    print(f"  等第：{grade_letter(avg)}")


# ══════════════════════════════════════════════════════
# 4. 顯示全部學生列表
# ══════════════════════════════════════════════════════
def list_all_students():
    print("\n【學生名單】")
    if not students:
        print("  目前沒有任何學生資料。")
        return

    print(f"  共 {len(students)} 位學生：")
    print("  ┌──────────┬──────────────┬────────┬──────┐")
    print("  │ 學號     │ 姓名         │ 平均   │ 等第 │")
    print("  ├──────────┼──────────────┼────────┼──────┤")
    for sid, info in students.items():
        scores = info["成績"]
        if scores:
            avg = sum(scores.values()) / len(scores)
            grade = grade_letter(avg)
        else:
            avg = 0.0
            grade = "—"
        print(f"  │ {sid:<8} │ {info['姓名']:<12} │ {avg:>6.1f} │ {grade:<4} │")
    print("  └──────────┴──────────────┴────────┴──────┘")


# ══════════════════════════════════════════════════════
# 5. 成績排名
# ══════════════════════════════════════════════════════
def show_ranking():
    print("\n【成績排名】")
    if not students:
        print("  目前沒有任何學生資料。")
        return

    # 只列出有成績的學生
    ranked = []
    for sid, info in students.items():
        scores = info["成績"]
        if scores:
            avg = sum(scores.values()) / len(scores)
            ranked.append((avg, info["姓名"], sid))

    if not ranked:
        print("  尚未輸入任何成績。")
        return

    ranked.sort(reverse=True)

    print("  排名  姓名            學號        平均    等第")
    print("  " + "-" * 48)
    for rank, (avg, name, sid) in enumerate(ranked, start=1):
        print(f"  {rank:<6}{name:<16}{sid:<12}{avg:>6.1f}  {grade_letter(avg)}")


# ══════════════════════════════════════════════════════
# 6. 科目統計（全班）
# ══════════════════════════════════════════════════════
def subject_statistics():
    print("\n【科目統計】")
    # 收集所有科目
    all_subjects = set()
    for info in students.values():
        all_subjects.update(info["成績"].keys())

    if not all_subjects:
        print("  尚未輸入任何成績。")
        return

    print("  ┌──────────────┬────────┬────────┬────────┬────────┐")
    print("  │ 科目         │  平均  │  最高  │  最低  │ 人數   │")
    print("  ├──────────────┼────────┼────────┼────────┼────────┤")
    for subject in sorted(all_subjects):
        scores = [
            info["成績"][subject]
            for info in students.values()
            if subject in info["成績"]
        ]
        avg  = sum(scores) / len(scores)
        high = max(scores)
        low  = min(scores)
        print(
            f"  │ {subject:<12} │ {avg:>6.1f} │ {high:>6.1f} │ {low:>6.1f} │ {len(scores):>6} │"
        )
    print("  └──────────────┴────────┴────────┴────────┴────────┘")


# ══════════════════════════════════════════════════════
# 7. 刪除學生
# ══════════════════════════════════════════════════════
def delete_student():
    print("\n【刪除學生】")
    student_id = input("輸入要刪除的學號：").strip()
    if student_id not in students:
        print("⚠️  找不到該學號。")
        return

    name = students[student_id]["姓名"]
    confirm = input(f"確定刪除 {name}（{student_id}）的所有資料？（y/n）：").strip().lower()
    if confirm == "y":
        del students[student_id]
        print(f"✅ 已刪除學生：{name}（{student_id}）")
    else:
        print("取消刪除。")


# ══════════════════════════════════════════════════════
# 輔助函式：換算等第
# ══════════════════════════════════════════════════════
def grade_letter(score: float) -> str:
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


# ══════════════════════════════════════════════════════
# 主選單
# ══════════════════════════════════════════════════════
def show_menu():
    print("\n" + "=" * 40)
    print("    📚 學生成績管理系統")
    print("=" * 40)
    print("  1. 新增學生")
    print("  2. 輸入 / 更新成績")
    print("  3. 查詢學生成績")
    print("  4. 顯示全部學生")
    print("  5. 成績排名")
    print("  6. 科目統計")
    print("  7. 刪除學生")
    print("  0. 離開")
    print("=" * 40)


def main():
    actions = {
        "1": add_student,
        "2": input_score,
        "3": query_student,
        "4": list_all_students,
        "5": show_ranking,
        "6": subject_statistics,
        "7": delete_student,
    }

    while True:
        show_menu()
        choice = input("請選擇功能（0-7）：").strip()

        if choice == "0":
            print("\n👋 感謝使用，再見！")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("⚠️  無效的選項，請重新輸入。")


if __name__ == "__main__":
    main()
