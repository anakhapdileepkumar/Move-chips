# 🎯 Minimum Cost to Move Chips to the Same Position

## 📜 Problem Statement
You are given `n` chips, where the position of the `i`th chip is `position[i]`.  
You can move chips in two ways:
1. `position[i] + 2` or `position[i] - 2` → **cost = 0**
2. `position[i] + 1` or `position[i] - 1` → **cost = 1**

Return the **minimum cost** to move all chips to the same position.


## 💡 Idea
- Moving by **2 steps** is free → chips stay within their parity (even ↔ even or odd ↔ odd).
- Cost occurs **only** when moving between odd and even positions.
- Count how many chips are on even positions and how many on odd positions.
- Move the smaller group to the larger group → **minimum cost**.
