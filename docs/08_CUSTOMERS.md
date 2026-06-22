# RAZCO PWANI™
# Customers Module

---

## Purpose

The Customers Module is the Customer Intelligence Engine of RAZCO PWANI.

It stores and manages all customer information across the Coast Region.

The module provides visibility into customer relationships, channel distribution, territory coverage and business opportunities.

---

# Business Objective

Answer the following questions:

- Who are our customers?
- Where are they located?
- Which channel do they belong to?
- Which customers are active?
- Which customers are at risk?
- Which customers offer growth opportunities?

---

# Database Table

customers

---

# Fields

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

# Customer Status

Active

Inactive

Dormant

Lost

Prospect

---

# Customer Profile Screen

Display:

Customer Name

Customer Code

Contact Person

Phone Number

Email Address

Physical Address

Territory

Channel

Customer Status

Credit Limit

Notes

---

# Customer Dashboard Widgets

---

## Total Customers

Example:

100

---

## Active Customers

Example:

82

---

## Dormant Customers

Example:

10

---

## Lost Customers

Example:

8

---

## New Customers This Month

Example:

5

---

# Customer Health Score

Display:

Green

Healthy

---

Yellow

Needs Attention

---

Red

At Risk

---

# Customer Classification

Allow customer categorization:

---

## General Trade

Kiosks

Retail Shops

Wholesalers

---

## Modern Trade

Supermarkets

Mini-Markets

Chain Stores

---

## HORECA

Hotels

Restaurants

Cafes

---

## Institutions

Schools

Hospitals

Colleges

Government

---

## Distributors

Regional Distributors

Wholesalers

---

# Customer Timeline

Display:

Visits

Opportunities

Competitor Activities

Lost Account Records

Action Plans

Chronologically.

---

# Customer Snapshot

Display:

Last Visit Date

Last Opportunity

Open Action Plans

Competitor Activities

Recovery Status

---

# Customer Map View

Future Enhancement.

Display customers by territory.

---

# Customer Search

Allow searching by:

Customer Name

Customer Code

Phone Number

Contact Person

---

# Filters

Provide:

Territory

Channel

Customer Status

Date Created

Health Score

---

# Customer Reports

Generate:

Customer Master List

Active Customers Report

Dormant Customers Report

Lost Customers Report

Customer Growth Report

Customer Territory Report

Customer Channel Report

---

# Export Options

PDF

Excel

CSV

Print View

---

# Charts

---

## Customers by Channel

Pie Chart

---

## Customers by Territory

Bar Chart

---

## Customer Status Distribution

Doughnut Chart

---

# Customer Relationships

Customer

↓

Visits

↓

Opportunities

↓

Competitor Activities

↓

Lost Accounts

↓

Action Plans

---

# Special Features

---

## Create Visit

Button:

Create Visit

---

## Create Opportunity

Button:

Create Opportunity

---

## Create Competitor Activity

Button:

Create Competitor Activity

---

## Create Action Plan

Button:

Create Action Plan

---

# Dashboard Integration

Dashboard should display:

Top Customers

New Customers

Dormant Customers

Customers Requiring Attention

---

# Example Dummy Customers

Modern Trade

- Naivas Nyali
- Carrefour Nyali
- Quickmart Nyali

---

HORECA

- Whitesands Hotel
- PrideInn Paradise
- Voyager Beach Resort

---

Institutions

- KMTC Mombasa
- Technical University of Mombasa

---

Distributors

- Coast Distributor Ltd
- South Coast Distributors

---

# Codex Instructions

Blueprint:

customers_bp

Model:

Customer

Template:

customers.html

Implement:

CRUD

Search

Filters

Pagination

Customer Profile Screen

Customer Timeline

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Every Customer must belong to one Channel.

Customer Name is mandatory.

Customer Code must be unique.

Customer records must not be deleted without confirmation.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED