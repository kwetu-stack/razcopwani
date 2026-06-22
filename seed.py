from datetime import date, time, timedelta
from random import choice, randint, random, seed as random_seed

from app import create_app
from models import (
    ActionPlan,
    Channel,
    CompetitorActivity,
    Customer,
    LostAccount,
    Opportunity,
    Product,
    Route,
    Swot,
    User,
    Visit,
    db,
)


random_seed(22)

TERRITORIES = [
    "Nyali",
    "Bamburi",
    "Mtwapa",
    "Kilifi",
    "Malindi",
    "Diani",
    "Ukunda",
    "Likoni",
    "Changamwe",
    "Mariakani",
    "Voi",
    "Taveta",
    "Lamu",
]
CHANNELS = ["General Trade", "Modern Trade", "HORECA", "Institutions", "Distributors"]
PRODUCTS = [
    ("Vanilla Ice Cream", "Ice Cream", "Razco", "1L", 650),
    ("Chocolate Ice Cream", "Ice Cream", "Razco", "1L", 670),
    ("Strawberry Ice Cream", "Ice Cream", "Razco", "1L", 660),
    ("Yoghurt 250ml", "Yoghurt", "Razco", "250ml", 90),
    ("Yoghurt 500ml", "Yoghurt", "Razco", "500ml", 160),
    ("Drinking Yoghurt", "Yoghurt", "Razco", "300ml", 120),
    ("Fresh Milk 500ml", "Milk", "Razco", "500ml", 80),
    ("Fresh Milk 1L", "Milk", "Razco", "1L", 150),
    ("UHT Milk 500ml", "Milk", "Razco", "500ml", 95),
    ("UHT Milk 1L", "Milk", "Razco", "1L", 180),
    ("Mayonnaise 250g", "Sauces", "Razco", "250g", 220),
    ("Mayonnaise 500g", "Sauces", "Razco", "500g", 390),
    ("Tomato Sauce", "Sauces", "Razco", "500g", 210),
    ("Chilli Sauce", "Sauces", "Razco", "250g", 180),
    ("Burger Sauce", "Sauces", "Razco", "250g", 240),
    ("Frozen Pastries", "Frozen Foods", "Razco", "12pc", 520),
    ("Croissants", "Bakery", "Razco", "6pc", 360),
    ("Muffins", "Bakery", "Razco", "6pc", 330),
    ("Cake Mix", "Bakery", "Razco", "1kg", 450),
    ("Whipping Cream", "Frozen Foods", "Razco", "1L", 480),
]


def reset_database():
    db.drop_all()
    db.create_all()


def create_users():
    admin = User(username="admin", role="Administrator", full_name="Administrator", must_change_password=True)
    admin.set_password("monozukuri")
    user = User(username="user", role="User", full_name="Read Only User")
    user.set_password("user123")
    db.session.add_all([admin, user])


def create_channels():
    rows = []
    for name in CHANNELS:
        rows.append(
            Channel(
                channel_name=name,
                description=f"{name} Coast Region commercial channel.",
                growth_target=25 + randint(0, 12),
                manager=choice(["Harun", "Amina", "Joseph", "Miriam", "Omar"]),
                status="Active",
                notes=f"Objective: grow {name.lower()} coverage and execution.",
            )
        )
    db.session.add_all(rows)
    db.session.flush()


def create_products():
    rows = []
    for index, (name, category, brand, unit, price) in enumerate(PRODUCTS, start=1):
        rows.append(
            Product(
                product_code=f"PRD-{index:03d}",
                product_name=name,
                category=category,
                brand=brand,
                unit_size=unit,
                selling_price=price,
                status="Active" if index < 19 else choice(["Active", "Discontinued", "Development"]),
                notes=f"{name} portfolio item for Coast Region.",
            )
        )
    db.session.add_all(rows)


def create_customers():
    channel_map = {channel.channel_name: channel for channel in Channel.query.all()}
    named = {
        "Modern Trade": ["Naivas Nyali", "Naivas Bamburi", "Naivas Diani", "Carrefour City Mall", "Carrefour Nyali", "Quickmart Nyali", "Chandarana Nyali"],
        "HORECA": ["PrideInn Paradise", "PrideInn Flamingo", "Whitesands Hotel", "Voyager Beach Resort", "Serena Beach Resort", "Reef Hotel", "Severin Sea Lodge", "English Point Marina"],
        "Institutions": ["KMTC Mombasa", "Technical University of Mombasa", "Aga Khan Academy", "Mombasa Polytechnic"],
        "Distributors": ["Coast Distributor Ltd", "Kilifi Wholesalers", "Malindi Trading Company", "South Coast Distributors"],
    }
    targets = {"General Trade": 50, "Modern Trade": 10, "HORECA": 20, "Institutions": 10, "Distributors": 10}
    rows = []
    counter = 1
    for channel_name, count in targets.items():
        names = list(named.get(channel_name, []))
        while len(names) < count:
            names.append(f"{choice(TERRITORIES)} {channel_name} Customer {len(names) + 1}")
        for name in names[:count]:
            territory = next((t for t in TERRITORIES if t in name), choice(TERRITORIES))
            rows.append(
                Customer(
                    customer_code=f"CUS-{counter:04d}",
                    customer_name=name,
                    contact_person=choice(["Amina Ali", "Joseph Mwangi", "Miriam Said", "Omar Abdalla", "Peter Otieno"]),
                    phone=f"07{randint(10000000, 99999999)}",
                    email=f"customer{counter}@example.com",
                    physical_address=f"{territory} business area",
                    territory=territory,
                    channel_id=channel_map[channel_name].id,
                    customer_status=choice(["Active", "Active", "Active", "Dormant", "Prospect", "Lost"]),
                    credit_limit=randint(50, 900) * 1000,
                    notes=f"{name} managed under {channel_name}.",
                )
            )
            counter += 1
    db.session.add_all(rows)
    db.session.flush()


def create_routes():
    channels = Channel.query.all()
    rows = []
    route_names = [
        "Nyali Route",
        "Bamburi Route",
        "Mtwapa Route",
        "Kilifi Route",
        "Malindi Route",
        "Diani Route",
        "Ukunda Route",
        "Likoni Route",
        "Changamwe Route",
        "Mariakani Route",
        "Voi Route",
        "Taveta Route",
    ]
    for index, name in enumerate(route_names, start=1):
        territory = name.replace(" Route", "")
        rows.append(
            Route(
                route_code=f"RTE-{index:03d}",
                route_name=name,
                territory=territory,
                county="Mombasa" if territory in ["Nyali", "Bamburi", "Likoni", "Changamwe"] else "Kilifi" if territory in ["Mtwapa", "Kilifi", "Malindi"] else "Kwale" if territory in ["Diani", "Ukunda"] else "Taita Taveta",
                route_day=choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]),
                channel_id=choice(channels).id,
                assigned_person=choice(["Harun", "Amina", "Joseph", "Miriam", "Omar"]),
                description=f"Route execution plan for {territory}.",
                status=choice(["Active", "Active", "Active", "Under Review"]),
            )
        )
    db.session.add_all(rows)
    db.session.flush()


def create_swot():
    examples = {
        "Strength": "Strong Coast customer relationships",
        "Weakness": "Limited freezer coverage",
        "Opportunity": "Tourism growth increasing hotel demand",
        "Threat": "Aggressive competitor promotions",
    }
    rows = []
    for category, title in examples.items():
        for index in range(10):
            rows.append(
                Swot(
                    category=category,
                    title=f"{title} {index + 1}",
                    description=f"{category} observation for Coast Region execution.",
                    territory=choice(TERRITORIES),
                    channel=choice(CHANNELS),
                    priority=choice(["Critical", "High", "Medium", "Low"]),
                    status=choice(["Open", "Monitoring", "Action Taken", "Closed"]),
                    owner=choice(["Harun", "Amina", "Joseph", "Miriam"]),
                )
            )
    db.session.add_all(rows)


def create_visits():
    customers = Customer.query.all()
    routes = Route.query.all()
    statuses = ["Completed"] * 150 + ["Planned"] * 30 + ["Missed"] * 20
    rows = []
    for index, status in enumerate(statuses, start=1):
        customer = choice(customers)
        route = choice(routes)
        rows.append(
            Visit(
                visit_number=f"VIS-{index:04d}",
                visit_date=date.today() - timedelta(days=randint(0, 120)),
                visit_time=time(randint(8, 16), choice([0, 15, 30, 45])),
                customer_id=customer.id,
                route_id=route.id,
                territory=customer.territory,
                purpose=choice(["Routine Visit", "New Customer Prospecting", "Order Follow-Up", "Relationship Management", "Product Listing", "Complaint Resolution", "Competitor Monitoring", "Opportunity Assessment", "Account Recovery"]),
                contact_person=customer.contact_person,
                phone=customer.phone,
                arrival_time=time(randint(8, 15), 0),
                departure_time=time(randint(9, 17), 30),
                visit_status=status,
                visit_outcome=choice(["Successful", "Partially Successful", "No Contact", "Follow-Up Required", "Opportunity Identified", "Competitor Activity Observed"]),
                next_action=choice(["Follow up order", "Schedule product listing", "Monitor competitor pricing", "Prepare proposal"]),
                next_visit_date=date.today() + timedelta(days=randint(1, 30)),
                notes="Field execution record captured during seed process.",
            )
        )
    db.session.add_all(rows)


def create_opportunities():
    customers = Customer.query.all()
    statuses = ["Open"] * 20 + ["Qualified"] * 10 + ["In Progress"] * 10 + ["Won"] * 5 + ["Lost"] * 5
    rows = []
    for index, status in enumerate(statuses, start=1):
        customer = choice(customers)
        rows.append(
            Opportunity(
                opportunity_code=f"OPP-{index:04d}",
                customer_id=customer.id,
                territory=customer.territory,
                channel_id=customer.channel_id,
                product_category=choice(["Ice Cream", "Yoghurt", "Milk", "Sauces", "Bakery", "Frozen Foods"]),
                opportunity_type=choice(["New Customer", "New Product Listing", "Range Expansion", "Distributor Expansion", "Contract Opportunity", "Institution Tender", "Hotel Listing", "Shelf Space Expansion", "Market Expansion", "Account Recovery"]),
                title=f"{customer.customer_name} growth opportunity",
                description="Revenue growth opportunity identified from market activity.",
                estimated_value=randint(80, 900) * 1000,
                probability=choice([0, 25, 50, 75, 100]),
                priority=choice(["Critical", "High", "Medium", "Low"]),
                status=status,
                owner=choice(["Harun", "Amina", "Joseph", "Miriam"]),
                source=choice(["Visit", "Competitor Activity", "Lost Account", "SWOT", "Direct Prospecting", "Referral", "Management Initiative"]),
                next_action="Prepare next commercial follow-up.",
                target_close_date=date.today() + timedelta(days=randint(10, 90)),
                actual_close_date=date.today() if status in ["Won", "Lost"] else None,
                notes="Pipeline record generated from dummy data.",
            )
        )
    db.session.add_all(rows)


