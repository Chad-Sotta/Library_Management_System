# 📚 Library Management System (Enhanced API Edition)

A modern, responsive Library Management System built with Python and Flask. This repository features an isolated core architecture for handling catalog searches, coupled with a newly engineered **RESTful Announcements Engine** validated by an automated, environment-independent testing suite.

---

## 📢 Feature Enhancement: Library Announcements API

To scale the platform from a static inventory management tool into an active communication hub, we implemented a decoupled **Announcements Micro-Engine** inside the application routing framework (`application/routes.py`). 

This API provides communication endpoints that output structured **JSON**, allowing library administrators to instantly broadcast system alerts, emergency facility closures, or reading events simultaneously across web frontends, mobile layouts, and physical information kiosks.

### ⚙️ Architectural Engineering Choices

* **In-Memory Cache Layer (`announcements_db`):** The engine operates within isolated runtime memory allocations rather than mutating standard production database tables. This completely eliminates the risk of SQL schema corruption during deployment.
* **Input Validation Guardrails:** The ingestion pipeline performs real-time structural audits on incoming data, actively preventing malformed requests from consuming system memory.
* **Dynamic Record Retrieval:** Implements an accelerated loop generation protocol to find explicit records by an integer ID pointer, gracefully falling back on standardized handling routines for missing records.

---

## 🛠️ API Architecture Reference

The API supports standardized REST protocols for data retrieval and resource generation:

| HTTP Method | API Path | Objective / Target | Expected Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/announcements` | Retrieve all active notification cards | `200 OK` |
| **POST** | `/api/announcements` | Publish a new library notice | `201 Created` / `400 Bad Request` |
| **GET** | `/api/announcements/<id>` | Fetch specific alert profile data via lookup ID | `200 OK` / `404 Not Found` |

### Expected Payload Schema (POST `/api/announcements`)
```json
{
  "title": "West Wing Renovation Notice",
  "content": "The quiet study rooms in the West Wing will be closed for maintenance this Friday."
}
