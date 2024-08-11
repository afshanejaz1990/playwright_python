# Fearless Tech Website Testing

This project contains automated tests for the Fearless Tech website using Playwright with Python.

## Project Structure
project_root/
│
├── pages/
│   ├── init.py
│   ├── home_page.py
│   ├── people_page.py
│   └── contact_page.py
│
├── tests/
│   ├── init.py
│   └── test_fearless_tech.py
│
├── conftest.py
└── pytest.ini

## Setup

1. Ensure you have Python 3.7+ installed.
2. Install the required packages: pytest-playwright
3. Install the Playwright browsers: chromium

## Running Tests

To run the tests, use the following command in the project root directory:
`pytest`

## Key Features

- Uses Page Object Model (POM) for better organization and maintenance.
- Implements fixtures for browser and page setup.
- Includes a custom fixture for common setup steps (navigating to home page and accepting consent).
- Verifies navigation and presence of key elements on the website.
- Demonstrates form filling and interaction with iframe elements.

## Test Cases

The main test file `test_fearless_tech.py` includes:

1. Verification of navigation menu items.
2. Navigation to the Contact page.
3. Filling out the contact form.

## Configuration

- The `pytest.ini` file contains configuration for running tests in headed mode.
- The `conftest.py` file sets up fixtures for browser, page, and initial navigation.

## Maintenance

To add new tests or page objects:

1. Create new page object files in the `pages/` directory if needed.
2. Add new test functions to `test_fearless_tech.py` or create new test files in the `tests/` directory.
3. Update fixtures in `conftest.py` if new common setup steps are required.