# Assessment-1: Analytical Problem Solving

## Contents

| File | Description |
|---|---|
| `Problem.pdf` | Original assignment questions (Annexure A) |
| `Solution.pdf` | Full worked solutions to Q1–Q5, with explanations, tables, and pseudocode |
| `Python_Code.py` | Python implementation for Q1 (BFS), Q3 (backtracking), Q4 (utility agent), Q5 (UCS) |
| `Output.png` | Visualization of the delivery-network graph with the least-cost UCS path highlighted |
| `Report.pdf` | Summary report: methodology, key results, tools used |
| `README.md` | This file |

## How to Run

```bash
pip install matplotlib networkx
python3 Python_Code.py
```

This prints the water jug solution steps, the 8-Queens board, the OLA cab
agent's ranked decision, and the UCS expansion trace + optimal path, and
regenerates `Output.png`.

## Notes

- **Q5 (Uniform Cost Search):** the delivery-network graph in the original
  assignment scan was partially cut off. A representative graph
  (`S, A, B, C, D, G` with the weights listed in `Python_Code.py` /
  `Solution.pdf`) was used to fully demonstrate the UCS method. If your
  actual assignment graph has different nodes/weights, update the `GRAPH`
  dictionary in `Python_Code.py` and re-run — the algorithm and write-up
  logic will still apply directly.
- All other questions (Q1–Q4) are answered in full against the assignment
  as given, with no assumptions required.

## Topics Covered

Breadth-First Search, PEAS agent analysis, constraint-satisfaction /
backtracking search, utility-based agents, and Uniform Cost Search.
