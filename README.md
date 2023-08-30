# Booking System

Welcome to the Booking System! This Python application allows you to manage customer bookings for various services using an SQLite database. This README will explain further details about the project!

## Introduction

This is a Python app I am creating to learn about SQL databases and more. Currently, this is only a CLI (command line interface) operation. Soon I will create a web app among other uses for this project!

## Setup

1. **Clone the Repository:** Start by cloning this repository to your machine using the following command:

   ```git clone https://github.com/fahad-ali1/Booking-System.git```

2. **Install Dependencies:** Navigate to the project folder and install the required dependencies:

    ```pip install sqlite3```

## Usage

1. **Run the Application:** To run the application, run the `booking_main.py` script using the following command:

    ```python booking_main.py```

2. **Menu Options:** The application provides the following menu options:

- **a. Make a Booking:** Enter customer details, booking date (YYMMDD), and service to make a new booking.
- **b. View Bookings:** Display all existing bookings with their details.
- **c. Remove a Booking:** Remove a booking by entering its ID.
- **d. Exit:** Quit the application.

3. **Error Validation:** The system checks for proper input validation for customer names and dates.

4. **Viewing Bookings:** Bookings are displayed with their ID, customer name, formatted dates, and service type.

5. **Removing Bookings:** You can remove a booking by providing its ID (see the view booking section).

6. **Exit:** Choose the "Exit" option to close the application.

## Functionality

The Booking System offers the following functionality:

- **Creation:** Bookings are stored in an SQLite database, providing a reliable and organized way to manage customer data.
- **Viewing:** The system allows you to view all existing bookings and IDs.
- **Deletion:** Bookings can be easily removed using their unique ID.
- **Input Validation:** The system ensures that customer names and dates are entered in the correct format.

---
