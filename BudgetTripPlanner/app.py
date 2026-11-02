
from flask import (
    Flask, render_template, request,
    redirect, url_for, flash, session
)
from datetime import datetime, timedelta
import os
import re
from functools import wraps

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from hotel_api import search_hotels

from database import (
    create_database,
    save_trip,
    get_saved_trips,
    delete_trip,
    create_users_table,
    create_user,
    get_user_by_email
)


app = Flask(__name__)

app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "tripwise-development-key-change-before-deployment"
)


# --------------------------------------------------
# LOGIN PROTECTION
# --------------------------------------------------

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))

        return function(*args, **kwargs)

    return wrapper


# --------------------------------------------------
# VALIDATION PATTERNS
# --------------------------------------------------

EMAIL_PATTERN = re.compile(
    r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
)

# Only English letters and spaces are allowed.
NAME_PATTERN = re.compile(
    r"^[A-Za-z]+(?: [A-Za-z]+)*$"
)

PASSWORD_UPPER = re.compile(r"[A-Z]")
PASSWORD_LOWER = re.compile(r"[a-z]")
PASSWORD_NUMBER = re.compile(r"[0-9]")
PASSWORD_SPECIAL = re.compile(r"[^A-Za-z0-9]")


# --------------------------------------------------
# DESTINATION COSTS
# --------------------------------------------------

DESTINATIONS = {
    "goa": {
        "transport": 2000,
        "food": 600,
        "sightseeing": 1000,
        "other": 500
    },

    "mumbai": {
        "transport": 1500,
        "food": 700,
        "sightseeing": 1000,
        "other": 500
    },

    "pune": {
        "transport": 800,
        "food": 500,
        "sightseeing": 700,
        "other": 400
    },

    "jaipur": {
        "transport": 2500,
        "food": 600,
        "sightseeing": 1000,
        "other": 500
    },

    "delhi": {
        "transport": 2000,
        "food": 700,
        "sightseeing": 1000,
        "other": 500
    },

    "hyderabad": {
        "transport": 1800,
        "food": 600,
        "sightseeing": 800,
        "other": 500
    }
}


DESTINATION_NAMES = [
    "Goa",
    "Mumbai",
    "Pune",
    "Jaipur",
    "Delhi",
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Kolkata",
    "Nashik"
]


DEFAULT_DESTINATION_COSTS = {
    "transport": 1800,
    "food": 600,
    "sightseeing": 900,
    "other": 500
}


def get_destination_costs(destination):
    """Return known city estimates or default estimates."""

    city_key = (
        destination.strip()
        .split(",")[0]
        .strip()
        .casefold()
    )

    return DESTINATIONS.get(
        city_key,
        DEFAULT_DESTINATION_COSTS
    )


# --------------------------------------------------
# DATABASE INITIALIZATION
# --------------------------------------------------

try:
    create_database()
    create_users_table()

except Exception as exc:
    print("Database initialization warning:", exc)


# --------------------------------------------------
# TEMPLATE FILTER
# --------------------------------------------------

@app.template_filter("inr")
def inr(value):
    """Format numbers as Indian rupees."""

    try:
        return f"₹{float(value):,.0f}"

    except (TypeError, ValueError):
        return "—"


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def get_trips():
    """Safely retrieve saved trips."""

    try:
        return get_saved_trips() or []

    except Exception as exc:
        print("Could not retrieve saved trips:", exc)
        return []


