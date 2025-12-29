# 🚀 Election Guardian: Real-Time Stream Monitoring

**Election Guardian** is a high-performance tool designed to detect "bad actors" or dominant signals in high-frequency data streams. Using the **Boyer-Moore Voting Algorithm**, it identifies potential network flooding or voting manipulation with industry-leading efficiency.



## 🛠 Technical Highlights

- **Optimal Performance:** The system identifies a majority candidate in a single pass $O(N)$ and verifies it in a second pass.
- **Space Efficiency:** Operates with **$O(1)$ auxiliary space**, meaning memory usage remains constant regardless of whether you process 1,000 or 1,000,000,000 data points.
- **The Intuition:** If a signal appears more than $N/2$ times, it is mathematically guaranteed to survive the "cancelation" process of the algorithm.

## 📂 Project Structure
- `/src`: Core logic for the StreamMonitor.
- `/simulations`: Scripts to mimic network traffic flooding.
- `/tests`: Edge case validation (empty streams, no majority, etc.).

## 🚀 Getting Started
1. Clone the repo: `git clone https://github.com/your-username/election-guardian.git`
2. Run the simulation: `python -m simulations.stream_generator`