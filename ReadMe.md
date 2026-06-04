---

## 📢 Library Announcements REST API (Feature Branch)

This feature branch adds an operational notification engine allowing staff to broadcast system alerts, branch hours, and library events directly via RESTful API endpoints.

### API Architecture Reference

| HTTP Method | API Path | Objective | Expected Status |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/announcements` | Retrieve all active notification cards | `200 OK` |
| **POST** | `/api/announcements` | Publish a new library notification | `201 Created` / `400 Bad Request` |
| **GET** | `/api/announcements/<id>` | Fetch specific record data by lookup ID | `200 OK` / `404 Not Found` |

### Sample Payload Schema (POST `/api/announcements`)
```json
{
  "title": "Holiday System Down-Time",
  "content": "Digital inventory checks will be offline this Sunday between 02:00 and 05:00 AM."
}