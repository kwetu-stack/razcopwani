# RAZCO PWANI™
# Dashboard Module

---

## Purpose

The Dashboard is the command center of RAZCO PWANI.

It provides a real-time summary of business performance, growth opportunities, field execution and management priorities.

The Dashboard must answer:

- What is happening?
- Are we on target?
- Where are the risks?
- Where are the opportunities?
- What actions require attention?

---

# Dashboard Objectives

Provide:

- Business Visibility
- Performance Monitoring
- Growth Tracking
- Opportunity Monitoring
- Action Tracking

The Dashboard must load immediately after login.

---

# KPI Cards

Display at top of dashboard.

---

## Sales Growth %

Example:

18%

Target:

25%

---

## Coverage %

Example:

84%

Definition:

Completed Visits ÷ Planned Visits

---

## Open Opportunities

Example:

35

---

## Pipeline Value

Example:

KES 4,500,000

---

## Lost Accounts

Example:

12

---

## Action Completion %

Example:

78%

---

# Dashboard Layout

Top Navigation

↓

Page Header

↓

KPI Cards

↓

Charts Row

↓

Insights Row

↓

Recent Activities

↓

Quick Actions

---

# KPI Card Design

Each KPI Card contains:

- Title
- Value
- Trend Indicator
- Icon

Style:

Large Cards

Rounded Corners

Shadow

---

# Charts Section

---

## Sales Trend

Type:

Line Chart

Period:

12 Months

Purpose:

Track sales growth trend.

---

## Channel Contribution

Type:

Pie Chart

Purpose:

Show sales contribution by channel.

Channels:

- General Trade
- Modern Trade
- HORECA
- Institutions
- Distributors

---

## Opportunity Pipeline

Type:

Bar Chart

Purpose:

Display opportunities by stage.

Stages:

- Open
- Qualified
- In Progress
- Won
- Lost

---

## Visit Performance

Type:

Bar Chart

Purpose:

Completed vs Planned Visits

---

# Dashboard Insights

Display:

---

## Fastest Growing Channel

Example:

HORECA +31%

---

## Highest Opportunity Territory

Example:

Nyali

---

## Most Active Competitor

Example:

Brookside

---

## Largest Lost Account

Example:

Whitesands Hotel

---

# Recent Activities

Display latest:

- Visits
- Opportunities
- Competitor Activities
- Action Plans

Limit:

10 records

---

# Quick Actions

Provide buttons:

- New Visit
- New Opportunity
- New Competitor Activity
- New Action Plan

---

# Alerts Section

Display:

---

## Overdue Actions

High Priority

---

## Missed Visits

Current Week

---

## Aging Opportunities

Over 60 Days

---

## Lost Accounts Requiring Recovery

High Probability

---

# Filters

Dashboard Filters:

- Date Range
- Territory
- Channel

---

# Dashboard Calculations

Coverage %

=

Completed Visits ÷ Planned Visits

---

Action Completion %

=

Completed Actions ÷ Total Actions

---

Pipeline Value

=

Sum of Open Opportunity Values

---

# Reports Accessible

Dashboard should provide links to:

- Monthly Review
- Opportunity Report
- Visit Report
- Competitor Report
- Recovery Report

---

# Codex Instructions

Blueprint:

dashboard_bp

Template:

dashboard.html

Implement:

KPI Cards

Chart.js Charts

Recent Activities

Quick Actions

Alerts

Filters

Responsive Design

Bootstrap 5

SQLAlchemy Queries

Use Dummy Data from seed.py

---

# Development Rules

Dashboard contains:

KPIs

Charts

Insights

Activities

Alerts

Dashboard does NOT contain:

CRUD Forms

Long Tables

Configuration Screens

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED