import sqlite3
import re
from datetime import datetime

class BookingSystem:
    """
    A class that represents a booking system.

    This class allows you to manage customer bookings for various services.

    Attributes:
        db_file (str): The path to the SQLite database file.

    Methods:
        create_table(): Create the 'bookings' table if it doesn't exist.
        make_booking(customer_name, date, service): Make a booking.
        view_bookings(): View all bookings in the system.
        remove_booking(booking_id): Remove a booking by ID.
        close_connection(): Close the database connection.
    """
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        # Create table of 4 values, id num, customer name, date, and what the service is
        query = """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                date TEXT,
                service TEXT
            )
        """
        self.connect.execute(query)
        self.connect.commit()

    def validate_name(self, name):
        return bool(re.match("^[a-zA-Z]+$", name))

    def validate_date(self, date):
        return bool(re.match(r"\d{6}$", date))

    def make_booking(self, customer_name, date, service):
        if not self.validate_name(customer_name):
            print("\n------------Invalid customer name. Please use letters only------------\n")
            return
        if not self.validate_date(date):
            print("\n------------Invalid date format. Please use YYMMDD format------------\n")
            return

        # Add slashes to the date before inserting it into the database
        formatted_date = f"{date[:2]}/{date[2:4]}/{date[4:]}"
        query = "INSERT INTO bookings (customer_name, date, service) VALUES (?, ?, ?)"
        self.connect.execute(query, (customer_name, formatted_date, service))
        self.connect.commit()
        print("\n------------Booking successful!------------\n")

    def view_bookings(self):
        # View booking by id, name, date and service
        query = "SELECT id, customer_name, date, service FROM bookings"
        cursor = self.connect.execute(query)
        
        row = cursor.fetchone()

        # If nothing in row, then no bookings
        if row is None:
            print("\n------------No bookings found------------\n")
        else:
            # Go through each row
            while row:
                print("---------------------------------")
                print("\nID:", row[0])
                print("Customer:", row[1])

                # Convert date string to a datetime object and format date as "Month Day, Year"
                date_object = datetime.strptime(row[2], "%y/%m/%d")
                formatted_date = date_object.strftime("%B %d, %Y")  

                print("Date:", formatted_date)
                print("Service:", row[3])
                print("---------------------------------\n")
                
                row = cursor.fetchone() 

        cursor.close()
            
    def remove_booking(self, booking_id):
        # Remove booking at certain ID
        query = "DELETE FROM bookings WHERE id = ?"
        cursor = self.connect.cursor()
        cursor.execute(query, (booking_id,))
        
        if cursor.rowcount == 0:
            print("\n------------Booking not found. No changes made------------\n")
        else:
            self.connect.commit()
            print("\n------------Booking removed successfully!------------\n")
        cursor.close()    
        
    def close_connection(self):
        # Close the connection
        self.connect.close()
        print("\n------------Database connection closed------------\n")
        
def main(db_file):
    booking_system = BookingSystem(db_file)

    try:
        while True:
            print("1. Make a Booking")
            print("2. View Bookings")
            print("3. Remove a Booking")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                customer_name = input("\nEnter customer name: ").capitalize()
                if not booking_system.validate_name(customer_name):
                    print("\n------------Invalid customer name. Please use letters only------------\n")
                    continue

                date = input("\nEnter booking date (YYMMDD): ")
                if not booking_system.validate_date(date):
                    print("\n------------Invalid date format. Please use YYMMDD format------------\n")
                    continue

                service = input("\nEnter service: ").capitalize()
                booking_system.make_booking(customer_name, date, service)
                
            elif choice == "2":
                booking_system.view_bookings()
            elif choice == "3":
                booking_id = int(input("Enter booking ID to remove: "))
                booking_system.remove_booking(booking_id)
            elif choice == "4":
                break
            else:
                print("\n------------Invalid choice. Please try again------------\n")
   
    except Exception as e:
        print(f"\n**********An error occurred: {str(e)}**********\n")
    finally:
        booking_system.close_connection()

if __name__ == "__main__":
    db_file = "data/bookings.db"
    main(db_file)
