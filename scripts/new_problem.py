#!/usr/bin/env python3
"""
new_problem.py — Scaffold a new LeetCode/HackerRank solution folder.

Creates:
    <platform>/<difficulty-or-category>/NNNN-problem-slug/
        ├── solution.<ext>
        └── README.md

Usage:
    python3 scripts/new_problem.py --platform leetcode --number 1 \\
        --title "Two Sum" --difficulty easy --lang py

    python3 scripts/new_problem.py --platform hackerrank --number 42 \\
        --title "Mini-Max Sum" --category algorithms --lang py

Security notes:
    - All user-supplied strings are validated against strict allow-lists/regexes
      before being used to build filesystem paths, preventing path traversal
      (e.g. "../../etc") or injection of unexpected characters.
    - The script performs no network calls and does not execute any
      user-supplied code — it only writes template files to disk.
    - Existing files/folders are never silently overwritten.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

VALID_PLATFORMS = {"leetcode", "hackerrank"}
VALID_DIFFICULTIES = {"easy", "medium", "hard"}
VALID_CATEGORIES = {"algorithms", "data-structures", "problem-solving"}

LANG_TEMPLATES = {
    "py": ("solution.py", '''"""
{title}

LeetCode/HackerRank link: {link}

Approach:
    TODO: describe your approach here.

Time complexity:  O(?)
Space complexity: O(?)
"""


def solve():
    """TODO: implement solution."""
    raise NotImplementedError


if __name__ == "__main__":
    solve()
'''),
    "js": ("solution.js", '''/**
 * {title}
 *
 * Link: {link}
 *
 * Approach:
 *   TODO: describe your approach here.
 *
 * Time complexity:  O(?)
 * Space complexity: O(?)
 */

function solve() {{
  throw new Error("Not implemented");
}}

module.exports = solve;
'''),
    "java": ("Solution.java", '''/**
 * {title}
 *
 * Link: {link}
 *
 * Approach:
 *   TODO: describe your approach here.
 *
 * Time complexity:  O(?)
 * Space complexity: O(?)
 */
public class Solution {{
    public void solve() {{
        throw new UnsupportedOperationException("Not implemented");
    }}
}}
'''),
    "cpp": ("solution.cpp", '''// {title}
//
// Link: {link}
//
// Approach:
//   TODO: describe your approach here.
//
// Time complexity:  O(?)
// Space complexity: O(?)

class Solution {{
public:
    void solve() {{
        // TODO: implement
    }}
}};
'''),
}

README_TEMPLATE = """# {title}

- **Platform:** {platform_display}
- **Number:** {number}
- **{difficulty_label}:** {difficulty_display}
- **Link:** {link}

## Approach

_TODO: describe your approach/intuition._

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Notes

_TODO: edge cases, alternative approaches, things learned._
"""


def slugify(title: str) -> str:
    """Convert a problem title into a filesystem-safe slug."""
    slug = title.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    if not slug:
        raise ValueError("Title must contain at least one alphanumeric character.")
    return slug


def validate_number(number: int) -> int:
    if number <= 0 or number > 99999:
        raise ValueError("Problem number must be a positive integer (<= 99999).")
    return number


def build_leetcode_link(number: int, slug: str) -> str:
    return f"https://leetcode.com/problems/{slug}/"


def build_hackerrank_link(slug: str) -> str:
    return f"https://www.hackerrank.com/challenges/{slug}/problem"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold a new problem folder.")
    parser.add_argument("--platform", required=True, choices=sorted(VALID_PLATFORMS))
    parser.add_argument("--number", required=True, type=int, help="Problem number/index")
    parser.add_argument("--title", required=True, help="Problem title")
    parser.add_argument(
        "--difficulty",
        choices=sorted(VALID_DIFFICULTIES),
        help="Required for --platform leetcode",
    )
    parser.add_argument(
        "--category",
        choices=sorted(VALID_CATEGORIES),
        help="Required for --platform hackerrank",
    )
    parser.add_argument(
        "--lang",
        default="py",
        choices=sorted(LANG_TEMPLATES.keys()),
        help="Solution language (default: py)",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        number = validate_number(args.number)
        slug = slugify(args.title)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    padded_number = f"{number:04d}"
    folder_name = f"{padded_number}-{slug}"

    if args.platform == "leetcode":
        if not args.difficulty:
            print("Error: --difficulty is required for leetcode.", file=sys.stderr)
            return 1
        subdir = args.difficulty
        link = build_leetcode_link(number, slug)
        difficulty_label = "Difficulty"
        difficulty_display = args.difficulty.capitalize()
        platform_display = "LeetCode"
    else:
        if not args.category:
            print("Error: --category is required for hackerrank.", file=sys.stderr)
            return 1
        subdir = args.category
        link = build_hackerrank_link(slug)
        difficulty_label = "Category"
        difficulty_display = args.category.replace("-", " ").title()
        platform_display = "HackerRank"

    target_dir = REPO_ROOT / args.platform / subdir / folder_name

    # Defense-in-depth: ensure the resolved path stays inside the repo root.
    resolved = target_dir.resolve()
    if REPO_ROOT.resolve() not in resolved.parents:
        print("Error: refusing to write outside repo root.", file=sys.stderr)
        return 1

    if target_dir.exists():
        print(f"Error: {target_dir} already exists.", file=sys.stderr)
        return 1

    target_dir.mkdir(parents=True)

    filename, template = LANG_TEMPLATES[args.lang]
    (target_dir / filename).write_text(
        template.format(title=args.title, link=link), encoding="utf-8"
    )
    (target_dir / "README.md").write_text(
        README_TEMPLATE.format(
            title=args.title,
            platform_display=platform_display,
            number=number,
            difficulty_label=difficulty_label,
            difficulty_display=difficulty_display,
            link=link,
        ),
        encoding="utf-8",
    )

    print(f"Created {target_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
