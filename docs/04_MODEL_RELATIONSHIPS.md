# RAZCO PWANI™
# Model Relationships

---

## Purpose

Define all SQLAlchemy relationships before development begins.

This document serves as the single source of truth for model design.

---

# CHANNEL RELATIONSHIPS

Channel

Has Many:

- Customers
- Routes
- Opportunities
- Competitor Activities
- Lost Accounts
- Action Plans

Relationship:

Channel (1)
↓
Many Records

---

# CUSTOMER RELATIONSHIPS

Customer

Has Many:

- Visits
- Opportunities
- Competitor Activities
- Lost Accounts
- Action Plans

Relationship:

Customer (1)
↓
Many Visits

Customer (1)
↓
Many Opportunities

Customer (1)
↓
Many Competitor Activities

Customer (1)
↓
Many Lost Accounts

Customer (1)
↓
Many Action Plans

---

# ROUTE RELATIONSHIPS

Route

Has Many:

- Visits

Relationship:

Route (1)
↓
Many Visits

---

# VISIT RELATIONSHIPS

Visit

Belongs To:

- Customer
- Route

Visit may generate:

- Opportunity
- Competitor Activity
- Action Plan

Workflow:

Visit
↓
Opportunity

Visit
↓
Competitor Activity

Visit
↓
Action Plan

---

# OPPORTUNITY RELATIONSHIPS

Opportunity

Belongs To:

- Customer
- Channel

Opportunity may generate:

- Action Plan

Workflow:

Opportunity
↓
Action Plan

---

# COMPETITOR RELATIONSHIPS

Competitor Activity

Belongs To:

- Customer
- Channel

Competitor Activity may generate:

- Opportunity
- Action Plan

Workflow:

Competitor Activity
↓
Opportunity

Competitor Activity
↓
Action Plan

---

# LOST ACCOUNT RELATIONSHIPS

Lost Account

Belongs To:

- Customer
- Channel

Lost Account may generate:

- Opportunity
- Action Plan

Workflow:

Lost Account
↓
Opportunity

Lost Account
↓
Action Plan

---

# ACTION PLAN RELATIONSHIPS

Action Plan

Optional Links:

- Customer
- Channel

Source Modules:

- SWOT
- Visit
- Opportunity
- Competitor Activity
- Lost Account

Relationship Type:

Polymorphic Reference

Fields:

source_module
source_record_id

Examples:

source_module = "Visit"

source_record_id = 15

---

# SWOT RELATIONSHIPS

SWOT entries are independent.

SWOT entries may generate:

- Action Plans

Workflow:

SWOT
↓
Action Plan

---

# SYSTEM FLOW

Dashboard
↓
SWOT
↓
Customers
↓
Routes
↓
Visits
↓
Opportunities
↓
Action Plans
↓
Reports

---

# FOREIGN KEY SUMMARY

Customer.channel_id
→ Channel.id

Route.channel_id
→ Channel.id

Visit.customer_id
→ Customer.id

Visit.route_id
→ Route.id

Opportunity.customer_id
→ Customer.id

Opportunity.channel_id
→ Channel.id

CompetitorActivity.customer_id
→ Customer.id

CompetitorActivity.channel_id
→ Channel.id

LostAccount.customer_id
→ Customer.id

LostAccount.channel_id
→ Channel.id

ActionPlan.customer_id
→ Customer.id

ActionPlan.channel_id
→ Channel.id

---

# SQLALCHEMY RULES

Use:

db.relationship()

and

db.ForeignKey()

Implement:

lazy=True

Use back_populates where appropriate.

Avoid circular imports.

---

# VERSION

RAZCO PWANI Version 1.0