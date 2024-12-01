import pandas as pd

# Load country codes and historical matches data
country_codes = pd.read_csv("country_codes.csv")
matches_data = pd.read_csv("results.csv")

# Filter countries whose names are spelled by concatenated FIFA codes
def find_full_name_matches(country_codes, code_type):
    codes = country_codes[code_type].tolist()
    countries = country_codes["Country"].tolist()
    matches = []
    for i, code1 in enumerate(codes):
        for j, code2 in enumerate(codes):
            if i != j:  # Exclude matches against itself
                scoreline = code1 + code2
                for country in countries:
                    if scoreline.lower() == country.lower():
                        matches.append((country, code1, code2, scoreline))
    return pd.DataFrame(matches, columns=["Country", "Code1", "Code2", "Scoreline"])

# Find full name matches for FIFA codes
full_name_fifa = find_full_name_matches(country_codes, "FIFA")

# Merge FIFA codes with the matches data
country_fifa_mapping = country_codes[["Country", "FIFA"]].rename(columns={"Country": "team", "FIFA": "code"})
matches_data = matches_data.merge(country_fifa_mapping, left_on="home_team", right_on="team", how="left").rename(columns={"code": "home_code"})
matches_data = matches_data.merge(country_fifa_mapping, left_on="away_team", right_on="team", how="left").rename(columns={"code": "away_code"})

# Generate the "scoreline" by concatenating the FIFA codes
matches_data["scoreline"] = matches_data["home_code"] + matches_data["away_code"]

# Filter matches where the scoreline matches a country's full name
historical_matches = matches_data[matches_data["scoreline"].isin(full_name_fifa["Scoreline"].values)]

# Print the resulting DataFrame
print(historical_matches)

historical_matches.to_csv("historical_scoreboards.csv")

def dataframe_to_scrollable_table(df, max_height=300):
    html_table = df.to_html(index=False, escape=False)  # Generate HTML table without escaping content
    scrollable_html = f"""
    <div style="max-height: {max_height}px; overflow-y: auto; border: 1px solid #ccc;">
        {html_table}
    </div>
    """
    return scrollable_html

# Example usage with a DataFrame (replace `historical_matches` with your DataFrame)
scrollable_table = dataframe_to_scrollable_table(historical_matches)

# Save to a markdown file
with open("table.md", "a") as file:
    file.write("\n## Historical Matches with FIFA Scoreline Condition\n")
    file.write(scrollable_table)