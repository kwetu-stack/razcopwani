# RAZCO PWANI™
# Action Plans Module

---

## Purpose

The Action Plans Module is the Execution Management Engine of RAZCO PWANI.

It captures, tracks and monitors all actions required to achieve business objectives, recover lost accounts, close opportunities, respond to competitor activities and execute strategic initiatives.

The module ensures that identified issues are converted into measurable actions.

---

# Business Objective

Answer the following questions:

- What actions are required?
- Who is responsible?
- When is the deadline?
- What progress has been made?
- Which actions are overdue?
- Which actions are delivering results?

---

# Database Table

action_plans

---

# Fields

id

action_code

title

description

source_module

source_record_id

territory

channel_id

priority

status

assigned_to

start_date

due_date

completion_date

progress_percent

expected_outcome

actual_outcome

notes

created_at

updated_at

---

# Source Modules

SWOT

Visit

Opportunity

Competitor Activity

Lost Account

Management Initiative

Direct Assignment

---

# Priority Levels

Critical

High

Medium

Low

---

# Status Values

Open

In Progress

Pending

Completed

Cancelled

Overdue

---

# Action Plan Entry Form

Display:

Action Code

Title

Description

Source Module

Source Record

Territory

Channel

Priority

Assigned To

Start Date

Due Date

Status

Progress %

Expected Outcome

Notes

---

# Action Plan Dashboard Widgets

---

## Total Actions

Example:

50

---

## Open Actions

Example:

20

---

## In Progress Actions

Example:

15

---

## Completed Actions

Example:

10

---

## Overdue Actions

Example:

5

---

## Completion Rate

Example:

78%

---

# Completion Formula

Completed Actions

÷

Total Actions

×

100

---

# Action Plan Scorecard

Display:

Action Code

Title

Priority

Assigned To

Due Date

Status

Progress %

---

# Execution Analysis

Display:

Most Active User

Highest Completion Rate

Critical Open Actions

Overdue Actions

Actions Closing This Week

---

# Action Search

Allow Search By:

Action Code

Title

Assigned Person

Territory

Source Module

---

# Filters

Provide:

Priority

Status

Assigned To

Territory

Channel

Source Module

Date Range

---

# Charts

---

## Actions by Status

Pie Chart

---

## Actions by Priority

Bar Chart

---

## Actions by Territory

Bar Chart

---

## Monthly Completion Trend

Line Chart

---

## Overdue Trend

Line Chart

---

# Action Workflow

Action Created

↓

Assigned

↓

In Progress

↓

Completed

or

Overdue

---

# Progress Tracking

Display:

0%

25%

50%

75%

100%

Purpose:

Monitor execution progress.

---

# Action Relationships

Action Plan

May Originate From:

SWOT

Visit

Opportunity

Competitor Activity

Lost Account

---

# Territory Execution Analysis

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

Track execution by territory.

---

# Channel Execution Analysis

Display:

General Trade

Modern Trade

HORECA

Institutions

Distributors

Purpose:

Track execution by channel.

---

# Special Features

---

## Mark Complete

Button:

Complete Action

---

## Update Progress

Button:

Update Progress

---

## Add Follow-Up Notes

Button:

Add Note

---

## Convert to Opportunity

Button:

Create Opportunity

Where applicable.

---

# Executive Review Section

Display:

Critical Actions

Overdue Actions

High Priority Actions

Actions Due This Week

Purpose:

Management visibility.

---

# Reports

Generate:

Action Plan Report

Open Actions Report

Completed Actions Report

Overdue Actions Report

Execution Report

Territory Execution Report

Channel Execution Report

Executive Action Summary

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Open Actions

Overdue Actions

Completion %

Critical Actions

Recent Updates

---

# Example Dummy Records

Action:

Recover Whitesands Hotel

Priority:

High

Status:

In Progress

Progress:

50%

---

Action:

Follow Up KMTC Tender

Priority:

Critical

Status:

Open

Progress:

0%

---

Action:

Respond to Brookside Promotion

Priority:

High

Status:

Completed

Progress:

100%

---

# Codex Instructions

Blueprint:

action_plans_bp

Model:

ActionPlan

Template:

action_plans.html

Implement:

CRUD

Search

Filters

Pagination

Progress Tracking

Execution Dashboard

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Action Code must be unique.

Title is mandatory.

Priority is mandatory.

Status is mandatory.

Assigned Person is mandatory.

Progress must be between 0 and 100.

Records must not be deleted without confirmation.

Completion calculations must use live database records.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED