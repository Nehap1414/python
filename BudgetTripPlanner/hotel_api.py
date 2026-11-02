
from datetime import date


DEMO_HOTELS = {
    "goa": [
        {"name": "Coastal Breeze Stay", "location": "North Goa", "price": 2200, "rating": 4.2, "reviews": 185},
        {"name": "Palm Garden Retreat", "location": "Candolim, Goa", "price": 3200, "rating": 4.5, "reviews": 240},
        {"name": "Sunset Bay Rooms", "location": "Calangute, Goa", "price": 1800, "rating": 4.0, "reviews": 126},
        {"name": "Seaside Comfort Inn", "location": "South Goa", "price": 2800, "rating": 4.3, "reviews": 164},
        {"name": "Green Escape Homestay", "location": "Anjuna, Goa", "price": 1500, "rating": 3.9, "reviews": 98},
    ],

    "mumbai": [
        {"name": "Harbour View Stay", "location": "Colaba, Mumbai", "price": 3500, "rating": 4.2, "reviews": 210},
        {"name": "City Comfort Rooms", "location": "Andheri, Mumbai", "price": 2200, "rating": 4.0, "reviews": 145},
        {"name": "Urban Nest Hotel", "location": "Bandra, Mumbai", "price": 4200, "rating": 4.5, "reviews": 275},
        {"name": "Metro Budget Inn", "location": "Dadar, Mumbai", "price": 1800, "rating": 3.9, "reviews": 112},
        {"name": "Palm Square Stay", "location": "Powai, Mumbai", "price": 3000, "rating": 4.3, "reviews": 176},
    ],

    "pune": [
        {"name": "Deccan Comfort Stay", "location": "Deccan, Pune", "price": 1800, "rating": 4.1, "reviews": 130},
        {"name": "Green Park Rooms", "location": "Baner, Pune", "price": 2400, "rating": 4.3, "reviews": 170},
        {"name": "Urban Leaf Inn", "location": "Hinjawadi, Pune", "price": 2000, "rating": 4.0, "reviews": 115},
        {"name": "Heritage Corner Stay", "location": "Shivajinagar, Pune", "price": 2800, "rating": 4.4, "reviews": 205},
        {"name": "Budget Nest Pune", "location": "Wakad, Pune", "price": 1500, "rating": 3.9, "reviews": 90},
    ],

    "jaipur": [
        {"name": "Pink City Comfort", "location": "Jaipur City", "price": 2000, "rating": 4.2, "reviews": 160},
        {"name": "Royal Courtyard Stay", "location": "Civil Lines, Jaipur", "price": 3200, "rating": 4.6, "reviews": 230},
        {"name": "Amber View Rooms", "location": "Amer, Jaipur", "price": 1800, "rating": 4.0, "reviews": 120},
        {"name": "Heritage Lane Inn", "location": "Bani Park, Jaipur", "price": 2600, "rating": 4.4, "reviews": 190},
        {"name": "Desert Rose Stay", "location": "Vaishali Nagar, Jaipur", "price": 1500, "rating": 3.9, "reviews": 85},
    ],

    "delhi": [
        {"name": "Capital Comfort Stay", "location": "Karol Bagh, Delhi", "price": 2200, "rating": 4.1, "reviews": 155},
        {"name": "Central Square Rooms", "location": "Connaught Place, Delhi", "price": 3800, "rating": 4.4, "reviews": 245},
        {"name": "Green Metro Inn", "location": "Dwarka, Delhi", "price": 1800, "rating": 4.0, "reviews": 118},
        {"name": "City Lights Stay", "location": "South Delhi", "price": 3000, "rating": 4.3, "reviews": 185},
        {"name": "Budget Corner Rooms", "location": "Paharganj, Delhi", "price": 1400, "rating": 3.8, "reviews": 102},
    ],

    "hyderabad": [
        {"name": "Pearl City Stay", "location": "Hitech City, Hyderabad", "price": 2500, "rating": 4.3, "reviews": 190},
        {"name": "Charminar Comfort Inn", "location": "Old City, Hyderabad", "price": 1600, "rating": 4.0, "reviews": 125},
        {"name": "Lake View Rooms", "location": "Hussain Sagar, Hyderabad", "price": 2800, "rating": 4.4, "reviews": 210},
        {"name": "Tech Park Budget Stay", "location": "Gachibowli, Hyderabad", "price": 2200, "rating": 4.1, "reviews": 145},
        {"name": "Royal Deccan Retreat", "location": "Banjara Hills, Hyderabad", "price": 3600, "rating": 4.6, "reviews": 260},
    ],
}



DEFAULT_DEMO_PRICES = [1400, 1800, 2200, 2800, 3500]


def create_fallback_hotels(destination):
    """
    Generate fictional sample listings for any other destination.
    These are not real or verified accommodations.
    """
    destination_name = destination.strip()

    if not destination_name:
        return []

    sample_hotels = []

    for index, price in enumerate(DEFAULT_DEMO_PRICES, start=1):
        sample_hotels.append({
            "name": f"Sample Stay {index} - {destination_name}",
            "location": f"{destination_name} (sample location)",
            "price": price,
            "rating": round(3.8 + (index * 0.1), 1),
            "reviews": 0,
        })

    return sample_hotels


def search_hotels(destination, check_in, check_out, travelers):
    """
    Return fictional sample accommodation listings for TripWise.

    Supports:
        - Existing destinations with custom demo listings.
        - Any other user-entered destination using fallback samples.

    Prices are illustrative INR estimates per night.
    Listings and ratings are fictional, not live booking data.
    """

    if not isinstance(destination, str) or not destination.strip():
        raise ValueError("Please enter a destination.")

    destination_name = destination.strip()

    
    city_key = destination_name.split(",")[0].strip().casefold()

    if isinstance(travelers, bool) or not isinstance(travelers, int):
        raise ValueError("The number of guests must be a whole number.")

    if not 1 <= travelers <= 20:
        raise ValueError("Guests must be between 1 and 20.")

    try:
        start_date = date.fromisoformat(check_in)
        end_date = date.fromisoformat(check_out)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "Enter valid check-in and check-out dates."
        ) from exc

    if end_date <= start_date:
        raise ValueError("Check-out must be after check-in.")

    
    listings = DEMO_HOTELS.get(city_key)

    if listings is None:
        listings = create_fallback_hotels(destination_name)

    number_of_nights = (end_date - start_date).days
    hotels = []

    for item in listings:
        nightly_price = float(item["price"])

        hotels.append({
            "name": item["name"],
            "location": item["location"],
            "price": nightly_price,
            "currency": "INR",
            "total_price": nightly_price * number_of_nights,
            "rating": item["rating"],
            "reviews": item["reviews"],
            "url": None,
            "platform": "Fictional demo listing",
            "is_demo": True,
        })

    return hotels
