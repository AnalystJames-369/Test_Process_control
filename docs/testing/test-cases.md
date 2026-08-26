
# 🧪 Test Cases & Verification Matrix (ISTQB CTFL v4.0 Aligned)

**Project:** Test_Process_Control  
**Target System:** RESTful Web API (`localhost` / Cloud Host)  
**Standards:** ISTQB® Certified Tester Foundation Level (CTFL) v4.0  

---

## 1. Test Case TC-001: Authentication Pre-condition & Session Initialization (Happy Path)
* **Objective:** Verify that virtual users successfully execute authentication (`/api/login`) prior to starting workload tasks.
* **Pre-conditions:** Target API online, test database initialized with test credentials.
* **Test Steps:**
  1. Initialize Locust execution profile.
  2. Trigger `on_start()` lifecycle hook for spawned Virtual Users (VUs).
  3. Execute `POST /api/login` with payload credentials.
* **Expected Result:** API returns HTTP status `200 OK` and issues a valid session/token, allowing the user to proceed to main tasks.
* **Pass/Fail Status:** Pass

---

## 2. Test Case TC-002: Nominal Load SLA Compliance (Performance Efficiency)
* **Objective:** Validate that the high-demand user directory endpoint (`/api/usuarios`) responds within the defined SLA under nominal load (50 VUs).
* **Pre-conditions:** Nominal load profile active (50 VUs, spawn rate 5 VUs/sec).
* **Test Steps:**
  1. Execute `GET /api/usuarios` weighted at 50% traffic distribution (`@task(5)`).
  2. Monitor response times and HTTP status codes via Locust engine.
* **Expected Result:** HTTP status is `200 OK` and 95th Percentile (P95) response time stays strictly below 2,000ms (2.0s). Requests exceeding the threshold are marked as failures (`catch_response=True`).
* **Pass/Fail Status:** Pass

---

## 3. Test Case TC-003: Stress Testing and Degradation Thresholds (Negative / Boundary Path)
* **Objective:** Identify system failure thresholds, error spikes, and response time degradation under heavy stress conditions (500 VUs).
* **Pre-conditions:** Stress test profile active (500 VUs, spawn rate 25 VUs/sec).
* **Test Steps:**
  1. Ramp up concurrency to 500 VUs over a 3-minute window.
  2. Track error rates, server exceptions (HTTP 5xx), and timeout boundaries.
* **Expected Result:** System maintains stability with overall error rate below 1.0%; any service bottlenecks are explicitly captured in execution logs.
* **Pass/Fail Status:** Pass
