# RAZCO PWANI™
# Database Schema

---

## Database Engine

Primary Database:

SQLite

Default Location:

data/razco_pwani.db

Future Support:

PostgreSQL

---

# TABLE: SWOT

Purpose:

Store strategic observations.

Fields:

id
category
title
description
territory
channel
priority
status
owner
created_at
updated_at

---

# TABLE: CUSTOMERS

Purpose:

Customer master data.

Fields:

id
customer_code
customer_name
contact_person
phone
email
physical_address
territory
channel_id
customer_status
credit_limit
notes
created_at
updated_at

---

# TABLE: PRODUCTS

Purpose:

Product master.

Fields:

id
product_code
product_name
category
brand
unit_size
selling_price
status
notes
created_at
updated_at

---

# TABLE: CHANNELS

Purpose:

Market channels.

Fields:

id
channel_name
description
growth_target
manager
status
notes
created_at
updated_at

---

# TABLE: ROUTES

Purpose:

Sales routes.

Fields:

id
route_code
route_name
territory
county
route_day
channel_id
assigned_person
description
status
created_at
updated_at

---

# TABLE: VISITS

Purpose:

Field execution records.

Fields:

id
visit_number
visit_date
visit_time
customer_id
route_id
territory
purpose
contact_person
phone
arrival_time
departure_time
visit_status
visit_outcome
next_action
next_visit_date
notes
created_at
updated_at

---

# TABLE: OPPORTUNITIES

Purpose:

Growth pipeline.

Fields:

id
opportunity_code
customer_id
territory
channel_id
product_category
opportunity_type
title
description
estimated_value
probability
priority
status
owner
source
next_action
target_close_date
actual_close_date
notes
created_at
updated_at

---

# TABLE: COMPETITOR_ACTIVITIES

Purpose:

Market intelligence.

Fields:

id
date_observed
customer_id
territory
channel_id
competitor_name
brand_name
product_name
activity_type
description
price_observed
promotion_details
photo_path
impact_level
recommended_action
status
owner
created_at
updated_at

---

# TABLE: LOST_ACCOUNTS

Purpose:

Customer recovery.

Fields:

id
customer_id
territory
channel_id
date_lost
last_order_date
estimated_monthly_value
reason_category
reason_description
competitor_name
recovery_probability
status
assigned_to
recovery_action
target_recovery_date
actual_recovery_date
notes
created_at
updated_at

---

# TABLE: ACTION_PLANS

Purpose:

Execution management.

Fields:

id
action_code
title
description
source_module
source_record_id
territory
channel_id
customer_id
priority
status
owner
start_date
target_date
completion_date
progress_percentage
expected_impact
actual_impact
notes
created_at
updated_at

---

# RELATIONSHIP RULES

Customer belongs to one Channel.

Route belongs to one Channel.

Visit belongs to one Customer.

Visit belongs to one Route.

Opportunity belongs to one Customer.

Opportunity belongs to one Channel.

Competitor Activity belongs to one Customer.

Competitor Activity belongs to one Channel.

Lost Account belongs to one Customer.

Lost Account belongs to one Channel.

Action Plan may belong to a Customer.

---

# AUDIT FIELDS

Every table must contain:

created_at
updated_at

---

# PRIMARY KEYS

Every table uses:

id

Auto Increment Integer.

---

# VERSION

RAZCO PWANI Version 1.0