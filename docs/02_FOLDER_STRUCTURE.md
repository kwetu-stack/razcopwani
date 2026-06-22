# RAZCO PWANI™
# Folder Structure

---

## Objective

Create a clean, scalable Flask architecture that follows the Kwetu development methodology.

The application must start without errors and be easy to maintain.

---

# Root Structure

razco-pwani/

├── app.py
├── config.py
├── requirements.txt
├── seed.py
├── .env
├── .env.example
│
├── docs/
│
├── data/
│   └── razco_pwani.db
│
├── models/
│
├── blueprints/
│
├── templates/
│
├── static/
│
├── reports/
│
└── uploads/

---

# Models Folder

models/

├── __init__.py
├── customer.py
├── product.py
├── channel.py
├── route.py
├── visit.py
├── opportunity.py
├── competitor.py
├── lost_account.py
├── action_plan.py
├── swot.py

Purpose:

Store SQLAlchemy models.

---

# Blueprints Folder

blueprints/

├── dashboard/
├── swot/
├── customers/
├── products/
├── channels/
├── routes/
├── visits/
├── opportunities/
├── competitors/
├── lost_accounts/
├── action_plans/
├── reports/

Each blueprint contains:

__init__.py
routes.py

---

# Templates Folder

templates/

├── base.html
├── dashboard/
├── swot/
├── customers/
├── products/
├── channels/
├── routes/
├── visits/
├── opportunities/
├── competitors/
├── lost_accounts/
├── action_plans/
├── reports/
├── partials/
└── errors/

---

# Static Folder

static/

├── css/
├── js/
├── images/
├── uploads/

---

# Upload Structure

static/uploads/

├── visits/
├── competitors/
├── customers/

---

# Reports Folder

reports/

Generated exports:

- PDF
- Excel
- CSV

---

# Database

Default:

SQLite

Location:

data/razco_pwani.db

Future:

PostgreSQL support.

---

# Error Pages

templates/errors/

404.html
500.html

---

# Design Rule

Every module must have:

CRUD
Search
Filters
Pagination
Export

---

# Navigation Order

Dashboard

SWOT

Customers

Products

Channels

Routes

Visits

Opportunities

Competitors

Lost Accounts

Action Plans

Reports

---

# Development Rule

Documentation First

Architecture Second

Code Third

---

# Version

RAZCO PWANI Version 1.0