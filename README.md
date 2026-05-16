# Car Rental Management System

A Python-based CLI (Command Line Interface) application engineered to streamline car rental operations. This system manages vehicle inventories, user authentication, and booking logs through structured JSON file storage, ensuring data persistence between sessions.

Developed as a first-year academic project at **El Sewedy University of Technology (SUT)**.

---

## 🚀 Features

The system features a dual-role access control system dividing functionalities between Administrators and Registered Customers:

### 🛠️ Admin Dashboard
* **Add New Vehicles:** Populate the inventory with details like model, registration number, pricing, and available days.
* **Update Vehicle Records:** Dynamically modify existing car details in the data sheets.
* **View Records:** Access the complete fleet list or filter vehicles available on specific reservation dates.
* **Track Transactions:** Review global booking histories or audit logs for specific users.
* **Cancel Bookings:** Revoke active rentals and automatically restore the vehicle to the available pool.

### 👥 Customer Portal
* **Secure Registration & Login:** Simple authentication using personalized user data.
* **Browse Inventory:** Look up all available vehicles or search for options matching target dates.
* **Book Vehicles:** Calculate total costs instantly and checkout cars from the available list.
* **Personal History:** Review individual active and past rental invoices.
* **Self-Service Cancellation:** Release rented vehicles back into the main inventory seamlessly.

---

## 📊 System Architecture & Flow

The operational business logic follows a precise pipeline verified via structured behavioral mapping:

* **Authentication Layer:** Routes users to targeted workspaces depending on security flags (`is_admin`).
* **Data Layer:** Maintains real-time synchronization between memory lists and physical `.json` databases to prevent state loss.
* **Inventory Control:** Implements atomic delete-on-booking operations to eliminate double-booking conflicts.

*For a detailed block-by-block breakdown of the application logic, check out the provided flowchart files included in the repository:*
* `car rental managment.drawio`
* `car rental managment.drawio.pdf`

---

## 🗃️ Data Schema

The application structures information using core database components:

### 1. Vehicle Fleet Database (`car_data.json`)
```json
[
   {
      "car_model": "Toyota",
      "reg_number": "ABC123",
      "price_per_day": 50.0,
      "car_days": 3,
      "reservation_date": "2025-04-20"
   }
]
