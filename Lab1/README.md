# Lab 1 – Python Testing & GitHub Actions (MLOps, IE-7374)

![Lab1 Pytest](https://github.com/kmaurya9/MLops-Labs/actions/workflows/pytest_action.yml/badge.svg)
![Lab1 Unittest](https://github.com/kmaurya9/MLops-Labs/actions/workflows/unittest_action.yml/badge.svg)

This lab sets up a small Python project with a virtual environment, a standard folder layout, unit tests written with both **pytest** and **unittest**, and **GitHub Actions** workflows that run those tests automatically on every push.

Based on [raminmohammadi/MLOps – Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1).

---

## Project Structure

```
MLops-Labs/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml     # CI: runs pytest, uploads JUnit XML report
│       └── unittest_action.yml   # CI: runs unittest
├── .gitignore                         # ignores venvs, caches, test reports
└── Lab1/
    ├── data/                          # placeholder for datasets
    ├── src/
    │   └── calculator.py              # functions under test
    ├── test/
    │   ├── test_pytest.py             # pytest test suite
    │   └── test_unittest.py           # unittest test suite
    ├── requirements.txt
    └── README.md
```

---

## What Was Implemented

### `src/calculator.py`

| Function | Description |
|---|---|
| `fun1(x, y)` | Returns `x + y` |
| `fun2(x, y)` | Returns `x - y` |
| `fun3(x, y)` | Returns `x * y` |
| `fun4(x, y)` | Combines the above: `fun1(x, y) + fun2(x, y) + fun3(x, y)` |
| `fun5(x, y)` | Returns `x / y`; raises `ZeroDivisionError` when `y == 0` |

All functions validate their inputs through a shared `_validate()` helper and raise `ValueError` for anything that is not an `int` or `float` (strings, `None`, lists, and booleans are rejected).

### `test/test_pytest.py`
- Uses `@pytest.mark.parametrize` to run each function against multiple input/expected-output cases (positives, negatives, zero, floats).
- Checks `fun5` with `pytest.approx` and verifies the divide-by-zero error with `pytest.raises`.
- A stacked parametrized test checks that **every** function rejects invalid inputs (`"2"`, `None`, `[1]`, `True`).

### `test/test_unittest.py`
- A `unittest.TestCase` class with one test method per function.
- Uses `assertEqual`, `assertAlmostEqual` (for floating-point results), and `assertRaises`.
- Uses `subTest` to check invalid inputs across all functions in one test, while still reporting each failing case individually.

### GitHub Actions
Both workflows live in `.github/workflows/` at the repository root (GitHub only discovers workflows there) and:
- Trigger on pushes and pull requests to `main` that touch `Lab1/**`, and can also be run manually (`workflow_dispatch`).
- Run all steps inside `Lab1/` via `defaults.run.working-directory`.
- Use `actions/checkout@v4` and `actions/setup-python@v5` with **Python 3.12**.

| Workflow | Steps |
|---|---|
| `pytest_action.yml` | Checkout → Set up Python → Install deps → `pytest --junitxml=pytest-report.xml` → Upload report as artifact `test-results` (`actions/upload-artifact@v4`, runs even on failure) → Notify on success/failure |
| `unittest_action.yml` | Checkout → Set up Python → Install deps → `python -m unittest -v test.test_unittest` → Notify on success/failure |

### Changes from the original lab template
- Workflows moved from `Lab1/workflows/` to `.github/workflows/` so they actually run, and scoped to the `Lab1/` subfolder.
- Updated to current action versions (the template's `upload-artifact@v2` is retired and fails) and Python 3.12 (3.8 is no longer available on `ubuntu-latest`).
- Fixed invalid keys in the template pytest workflow (`run-nam`, `label` event).
- `requirements.txt` now lists `pytest` (it was empty, so CI could not run pytest).
- Added a `.gitignore`, input validation for all functions, a new `fun5` (division), and edge-case / error-path tests.

---

## Running Locally

1. **Create and activate a virtual environment** (from the repo root):
    ```bash
    python3 -m venv lab_01
    source lab_01/bin/activate        # macOS / Linux
    # lab_01\Scripts\activate         # Windows
    ```

2. **Install dependencies:**
    ```bash
    cd Lab1
    pip install -r requirements.txt
    ```

3. **Run the pytest suite** (from `Lab1/`):
    ```bash
    pytest -v
    # optional: generate the same XML report CI produces
    pytest --junitxml=pytest-report.xml
    ```

4. **Run the unittest suite** (from `Lab1/`):
    ```bash
    python -m unittest -v test.test_unittest
    ```
    > Run this from inside `Lab1/`. The `test/__init__.py` file makes `test` a local package so Python doesn't pick up its own built-in `test` module instead.

### Expected output
```
pytest:   47 passed, 15 subtests passed
unittest: Ran 6 tests ... OK
```

---

## Viewing CI Results

1. Push to `main` (or open a pull request) with changes under `Lab1/`.
2. Open the repository's **Actions** tab and select *Testing with Pytest* or *Python Unittests*.
3. For the pytest run, download the **test-results** artifact to view the JUnit XML report.
