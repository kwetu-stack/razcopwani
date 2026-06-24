from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import pandas as pd

from app import create_app
from models import Customer, db

app = create_app()

EXCEL_FILE = Path("Razco Customers/razco customers.xlsx")


CHANNEL_MAP = {
    "KEY ACCOUNT": 2,        # Modern Trade
    "HORECA": 3,             # HORECA
    "GENERAL TRADING": 1,    # General Trade
    "OFFICE SALES": 5,       # Distributors
}


def add_customer(
    code,
    name,
    channel_id,
    status="Active",
):
    customer = Customer(
        customer_code=code,
        customer_name=name.strip(),
        contact_person="N/A",
        phone="N/A",
        email="N/A",
        physical_address="N/A",
        territory="Coast",
        channel_id=channel_id,
        customer_status=status,
        credit_limit=0,
        notes="Imported from Razco Customer Master",
    )

    db.session.add(customer)


with app.app_context():

    print("Deleting dummy customers...")

    Customer.query.delete()
    db.session.commit()

    counter = 1

    # KEY ACCOUNT / HORECA / GENERAL TRADING / OFFICE SALES

    for sheet_name, channel_id in CHANNEL_MAP.items():

        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)

        customer_column = df.columns[1]

        for customer_name in df[customer_column].tolist():

            if pd.isna(customer_name):
                continue

            if str(customer_name).strip().upper() == "NAMES":
                continue

            code = f"CUS-{counter:04d}"

            add_customer(
                code=code,
                name=str(customer_name),
                channel_id=channel_id,
                status="Active",
            )

            counter += 1

    # DORMANT ACCOUNTS

    df = pd.read_excel(EXCEL_FILE, sheet_name="DOMANT ACCOUNTS")

    customer_column = df.columns[1]

    for customer_name in df[customer_column].tolist():

        if pd.isna(customer_name):
            continue

        code = f"CUS-{counter:04d}"

        add_customer(
            code=code,
            name=str(customer_name),
            channel_id=1,
            status="Lost",
        )

        counter += 1

    db.session.commit()

    print(f"Imported {counter - 1} customers successfully.")