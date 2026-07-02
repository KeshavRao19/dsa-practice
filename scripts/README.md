# scripts/

## `new_problem.py`

Scaffolds a new solution folder with a solution stub and a filled-in README.

### LeetCode

```bash
python3 scripts/new_problem.py \
    --platform leetcode \
    --number 1 \
    --title "Two Sum" \
    --difficulty easy \
    --lang py
```

### HackerRank

```bash
python3 scripts/new_problem.py \
    --platform hackerrank \
    --number 42 \
    --title "Mini-Max Sum" \
    --category algorithms \
    --lang py
```

### Options

| Flag | Required | Description |
|------|----------|-------------|
| `--platform` | yes | `leetcode` or `hackerrank` |
| `--number` | yes | Problem number (positive integer) |
| `--title` | yes | Problem title (used to generate the slug) |
| `--difficulty` | leetcode only | `easy` \| `medium` \| `hard` |
| `--category` | hackerrank only | `algorithms` \| `data-structures` \| `problem-solving` |
| `--lang` | no | `py` (default) \| `js` \| `java` \| `cpp` |

The script validates all inputs and will not overwrite an existing folder or write
outside the repository.