def clean_destination(value):
    """Validate destination from the approved city list."""

    destination = (value or "").strip()

    if destination not in DESTINATION_NAMES:
        raise ValueError(
            "Please select a valid destination from the list."
        )

    return destination


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Name validation
        if not name:
            flash("Please enter your full name.", "error")
            return redirect(url_for("login"))

        if len(name) < 2 or len(name) > 80:
            flash(
                "Name must contain between 2 and 80 characters.",
                "error"
            )
            return redirect(url_for("login"))

        if not NAME_PATTERN.fullmatch(name):
            flash(
                "Name can contain only English letters and spaces. "
                "Numbers and special characters are not allowed.",
                "error"
            )
            return redirect(url_for("login"))

        # Email validation
        if not EMAIL_PATTERN.fullmatch(email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("login"))

        # Password validation
        if len(password) < 8:
            flash(
                "Password must contain at least 8 characters.",
                "error"
            )
            return redirect(url_for("login"))

        if not PASSWORD_UPPER.search(password):
            flash(
                "Password must contain at least one uppercase letter.",
                "error"
            )
            return redirect(url_for("login"))

        if not PASSWORD_LOWER.search(password):
            flash(
                "Password must contain at least one lowercase letter.",
                "error"
            )
            return redirect(url_for("login"))

        if not PASSWORD_NUMBER.search(password):
            flash(
                "Password must contain at least one number.",
                "error"
            )
            return redirect(url_for("login"))

        if not PASSWORD_SPECIAL.search(password):
            flash(
                "Password must contain at least one special symbol.",
                "error"
            )
            return redirect(url_for("login"))

        # Hash password before saving
        password_hash = generate_password_hash(password)

        try:
            created = create_user(
                name,
                email,
                password_hash
            )

            if not created:
                flash(
                    "An account with this email already exists.",
                    "error"
                )
                return redirect(url_for("login"))

            flash(
                "Account created successfully! Please log in.",
                "success"
            )

            return redirect(url_for("login"))

        except Exception as exc:
            app.logger.exception("Registration failed: %s", exc)

            flash(
                "Could not create your account. Please try again.",
                "error"
            )

            return redirect(url_for("login"))

    return render_template("login.html")


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash(
                "Please enter your email and password.",
                "error"
            )
            return redirect(url_for("login"))

        try:
            user = get_user_by_email(email)

            if user and check_password_hash(user[3], password):

                session.clear()

                session["user_id"] = user[0]
                session["user_name"] = user[1]
                session["user_email"] = user[2]

                flash(
                    f"Welcome back, {user[1]}!",
                    "success"
                )

                return redirect(url_for("home"))

            flash(
                "Invalid email or password.",
                "error"
            )

        except Exception as exc:
            app.logger.exception("Login failed: %s", exc)

            flash(
                "Could not log in. Please try again.",
                "error"
            )

        return redirect(url_for("login"))

    if "user_id" in session:
        return redirect(url_for("home"))

    return render_template("login.html")


# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "You have been logged out successfully.",
        "success"
    )

    return redirect(url_for("login"))


# --------------------------------------------------
# HOME DASHBOARD
# --------------------------------------------------

@app.route("/")
@login_required
def home():

    trips = get_trips()

    try:
        total_budget = sum(
            float(trip[2]) for trip in trips
        )

        total_travelers = sum(
            int(trip[3]) for trip in trips
        )

    except (IndexError, TypeError, ValueError):
        total_budget = 0
        total_travelers = 0

    return render_template(
        "index.html",
        page="home",
        trips=trips,
        total_trips=len(trips),
        total_budget=total_budget,
        travelers=total_travelers,
        average=(
            total_budget / len(trips)
            if trips else 0
        ),
        destinations=DESTINATION_NAMES
    )


# --------------------------------------------------
# PLAN TRIP
# --------------------------------------------------

