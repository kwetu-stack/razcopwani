# RAZCO PWANI™
# UI Theme Guide

---

## Purpose

Define the official visual identity for RAZCO PWANI Version 1.0.

All screens, pages, dashboards, reports and modules must follow this document.

This document is the single source of truth for UI design.

---

# Design Philosophy

RAZCO PWANI is a management operating system.

The design must feel:

- Professional
- Executive
- Operational
- Clean
- Modern
- Data Driven

The interface should help users make decisions quickly.

Avoid:

- Bright colors
- Cluttered layouts
- Excessive animations
- Fancy visual effects
- Unnecessary widgets

---

# Official Theme

RAZCO PWANI uses the official Kwetu Operations Center theme.

The objective is operational efficiency rather than executive presentation.

The interface must support daily field management, customer management, opportunity tracking and action execution.

The system should visually align with:

- Inventa™
- QikSend-X™
- SiteManager360™
- Juris360™

Users should immediately recognize RAZCO PWANI as a member of the Kwetu software family.

---

# Theme Identity

Style:

Kwetu Operations Center

Characteristics:

- Dark Navy Navbar
- White Data Cards
- Light Gray Background
- Cyan Action Colors
- Large KPI Cards
- Simple Charts
- Readable Tables
- Minimal Animations

Avoid:

- Generic Bootstrap Admin Templates
- Bright Corporate Colors
- Overly Complex Dashboards
- Heavy Visual Effects

---

# Design Inspiration

Kwetu Management Systems

Characteristics:

- Dark Navigation
- Executive KPI Cards
- Operational Workflows
- Large Data Tables
- Fast Data Entry
- Mobile Friendly

---

# Color Palette

## Primary Navbar

```css
#0f172a
```

Dark Navy

---

## Secondary Navbar Surface

```css
#1e293b
```

Slate Navy

---

## Page Background

```css
#f8fafc
```

Light Gray

---

## Card Background

```css
#ffffff
```

White

---

## Primary Accent

```css
#22d3ee
```

Kwetu Cyan

---

## Secondary Accent

```css
#38bdf8
```

Sky Blue

---

## Text Primary

```css
#0f172a
```

---

## Text Secondary

```css
#64748b
```

---

## Success

```css
#16a34a
```

Green

---

## Warning

```css
#f59e0b
```

Amber

---

## Danger

```css
#dc2626
```

Red

---

# Typography

Primary Font:

```css
Inter
```

Fallback:

```css
Arial, sans-serif
```

---

# Layout Structure

Top Navbar

↓

Page Header

↓

KPI Summary Cards

↓

Charts

↓

Filters

↓

Data Tables

↓

Reports

---

# Navbar

Background:

```css
#0f172a
```

Text:

```css
#E2E8F0
```

Hover:

```css
#38bdf8
```

Height:

```css
64px
```

Position:

Fixed Top

Brand:

```text
RAZCO PWANI™
```

Subtitle:

```text
Coast Growth Management System
```

---

# Dashboard Cards

Style:

Rounded

```css
border-radius:16px;
```

Shadow:

```css
box-shadow:0 2px 10px rgba(0,0,0,0.08);
```

Padding:

```css
24px
```

Display:

- KPI Value
- KPI Label
- Trend Indicator

---

# KPI Cards

Examples:

- Growth %
- Coverage %
- Open Opportunities
- Lost Accounts
- Recovery Rate
- Action Completion %

Cards should be large and easy to read.

---

# Tables

Requirements:

- Bootstrap Responsive Tables
- Searchable
- Sortable
- Pagination
- Export Friendly

Row Hover:

```css
#f1f5f9
```

---

# Forms

Requirements:

- Consistent spacing
- Bootstrap styling
- Validation messages
- Mobile responsive

Form Labels:

Bold

Required Fields:

Clearly marked

---

# Buttons

Primary

```css
#22d3ee
```

Secondary

```css
#64748b
```

Success

```css
#16a34a
```

Danger

```css
#dc2626
```

Warning

```css
#f59e0b
```

---

# Status Badges

Open

Blue

In Progress

Orange

Completed

Green

Closed

Gray

Critical

Red

---

# Charts

Library:

Chart.js

Approved Charts:

- Line Chart
- Bar Chart
- Pie Chart
- Doughnut Chart

Not Allowed:

- 3D Charts
- Animated Charts
- Complex Visualizations

Charts should communicate information quickly.

---

# Dashboard Rules

Dashboard must contain:

- KPI Cards
- Charts
- Recent Activities
- Quick Insights

Dashboard must NOT contain:

- Data Entry Forms
- Long Tables
- Configuration Screens

---

# Page Rules

Every module page must contain:

- Page Header
- Search
- Filters
- Data Table
- CRUD Actions

Preferred Layout:

Header
↓
KPIs
↓
Filters
↓
Table
↓
Reports

---

# Mobile Responsiveness

Mandatory.

Supported Devices:

- Mobile Phones
- Tablets
- Laptops
- Desktops

Use Bootstrap 5 Responsive Grid.

Use Hamburger Menu on Mobile.

---

# Footer

Display:

```text
RAZCO PWANI™ Version 1.0
```

---

# Branding Rules

Always display:

```text
RAZCO PWANI™
```

Never abbreviate the application name.

Do not introduce additional branding.

---

# Development Rules

Codex must follow this document exactly.

Do not introduce:

- Alternative Themes
- Alternative Color Schemes
- Dark Mode
- Admin Template Themes

Use only the Kwetu Operations Center Theme.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED