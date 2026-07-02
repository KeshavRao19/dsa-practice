# DSA Practice — LeetCode & HackerRank Solutions

Personal archive of problem-solving practice across LeetCode and HackerRank, organized for
quick review and to track progress over time.

## 📁 Structure

```
dsa-practice/
├── leetcode/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── hackerrank/
│   ├── algorithms/
│   ├── data-structures/
│   └── problem-solving/
└── scripts/
    └── new_problem.py   # scaffolds a new problem folder
```

Each problem lives in its own folder named `NNNN-problem-slug` (e.g. `0001-two-sum`) and
contains:

- `solution.<ext>` — the solution code
- `README.md` — problem link, approach, complexity analysis

## 🚀 Adding a new problem

```bash
python3 scripts/new_problem.py --platform leetcode --number 1 --title "Two Sum" \
    --difficulty easy --lang py
```

This creates `leetcode/easy/0001-two-sum/` with a solution stub and a README template
already filled in. See `scripts/README.md` for full usage and options.

## 📊 Progress

| # | Problem | Difficulty | Platform | Solution | Notes |
|---|---------|------------|----------|----------|-------|
| — | _(add rows as you solve problems)_ | | | | |

> Tip: keep this table updated as you go — it doubles as a portfolio view of your work.

## ✅ Workflow

1. Solve the problem locally or on-platform.
2. Scaffold the folder with `new_problem.py`.
3. Fill in `solution.*` and the problem `README.md` (approach + complexity).
4. Add a row to the progress table above.
5. Commit with a descriptive message, e.g.:
   ```
   git add leetcode/easy/0001-two-sum
   git commit -m "Add: Two Sum (LeetCode #1) - O(n) hashmap solution"
   ```

Committing per-problem (rather than in batches) keeps a meaningful, consistent history on
your GitHub contribution graph.

## 🔒 Notes on code quality

- Solutions favor clarity over cleverness — readable code with meaningful names.
- Each solution documents time and space complexity.
- No external/untrusted input is executed by any script in this repo (see
  `scripts/new_problem.py` for input handling/validation notes).