@app.route("/plan", methods=["GET", "POST"])
@login_required
def plan_trip():

    if request.method == "POST":

        try:
            destination = clean_destination(
                request.form.get("destination", "")
            )

            budget = float(
                request.form.get("budget", "0")
            )

            travelers = int(
                request.form.get("travelers", "0")
            )

            nights = int(
                request.form.get("nights", "0")
            )

            checkin_text = request.form.get(
                "checkin", ""
            )

            checkin = datetime.strptime(
                checkin_text,
                "%Y-%m-%d"
            )

            if budget <= 0 or travelers < 1 or nights < 1:
                raise ValueError(
                    "Enter valid trip details."
                )

            if travelers > 20 or nights > 30:
                raise ValueError(
                    "The maximum is 20 travelers and 30 nights."
                )

            if checkin.date() < datetime.now().date():
                raise ValueError(
                    "Check-in cannot be in the past."
                )

        except ValueError as exc:

            flash(
                str(exc) or
                "Enter valid destination, dates, budget and travelers.",
                "error"
            )

            return redirect(url_for("plan_trip"))

        checkout = checkin + timedelta(days=nights)

        costs = get_destination_costs(destination)

        transport = costs["transport"] * travelers
        food = costs["food"] * travelers * nights
        sightseeing = costs["sightseeing"] * travelers
        other = costs["other"]

        non_hotel = (
            transport +
            food +
            sightseeing +
            other
        )

        hotel_budget = budget - non_hotel

        if hotel_budget <= 0:

            flash(
                "Your budget does not cover the estimated "
                "non-hotel expenses. Increase your budget or "
                "reduce the number of travelers or nights.",
                "error"
            )

            return redirect(url_for("plan_trip"))

        estimated_total = non_hotel + hotel_budget
        remaining = budget - estimated_total

        breakdown = [
            {"label": "Transport", "amount": transport},
            {"label": "Food", "amount": food},
            {"label": "Sightseeing", "amount": sightseeing},
            {"label": "Other expenses", "amount": other},
            {"label": "Hotel allowance", "amount": hotel_budget}
        ]

        result = {
            "destination": destination,
            "budget": budget,
            "travelers": travelers,
            "nights": nights,
            "checkin": checkin.strftime("%Y-%m-%d"),
            "checkout": checkout.strftime("%Y-%m-%d"),
            "transport": transport,
            "food": food,
            "sightseeing": sightseeing,
            "other": other,
            "non_hotel": non_hotel,
            "hotel_budget": hotel_budget,
            "hotel_per_night": hotel_budget / nights,
            "per_person": budget / travelers
        }

        return render_template(
            "summary.html",
            page="plan",
            result=result,
            destination=destination,
            budget=budget,
            travelers=travelers,
            nights=nights,
            checkin=checkin.strftime("%Y-%m-%d"),
            checkout=checkout.strftime("%Y-%m-%d"),
            hotel_budget=hotel_budget,
            breakdown=breakdown,
            estimated_total=estimated_total,
            remaining=remaining
        )

    return render_template(
        "plan.html",
        page="plan",
        destinations=DESTINATION_NAMES,
        today=datetime.now().strftime("%Y-%m-%d")
    )


# --------------------------------------------------
# SAVE TRIP
# --------------------------------------------------

@app.route("/save-trip", methods=["POST"])
@login_required
def save_trip_route():

    try:
        destination = clean_destination(
            request.form.get("destination", "")
        )

        budget = float(request.form["budget"])
        travelers = int(request.form["travelers"])
        nights = int(request.form["nights"])

        checkin = datetime.strptime(
            request.form["checkin"],
            "%Y-%m-%d"
        )

        checkout = datetime.strptime(
            request.form["checkout"],
            "%Y-%m-%d"
        )

        hotel_per_night = float(
            request.form["hotel_per_night"]
        )

        if (
            budget <= 0
            or travelers < 1
            or travelers > 20
            or nights < 1
            or nights > 30
            or hotel_per_night < 0
            or checkout <= checkin
            or (checkout - checkin).days != nights
            or checkin.date() < datetime.now().date()
        ):
            raise ValueError("Invalid trip details.")

        save_trip(
            destination,
            budget,
            travelers,
            nights,
            checkin.strftime("%Y-%m-%d"),
            checkout.strftime("%Y-%m-%d"),
            hotel_per_night
        )

        flash(
            "Trip saved successfully.",
            "success"
        )

    except Exception as exc:

        flash(
            f"Could not save trip: {exc}",
            "error"
        )

    return redirect(url_for("saved_trips"))


# --------------------------------------------------
# HOTEL SEARCH
# --------------------------------------------------

