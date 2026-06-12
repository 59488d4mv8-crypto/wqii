#!/usr/bin/env python3
"""课程内容验证脚本
检查 content/courses 下每个课程包的结构完整性与 JSON/Markdown 语法。
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = ROOT / "content" / "courses"

REQUIRED_COURSE_FIELDS = {"title", "description", "stage", "chapters"}
REQUIRED_CHAPTER_FIELDS = {"title", "lessons"}
REQUIRED_LESSON_FIELDS = {"title", "type"}
VALID_LESSON_TYPES = {"read", "code", "quiz", "exam"}


def check_course(course_id: str) -> int:
    errors = 0
    course_dir = COURSES_DIR / course_id
    meta_path = course_dir / "course.json"
    if not meta_path.exists():
        print(f"  ❌ 缺少 course.json")
        return 1

    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"  ❌ course.json 语法错误: {e}")
        return 1

    for field in REQUIRED_COURSE_FIELDS:
        if field not in meta:
            print(f"  ❌ course.json 缺少字段: {field}")
            errors += 1

    chapters = meta.get("chapters", [])
    if not chapters:
        print("  ❌ 至少需要 1 个章节")
        errors += 1

    for i, ch in enumerate(chapters):
        for field in REQUIRED_CHAPTER_FIELDS:
            if field not in ch:
                print(f"  ❌ chapter[{i}] 缺少字段: {field}")
                errors += 1
        for j, lesson in enumerate(ch.get("lessons", [])):
            for field in REQUIRED_LESSON_FIELDS:
                if field not in lesson:
                    print(f"  ❌ chapter[{i}] lesson[{j}] 缺少字段: {field}")
                    errors += 1
            if lesson.get("type") not in VALID_LESSON_TYPES:
                print(f"  ❌ chapter[{i}] lesson[{j}] type 非法: {lesson.get('type')}")
                errors += 1
            # 检查引用的文件是否存在
            for key in ("content", "template", "tests", "questions"):
                fn = lesson.get(key)
                if fn:
                    fp = course_dir / fn
                    if not fp.exists():
                        print(f"  ⚠️  chapter[{i}] lesson[{j}] 引用文件不存在: {fn}")

    return errors


def main() -> int:
    if not COURSES_DIR.exists():
        print(f"❌ 未找到课程目录: {COURSES_DIR}")
        return 1
    total_errors = 0
    course_count = 0
    for course_id in sorted(os.listdir(COURSES_DIR)):
        if course_id.startswith("."):
            continue
        if not (COURSES_DIR / course_id).is_dir():
            continue
        course_count += 1
        print(f"\n[{course_id}]")
        total_errors += check_course(course_id)
    print(f"\n==== 共检查 {course_count} 门课程，错误数：{total_errors} ====")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
