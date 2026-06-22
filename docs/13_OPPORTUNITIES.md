# RAZCO PWANI™
# Opportunities Module

---

## Purpose

The Opportunities Module is the Growth Pipeline Engine of RAZCO PWANI.

It captures, tracks and manages all revenue growth opportunities across the Coast Region.

The module provides visibility into future business, expansion opportunities and strategic growth initiatives.

---

# Business Objective

Answer the following questions:

- Where will growth come from?
- Which opportunities are active?
- What is the value of the pipeline?
- Which opportunities require action?
- Which opportunities are most likely to close?
- Are we on track to achieve growth targets?

---

# Database Table

opportunities

---

# Fields

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

# Opportunity Types

New Customer

New Product Listing

Range Expansion

Distributor Expansion

Contract Opportunity

Institution Tender

Hotel Listing

Shelf Space Expansion

Market Expansion

Account Recovery

---

# Opportunity Status

Open

Qualified

In Progress

Negotiation

Won

Lost

On Hold

---

# Priority Levels

Critical

High

Medium

Low

---

# Probability Levels

0%

25%

50%

75%

100%

---

# Opportunity Entry Form

Display:

Opportunity Code

Customer

Territory

Channel

Product Category

Opportunity Type

Title

Description

Estimated Value

Probability

Priority

Status

Owner

Source

Next Action

Target Close Date

Notes

---

# Opportunity Dashboard Widgets

---

## Total Opportunities

Example:

50

---

## Open Opportunities

Example:

20

---

## Won Opportunities

Example:

5

---

## Lost Opportunities

Example:

5

---

## Pipeline Value

Example:

KES 4,500,000

---

## Weighted Pipeline Value

Example:

KES 2,750,000

---

# Weighted Pipeline Formula

Estimated Value

×

Probability

=

Weighted Value

---

# Opportunity Scorecard

Display:

Opportunity Code

Customer

Value

Probability

Status

Priority

Target Close Date

Owner

---

# Opportunity Pipeline Stages

Open

↓

Qualified

↓

In Progress

↓

Negotiation

↓

Won

or

Lost

---

# Opportunity Intelligence

Display:

Highest Value Opportunity

Highest Probability Opportunity

Aging Opportunities

Quick Win Opportunities

Strategic Opportunities

---

# Opportunity Search

Allow Search By:

Opportunity Code

Customer

Title

Territory

Owner

---

# Filters

Provide:

Status

Priority

Channel

Territory

Opportunity Type

Probability

Owner

Date Range

---

# Charts

---

## Pipeline by Stage

Funnel Chart

---

## Pipeline by Channel

Bar Chart

---

## Pipeline by Territory

Bar Chart

---

## Opportunity Status Distribution

Pie Chart

---

## Monthly Opportunity Trend

Line Chart

---

# Opportunity Aging Analysis

Display:

0 - 30 Days

31 - 60 Days

61 - 90 Days

90+ Days

Purpose:

Identify stalled opportunities.

---

# Opportunity Sources

Display:

Visit

Competitor Activity

Lost Account

SWOT

Direct Prospecting

Referral

Management Initiative

---

# Opportunity Relationships

Opportunity

Belongs To:

Customer

Channel

Opportunity May Generate:

Action Plan

---

# Special Features

---

## Convert to Action Plan

Button:

Create Action Plan

---

## Mark as Won

Button:

Close Won

---

## Mark as Lost

Button:

Close Lost

---

## Schedule Follow-Up

Button:

Create Follow-Up Action

---

# Growth Forecast

Display:

Projected Revenue

Weighted Pipeline

Target Achievement %

Purpose:

Forecast growth performance.

---

# Reports

Generate:

Opportunity Pipeline Report

Pipeline Value Report

Won Opportunities Report

Lost Opportunities Report

Opportunity Aging Report

Opportunity Forecast Report

Growth Projection Report

Executive Opportunity Summary

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Pipeline Value

Open Opportunities

High Priority Opportunities

Opportunities Closing This Month

---

# Example Dummy Opportunities

Opportunity:

Whitesands Hotel

Type:

New Product Listing

Value:

KES 250,000

Status:

In Progress

---

Opportunity:

KMTC Mombasa

Type:

Institution Tender

Value:

KES 500,000

Status:

Qualified

---

Opportunity:

Naivas Nyali

Type:

Range Expansion

Value:

KES 150,000

Status:

Open

---

# Codex Instructions

Blueprint:

opportunities_bp

Model:

Opportunity

Template:

opportunities.html

Implement:

CRUD

Search

Filters

Pagination

Pipeline Dashboard

Opportunity Aging Analysis

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Every Opportunity must belong to one Customer.

Every Opportunity must belong to one Channel.

Estimated Value is mandatory.

Status is mandatory.

Probability must be numeric.

Opportunity Code must be unique.

Opportunities must not be deleted without confirmation.

Pipeline calculations must use live database records.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED