# RAZCO PWANI™
# Visits Module

---

## Purpose

The Visits Module is the Field Execution Engine of RAZCO PWANI.

It captures all customer visits performed across the Coast Region and provides visibility into coverage, execution quality, opportunities, competitor intelligence and follow-up actions.

This is the most important operational module in the system.

---

# Business Objective

Answer the following questions:

- Which customers were visited?
- Which customers were missed?
- What happened during the visit?
- What opportunities were identified?
- What competitor activities were observed?
- What actions are required?

---

# Database Table

visits

---

# Fields

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

# Visit Status

Planned

Completed

Missed

Cancelled

Rescheduled

---

# Visit Purpose

Routine Visit

New Customer Prospecting

Order Follow-Up

Relationship Management

Product Listing

Complaint Resolution

Competitor Monitoring

Opportunity Assessment

Account Recovery

---

# Visit Outcome

Successful

Partially Successful

No Contact

Customer Closed

Follow-Up Required

Opportunity Identified

Competitor Activity Observed

---

# Visit Entry Form

Display:

Visit Date

Visit Time

Customer

Route

Territory

Purpose

Contact Person

Phone

Arrival Time

Departure Time

Visit Status

Visit Outcome

Next Action

Next Visit Date

Notes

---

# Visit Dashboard Widgets

---

## Planned Visits

Example:

200

---

## Completed Visits

Example:

150

---

## Missed Visits

Example:

20

---

## Coverage %

Example:

84%

---

## Opportunities Generated

Example:

35

---

## Competitor Activities Captured

Example:

18

---

# Visit Performance Scorecard

Display:

Visit Date

Customer

Route

Status

Outcome

Duration

Follow-Up Required

---

# Coverage Calculation

Coverage %

=

Completed Visits

÷

Planned Visits

×

100

---

# Visit Productivity Analysis

Display:

Visits Completed

Opportunities Generated

Competitor Activities Logged

Action Plans Created

Purpose:

Measure field productivity.

---

# Visit Search

Allow Search By:

Visit Number

Customer Name

Contact Person

Territory

Route

---

# Filters

Provide:

Date Range

Territory

Route

Customer

Visit Status

Visit Outcome

Purpose

---

# Charts

---

## Visits By Territory

Bar Chart

---

## Visits By Route

Bar Chart

---

## Visit Status Distribution

Pie Chart

---

## Weekly Visit Trend

Line Chart

---

# Visit Timeline

Display chronological history:

Visit

↓

Opportunity

↓

Action Plan

↓

Outcome

---

# Customer Visit History

Display:

Last Visit

Visit Count

Visit Outcomes

Open Actions

Opportunities Generated

Competitor Activities

---

# Route Visit Analysis

Display:

Route

Planned Visits

Completed Visits

Coverage %

Missed Visits

---

# Special Features

---

## Create Opportunity

Button:

Create Opportunity

Purpose:

Convert visit findings into pipeline.

---

## Create Competitor Activity

Button:

Create Competitor Activity

Purpose:

Capture market intelligence.

---

## Create Action Plan

Button:

Create Action Plan

Purpose:

Assign follow-up actions.

---

## Schedule Follow-Up Visit

Button:

Schedule Visit

---

# Visit Workflow

Visit

↓

Observation

↓

Opportunity

↓

Action Plan

↓

Execution

↓

Result

---

# Reports

Generate:

Visit Report

Daily Visit Report

Weekly Visit Report

Monthly Visit Report

Coverage Report

Missed Visit Report

Visit Productivity Report

Customer Visit History Report

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Today's Visits

Coverage %

Missed Visits

Recent Visits

Opportunities Generated

---

# Example Dummy Visits

Visit:

Naivas Nyali

Outcome:

Opportunity Identified

---

Visit:

Whitesands Hotel

Outcome:

Competitor Promotion Observed

---

Visit:

KMTC Mombasa

Outcome:

Follow-Up Required

---

# Relationships

Visit

Belongs To:

Customer

Route

Visit May Generate:

Opportunity

Competitor Activity

Action Plan

---

# Codex Instructions

Blueprint:

visits_bp

Model:

Visit

Template:

visits.html

Implement:

CRUD

Search

Filters

Pagination

Visit Timeline

Coverage Analysis

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Every Visit must belong to one Customer.

Every Visit must belong to one Route.

Visit Date is mandatory.

Visit Status is mandatory.

Visit records must not be deleted without confirmation.

Coverage calculations must use live database records.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED