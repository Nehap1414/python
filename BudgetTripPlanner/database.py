import sqlite3

DATABASE_NAME = "budget_trip_planner.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination TEXT NOT NULL,
            total_budget REAL NOT NULL,
            travelers INTEGER NOT NULL,
            nights INTEGER NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            hotel_budget_per_night REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_trip(
    destination,
    total_budget,
    travelers,
    nights,
    check_in,
    check_out,
    hotel_budget_per_night
):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO trips (
            destination,
            total_budget,
            travelers,
            nights,
            check_in,
            check_out,
            hotel_budget_per_night
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        destination,
        total_budget,
        travelers,
        nights,
        check_in,
        check_out,
        hotel_budget_per_night
    ))

    conn.commit()
    conn.close()


def get_saved_trips():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            destination,
            total_budget,
            travelers,
            nights,
            check_in,
            check_out,
            hotel_budget_per_night
        FROM trips
        ORDER BY id DESC
    """)

    trips = cursor.fetchall()

    conn.close()

    return trips



if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
    
def delete_trip(trip_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM trips WHERE id = ?",
        (trip_id,)
    )

    conn.commit()
    conn.close()    

# ---------------- USER LOGIN / REGISTRATION ----------------

def create_users_table():
    """Create the users table used by TripWise authentication."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def create_user(name, email, password_hash):
    """Save a new user. Returns False if the email already exists."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
        """, (name, email.strip().lower(), password_hash))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_user_by_email(email):
    """Find a registered user by email address."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, password_hash
        FROM users
        WHERE email = ? COLLATE NOCASE
    """, (email.strip().lower(),))

    user = cursor.fetchone()
    conn.close()

    return user
