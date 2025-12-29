# 🚀 Election Guardian: Real-Time Stream Monitoring

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Election Guardian** is a high-performance monitoring tool designed to identify "bad actors" or dominant signals in high-frequency data streams. By implementing the **Boyer-Moore Voting Algorithm**, it provides a mathematically guaranteed method to detect majority elements with absolute minimal memory overhead.

---

## 💡 The Problem
In high-velocity systems (like voting servers or network firewalls), tracking the frequency of *every* incoming ID is memory-intensive. If you have millions of unique IPs, a standard hash map will crash your system. 

**Election Guardian** solves this by finding the most frequent element without storing a counter for every item.

## 🛠 Technical Highlights

- **Optimal Performance:** Identifies a majority candidate in a single pass $O(N)$ and verifies it in a second pass.
- **Space Efficiency:** Operates with **$O(1)$ auxiliary space**, maintaining constant memory usage regardless of stream size.
- **Strict Verification:** Distinguishes between a "true majority" ($> N/2$) and a simple plurality.

---

## 🧠 How It Works (The Intuition)
The algorithm works like a series of "duels." 
1. If we see a new candidate and our `vote` count is 0, they take the lead.
2. If we see the same candidate again, their `vote` increases.
3. If we see a *different* signal, they "fight" and one vote is removed.
4. Because a true majority occupies more than half the stream, they will mathematically always be the last one standing.


---

## 📂 Project Structure
- `src/`: Core logic for the `StreamMonitor` engine.
- `simulations/`: Real-time traffic simulation mimicking a network flood.
- `tests/`: Robust test suite covering edge cases (empty streams, no majority, etc.).

---

## 🚀 Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/election-guardian.git](https://github.com/your-username/election-guardian.git)
   cd election-guardian
