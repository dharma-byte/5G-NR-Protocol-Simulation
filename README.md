# 5G NR Protocol Stack Simulation & Traffic Analysis

## 📌 Overview
This project simulates a simplified version of the 5G NR Layer 2 protocol stack, focusing on packet flow, segmentation, retransmission, and performance analysis under lossy network conditions.

It models key components of the 5G communication pipeline and demonstrates how data is transmitted, lost, retransmitted, and reconstructed reliably.

---

## 🧠 Architecture

```text
Client → PDCP → RLC → MAC → Channel → Receiver


### Components:
- **PDCP (Packet Data Convergence Protocol)**  
  Handles packet formatting and prepares data for transmission.

- **RLC (Radio Link Control)**  
  Performs segmentation and assigns sequence numbers for reliable delivery.

- **MAC (Medium Access Control)**  
  Simulates scheduling and transmission delay.

- **Channel**  
  Introduces packet loss (20%) and latency to mimic real-world network conditions.

---

## ⚙️ Features

- ✔ Layered protocol simulation (PDCP, RLC, MAC)
- ✔ Packet segmentation with sequence numbers
- ✔ Probabilistic packet loss simulation
- ✔ Retransmission mechanism (reliability)
- ✔ Packet reordering using sequence numbers
- ✔ End-to-end message reconstruction
- ✔ Performance metrics:
  - Latency
  - Throughput

---

## 🔧 Tech Stack

- Python 3.x
- Standard libraries:
  - `time`
  - `random`
  - `logging`

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/dharma-byte/5G-NR-Protocol-Simulation.git
cd 5G-NR-Protocol-Simulation

### 2. Run the project
python main.py


## Sample Output
[INFO] Starting 5G Simulation
[INFO] [PDCP] Processing data: HELLO_5G_NETWORK_SIMULATION
[INFO] [RLC] Segmenting packet
[INFO] [MAC] Scheduling transmission
[WARNING] [Channel] Packet lost: HELLO
[INFO] Retransmitting lost packets: [(0, 'HELLO')]
[INFO] Final Received Data: ['HELLO', '_5G_N', 'ETWOR', 'K_SIM', 'ULATI', 'ON']
[INFO] Reconstructed Message: HELLO_5G_NETWORK_SIMULATION
[INFO] Latency: 0.41 sec
[INFO] Throughput: 64.97 chars/sec


