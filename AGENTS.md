# AGENTS

# Civic Pulse Agent Architecture

## Overview

Civic Pulse uses multiple logical agents/modules that work together to process civic complaints and generate insights.

---

## Agent 1: Complaint Collection Agent

### Responsibilities

* Receive complaints from users.
* Validate submitted data.
* Store complaint information.

### Inputs

* Complaint Description
* Category
* Location

### Outputs

* Structured Complaint Record

---

## Agent 2: Classification Agent

### Responsibilities

* Analyze complaint text.
* Identify issue category.
* Assign classification label.

### Outputs

* Water Supply
* Electricity
* Roads
* Garbage
* Traffic
* Public Safety

---

## Agent 3: Duplicate Detection Agent

### Responsibilities

* Compare incoming complaints.
* Detect similar reports.
* Merge duplicate complaints.

### Outputs

* Unique Complaint Groups

---

## Agent 4: Analytics Agent

### Responsibilities

* Calculate complaint statistics.
* Identify trends.
* Generate priority scores.

### Outputs

* Complaint Metrics
* Trend Reports
* Priority Rankings

---

## Agent 5: Visualization Agent

### Responsibilities

* Generate heatmaps.
* Create charts and dashboards.
* Display hotspot locations.

### Outputs

* Interactive Maps
* Graphs
* Dashboard Views

---

## Team Responsibilities

### Member 1 – Project Lead

* Integration
* Testing
* Coordination

### Member 2 – Data Engineer

* Data Collection
* Database Management

### Member 3 – AI Engineer

* Classification Logic
* Duplicate Detection

### Member 4 – Frontend Developer

* Streamlit Interface
* User Experience

### Member 5 – Visualization & Documentation

* Dashboard Development
* Documentation
* Presentation

---

## Workflow

Complaint Submission
↓
Collection Agent
↓
Classification Agent
↓
Duplicate Detection Agent
↓
Analytics Agent
↓
Visualization Agent
↓
Dashboard & Heatmap