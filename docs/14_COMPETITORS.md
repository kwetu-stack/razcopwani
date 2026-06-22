# RAZCO PWANI™
# Competitors Module

---

## Purpose

The Competitors Module is the Market Intelligence Engine of RAZCO PWANI.

It captures and analyzes competitor activities observed in the market.

The module helps identify threats, opportunities and strategic actions required to protect and grow business.

---

# Business Objective

Answer the following questions:

- What are competitors doing?
- Which competitors are most active?
- Which territories are under attack?
- Which customers are at risk?
- What promotions are running?
- What actions should be taken?

---

# Database Table

competitor_activities

---

# Fields

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

# Competitor Companies

Brookside

KCC

Bidco

Kevian

Trufoods

Delamere

Bio Foods

Other

---

# Activity Types

Promotion

Price Reduction

Price Increase

New Product Launch

Shelf Expansion

Sampling

Merchandising

Freezer Placement

Distributor Appointment

Brand Activation

Competitor Visit

Other

---

# Impact Levels

Critical

High

Medium

Low

---

# Status

Open

Monitoring

Action Required

Closed

---

# Competitor Activity Entry Form

Display:

Date Observed

Customer

Territory

Channel

Competitor Name

Brand Name

Product Name

Activity Type

Description

Price Observed

Promotion Details

Photo Upload

Impact Level

Recommended Action

Status

Owner

---

# Competitor Dashboard Widgets

---

## Total Activities

Example:

40

---

## Active Threats

Example:

12

---

## Most Active Competitor

Example:

Brookside

---

## Critical Threats

Example:

5

---

## Activities This Month

Example:

18

---

# Competitor Scorecard

Display:

Competitor

Activities

Critical Threats

Territories Affected

Customers Affected

Risk Score

---

# Market Intelligence Analysis

Display:

Most Active Competitor

Most Affected Territory

Most Affected Channel

Most Threatened Customer

Most Common Activity Type

---

# Competitor Search

Allow Search By:

Competitor Name

Brand Name

Product Name

Customer

Territory

---

# Filters

Provide:

Competitor

Activity Type

Impact Level

Territory

Channel

Status

Date Range

---

# Charts

---

## Activities by Competitor

Bar Chart

---

## Activities by Territory

Bar Chart

---

## Activities by Channel

Pie Chart

---

## Activity Type Distribution

Doughnut Chart

---

## Monthly Competitor Trend

Line Chart

---

# Territory Threat Analysis

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

Identify threat concentration.

---

# Channel Threat Analysis

Display:

General Trade

Modern Trade

HORECA

Institutions

Distributors

Purpose:

Identify channel vulnerability.

---

# Competitor Relationships

Competitor Activity

Belongs To:

Customer

Channel

Competitor Activity May Generate:

Opportunity

Action Plan

---

# Special Features

---

## Create Opportunity

Button:

Create Opportunity

Purpose:

Convert threat into growth opportunity.

---

## Create Action Plan

Button:

Create Action Plan

Purpose:

Respond to competitor activity.

---

## Upload Photo Evidence

Button:

Upload Image

Purpose:

Store field intelligence.

---

# Threat Workflow

Competitor Activity

↓

Threat Assessment

↓

Action Plan

↓

Execution

↓

Result

---

# Reports

Generate:

Competitor Activity Report

Competitor Threat Report

Territory Threat Report

Channel Threat Report

Market Intelligence Report

Monthly Competitor Review

Executive Threat Summary

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Most Active Competitor

Critical Threats

Recent Competitor Activities

Threat Trend

---

# Example Dummy Records

Competitor:

Brookside

Activity:

Price Reduction

Territory:

Nyali

Impact:

High

---

Competitor:

KCC

Activity:

Freezer Placement

Territory:

Mtwapa

Impact:

Medium

---

Competitor:

Bidco

Activity:

New Product Launch

Territory:

Diani

Impact:

High

---

# Codex Instructions

Blueprint:

competitors_bp

Model:

CompetitorActivity

Template:

competitors.html

Implement:

CRUD

Search

Filters

Pagination

Threat Analysis

Photo Upload

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Competitor Name is mandatory.

Activity Type is mandatory.

Date Observed is mandatory.

Impact Level is mandatory.

Photo uploads are optional.

Records must not be deleted without confirmation.

Threat calculations must use live database records.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED