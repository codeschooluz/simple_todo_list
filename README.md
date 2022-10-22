# Software Requirements Specification for the TODO List Application

# Project Description
TODO list application is a simple application that allows users to create a list of tasks that they need to complete.
The application will allow users to add, edit, and delete tasks from their list. The application will also allow users to mark tasks as complete.

# Purpose
This is a SRS for the TODO list application. The purpose of this document is to provide a detailed description of the TODO list application and its requirements.

# Scope

This a simple TODO list application wtithout any complex features. 

# Features

- Add a task
- Edit a task
- Delete a task
- Mark a task as complete
- View all tasks
- View completed tasks
- View incomplete tasks

# Database Schema

The database schema for the TODO list application is as follows:

| Field | Type | Null | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id | int(11) | NO | PRI | NULL | auto_increment |
| task | varchar(255) | NO | | NULL | |
| status | tinyint(1) | NO | | 0 | |
| created_at | timestamp | NO | | CURRENT_TIMESTAMP | |
| updated_at | timestamp | NO | | CURRENT_TIMESTAMP | |


# User Interface
- The user interface will be a simple web application.

# User Interface Design

The user interface design for the TODO list application is as follows:


# List of Tasks

## 1. Create a virtual environment

- Create the requirements.txt file
- Create the virtual environment
- Create the .gitignore file

## 2. Create the Django project

- Create the Django project
- Create the Django app
- Create the database
- Create the models
- Create the views
- Create the templates
- Create the urls

## 3. Create the user interface

- Create the home page
- Create the add task page
- Create the edit task page
- Create the delete task page
- Create the complete task page
- Create the incomplete tasks page

## 4. Create the tests

- Create the tests
- Run the tests







