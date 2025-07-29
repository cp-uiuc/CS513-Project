
# @begin PythonWorkflow
# @in dish_in
# @in menu_in
# @param soup_terms
# @out dish_out
# @out menu_out

import os
import pandas as pd

soup_terms = [
        "broth",
        "bouillon",
        "stock",
        "consommé",
        "chowder",
        "clam chowder",
        "corn chowder",
        "bisque",
        "seafood bisque",
        "stew",
        "ragout",
        "goulash",
        "soupe",
        "potage",
        "velouté",
        "sopa",
        "caldo",
        "guiso",
        "zuppa",
        "minestra",
        "minestrone",
        "sopas",
        "shorba",
        "chorba",
        "supu",
        "supă",
        "zeamă",
        "keitto",
        "zupa",
        "juha",
        "çorba",
        "supa",
        "tom yum",
        "tom kha",
        "pho",
        "canh",
        "miso",
        "shiru",
        "ramen",
        "udon",
        "borscht",
        "barszcz",
        "gazpacho",
        "menudo",
        "pozole",
        "avgolemono"
    ]

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_normalized_dish_name(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(subset=['normalized_dish_name'], inplace=True)
    df['normalized_dish_name'] = df['normalized_dish_name'].apply(lambda x: str(x).strip() if pd.notnull(x) else '')
    return df


def is_soup(dish_name: str, soup_terms: list[str]) -> bool:
    """
    Check if the dish name contains any soup-related keywords.
    """
    dish_lower = dish_name.lower()
    return any(term in dish_lower for term in soup_terms)


def update_is_soup_column(df: pd.DataFrame, soup_terms: list[str]) -> pd.DataFrame:
    df['isSoup'] = df['normalized_dish_name'].apply(lambda x: is_soup(str(x), soup_terms))
    return df

def print_dish_stats(label: str, df: pd.DataFrame):
    num_null = df['normalized_dish_name'].isnull().sum()
    num_empty = df['normalized_dish_name'].apply(lambda x: str(x).strip() == '').sum()
    soup_true = df['isSoup'].sum() if 'isSoup' in df.columns else 'N/A'
    soup_false = (df['isSoup'] == False).sum() if 'isSoup' in df.columns else 'N/A'
    print(f"[{label}] Nulls: {num_null}, Empty: {num_empty}, isSoup True: {soup_true}, isSoup False: {soup_false}")

def process_dish_file(in_path: str, out_path: str, soup_terms: list[str]):
    # @begin load_dish_csv
    # @in dish_in
    # @out dish_df
    df = load_csv(in_path)
    # @end load_dish_csv

    print_dish_stats("Dish (Pre-Clean)", df)

    num_null = df['normalized_dish_name'].isnull().sum()
    num_empty = df['normalized_dish_name'].apply(lambda x: str(x).strip() == '').sum()

    # @begin clean_normalized_dish_name
    # @in dish_df
    # @out dish_df_clean_1
    df = clean_normalized_dish_name(df)
    # @end clean_normalized_dish_name


    # @begin update_is_soup_column
    # @in dish_df_clean_1
    # @param soup_terms
    # @out dish_df_clean_2
    df = update_is_soup_column(df, soup_terms)
    # @end update_is_soup_column

    print_dish_stats("Dish (Post-Clean)", df)

    # @begin save_dish_csv
    # @in dish_df_clean_2
    # @out dish_out
    df.to_csv(out_path, index=False)
    # @end save_dish_csv

def process_menu_file(in_path: str, out_path: str):
    # @begin load_csv_menu
    # @in menu_in
    # @out menu_df
    df = load_csv(in_path)
    # @end load_csv_menu

    print(f"[Menu (Pre-Clean)] Invalid dates: {df['date'].isnull().sum()}")

    # @begin clean_menu_dates
    # @in menu_df
    # @out menu_df_clean
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df['date'] = df['date'].dt.strftime('%m/%d/%Y')
    # @end clean_menu_dates

    print(f"[Menu (Post-Clean)] Invalid dates: {df['date'].isnull().sum()}")
    
    # @begin save_csv_menu
    # @in menu_df_clean
    # @out menu_out
    df.to_csv(out_path, index=False)
    # @end save_csv_menu


if __name__ == "__main__":
    in_data_folder = "cleaned_data_a"
    out_data_folder = "cleaned_data_b"

    dish_in = os.path.join(in_data_folder, "Dish_clean.csv")
    dish_out = os.path.join(out_data_folder, "Dish_clean.csv")

    menu_in = os.path.join(in_data_folder, "Menu-clean.csv")
    menu_out = os.path.join(out_data_folder, "Menu-clean.csv")

    process_dish_file(dish_in, dish_out, soup_terms)

    process_menu_file(menu_in, menu_out)

# @end PythonWorkflow



