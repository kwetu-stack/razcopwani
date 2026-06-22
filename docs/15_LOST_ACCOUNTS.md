# RAZCO PWANI™
# Lost Accounts Module

---

## Purpose

The Lost Accounts Module is the Customer Recovery Engine of RAZCO PWANI.

It captures, tracks and manages customers that have stopped buying, reduced business significantly or shifted to competitors.

The objective is to identify recovery opportunities and return lost revenue back into the business.

---

# Business Objective

Answer the following questions:

- Which customers have been lost?
- Why were they lost?
- Which competitor gained the business?
- What revenue was lost?
- Which accounts can be recovered?
- What actions are required?

---

# Database Table

lost_accounts

---

# Fields

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

# Loss Categories

Price

Competitor Activity

Poor Service

Stock Availability

Relationship Breakdown

Credit Issues

Product Quality

Distribution Issues

Management Decision

Other

---

# Recovery Probability

Very High

High

Medium

Low

Very Low

---

# Account Status

Open

Under Investigation

Recovery Plan Active

Recovered

Permanently Lost

Closed

---

# Lost Account Entry Form

Display:

Customer

Territory

Channel

Date Lost

Last Order Date

Estimated Monthly Value

Reason Category

Reason Description

Competitor Name

Recovery Probability

Assigned To

Recovery Action

Target Recovery Date

Status

Notes

---

# Lost Accounts Dashboard Widgets

---

## Total Lost Accounts

Example:

20

---

## Recovery Pipeline

Example:

12

---

## Recovered Accounts

Example:

5

---

## Revenue at Risk

Example:

KES 2,400,000

---

## Recovery Value

Example:

KES 1,350,000

---

# Recovery Value Formula

Sum of:

Estimated Monthly Value

for all accounts with:

High

or

Very High

Recovery Probability

---

# Recovery Scorecard

Display:

Customer

Territory

Value

Competitor

Probability

Status

Target Date

Assigned To

---

# Recovery Analysis

Display:

Highest Value Lost Account

Most Common Loss Reason

Most Aggressive Competitor

Most Recoverable Account

Highest Risk Territory

---

# Lost Account Search

Allow Search By:

Customer Name

Competitor Name

Territory

Assigned Person

---

# Filters

Provide:

Status

Recovery Probability

Reason Category

Competitor

Territory

Channel

Date Range

Assigned To

---

# Charts

---

## Lost Accounts by Reason

Pie Chart

---

## Lost Accounts by Competitor

Bar Chart

---

## Lost Accounts by Territory

Bar Chart

---

## Recovery Status Distribution

Doughnut Chart

---

## Monthly Recovery Trend

Line Chart

---

# Competitor Analysis

Display:

Brookside

KCC

Bidco

Kevian

Trufoods

Other

Purpose:

Determine where business was lost.

---

# Recovery Workflow

Lost Account

↓

Investigation

↓

Recovery Plan

↓

Customer Engagement

↓

Recovery

↓

Revenue Restoration

---

# Recovery Plan Section

Display:

Root Cause

Recovery Strategy

Actions Required

Owner

Target Date

Progress %

Expected Revenue

---

# Lost Account Relationships

Lost Account

Belongs To:

Customer

Channel

Lost Account May Generate:

Opportunity

Action Plan

---

# Special Features

---

## Create Recovery Action Plan

Button:

Create Action Plan

---

## Create Opportunity

Button:

Create Opportunity

---

## Mark as Recovered

Button:

Recovered

---

## Recovery Notes

Maintain chronological recovery history.

---

# Reports

Generate:

Lost Accounts Report

Recovery Pipeline Report

Recovered Accounts Report

Revenue Recovery Report

Competitor Loss Report

Territory Recovery Report

Executive Recovery Summary

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Revenue at Risk

Recovery Pipeline

Recently Recovered Accounts

Highest Priority Recoveries

---

# Example Dummy Records

Customer:

Whitesands Hotel

Reason:

Competitor Promotion

Competitor:

Brookside

Probability:

High

Status:

Recovery Plan Active

---

Customer:

KMTC Mombasa

Reason:

Price

Competitor:

KCC

Probability:

Medium

Status:

Under Investigation

---

Customer:

Coast Distributor Ltd

Reason:

Service Issues

Probability:

Very High

Status:

Open

---

# Codex Instructions

Blueprint:

lost_accounts_bp

Model:

LostAccount

Template:

lost_accounts.html

Implement:

CRUD

Search

Filters

Pagination

Recovery Dashboard

Recovery Analysis

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Every Lost Account must belong to one Customer.

Every Lost Account must belong to one Channel.

Reason Category is mandatory.

Status is mandatory.

Recovery Probability is mandatory.

Records must not be deleted without confirmation.

Recovery calculations must use live database records.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED