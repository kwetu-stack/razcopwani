# RAZCO PWANI™
# CODEX MASTER BUILD PROMPT

---

## Mission

Build the complete RAZCO PWANI application from the project documentation.

This is a Coast Region FMCG Strategic Management System designed to help management achieve sales growth through disciplined execution, market intelligence, opportunity management and action planning.

---

# IMPORTANT

Read ALL project documentation before generating any code.

Do NOT start coding until all documents have been reviewed.

The documentation is the source of truth.

If code conflicts with documentation:

Documentation wins.

---

# Documents To Read

Read in this exact order:

01_PROJECT_OVERVIEW.md

02_FOLDER_STRUCTURE.md

03_DATABASE_SCHEMA.md

04_MODEL_RELATIONSHIPS.md

05_NAVBAR_STRUCTURE.md

06_DASHBOARD.md

07_SWOT.md

08_CUSTOMERS.md

09_PRODUCTS.md

10_CHANNELS.md

11_ROUTES.md

12_VISITS.md

13_OPPORTUNITIES.md

14_COMPETITORS.md

15_LOST_ACCOUNTS.md

16_ACTION_PLANS.md

17_REPORTS.md

18_DUMMY_DATA.md

19_UI_THEME.md

20_CODEX_RULES.md

21_USER_ROLES.md

22_CODEX_MASTER_PROMPT.md

---

# Build Objective

Generate a complete ready-to-run Flask application.

The application must run immediately after:

```bash
pip install -r requirements.txt
python seed.py
python app.py
```

No manual code editing required.

No patching required.

No missing files.

No missing templates.

No placeholder pages.

---

# Development Method

Follow:

Architecture First

↓

Database

↓

Models

↓

Relationships

↓

Routes

↓

Templates

↓

Seed Data

↓

Testing

---

# Build Everything First

IMPORTANT

Build the ENTIRE application first.

Do NOT stop after each page.

Do NOT partially build modules.

Do NOT debug one page at a time.

Complete all modules first.

Only after the full application exists:

Perform testing.

---

# Zero Patch Rule

If architecture is wrong:

Stop.

Delete.

Regenerate cleanly.

Never stack fixes on top of fixes.

Never patch broken architecture.

---

# Technology Stack

Backend:

Flask

ORM:

SQLAlchemy

Database:

SQLite

Future Database Support:

PostgreSQL

Frontend:

Bootstrap 5

Charts:

Chart.js

Reporting:

Pandas

Excel Export:

OpenPyXL

Authentication:

Flask-Login

Environment Variables:

python-dotenv

---

# Required Modules

Build:

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

Authentication

User Management

---

# Required Authentication

Implement:

Flask-Login

Login

Logout

Session Management

Role Based Access Control

---

# User Accounts

Create automatically during seed process.

Administrator

Username:

admin

Password:

monozukuri

Role:

Administrator

---

User

Username:

user

Password:

user123

Role:

User

---

# Password Security

Passwords must be hashed.

Use:

generate_password_hash()

check_password_hash()

Never store plaintext passwords.

---

# User Roles

Role 1

Administrator

Permissions:

Create

Read

Update

Delete

Export

User Management

Settings

System Administration

---

Role 2

User

Permissions:

Read Only

Can view all modules.

Cannot:

Create

Edit

Delete

Export

Manage Users

Modify Settings

---

# RBAC Security Rule

Permissions must be enforced:

Frontend

AND

Backend

Example:

```python
if current_user.role != "admin":
    abort(403)
```

Never rely only on hidden buttons.

---

# Navbar Rules

Administrator:

Full menu

Full actions

---

User:

Full menu visibility

Read-only pages

Hidden:

Create buttons

Edit buttons

Delete buttons

Import buttons

Settings

User Management

---

# Database Rules

Use:

03_DATABASE_SCHEMA.md

Exactly.

Do not invent tables.

Do not rename fields.

Do not remove fields.

---

# Relationship Rules

Use:

04_MODEL_RELATIONSHIPS.md

Exactly.

Implement all foreign keys.

Implement all relationships.

Avoid circular imports.

---

# UI Rules

Use:

19_UI_THEME.md

Exactly.

Theme:

Kwetu Operations Center

Use:

Dark Navy

Cyan Accent

Rounded Cards

Professional Executive Layout

---

# Responsive Design

Support:

Mobile

Tablet

Laptop

Desktop

---

# Charts

Implement all charts documented.

Use:

Chart.js

No placeholder charts.

Use real database queries.

---

# Reports

Implement:

PDF Export

Excel Export

CSV Export

Print View

All reports must use live database data.

---

# Seed Data

Create:

seed.py

Populate:

Channels

Routes

Products

Customers

Visits

SWOT Entries

Opportunities

Competitor Activities

Lost Accounts

Action Plans

Users

Use:

18_DUMMY_DATA.md

Exactly.

---

# Application Startup

Running:

```bash
python seed.py
```

must create:

Database

Tables

Relationships

Dummy Data

Users

---

Running:

```bash
python app.py
```

must launch the application successfully.

---

# Error Handling

Implement:

403

404

500

Friendly user interfaces.

No raw tracebacks visible to users.

---

# Code Quality Rules

No TODO comments.

No placeholder code.

No unused imports.

No dead code.

No unfinished modules.

---

# Performance Rules

Avoid:

N+1 queries

Duplicate queries

Inefficient loading

Use:

SQLAlchemy relationships

Efficient filtering

Pagination

---

# Testing Checklist

Verify:

Application Starts

Database Creates

Seed Data Loads

Login Works

Logout Works

RBAC Works

CRUD Works

Search Works

Filters Work

Charts Render

Reports Export

Navbar Works

No Broken Links

No Errors

---

# Final Acceptance Criteria

The application is accepted only if:

All pages load.

All CRUD functions work.

All reports work.

All exports work.

RBAC works.

Seed data loads.

Charts display correctly.

Application starts without errors.

No manual fixes required.

No patches required.

---

# Golden Rule

If something fails:

Do not patch.

Return to architecture.

Fix correctly.

Regenerate cleanly.

---

# Project Authority

Business Authority:

Harun

System Name:

RAZCO PWANI™

Version:

1.0

Status:

LOCKED FOR BUILD