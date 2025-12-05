# FlashTicket API

## 🚀 Key Engineering Features

This project demonstrates a high-concurrency ticketing system designed to handle race conditions and high traffic loads.

* **Concurrency Control:** Implemented **Pessimistic Locking** (`SELECT ... FOR UPDATE`) to guarantee data integrity. This prevents "overselling" tickets even when thousands of users attempt to book the same seat at the exact same millisecond.
* **Scalable Architecture:** Fully containerized with **Docker**, using **PostgreSQL** for persistence and **Redis** for high-speed caching (provisioned for future implementation).
* **Automated Load Testing:** Includes a custom **K6** stress-test suite that simulates 1,000 concurrent users to verify system stability and validate the locking mechanism.
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

## ⚡ How to Run (The Easy Way)

I have included a one-click shell script that automates the entire lifecycle: cleaning the environment, building containers, seeding the database, and running the load tests.

### Prerequisites
* **Docker & Docker Compose** installed.
* **Git Bash** (if on Windows) or **Terminal** (Linux/Mac).

### Steps

git clone https://github.com/YOUR_USERNAME/flashticket.git

cd flashticket

chmod +x run_tests.sh

./run_tests.sh

### 🔍 What the script does
When you execute `./run_tests.sh`, it performs the following automated workflow:

1.  **Cleanup:** Nukes any existing database volumes to ensure a perfectly clean test state.
2.  **Build:** Builds & Starts the API, Database, and Redis containers.
3.  **Seed:** Populates the database with:
    * 1 Venue (Capacity: 50)
    * 1 Event
    * 1,000 Pre-registered Users
4.  **Attack:** Launches **K6**, simulating 100 users trying to buy tickets simultaneously 10 times.
5.  **Verify:** Checks database integrity by counting the final bookings (Result must be exactly **50**).
