# FIFA Scoreline Trivia Analysis

This repository explores a quirky piece of football trivia: when the abbreviations of two international football teams' FIFA codes combine to spell the full name of a country. We analyse historical football matches to identify and highlight these rare occurrences.

## Project Overview

### Objective
To identify historical matches where the concatenated FIFA codes of the home and away teams spell out the name of a country, and to explore the occurrence of such matches in the history of international football.

### Key Findings
- Some country names (e.g., **SWEDEN**, **CYPRUS**, **POLAND**, **BHUTAN**) can be formed by combining the FIFA codes of two playing teams.
- Historical matches, such as Sweden (SWE) vs. Denmark (DEN), resulted in the scoreline spelling **SWEDEN**.
- However, **Bhutan (BHU)** and **Tanzania (TAN)**—which spell **BHUTAN**—have *never* faced each other in recorded history. (#TANtoThimphu)
- **Cyprus (CYP)** - **Russia (RUS)** (**CYP-RUS**) and **Poland (POL)** - **Andorra (AND)** (**POL-AND**) have both occurred in World Cup qualification rounds.
- The country whose name is spelled out is always at home (sad times).
- Countries whose names are shorter than 6 characters are common enough to make this trivial and boring (looking at you Cuba and any country starting with A...)

---

## Methodology

1. **Data Sources**
   - **`country_codes.csv`**: List of all FIFA-recognised countries, their FIFA and IOC codes, and regions.
   - **`results.csv`**: Historical dataset of international football matches, including dates, teams, and scores.

2. **Analysis Steps**
   - Identified country names that can be spelled using the FIFA codes of two teams (e.g., SWE + DEN = SWEDEN).
   - Mapped FIFA codes to historical match data and generated "scorelines" by concatenating home and away FIFA codes.
   - Filtered matches where the scoreline matched a country name.
   - Highlighted Bhutan vs. Tanzania as the only potential scoreline country (**BHUTAN**) without a historical match.

---

## Repository Contents

- **`country_codes.csv`**: Dataset of countries and their codes.
- **`results.csv`**: Historical match data.
- **`analysis.py`**: Python script to:
  - Identify full names formed by FIFA codes.
  - Analyse historical matches for these conditions.
  - Output matches where the condition is met.
- **`README.md`**: Project summary and instructions.

---

## How to Run the Analysis

1. **Clone the Repository**  
   Run the following commands in your terminal:
   ```bash
   git clone https://github.com/jamieagraham/FIFA-Redundant-Scoreboards.git
   cd FIFA-Redundant-Scoreboards
   ```

2. **Install Dependencies**  
   Ensure you have Python 3.x and `pandas` installed:
   ```bash
   pip install pandas
   ```

3. **Run the Script**  
   Execute the analysis script:
   ```bash
   python parse_data.py
   python historical_frequency.py
   ```
   The script will output a list of matches where the scoreline spells out a country's name.

---

## Acknowledgements

Thanks to [FIFA](https://www.fifa.com/) and other public datasets (most notably [this Kaggle dataset](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017/data?select=results.csv) and the [Rec.Sport.Soccer Statistics Foundation](https://www.rsssf.org/miscellaneous/fifa-codes.html)) for providing the necessary data to make this project possible.


## Historical Matches with FIFA Scoreline Condition

<div style="overflow-x: auto;">
  <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>date</th>
      <th>home_team</th>
      <th>away_team</th>
      <th>home_score</th>
      <th>away_score</th>
      <th>tournament</th>
      <th>city</th>
      <th>country</th>
      <th>neutral</th>
      <th>team_x</th>
      <th>home_code</th>
      <th>team_y</th>
      <th>away_code</th>
      <th>scoreline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1913-10-05</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>10</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1915-10-31</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1916-10-08</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1917-10-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1918-10-20</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1919-10-12</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1920-10-10</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1921-10-09</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1923-10-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>3</td>
      <td>Friendly</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1925-06-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1927-06-19</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1929-06-16</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1931-06-28</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1933-06-18</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>3</td>
      <td>Nordic Championship</td>
      <td>Stockholm</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1935-06-16</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1937-10-03</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1939-10-01</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1940-10-06</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1941-09-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1942-10-04</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1945-06-24</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1945-09-30</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1946-10-06</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>3</td>
      <td>Friendly</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1947-06-26</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>6</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1948-10-10</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1950-10-15</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1952-06-22</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>3</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1954-10-10</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>5</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1956-10-21</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1958-10-26</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>4</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1960-10-23</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1962-10-28</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1964-06-28</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1966-11-06</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1968-06-27</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1970-06-25</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1970-11-15</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>1</td>
      <td>3</td>
      <td>UEFA Euro qualification</td>
      <td>Nicosia</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
    <tr>
      <td>1972-06-29</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1975-09-25</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>0</td>
      <td>Nordic Championship</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1976-05-11</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1977-10-05</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1980-05-07</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>1</td>
      <td>Nordic Championship</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1981-05-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Nordic Championship</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1984-06-06</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1987-08-26</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1988-08-31</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>2</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1990-09-05</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>1</td>
      <td>Friendly</td>
      <td>V�ster�s</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1991-06-15</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>4</td>
      <td>0</td>
      <td>Scania 100 Tournament</td>
      <td>Norrk�ping</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1991-11-13</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>0</td>
      <td>3</td>
      <td>UEFA Euro qualification</td>
      <td>Larnaca</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
    <tr>
      <td>1992-06-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>1</td>
      <td>0</td>
      <td>UEFA Euro</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1996-08-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>1</td>
      <td>Friendly</td>
      <td>Gothenburg</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>1997-03-29</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>1</td>
      <td>1</td>
      <td>FIFA World Cup qualification</td>
      <td>Paral�mni</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
    <tr>
      <td>1998-05-28</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>3</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Malm�</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>2003-02-12</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>0</td>
      <td>1</td>
      <td>Cyprus International Tournament</td>
      <td>Limassol</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
    <tr>
      <td>2007-09-08</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>0</td>
      <td>UEFA Euro qualification</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>2009-06-06</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>1</td>
      <td>FIFA World Cup qualification</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>2012-06-02</td>
      <td>Poland</td>
      <td>Andorra</td>
      <td>4</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Warsaw</td>
      <td>Poland</td>
      <td>False</td>
      <td>Poland</td>
      <td>POL</td>
      <td>Andorra</td>
      <td>AND</td>
      <td>POLAND</td>
    </tr>
    <tr>
      <td>2015-11-14</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>2</td>
      <td>1</td>
      <td>UEFA Euro qualification</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>2018-06-02</td>
      <td>Sweden</td>
      <td>Denmark</td>
      <td>0</td>
      <td>0</td>
      <td>Friendly</td>
      <td>Solna</td>
      <td>Sweden</td>
      <td>False</td>
      <td>Sweden</td>
      <td>SWE</td>
      <td>Denmark</td>
      <td>DEN</td>
      <td>SWEDEN</td>
    </tr>
    <tr>
      <td>2019-10-13</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>0</td>
      <td>5</td>
      <td>UEFA Euro qualification</td>
      <td>Nicosia</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
    <tr>
      <td>2021-03-28</td>
      <td>Poland</td>
      <td>Andorra</td>
      <td>3</td>
      <td>0</td>
      <td>FIFA World Cup qualification</td>
      <td>Warsaw</td>
      <td>Poland</td>
      <td>False</td>
      <td>Poland</td>
      <td>POL</td>
      <td>Andorra</td>
      <td>AND</td>
      <td>POLAND</td>
    </tr>
    <tr>
      <td>2021-09-04</td>
      <td>Cyprus</td>
      <td>Russia</td>
      <td>0</td>
      <td>2</td>
      <td>FIFA World Cup qualification</td>
      <td>Nicosia</td>
      <td>Cyprus</td>
      <td>False</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>CYPRUS</td>
    </tr>
  </tbody>
</table>
</div>
