# RAZCO PWANI™
# Routes Module

---

## Purpose

The Routes Module is the Route Execution Engine of RAZCO PWANI.

It manages route planning, territory coverage and customer visitation strategy.

The module ensures that market coverage is systematic, measurable and aligned with growth objectives.

---

# Business Objective

Answer the following questions:

- Which routes exist?
- Which routes are being serviced?
- Which routes have growth opportunities?
- Which routes have poor coverage?
- Which routes require attention?
- Are we covering the market effectively?

---

# Database Table

routes

---

# Fields

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

# Route Status

Active

Inactive

Under Review

Suspended

---

# Standard Coast Routes

Nyali Route

Bamburi Route

Mtwapa Route

Kilifi Route

Malindi Route

Diani Route

Ukunda Route

Likoni Route

Changamwe Route

Mariakani Route

Voi Route

Taveta Route

Lamu Route

---

# Route Profile Screen

Display:

Route Code

Route Name

Territory

County

Route Day

Assigned Person

Channel

Status

Description

Created Date

Updated Date

---

# Route Dashboard Widgets

---

## Total Routes

Example:

13

---

## Active Routes

Example:

12

---

## Coverage %

Example:

84%

---

## Missed Routes

Example:

2

---

## High Potential Routes

Example:

5

---

# Route Performance Scorecard

Display:

Route Name

Customer Count

Visit Count

Opportunity Count

Coverage %

Growth Potential

Health Score

---

# Route Health Score

Green

Healthy

---

Yellow

Needs Attention

---

Red

Critical

---

# Route Coverage Analysis

Display:

Planned Customers

Visited Customers

Missed Customers

Coverage %

Purpose:

Measure route execution.

---

# Route Opportunity Analysis

Display:

Open Opportunities

Pipeline Value

High Potential Accounts

Lost Accounts

Competitor Activities

Purpose:

Identify growth opportunities by route.

---

# Route Search

Allow Search By:

Route Name

Route Code

Territory

Assigned Person

---

# Filters

Provide:

Territory

County

Channel

Status

Route Day

Assigned Person

---

# Charts

---

## Route Coverage %

Bar Chart

---

## Opportunities By Route

Bar Chart

---

## Customers By Route

Pie Chart

---

## Route Performance Trend

Line Chart

---

# Route Relationships

Route

↓

Visits

Route

↓

Customers

Route

↓

Opportunities

Route

↓

Competitor Activities

---

# Route Calendar View

Display:

Monday

Tuesday

Wednesday

Thursday

Friday

Saturday

Purpose:

Weekly route planning.

---

# Weekly Route Planner

Display:

Planned Visits

Completed Visits

Missed Visits

Coverage %

---

# Territory Analysis

Display:

Nyali

Bamburi

Mtwapa

Kilifi

Malindi

Diani

Ukunda

Likoni

Changamwe

Mariakani

Voi

Taveta

Lamu

Purpose:

Territory coverage monitoring.

---

# Example Route Objectives

Nyali Route

Objective:

Increase Modern Trade penetration.

---

Mtwapa Route

Objective:

Expand HORECA coverage.

---

Diani Route

Objective:

Increase hotel product listings.

---

Voi Route

Objective:

Strengthen distributor relationships.

---

# Reports

Generate:

Route Master Report

Route Coverage Report

Route Performance Report

Territory Coverage Report

Route Opportunity Report

Weekly Route Report

Monthly Route Review

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Coverage %

Missed Routes

Best Performing Route

Highest Opportunity Route

---

# Special Features

---

## Generate Weekly Plan

Button:

Generate Weekly Route Plan

---

## Create Visit

Button:

Create Visit

---

## Route Heat Map

Future Version

Display territory intensity.

---

# Codex Instructions

Blueprint:

routes_bp

Model:

Route

Template:

routes.html

Implement:

CRUD

Search

Filters

Pagination

Route Profile Screen

Coverage Analysis

Route Calendar

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Route Name is mandatory.

Route Code must be unique.

Every Route belongs to one Channel.

Routes must not be deleted without confirmation.

Coverage calculations must use live Visit data.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED