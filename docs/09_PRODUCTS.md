# RAZCO PWANI™
# Products Module

---

## Purpose

The Products Module is the Product Intelligence Engine of RAZCO PWANI.

It manages the complete product portfolio and helps identify products that drive growth, profitability and market penetration.

The module provides visibility into product performance across territories, channels and customers.

---

# Business Objective

Answer the following questions:

- What products do we sell?
- Which products drive growth?
- Which products are underperforming?
- Which channels consume which products?
- Which territories have product gaps?
- Which products present opportunity for expansion?

---

# Database Table

products

---

# Fields

id

product_code

product_name

category

brand

unit_size

selling_price

status

notes

created_at

updated_at

---

# Product Status

Active

Inactive

Discontinued

Development

---

# Product Categories

Ice Cream

Yoghurt

Milk

Sauces

Bakery

Frozen Foods

Desserts

Beverages

Other

---

# Product Profile Screen

Display:

Product Code

Product Name

Category

Brand

Unit Size

Selling Price

Status

Notes

Created Date

Last Updated

---

# Product Dashboard Widgets

---

## Total Products

Example:

20

---

## Active Products

Example:

18

---

## Discontinued Products

Example:

2

---

## High Growth Products

Example:

6

---

## Products Needing Attention

Example:

4

---

# Product Performance Classification

Allow classification:

Star Product

Growth Product

Core Product

Seasonal Product

Declining Product

---

# Product Opportunity Analysis

Display:

Products with growth potential.

Examples:

- Hotel expansion opportunities
- School opportunities
- Distributor expansion opportunities
- Tourism season opportunities

---

# Product Coverage Analysis

Display:

Products by Territory

Products by Channel

Products by Customer Type

Purpose:

Identify distribution gaps.

---

# Product Search

Allow searching by:

Product Name

Product Code

Category

Brand

---

# Filters

Provide:

Category

Brand

Status

Territory

Channel

Date Created

---

# Product Reports

Generate:

Product Master Report

Product Portfolio Report

Products by Category

Products by Brand

Products by Channel

Products by Territory

Growth Products Report

Declining Products Report

---

# Export Options

PDF

Excel

CSV

Print View

---

# Charts

---

## Products by Category

Pie Chart

---

## Products by Brand

Bar Chart

---

## Product Status Distribution

Doughnut Chart

---

## Growth Product Analysis

Bar Chart

---

# Product Intelligence

Display:

Top Growth Products

Top Opportunity Products

Products with Weak Coverage

Products Requiring Promotion

Products Requiring Distribution Expansion

---

# Example Dummy Products

Ice Cream

- Vanilla Ice Cream
- Chocolate Ice Cream
- Strawberry Ice Cream

---

Yoghurt

- Yoghurt 250ml
- Yoghurt 500ml
- Drinking Yoghurt

---

Milk

- Fresh Milk 500ml
- Fresh Milk 1L
- UHT Milk 500ml
- UHT Milk 1L

---

Sauces

- Tomato Sauce
- Chilli Sauce
- Burger Sauce

---

Bakery

- Croissants
- Muffins
- Cake Mix

---

Frozen Foods

- Frozen Pastries
- Whipping Cream

---

# Product Growth Matrix

Display:

High Growth / High Volume

High Growth / Low Volume

Low Growth / High Volume

Low Growth / Low Volume

Purpose:

Prioritize focus products.

---

# Dashboard Integration

Dashboard should display:

Top Growth Products

Most Active Product Category

Product Opportunities

Products Requiring Attention

---

# Codex Instructions

Blueprint:

products_bp

Model:

Product

Template:

products.html

Implement:

CRUD

Search

Filters

Pagination

Product Profile Screen

Charts

Reports

Export Functions

Bootstrap 5

Chart.js

SQLAlchemy ORM

Responsive Design

---

# Development Rules

Product Name is mandatory.

Product Code must be unique.

Every Product must belong to a Category.

Discontinued products remain visible for historical reporting.

Products must not be deleted without confirmation.

---

# Version

RAZCO PWANI Version 1.0

---

# Status

LOCKED