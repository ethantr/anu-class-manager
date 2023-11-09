# anu-class-manager

ANU Class Manager is a Python application for scraping and managing class information for Australian National University (ANU) courses.
The original purpose was to have a simple command for easy and quick access of class information for enrollment.

## Features

- Web scraping of class information for ANU courses.
- Find class numbers for quick enrollment.
- Data storage in CSV format.
- Easy-to-use command-line interface.
- Data caching to avoid repeated scraping.


## Getting Started

### Prerequisites

Before using ANU Class Manager, ensure you have the following installed:

- Python 3.x
- Chrome web browser
You can choose to create a virtual environment, or setup directly.

### Create a virtual environment (optional)
python -m venv myenv

### Activate the virtual environment (Windows)
myenv\Scripts\activate

### Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

## Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

- Open a terminal in the project directory.
- Run the application with your desired ANU course name and, optionally, the academic year:
```bash
  python main.py COURSE_NAME --year YEAR
```  
Example:

```bash

  python main.py ASTR1001 --year 2023
```
This example will find the class numbers for the course ASTR1001, for the year 2023.
The application will scrape class information from the ANU website and save it in a CSV file in the data directory.



**Disclaimer:** The data obtained by this project is sourced from the Australian National University (ANU) website and is not owned by the author. This project is intended for educational and demonstrative purposes and does not claim ownership of the data. If required, please contact me and I can remove this from GitHub.
