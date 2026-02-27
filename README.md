# Robotic-Task-Scheduler-Command-Processing-Engine
📌 Overview

The Robotic Task Scheduler is a Python-based automation engine that manages and executes structured robotic movement commands using a database-driven task queue.

The system simulates robotic command processing in industrial automation environments by tracking task execution status, applying validation rules, and ensuring reliable processing through retry mechanisms.

This project demonstrates:

Automation workflow orchestration

SQL task queue design

JSON API development

Error handling and logging

System reliability engineering

🏗 System Architecture

Client (Postman)
⬇
Flask REST API
⬇
Task Queue Database
⬇
Execution Engine
⬇
Status Updates & Logs

⚙️ Features

Add robotic movement tasks

Queue-based execution engine

Status tracking (PENDING, RUNNING, COMPLETED, FAILED)

Retry mechanism for failed tasks

Boundary validation logic

Execution logging

🛠 Tech Stack

Python 3

Flask

SQLite

SQL Query Optimization

JSON Processing

📂 Database Schema
Table: tasks

id (Primary Key)

action

value

status

created_at
