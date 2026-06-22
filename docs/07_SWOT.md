# RAZCO PWANI™
# SWOT Module

---

## Purpose

The SWOT Module is the Strategic Intelligence Engine of RAZCO PWANI.

It captures and manages:

- Strengths
- Weaknesses
- Opportunities
- Threats

affecting Coast Region business performance.

The SWOT Module provides structured strategic thinking and supports decision making.

---

# Business Objective

Answer the following questions:

- What are we doing well?
- What are we doing poorly?
- Where are growth opportunities?
- What risks threaten growth?

---

# SWOT Categories

---

## Strengths

Internal advantages.

Examples:

- Strong customer relationships
- Strong distributor network
- Good brand recognition
- Experienced sales team

---

## Weaknesses

Internal limitations.

Examples:

- Limited freezer coverage
- Poor route coverage
- Product availability issues
- Slow response times

---

## Opportunities

External growth possibilities.

Examples:

- Tourism growth
- Hotel expansion
- New schools opening
- Competitor stock-outs

---

## Threats

External risks.

Examples:

- Aggressive competitor promotions
- Rising operating costs
- New market entrants
- Economic slowdown

---

# Database Table

swot

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

# Category Values

Strength

Weakness

Opportunity

Threat

---

# Priority Values

Critical

High

Medium

Low

---

# Status Values

Open

Monitoring

Action Taken

Closed

---

# SWOT Entry Form

Fields:

Category

Title

Description

Territory

Channel

Priority

Status

Owner

---

# SWOT Dashboard Widgets

Display:

---

## Total Strengths

Example:

25

---

## Total Weaknesses

Example:

14

---

## Total Opportunities

Example:

32

---

## Total Threats

Example:

18

---

# SWOT Summary Chart

Type:

Doughnut Chart

Display:

Strengths

Weaknesses

Opportunities

Threats

---

# SWOT Trend Chart

Type:

Line Chart

Purpose:

Track SWOT entries over time.

---

# Territory SWOT Analysis

Display SWOT entries grouped by territory.

Example:

Nyali

Mtwapa

Kilifi

Malindi

Diani

---

# Channel SWOT Analysis

Display SWOT entries grouped by:

General Trade

Modern Trade

HORECA

Institutions

Distributors

---

# SWOT Matrix View

Display:

| Strengths | Weaknesses |
|------------|------------|
| Item | Item |

| Opportunities | Threats |
|---------------|----------|
| Item | Item |

Purpose:

Executive strategic review.

---

# Special Feature

Create Action Plan

Every SWOT entry should include:

Button:

Create Action Plan

Purpose:

Convert strategy into execution.

---

# Workflow

SWOT Entry

↓

Action Plan

↓

Execution

↓

Result

---

# Search

Enable:

Keyword Search

---

# Filters

Provide:

Category

Territory

Channel

Priority

Status

Owner

Date Range

---

# Reports

Generate:

SWOT Summary Report

SWOT by Territory

SWOT by Channel

SWOT Opportunities Report

SWOT Threat Report

Strategic Review Report

---

# Export Options

PDF

Excel

CSV

Print View

---

# Dashboard Integration

Dashboard should display:

Top Opportunities

Critical Threats

Recent SWOT Entries

---

# Example Dummy Entries

Strength:

Strong relationships with hotels.

---

Weakness:

Insufficient freezer placement.

---

Opportunity:

New hotels opening in Diani.

---

Threat:

Competitor discount campaign.

---

# Codex Instructions

Blueprint:

swot_bp

Model:

Swot

Template:

swot.html

Implement:

CRUD

Search

Filters

Pagination

SWOT Matrix View

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Every SWOT entry must belong to one category.

Every SWOT entry may generate an Action Plan.

No SWOT entry should be deleted without confirmation.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED