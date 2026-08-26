# 📋 Master Test Plan (ISTQB CTFL v4.0 Aligned)

**Project Name:** Test_Process_Control  
**Project Type:** Performance & Load Test Automation Suite  
**Standards:** ISTQB® Certified Tester Foundation Level (CTFL) v4.0  

---

## 1. Introduction & Objectives
This Master Test Plan defines the testing scope, schedule, resources, and execution strategies for the automated performance and load test suite developed for the target RESTful Web API. The main objective is to evaluate system behavior, throughput, and latency under various concurrency profiles (Nominal, Stress, and Spike testing) using Locust and Python automation scripts.

---

## 2. Scope of Testing
* **In-Scope:**
  * Authentication flow (`/api/login`) executed as a pre-condition (`on_start`).
  * High-demand user directory endpoints (`/api/usuarios`) evaluated under weighted task distributions (`@task`).
  * SLA validation of 95th Percentile (P95) response times staying below the 2.0-second threshold.
  * Automated headless execution and artifact report generation (`./reports/`).
* **Out-of-Scope:**
  * UI/Frontend end-to-end functional user interface tests.
  * Native mobile application testing.

---

## 3. Test Environment & Tools
* **Execution Engine:** Locust (v2.20.0 or higher)
* **Orchestration Script:** Custom Python harness (`run_tests.py`)
* **Operating System:** Ubuntu Linux / Localhost environment
* **Version Control:** Git & GitHub (`Test_Process_control`)

---

## 4. Entry & Exit Criteria
* **Entry Criteria:**
  * Target environment/API is online and reachable.
  * Test dependencies (`requirements.txt`) are installed in a clean virtual environment (`venv`).
  * Test scripts (`locustfile.py`) successfully validated for syntax and execution integrity.
* **Exit Criteria:**
  * Completion of all planned load test profiles (Nominal, Stress, Spike).
  * Overall HTTP error rate maintained below 1.0%.
  * Historical HTML reports successfully exported to `./reports/`.
  * Documentation (Test Cases, Summary Report) fully updated and committed.

---

## 5. Risk Management & Mitigation
* **Risk 1:** Network latency fluctuations interfering with local performance metrics.
  * *Mitigation:* Execution restricted to localized environments or controlled staging endpoints with dedicated resources.
* **Risk 2:** Sudden resource exhaustion on the local host during spike tests (5,000 VUs).
  * *Mitigation:* Use headless mode via the Python orchestrator to optimize resource consumption and monitor local process thresholds.
