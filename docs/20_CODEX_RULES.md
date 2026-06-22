# RAZCO PWANI™
# CODEX DEVELOPMENT RULES

---

## Purpose

This document defines the mandatory development rules that Codex must follow when building RAZCO PWANI.

These rules are not suggestions.

They are requirements.

Codex must obey them throughout development.

---

# Development Philosophy

RAZCO PWANI follows the Kwetu Development Method.

Human Experience
↓
Documentation
↓
Architecture
↓
Implementation
↓
Testing
↓
Deployment

Codex is an implementation tool.

Codex is not responsible for business decisions.

Business decisions are defined in the project documentation.

---

# ZERO PATCH WORKFLOW

The application must follow:

Download
↓
Extract
↓
Open In VS Code
↓
Install Requirements
↓
Run

The application must work without manual fixes.

The application must work without code patches.

The application must work without missing files.

The application must work without developer intervention.

---

# PRIMARY RULE

No patching.

If architecture is wrong:

Stop.

Fix architecture.

Regenerate cleanly.

Never stack patches on top of patches.

---

# Technology Stack

Backend:

Flask

ORM:

SQLAlchemy

Database:

SQLite

Future Support:

PostgreSQL

Frontend:

Bootstrap 5

Charts:

Chart.js

Reporting:

Pandas

Excel Export:

OpenPyXL

Environment Variables:

python-dotenv

---

# Forbidden Technologies

Do NOT use:

Django

FastAPI

React

Vue

Angular

Redis

Celery

Docker

Microservices

External APIs

Complex JavaScript Frameworks

---

# Application Structure

Must follow:

02_FOLDER_STRUCTURE.md

Exactly.

Do not invent new folders.

Do not rename folders.

Do not move folders.

---

# Database Rules

Must follow:

03_DATABASE_SCHEMA.md

Exactly.

Do not:

- Add tables
- Remove tables
- Rename fields
- Rename tables

without documentation updates.

---

# Relationship Rules

Must follow:

04_MODEL_RELATIONSHIPS.md

Exactly.

Use:

db.ForeignKey()

db.relationship()

Avoid circular imports.

---

# Navigation Rules

Must follow:

05_NAVBAR_STRUCTURE.md

Exactly.

Menu order is locked.

Do not reorder navigation.

---

# UI Rules

Must follow:

19_UI_THEME.md

Exactly.

Use:

Kwetu Operations Center Theme

Do not use:

Generic Admin Templates

Do not use:

Alternative Color Schemes

---

# CRUD Rules

Every module must provide:

Create
Read
Update
Delete

Without exception.

---

# Search Rules

Every module must provide:

Search

Where applicable.

---

# Filter Rules

Every module must provide:

Filters

Where applicable.

---

# Pagination Rules

Large tables must support pagination.

---

# Export Rules

Where applicable provide:

PDF

Excel

CSV

Print View

---

# Dummy Data Rules

System must include seed data.

Application must demonstrate functionality immediately after startup.

Empty screens are not allowed.

---

# Error Handling Rules

Provide:

404 Page

500 Page

Graceful Validation Errors

No raw Flask tracebacks visible to users.

---

# Security Rules

Use:

Flask-WTF

CSRF Protection

Input Validation

Parameterized Queries

SQLAlchemy ORM

Never use raw SQL where ORM can be used.

---

# Configuration Rules

Use:

.env

Provide:

.env.example

Never hardcode:

Passwords

Secrets

Connection Strings

---

# Code Quality Rules

No TODO comments.

No placeholder functions.

No unfinished pages.

No dead code.

No unused imports.

No duplicate files.

---

# Documentation Rules

Documentation is the source of truth.

If documentation conflicts with generated code:

Documentation wins.

---

# Performance Rules

Avoid:

N+1 Queries

Duplicate Queries

Unnecessary Database Calls

Use:

SQLAlchemy Relationships

Efficient Querying

---

# Mobile Responsiveness

Mandatory.

Must support:

Mobile

Tablet

Laptop

Desktop

---

# Naming Rules

Use:

snake_case

Examples:

customer_id

route_name

opportunity_code

Avoid inconsistent naming.

---

# Route Rules

Do not invent routes.

Use only documented routes.

Route naming must remain consistent.

---

# Reporting Rules

Reports must query live database records.

Reports must not use hardcoded values.

---

# Testing Rules

Before completion verify:

Application Starts

Database Creates

Seed Data Loads

Navigation Works

CRUD Works

Search Works

Filters Work

Exports Work

No Errors

---

# Completion Rule

A module is complete only when:

CRUD Works

Search Works

Filters Work

Pagination Works

Responsive Layout Works

No Errors Exist

---

# Final Acceptance Checklist

Application starts successfully.

No missing templates.

No missing imports.

No missing models.

No broken links.

No console errors.

No manual fixes required.

No patches required.

---

# Golden Rule

If something fails:

Do not patch.

Return to architecture.

Fix correctly.

Regenerate cleanly.

---

# Development Authority

Business Authority:

Harun

Architecture Authority:

Project Documentation

Implementation Authority:

Codex

---

# Version

RAZCO PWANI Version 1.0

---

# Status# Role Based Access Control (RBAC)

System must implement:

Administrator
User

Administrator:
Full CRUD Access

User:
Read Only Access

All permissions must be enforced:

Frontend
AND
Backend

Never rely on hidden buttons alone.

Unauthorized actions must return:

403 Forbidden

# First Login Rule

On first login, Administrator must be able to change password.

Default credentials exist only for initial setup.

Password hashes must be stored using Werkzeug security functions.

Never store plaintext passwords.



LOCKED