# Tic-Tac-Toe with Rule-Based Decision Engine (Python)

## Project Overview

This project implements a **deterministic, rule-based decision engine** for the game of Tic-Tac-Toe, designed to simulate strategic reasoning rather than relying on random or brute-force approaches. The system models the game as a constrained decision problem and evaluates board states to select **locally optimal moves** at each turn.

Unlike trivial implementations, the computer opponent follows a **prioritized decision hierarchy** that approximates optimal play without using full minimax search, demonstrating an understanding of **game theory, state evaluation, and algorithmic tradeoffs**.

---

## Decision Architecture

The computer’s move selection is governed by a **multi-stage priority system**, evaluated sequentially at each turn:

1. **Immediate win detection**
2. **Opponent win prevention**
3. **Fork creation** (multiple simultaneous winning threats)
4. **Fork prevention**
5. **Positional optimization** (center control)
6. **Corner acquisition**
7. **Fallback random move (guaranteed valid)**

Each decision stage is implemented as a **pure board-state evaluation**, enabling deterministic reasoning and reproducibility.

---

## Core Algorithms

### Board State Evaluation

The project abstracts board evaluation into reusable predicates:

* `checkWin(board, player)`
  Determines whether a given board configuration satisfies any winning condition.

* `testWin(board, player, r, c)`
  Simulates a hypothetical move and evaluates whether it produces a terminal winning state.

* `testFork(board, player, r, c)`
  Simulates a move and counts future winning opportunities to detect fork states.

These functions allow the AI to reason about **future consequences of moves** without mutating the true game state.

---

## Design Rationale

* **Rule-based strategy over brute force**
  Demonstrates how constrained logic can approximate optimal play with minimal computational overhead.

* **State simulation via deep copying**
  Enables hypothetical reasoning without side effects.

* **Deterministic control flow**
  Guarantees predictable and explainable behavior — essential for interpretable AI systems.

* **Turn-based state machine**
  Clean separation of game progression, evaluation, and terminal conditions.

---

## Technical Scope

* Language: Python
* Paradigm: Procedural + functional decomposition
* Concepts demonstrated:

  * State evaluation
  * Decision hierarchies
  * Game theory heuristics
  * Algorithmic optimization
  * Constraint-based reasoning

---

## Project Significance

This project illustrates how **strategic reasoning can be encoded algorithmically** without advanced machine-learning techniques. It reflects principles used in:

* Game AI
* Search heuristics
* Decision engines
* Rule-based expert systems

The implementation emphasizes **clarity, correctness, and strategic depth** over UI or graphics, aligning with core computer science fundamentals.

---

## Extensions & Research Directions

* Implement full minimax with alpha-beta pruning
* Compare heuristic vs optimal play performance
* Generalize decision engine to N×N boards
* Add formal state evaluation scoring functions
* Analyze decision tree complexity empirically

---

## Short Description (GitHub “About” section)

Use one of these:

**Recommended:**

> Rule-based Tic-Tac-Toe AI implementing strategic decision hierarchies, fork detection, and deterministic state evaluation in Python.

**Alternative:**

> Deterministic game-playing engine for Tic-Tac-Toe using state simulation and heuristic decision rules.


