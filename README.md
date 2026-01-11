# FlashTicket API

## 🚀 Key Engineering Features

This project demonstrates a high-concurrency ticketing system designed to handle race conditions and high traffic loads.

* **Concurrency Control:** Implemented **Pessimistic Locking** (`SELECT ... FOR UPDATE`) to guarantee data integrity. This prevents "overselling" tickets even when thousands of users attempt to book the same seat at the exact same millisecond.
* **Database Optimization:** Added **indexes** on foreign keys (`event_id`, `user_id`) for efficient query performance at scale.
* **Scalable Architecture:** Fully containerized with **Docker**, using **PostgreSQL** for persistence and **Redis** for high-speed caching (provisioned for future implementation).
* **Automated Load Testing:** Includes a custom **K6** stress-test suite that simulates **1,000 concurrent users** making **10,000 booking attempts** to verify system stability and validate the locking mechanism.
* **RESTful API:** Developed with **FastAPI** and **Uvicorn** for high-performance, asynchronous request handling.
* **Robust Error Handling:** Designed graceful handling of foreign key constraints and "sold out" scenarios, ensuring the API never crashes under bad input.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.9 |
| **Framework** | FastAPI (ASGI) + Uvicorn |
| **Database** | PostgreSQL (SQLAlchemy ORM) |
| **Cache** | Redis |
| **Testing** | K6 (Load Testing) |
| **Infrastructure** | Docker & Docker Compose |

---

## ⚡ How to Run

I have included a one-click shell script that automates the entire lifecycle: cleaning the environment, building containers, seeding the database, and running the load tests.

### Prerequisites
* **Docker & Docker Compose** installed and running.
* **WSL** (Windows Subsystem for Linux) if on Windows, or **Terminal** (Linux/Mac).

### Steps

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/flashticket.git

# Navigate to project folder
cd flashticket

# Make script executable (first time only)
chmod +x run_tests.sh

# Run the test
./run_tests.sh
```

> **Windows Users:** Run the script from WSL, not PowerShell. Navigate to the project using `/mnt/c/path/to/project`.

### 🔍 What the Script Does
When you execute `./run_tests.sh`, it performs the following automated workflow:

1.  **Cleanup:** Stops containers and nukes any existing database volumes to ensure a clean test state.
2.  **Build:** Builds & starts the API, Database, and Redis containers.
3.  **Seed:** Populates the database with:
    * 1 Venue (Capacity: **1,000**)
    * 1 Event
    * **10,000** Pre-registered Users
4.  **Load Test:** Launches **K6**, simulating **1,000 concurrent users** making **10,000 booking attempts** (max duration: 5 minutes).
5.  **Verify:** Checks database integrity by counting the final bookings (Result must be exactly **1,000** - matching venue capacity).
