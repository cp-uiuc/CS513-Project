# CS513-Project: Data Cleaning Script

## Overview
This script processes and cleans dish and menu data files. It identifies soup-related dishes and formats menu dates.

## Requirements
- Python 3.x
- Pandas library

Install dependencies:
```sh
pip install pandas
```

## File Structure
- `python_cleaning.py`: Main script.
- `cleaned_data_a/`: Input data folder.
  - `Dish_clean.csv`
  - `Menu-clean.csv`
- `cleaned_data_b/`: Output data folder (created after running the script).

## How to Run
1. Place input files (`Dish_clean.csv` and `Menu-clean.csv`) in the `cleaned_data_a/` folder.
2. Run the script:
```sh
python3 python_cleaning.py
```
3. Check the cleaned files in the `cleaned_data_b/` folder.

## Output
- `Dish_clean.csv`: Processed dish data with a new `isSoup` column.
- `Menu-clean.csv`: Menu data with cleaned and formatted dates.