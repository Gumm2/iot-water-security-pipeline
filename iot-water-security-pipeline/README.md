# Secure IoT Water Sensor Monitoring & Anomaly Detection Pipeline

## Overview

This project simulates a cybersecurity pipeline for smart water infrastructure systems. It models how IoT sensors generate operational data, transmit readings over a network, and require security controls to prevent unauthorized access or manipulation.

The system generates realistic water sensor telemetry, streams data using MQTT communication, implements TLS/mTLS security, and applies anomaly detection techniques to identify abnormal sensor behavior.

Built as part of the Extern IoT Cybersecurity program.

---

## System Architecture

```
Water Sensor Simulation
          |
          v
Python Telemetry Generator
          |
          v
MQTT Publisher
          |
          v
MQTT Broker
          |
          v
Dashboard Subscriber
          |
          v
Anomaly Detection & Security Monitoring
```

---

## Features

- Generated realistic IoT sensor telemetry including:
  - Water pressure readings
  - Flow rate measurements
  - Timestamped device data
  - Simulated abnormal behavior

- Built real-time MQTT communication:
  - Sensor publisher
  - Dashboard subscriber
  - Live data monitoring

- Analyzed IoT security vulnerabilities:
  - Unencrypted traffic exposure
  - Unauthorized message access
  - Lack of device authentication

- Implemented security improvements:
  - TLS encryption
  - Mutual TLS (mTLS)
  - Certificate-based authentication

- Developed anomaly detection workflow:
  - Injected abnormal sensor events
  - Detected suspicious readings
  - Evaluated infrastructure risks

---

## Repository Structure

```
src/
├── core/
│   ├── sensor_publisher.py
│   └── dashboard_subscriber.py
│
├── security/
│   ├── publisher_mtls.py
│   ├── subscriber_mtls.py
│   └── generate_client_certs.py
│
├── security_testing/
│   ├── attack_simulator.py
│   ├── defense_tester.py
│   ├── identity_tester.py
│   ├── mtls_benchmark.py
│   └── experiment_runner.py
│
└── anomaly_detection/
    ├── anomaly_injector.py
    ├── dashboard_server_ai.py
    └── subscriber_dashboard_ai.py
```

---

## Technologies Used

- Python
- MQTT
- Eclipse Mosquitto
- TLS/mTLS Security
- Certificate Authentication
- Flask
- Pandas / NumPy
- Scikit-Learn

---

## Key Takeaways

This project demonstrates how cybersecurity, data engineering, and analytics intersect in real-world connected systems. IoT devices are not only a hardware problem — they create continuous streams of operational data that require secure transmission, monitoring, and anomaly detection.
