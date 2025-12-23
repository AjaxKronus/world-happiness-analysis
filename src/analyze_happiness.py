"""
World Happiness 2023 Analysis - Complete pipeline
Analyzes happiness scores by country and region with visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for professional plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_data(file_path: str) -> pd.DataFrame:
    """Load and inspect the World Happiness dataset."""
    df = pd.read_csv(file_path)
    print(f"Dataset loaded: {df.shape[0]} countries, {df.shape[1]} features")
    print("\nDataset preview:")
    print(df.head())
    return df

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select core happiness columns and clean data."""
    core_cols = [
        'Country name', 'Regional indicator', 'Ladder score',
        'Logged GDP per capita', 'Social support', 
        'Healthy life expectancy', 'Freedom to make life choices',
        'Generosity', 'Perceptions of corruption'
    ]
    df_clean = df[core_cols].copy()
    print(f"\nClean data shape: {df_clean.shape}")
    return df_clean

def top_countries(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Get top N happiest countries by Ladder score."""
    top_n = (df[['Country name', 'Ladder score']]
             .nlargest(n, 'Ladder score')
             .round(2))
    print(f"\nTop {n} Happiest Countries:")
    print(top_n)
    return top_n

def regional_averages(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate average happiness score by region."""
    region_avg = (df.groupby('Regional indicator')['Ladder score']
                  .mean()
                  .round(3)
                  .sort_values(ascending=False)
                  .reset_index())
    print("\nRegional Happiness Averages:")
    print(region_avg)
    return region_avg

def create_visualizations(df: pd.DataFrame, region_avg: pd.DataFrame):
    """Generate and save key plots."""
    os.makedirs('output', exist_ok=True)
    
    # Top 10 countries bar chart
    plt.figure(figsize=(10, 6))
    top10 = top_countries(df, 10)
    plt.barh(range(len(top10)), top10['Ladder score'])
    plt.yticks(range(len(top10)), top10['Country name'])
    plt.xlabel('Ladder Score (Happiness)')
    plt.title('Top 10 Happiest Countries 2023')
    plt.tight_layout()
    plt.savefig('output/top10_countries.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Regional comparison
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(region_avg)), region_avg['Ladder score'])
    plt.xticks(range(len(region_avg)), region_avg['Regional indicator'], 
               rotation=45, ha='right')
    plt.ylabel('Average Ladder Score')
    plt.title('Average Happiness by Region')
    plt.tight_layout()
    plt.savefig('output/regional_happiness.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("\nPlots saved to 'output/' folder.")

def main():
    """Execute complete analysis pipeline."""
    print("=== World Happiness 2023 Analysis ===\n")
    
    # Load and prepare data
    df = load_data('data/world_happiness_2023.csv')
    df_clean = prepare_data(df)
    
    # Generate key insights
    top_countries(df_clean)
    region_avg = regional_averages(df_clean)
    
    # Create visualizations
    create_visualizations(df_clean, region_avg)
    
    print("\nAnalysis complete! Check 'output/' for plots.")

if __name__ == "__main__":
    main()
