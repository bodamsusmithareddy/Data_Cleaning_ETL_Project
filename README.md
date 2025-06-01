
# Data Cleaning & ETL Project (CSV → Postgres)

## Project Overview

This project demonstrates a simple but production-style **ETL pipeline**:

Extract raw data from CSV  
Clean and transform data (remove nulls, fix casing, deduplicate)  
Load cleaned data into a **Postgres database**  

## Tech Stack

- Python 3.9+
- Pandas
- SQLAlchemy
- PostgreSQL
- Jupyter Notebook

## Project Structure

```
├── data/
├── python files/
├── sql/
├── src/
└── README.md
```

## How to Run

1️ Create virtualenv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2️ Run ETL script:

```bash
python src/etl.py
```

3️ Open notebook:

```bash
jupyter notebook notebooks/data_cleaning.ipynb
```

## Database Schema

```sql
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE
);
```

## Author

Built as part of my Data Engineering Learning by Susmitha Reddy Bodam.