def create_competitors():
    customers = Customer.query.all()
    rows = []
    for index in range(40):
        customer = choice(customers)
        rows.append(
            CompetitorActivity(
                date_observed=date.today() - timedelta(days=randint(0, 90)),
                customer_id=customer.id,
                territory=customer.territory,
                channel_id=customer.channel_id,
                competitor_name=choice(["Brookside", "KCC", "Bidco", "Kevian", "Trufoods"]),
                brand_name=choice(["Fresh", "Gold", "Coastline", "Prime", "Value"]),
                product_name=choice(["Milk", "Yoghurt", "Sauce", "Ice Cream", "Juice"]),
                activity_type=choice(["Promotion", "Price Reduction", "New Product Launch", "Shelf Expansion", "Sampling"]),
                description="Competitor market activity observed in the field.",
                price_observed=randint(80, 900),
                promotion_details="Retail promotion and merchandising activity.",
                photo_path="",
                impact_level=choice(["Critical", "High", "Medium", "Low"]),
                recommended_action="Create action plan and monitor customer response.",
                status=choice(["Open", "Monitoring", "Action Required", "Closed"]),
                owner=choice(["Harun", "Amina", "Joseph", "Miriam"]),
            )
        )
    db.session.add_all(rows)


def create_lost_accounts():
    customers = Customer.query.all()
    rows = []
    for index in range(20):
        customer = choice(customers)
        rows.append(
            LostAccount(
                customer_id=customer.id,
                territory=customer.territory,
                channel_id=customer.channel_id,
                date_lost=date.today() - timedelta(days=randint(30, 180)),
                last_order_date=date.today() - timedelta(days=randint(45, 210)),
                estimated_monthly_value=randint(80, 700) * 1000,
                reason_category=choice(["Competitor Activity", "Price", "Service Issues", "Stock-Out", "Relationship Breakdown"]),
                reason_description="Account requires recovery intervention.",
                competitor_name=choice(["Brookside", "KCC", "Bidco", "Kevian", "Trufoods"]),
                recovery_probability=choice(["Very High", "High", "Medium", "Low", "Very Low"]),
                status=choice(["Open", "Under Investigation", "Recovery Plan Active", "Recovered", "Permanently Lost", "Closed"]),
                assigned_to=choice(["Harun", "Amina", "Joseph", "Miriam"]),
                recovery_action="Engage decision maker and prepare recovery offer.",
                target_recovery_date=date.today() + timedelta(days=randint(10, 90)),
                actual_recovery_date=date.today() if random() > 0.75 else None,
                notes="Recovery record generated from dummy data.",
            )
        )
    db.session.add_all(rows)


def create_action_plans():
    customers = Customer.query.all()
    statuses = ["Open"] * 20 + ["In Progress"] * 15 + ["Completed"] * 10 + ["Overdue"] * 5
    rows = []
    for index, status in enumerate(statuses, start=1):
        customer = choice(customers)
        progress = 100 if status == "Completed" else 50 if status == "In Progress" else 0
        rows.append(
            ActionPlan(
                action_code=f"ACT-{index:04d}",
                title=choice(["Recover account", "Follow up tender", "Respond to promotion", "Improve route coverage", "Close opportunity"]) + f" {index}",
                description="Documented execution action for Coast Region growth.",
                source_module=choice(["SWOT", "Visit", "Opportunity", "Competitor Activity", "Lost Account", "Management Initiative", "Direct Assignment"]),
                source_record_id=randint(1, 50),
                territory=customer.territory,
                channel_id=customer.channel_id,
                customer_id=customer.id,
                priority=choice(["Critical", "High", "Medium", "Low"]),
                status=status,
                owner=choice(["Harun", "Amina", "Joseph", "Miriam"]),
                start_date=date.today() - timedelta(days=randint(0, 45)),
                target_date=date.today() + timedelta(days=randint(-15, 60)),
                completion_date=date.today() if status == "Completed" else None,
                progress_percentage=progress,
                expected_impact="Improve execution, defend revenue or close growth gap.",
                actual_impact="Impact captured after action completion." if status == "Completed" else "",
                notes="Action plan generated from dummy data.",
            )
        )
    db.session.add_all(rows)


def seed_database():
    reset_database()
    create_users()
    create_channels()
    create_products()
    create_customers()
    create_routes()
    create_swot()
    create_visits()
    create_opportunities()
    create_competitors()
    create_lost_accounts()
    create_action_plans()
    db.session.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_database()
        print("RAZCO PWANI database seeded successfully.")