@app.route("/hotels", methods=["GET", "POST"])
@login_required
def find_hotels():

    today = datetime.now().date()

    default_checkin = today + timedelta(days=1)
    default_checkout = today + timedelta(days=3)

    form = {
        "destination": request.values.get(
            "destination", "Goa"
        ).strip(),

        "travelers": request.values.get(
            "travelers",
            request.values.get("guests", "2")
        ),

        "checkin": request.values.get(
            "checkin",
            default_checkin.strftime("%Y-%m-%d")
        ),

        "checkout": request.values.get(
            "checkout",
            default_checkout.strftime("%Y-%m-%d")
        ),

        "budget": request.values.get(
            "budget", "5000"
        )
    }

    results = []

    search_fields = {
        "destination",
        "checkin",
        "checkout",
        "guests",
        "travelers",
        "budget"
    }

    searched = (
        request.method == "POST"
        or any(
            key in request.args
            for key in search_fields
        )
    )

    if searched:

        try:
            destination = clean_destination(
                form["destination"]
            )

            guests = int(form["travelers"])
            budget = float(form["budget"])

            start = datetime.strptime(
                form["checkin"],
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                form["checkout"],
                "%Y-%m-%d"
            )

            if guests < 1 or guests > 20:
                raise ValueError(
                    "Guests must be between 1 and 20."
                )

            if budget <= 0:
                raise ValueError(
                    "Enter a budget greater than zero."
                )

            if end <= start:
                raise ValueError(
                    "Check-out must be after check-in."
                )

            if start.date() < today:
                raise ValueError(
                    "Check-in cannot be in the past."
                )

            found = search_hotels(
                destination,
                form["checkin"],
                form["checkout"],
                guests
            ) or []

            for hotel in found:

                if not isinstance(hotel, dict):
                    continue

                if hotel.get("is_demo") is not True:
                    continue

                if hotel.get("currency", "INR") != "INR":
                    continue

                try:
                    price = float(hotel["price"])

                except (KeyError, TypeError, ValueError):
                    continue

                if price < 0 or price > budget:
                    continue

                results.append(hotel)

            results.sort(
                key=lambda hotel: float(hotel["price"])
            )

            if not results:
                flash(
                    "No sample listings matched this destination "
                    "and budget. Try another budget or destination. "
                    "Listings are illustrative, not live availability.",
                    "warning"
                )

        except ValueError as exc:

            flash(
                str(exc) or
                "Enter valid destination, guests, budget and dates.",
                "error"
            )

        except Exception as exc:

            app.logger.exception(
                "Demo hotel search failed: %s",
                exc
            )

            flash(
                "Could not load sample hotel listings. "
                "Check hotel_api.py and try again.",
                "error"
            )

    return render_template(
        "hotels.html",
        page="hotels",
        destinations=DESTINATION_NAMES,
        form=form,
        destination=form["destination"],
        travelers=form["travelers"],
        guests=form["travelers"],
        checkin=form["checkin"],
        checkout=form["checkout"],
        budget=form["budget"],
        hotels=results,
        searched=searched,
        demo_mode=True,
        today=today.strftime("%Y-%m-%d")
    )


# --------------------------------------------------
# SAVED TRIPS
# --------------------------------------------------

@app.route("/trips")
@login_required
def saved_trips():

    return render_template(
        "trips.html",
        page="trips",
        trips=get_trips()
    )


# --------------------------------------------------
# DELETE TRIP
# --------------------------------------------------

@app.route("/delete-trip/<int:trip_id>", methods=["POST"])
@login_required
def delete_trip_route(trip_id):

    try:
        delete_trip(trip_id)

        flash(
            "Trip deleted successfully.",
            "success"
        )

    except Exception as exc:

        flash(
            f"Could not delete trip: {exc}",
            "error"
        )

    return redirect(url_for("saved_trips"))


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

@app.route("/settings")
@login_required
def settings():

    return render_template(
        "settings.html",
        page="settings",
        destinations=DESTINATION_NAMES
    )


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
