# World Happiness Analysis

Analyzes the 2023 World Happiness Report dataset to explore happiness factors across countries and regions.[file:1]

## Dataset
- **Source**: World Happiness Report 2023
- **Key columns**: Country name, Regional indicator, Ladder score (happiness), Logged GDP per capita, Social support, Healthy life expectancy, Freedom, Generosity, Perceptions of corruption[file:1]
- **File**: `data/world_happiness_2023.csv`

## Key Insights
- **Top countries**: Luxembourg, Norway, Switzerland lead in ladder score[file:1]
- **Regional rankings**: North America & ANZ highest (7.17 avg), Sub-Saharan Africa lowest (4.37 avg)[file:1]
- **Correlations**: Higher GDP, social support → higher happiness scores[file:1]

## Usage
pip install -r requirements.txt
python src/analyze_happiness.py
