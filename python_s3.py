
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

def is_soup(dish_name: str, soup_terms: list[str]) -> bool:
    """
    Check if the dish name contains any soup-related keywords.
    """
    dish_lower = dish_name.lower()
    return any(term in dish_lower for term in soup_terms)

def load_and_clean(in_file_path, out_path, soup_terms: list[str]):
    df = pd.read_csv(in_file_path)

    num_null = df['normalized_dish_name'].isnull().sum()
    print(f"Number of null normalized_dish_name: {num_null}")

    num_empty = df['normalized_dish_name'].apply(lambda x: str(x).strip() == '').sum()
    print(f"Number of empty normalized_dish_name: {num_empty}")

    df.dropna(subset=['normalized_dish_name'], inplace=True)
    df['normalized_dish_name'] = df['normalized_dish_name'].apply(lambda x: str(x).strip() if pd.notnull(x) else '')

    # Create new column: IsSoup (True/False)
    df['IsSoup'] = df['normalized_dish_name'].apply(lambda x: is_soup(str(x), soup_terms))
    df.to_csv(out_path, index=False)
    return df


if __name__ == "__main__":
    in_data_folder = "s2a_cleaned_data"
    out_data_folder = "s2b_cleaned_data"
    file_name = "Dish_clean.csv"
    in_path = os.path.join(in_data_folder, file_name)
    out_path = os.path.join(out_data_folder, file_name)

    cleaned_df = load_and_clean(in_path, out_path, soup_terms)
    print(f"Count of isSoup True: {cleaned_df['IsSoup'].sum()}")
    print(f"Count of isSoup False: {(cleaned_df['IsSoup'] == False).sum()}")
