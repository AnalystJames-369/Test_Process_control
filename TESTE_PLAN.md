# 📋 Performance & Load Test Plan (ISTQB CTFL v4.0 Aligned)

**Project:** Test_Process_Control  
**Target System:** RESTful Web API (`localhost` / Cloud Host)  
**Author:** QA Engineering Team  
**Standards:** ISTQB® Certified Tester Foundation Level (CTFL) v4.0  

---

## 1. Test Objectives & Scope

### 1.1 Objectives
Evaluate system performance, stability, response times, throughput (RPS), and failure conditions under varying concurrent user load profiles using Locust.

### 1.2 In-Scope
* **Target Endpoints:** Authentication (`/api/login`), User Directory (`/api/usuarios`), Profile Management (`/api/perfil`), and Dashboard (`/api/dashboard`).
* **Non-Functional Attributes:** Performance efficiency, response time SLAs, throughput capacity, and error rate boundaries.
* **Execution Profiles:** Nominal Load, Stress, Spike, and Endurance/Soak testing.

### 1.3 Out-of-Scope
* Security and Penetration Testing (Pentest).
* Third-party external API integration benchmarks (unless hosted locally).
* Graphical User Interface (GUI) visual or cross-browser testing.

---

## 2. ISTQB CTFL v4.0 Alignment Matrix

| ISTQB Concept | Implementation Detail in Repository |
| :--- | :--- |
| **System Under Test (SUT)** | Localhost RESTful API target service. |
| **Test Basis** | Performance non-functional requirements and SLA definitions (< 2.0s latency). |
| **Test Execution Tool** | Locust Framework (Python-based). |
| **Test Harness / Orchestrator** | Automated execution script (`run_tests.py`). |
| **Test Artifacts** | Time-stamped HTML Execution Reports generated in `./reports/`. |
| **Exit Criteria** | Zero unhandled crashes, HTTP Error Rate < 1.0%, P95 Latency < 2000ms. |

---

## 3. Load Test Profiles & Execution Criteria

1. **Nominal Load Test:**
   * **Virtual Users (VUs):** 50
   * **Spawn Rate:** 5 VUs/sec
   * **Duration:** 2 minutes
   * **Objective:** Establish baseline metrics under normal expected traffic.

2. **Stress Test:**
   * **Virtual Users (VUs):** 500
   * **Spawn Rate:** 25 VUs/sec
   * **Duration:** 3 minutes
   * **Objective:** Identify performance degradation thresholds beyond normal operational limits.

3. **Spike Test:**
   * **Virtual Users (VUs):** 5,000
   * **Spawn Rate:** 100 VUs/sec
   * **Duration:** 1 minute
   * **Objective:** Measure resilience and post-surge system recovery during sudden traffic spikes.

4. **Endurance / Soak Test:**
   * **Virtual Users (VUs):** 500
   * **Spawn Rate:** 20 VUs/sec
   * **Duration:** 10+ minutes
   * **Objective:** Detect memory leaks and resource degradation over an extended period.

---

## 4. Entry and Exit Criteria

### 4.1 Entry Criteria
* Source code committed and operational on `localhost`.
* All dependencies specified in `requirements.txt` installed in virtual environment.
* Target endpoints accessible and returning HTTP 200 under single-user access.

### 4.2 Exit Criteria
* 100% of planned test profiles executed via `run_tests.py`.
* Overall HTTP request error rate remains below 1.0%.
* 95th Percentile (P95) response time stays strictly under 2,000ms.
* Execution summary reports successfully stored in `./reports/`.
