# IoT Observer System

A lightweight Python implementation of the **Observer design pattern** for IoT device monitoring. A central Observer server listens for TCP connections, while Subject clients (IoT devices) report their status and location over the network.

---

## Architecture

```
┌─────────────────────┐         TCP (localhost:65432)        ┌─────────────────────┐
│      Subject        │  ──────────────────────────────────► │      Observer       │
│   (IoT Device)      │                                       │   (Comm Centre)     │
│                     │ ◄──────────────────────────────────── │                     │
│  ID | X | Y | msg   │          "Received"                   │  Logs & Displays    │
└─────────────────────┘                                       └─────────────────────┘
```

- **`observer.py`** — Runs a persistent TCP server that accepts messages from devices and maintains a timestamped log.
- **`subject.py`** — Represents an IoT device. Connects to the Observer on startup and sends a status message.

---

## Files

| File | Role |
|---|---|
| `observer.py` | Observer server — receives and logs device messages |
| `subject.py` | Subject client — IoT device that reports to the Observer |

---

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library: `socket`, `datetime`, `sys`)

---

## Usage

### 1. Start the Observer (server)

Open a terminal and run:

```bash
python observer.py
```

The Observer will start and display:

```
Comm Centre waiting for messages...
```

It will continue running, accepting connections from multiple Subject devices.

### 2. Start a Subject (IoT device client)

Open a separate terminal and run:

```bash
python subject.py <SUB_ID> <X_CORD> <Y_CORD>
```

**Arguments:**

| Argument | Description | Example |
|---|---|---|
| `SUB_ID` | Unique identifier for the device | `SUB0001` |
| `X_CORD` | X coordinate on the grid | `10` |
| `Y_CORD` | Y coordinate on the grid | `25` |

**Example:**

```bash
python subject.py SUB0001 10 25
```

**Subject output:**
```
Connecting to Observer...
Sending message...
Received from observer: Received
```

**Observer output:**
```
======== LOGS ========
2025-01-15 10:32:45.123456,SUB0001,10,25,Device is now online
```

---

## Message Format

Messages sent from a Subject to the Observer follow this format:

```
<ID>,<X>,<Y>,<message>
```

Example:
```
SUB0001,10,25,Device is now online
```

Logged entries are prepended with a timestamp:
```
2025-01-15 10:32:45.123456,SUB0001,10,25,Device is now online
```

---

## Configuration

Network settings are hardcoded in each file. To change them, update the following constants:

| Setting | File | Default |
|---|---|---|
| IP Address | `observer.py` | `127.0.0.1` |
| Port | `observer.py` | `65432` |
| Host | `subject.py` | `127.0.0.1` |
| Port | `subject.py` | `65432` |

> **Note:** Both files must use matching host and port values.

---

## Design Pattern

This project implements the **Observer (Pub/Sub) pattern**:

- The **Observer** is the subscriber — it passively waits and reacts to incoming data.
- The **Subject** is the publisher — it actively pushes updates when its state changes (e.g., coming online).

Communication is handled via **TCP sockets** over localhost, making it straightforward to extend to a real network by updating the IP address.

---

## Limitations & Future Improvements

- The Observer handles one connection at a time (no threading). Consider using `threading` or `asyncio` for concurrent device connections.
- Logs are stored in memory only — adding file persistence (e.g., writing to a `.csv`) would survive restarts.
- Subjects currently only send one message on startup. Additional `send_message()` calls can be added to report status changes.
- No authentication or encryption — suitable for local/lab use only.

---

## Licence

This project is provided for educational purposes only as part of the course 26W-CST8400-Analysis and Design Using Emerging Technologies at Algonquin College, Ottawa, ON, Canada.
