# Expense Tracker API

## Project Description

The Expense Tracker API is a Django-based application that allows users to manage their expenses. Users can create, read, update, and delete (CRUD) expense records. The API also provides endpoints to list expenses within a specific date range and to summarize expenses by category for a given month.

### Features

- **User Management**: Simple user model with username and email.
- **Expense Management**: CRUD operations for managing expenses.
- **Date Range Filtering**: List expenses for a user within a specific date range.
- **Category Summary**: Calculate total expenses per category for a given month.
- **Validation**: Ensure expense amounts are positive.
- **API Documentation**: Interactive API documentation using Swagger.

## Setup Instructions

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt