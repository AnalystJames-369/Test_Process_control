# Test_Process_Control

repository for tracking and managing test process control and compliance

Project Overview: This repository contains scripts and tools for test automation.

KEY FEATURES

---

## 🧪 Load & Performance Engineering Portfolio (Locust + Cloud Host)

An end-to-end performance testing suite designed according to international quality standards defined by the **ISTQB® Certified Tester Foundation Level (CTFL) v4.0 Syllabus**.

This project simulates realistic, high-concurrency user traffic against a target API deployed on both **Localhost** and **Render Cloud Infrastructure**, capturing response times, throughput (RPS), and failure conditions.

---

## 📋 ISTQB CTFL v4.0 Standards Alignment

| ISTQB Concept | Technical Implementation in Repository |
| :--- | :--- |
| **System Under Test (SUT)** | RESTful Web API hosted on Localhost (`http://localhost:8000`) & Render Host. |
| **Test Basis** | Non-functional performance SLAs (Response Time < 500ms, HTTP Error Rate < 1%). |
| **Test Execution Tool** | Locust Framework (Python-based) executing HEADLESS and Web UI modes. |
| **Test Harness / Orchestrator** | Automated Python runner (`run_tests.py`) executing sequential profiles. |
| **Test Artifacts** | Time-stamped HTML Execution Reports stored automatically in `./reports/`. |
| **Exit Criteria** | Zero unhandled failures, P95 Latency strictly < 500ms, 100% SLA validation. |

---

## 🎯 Load Profiles & Test Execution Matrix

The test harness automates four distinct load profiles to evaluate system behavior under varying traffic conditions:

1. **Nominal Load Test (50 Virtual Users):**
   * **Objective:** Establish baseline operational metrics under expected normal load.
   * **Ramp-up:** 5 VUs/sec | **Duration:** 2 minutes.

2. **Stress Testing (500 Virtual Users):**
   * **Objective:** Identify system bottlenecks and response time degradation beyond capacity limits.
   * **Ramp-up:** 25 VUs/sec | **Duration:** 3 minutes.

3. **Spike / Capacity Test (5,000 Virtual Users):**
   * **Objective:** Evaluate resilience, error spike recovery, and stability during sudden surge traffic.
   * **Ramp-up:** 100 VUs/sec | **Duration:** 1 minute.

4. **Endurance / Soak Test (500 Virtual Users - Extended):**
   * **Objective:** Detect memory leaks, connection pool exhaustion, and performance degradation over time.
   * **Ramp-up:** 20 VUs/sec | **Duration:** 10+ minutes.

---

## 🛠️ Key Technical Differentiators

* **Explicit SLA & Exception Validation:** Custom HTTP status checks (`catch_response=True`) validating whether endpoints respond within the 500ms SLA limit.
* **Automated Harness Orchestration:** `run_tests.py` triggers all four load profiles sequentially in headless mode without manual intervention.
* **Portable Container Architecture:** Fully containerized setup via `Dockerfile` and `docker-compose.yml` for execution in any CI/CD environment.

---

## 📂 Repository Structure

```text
.
├── locustfile.py          # Core Locust Test Scenario Definitions (Tasks & SLAs)
├── run_tests.py           # Automated Test Harness Orchestrator (Executes all profiles)
├── requirements.txt       # Project Dependencies (Locust >= 2.20.0)
├── Dockerfile             # Container definition for portable execution
├── docker-compose.yml     # Service orchestrator for Docker deployment
├── .gitignore             # Exclusion rules for local logs and report caches
├── reports/               # Automated HTML execution summary artifacts
└── README.md              # Master Project Documentation
