import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('default')
sns.set_palette("husl")

print("=== AGRISMART AI PRECISION AGRICULTURE DATA ANALYSIS ===\n")

# 1. LOAD AND INSPECT DATASET
print("1. LOADING AND INSPECTING DATASET")
print("=" * 50)

# Load the dataset
df = pd.read_csv('climate_action_data.csv')

print(f"Dataset shape: {df.shape}")
print(f"Number of records: {len(df)}")
print(f"Number of variables: {df.shape[1]}")
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nData types:")
print(df.dtypes)

# 2. DATA QUALITY ASSESSMENT
print("\n\n2. DATA QUALITY ASSESSMENT")
print("=" * 50)

# Check for missing values
print("Missing values per column:")
missing_values = df.isnull().sum()
print(missing_values)

# Check for duplicate records
print(f"\nDuplicate records: {df.duplicated().sum()}")

# Check for 'error' entries
print("\nChecking for 'error' entries in each column:")
for col in df.columns:
    if df[col].dtype == 'object':
        error_count = df[col].astype(str).str.contains('error', case=False, na=False).sum()
        print(f"{col}: {error_count} error entries")

# Check for unusual values in numeric columns
# First, let's see what columns we actually have and their types
print(f"\nActual column names: {df.columns.tolist()}")
print(f"\nData types:")
print(df.dtypes)

# Define expected numeric columns based on the data structure
expected_numeric_cols = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 
                        'Humidity(%)', 'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']

# Find which columns actually exist and convert them to numeric if needed
numeric_cols = []
for col in expected_numeric_cols:
    if col in df.columns:
        # Try to convert to numeric, handling any 'error' values
        df[col] = pd.to_numeric(df[col], errors='coerce')
        numeric_cols.append(col)

print(f"\nNumeric columns found and converted: {numeric_cols}")

if len(numeric_cols) > 0:
    print("\nBasic statistics for numeric columns:")
    print(df[numeric_cols].describe())
else:
    print("\nNo numeric columns detected - checking column names and data types...")

# 3. DATA CLEANING
print("\n\n3. DATA CLEANING")
print("=" * 50)

# Create a copy for cleaning
df_clean = df.copy()

# Remove duplicate records
initial_count = len(df_clean)
df_clean = df_clean.drop_duplicates()
duplicates_removed = initial_count - len(df_clean)
print(f"Removed {duplicates_removed} duplicate records")

# Replace 'error' entries with NaN
for col in df_clean.columns:
    if df_clean[col].dtype == 'object':
        df_clean[col] = df_clean[col].replace('error', np.nan, regex=True)

# Convert Date column to datetime
df_clean['Date'] = pd.to_datetime(df_clean['Date'])

# Convert numeric columns in the clean dataset too
for col in expected_numeric_cols:
    if col in df_clean.columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# Handle missing values based on logical reasoning
print("\nHandling missing values:")

# For numeric columns, check if we should fill or drop
for col in numeric_cols:
    if col in df_clean.columns:
        missing_count = df_clean[col].isnull().sum()
        if missing_count > 0:
            print(f"{col}: {missing_count} missing values")
            # If less than 10% missing, fill with median; otherwise consider dropping
            if missing_count / len(df_clean) < 0.1:
                df_clean[col].fillna(df_clean[col].median(), inplace=True)
                print(f"  -> Filled with median: {df_clean[col].median():.2f}")
            else:
                print(f"  -> High missing rate ({missing_count/len(df_clean)*100:.1f}%), consider dropping")

# For categorical columns
for col in ['Crop_Type', 'Sensor_ID', 'Drone_Image_ID']:
    if col in df_clean.columns:
        missing_count = df_clean[col].isnull().sum()
        if missing_count > 0:
            print(f"{col}: {missing_count} missing values")
            # Drop rows with missing categorical data if reasonable
            if missing_count / len(df_clean) < 0.05:
                df_clean = df_clean.dropna(subset=[col])
                print(f"  -> Dropped rows with missing {col}")

print(f"\nCleaned dataset shape: {df_clean.shape}")
print(f"Records after cleaning: {len(df_clean)}")

# 4. EXPLORATORY DATA ANALYSIS
print("\n\n4. EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Descriptive statistics
print("Descriptive Statistics:")
if len(numeric_cols) > 0:
    print(df_clean[numeric_cols].describe())
else:
    print("No numeric columns available for statistics")

# Distribution of crop types
print(f"\nCrop Type Distribution:")
crop_counts = df_clean['Crop_Type'].value_counts()
print(crop_counts)

# Create visualizations
if len(numeric_cols) > 0:
    # Calculate number of subplots needed
    n_plots = len(numeric_cols)
    n_rows = (n_plots + 2) // 3  # Round up division
    n_cols = min(3, n_plots)
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 6*n_rows))
    fig.suptitle('Distribution of Numeric Variables', fontsize=16, fontweight='bold')
    
    # Handle case where we have only one subplot
    if n_plots == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = [axes] if n_plots == 1 else axes
    else:
        axes = axes.flatten()
    
    for i, var in enumerate(numeric_cols):
        if var in df_clean.columns:
            # Remove NaN values for plotting
            data_to_plot = df_clean[var].dropna()
            
            if len(data_to_plot) > 0:
                axes[i].hist(data_to_plot, bins=20, alpha=0.7, edgecolor='black')
                axes[i].set_title(f'Distribution of {var}')
                axes[i].set_xlabel(var)
                axes[i].set_ylabel('Frequency')
                axes[i].grid(True, alpha=0.3)
            else:
                axes[i].text(0.5, 0.5, 'No data available', 
                           horizontalalignment='center', verticalalignment='center',
                           transform=axes[i].transAxes)
                axes[i].set_title(f'{var} - No Data')
    
    # Hide empty subplots
    for i in range(len(numeric_cols), len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()
else:
    print("No numeric columns available for visualization")

# Correlation analysis
print("\n5. CORRELATION ANALYSIS")
print("=" * 50)

# Select numeric columns for correlation
available_cols = [col for col in numeric_cols if col in df_clean.columns]

if len(available_cols) >= 2:
    correlation_matrix = df_clean[available_cols].corr()
    
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # Create correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.3f', cbar_kws={'label': 'Correlation'})
    plt.title('Correlation Heatmap of Soil and Environmental Variables', 
              fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
else:
    print("Insufficient numeric columns for correlation analysis")
    correlation_matrix = pd.DataFrame()  # Empty dataframe for later use

# 6. SPECIFIC ANALYSIS QUESTIONS
print("\n\n6. SPECIFIC ANALYSIS AND INSIGHTS")
print("=" * 50)

# Question 1: Variables that most influence fertilizer recommendations
print("1. Variables that most influence Fertilizer Recommendations:")

# Check if correlation_matrix exists and has the fertilizer column
try:
    if 'correlation_matrix' in locals() and 'Fertilizer_Recommended(kg/ha)' in correlation_matrix.columns and len(correlation_matrix) > 1:
        fert_correlations = correlation_matrix['Fertilizer_Recommended(kg/ha)'].abs().sort_values(ascending=False)
        print(fert_correlations.drop('Fertilizer_Recommended(kg/ha)'))
        
        top_influencers = fert_correlations.drop('Fertilizer_Recommended(kg/ha)').head(3)
        print(f"\nTop 3 variables influencing fertilizer recommendations:")
        for var, corr in top_influencers.items():
            print(f"  • {var}: {corr:.3f} correlation")
    else:
        raise Exception("Using direct correlation method")
        
except:
    print("Using direct correlation analysis...")
    if 'Fertilizer_Recommended(kg/ha)' in df_clean.columns:
        # Alternative analysis using direct correlation with available numeric columns
        fert_col = 'Fertilizer_Recommended(kg/ha)'
        correlations = {}
        for col in numeric_cols:
            if col != fert_col and col in df_clean.columns:
                corr = df_clean[fert_col].corr(df_clean[col])
                if not pd.isna(corr):
                    correlations[col] = abs(corr)
        
        if correlations:
            sorted_corr = sorted(correlations.items(), key=lambda x: x[1], reverse=True)
            print("Variables influencing fertilizer recommendations:")
            for var, corr in sorted_corr:
                print(f"  • {var}: {corr:.3f} correlation")
            top_influencers = dict(sorted_corr[:3])
            
            print(f"\nTop 3 variables influencing fertilizer recommendations:")
            for var, corr in list(top_influencers.items())[:3]:
                print(f"  • {var}: {corr:.3f} correlation")
        else:
            print("No significant correlations found")
            top_influencers = {}
    else:
        print("Fertilizer recommendation column not found")
        top_influencers = {}

# Question 2: Crop type with highest average soil moisture
print("\n2. Crop Type with Highest Average Soil Moisture:")
if 'Soil_Moisture(%)' in df_clean.columns and 'Crop_Type' in df_clean.columns:
    # Ensure Soil_Moisture is numeric
    df_clean['Soil_Moisture(%)'] = pd.to_numeric(df_clean['Soil_Moisture(%)'], errors='coerce')
    
    # Remove any rows where Soil_Moisture or Crop_Type is NaN
    moisture_data = df_clean[['Crop_Type', 'Soil_Moisture(%)']].dropna()
    
    if len(moisture_data) > 0:
        avg_moisture_by_crop = moisture_data.groupby('Crop_Type')['Soil_Moisture(%)'].agg(['mean', 'count']).round(2)
        avg_moisture_by_crop = avg_moisture_by_crop.sort_values('mean', ascending=False)
        print(avg_moisture_by_crop)
        
        highest_moisture_crop = avg_moisture_by_crop.index[0]
        highest_moisture_value = avg_moisture_by_crop.iloc[0]['mean']
        print(f"\nCrop with highest average soil moisture: {highest_moisture_crop} ({highest_moisture_value}%)")
    else:
        print("No valid soil moisture data available")
        highest_moisture_crop = "Unknown"
        highest_moisture_value = "N/A"
else:
    print("Required columns (Soil_Moisture(%) or Crop_Type) not found")
    highest_moisture_crop = "Unknown"
    highest_moisture_value = "N/A"

# Question 3: Irrigation adjustments for crops with temperature > 30°C
print("\n3. Irrigation Recommendations for Crops with Temperature > 30°C:")
if 'Temperature(C)' in df_clean.columns:
    # Ensure Temperature is numeric
    df_clean['Temperature(C)'] = pd.to_numeric(df_clean['Temperature(C)'], errors='coerce')
    
    high_temp_crops = df_clean[df_clean['Temperature(C)'] > 30]
    print(f"Number of records with temperature > 30°C: {len(high_temp_crops)}")
    
    if len(high_temp_crops) > 0:
        # Ensure all required columns are numeric
        for col in ['Temperature(C)', 'Irrigation_Recommended(mm)', 'Soil_Moisture(%)']:
            if col in high_temp_crops.columns:
                high_temp_crops[col] = pd.to_numeric(high_temp_crops[col], errors='coerce')
        
        # Remove rows with NaN values in critical columns
        analysis_data = high_temp_crops[['Crop_Type', 'Temperature(C)', 'Irrigation_Recommended(mm)', 'Soil_Moisture(%)']].dropna()
        
        if len(analysis_data) > 0:
            irrigation_analysis = analysis_data.groupby('Crop_Type').agg({
                'Temperature(C)': ['mean', 'count'],
                'Irrigation_Recommended(mm)': 'mean',
                'Soil_Moisture(%)': 'mean'
            }).round(2)
            
            print("Analysis by crop type for high temperature conditions:")
            print(irrigation_analysis)
            
            # Recommendations
            print("\nIrrigation Adjustment Recommendations:")
            for crop in irrigation_analysis.index:
                avg_temp = irrigation_analysis.loc[crop, ('Temperature(C)', 'mean')]
                avg_irrigation = irrigation_analysis.loc[crop, ('Irrigation_Recommended(mm)', 'mean')]
                avg_moisture = irrigation_analysis.loc[crop, ('Soil_Moisture(%)', 'mean')]
                
                print(f"\n• {crop}:")
                print(f"  - Average temperature: {avg_temp}°C")
                print(f"  - Current irrigation: {avg_irrigation}mm")
                print(f"  - Soil moisture: {avg_moisture}%")
                
                # Suggest adjustments based on conditions
                if avg_moisture < 40:
                    suggested_increase = avg_irrigation * 1.2
                    print(f"  - RECOMMENDATION: Increase irrigation to {suggested_increase:.1f}mm (+20%)")
                    print(f"    Reason: Low soil moisture under high temperature stress")
                elif avg_moisture > 60:
                    suggested_decrease = avg_irrigation * 0.9
                    print(f"  - RECOMMENDATION: Reduce irrigation to {suggested_decrease:.1f}mm (-10%)")
                    print(f"    Reason: Adequate soil moisture, avoid over-watering")
                else:
                    print(f"  - RECOMMENDATION: Maintain current irrigation level")
                    print(f"    Reason: Soil moisture is at optimal level")
        else:
            print("No valid data available for high temperature analysis")
    else:
        print("No records found with temperature > 30°C")
else:
    print("Temperature column not found in dataset")

# Additional insights
print("\n\n7. ADDITIONAL INSIGHTS")
print("=" * 50)

# Seasonal patterns (if data spans multiple months)
if 'Date' in df_clean.columns:
    try:
        df_clean['Month'] = df_clean['Date'].dt.month
        
        # Ensure numeric columns for groupby
        analysis_cols = ['Temperature(C)', 'Humidity(%)', 'Soil_Moisture(%)']
        available_analysis_cols = []
        
        for col in analysis_cols:
            if col in df_clean.columns:
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
                available_analysis_cols.append(col)
        
        if available_analysis_cols:
            monthly_data = df_clean[['Month'] + available_analysis_cols].dropna()
            if len(monthly_data) > 0:
                monthly_summary = monthly_data.groupby('Month')[available_analysis_cols].mean().round(2)
                print("Monthly Environmental Patterns:")
                print(monthly_summary)
            else:
                print("No valid data for monthly analysis")
        else:
            print("No suitable columns for monthly analysis")
    except Exception as e:
        print(f"Monthly analysis not available: {str(e)}")

# Optimal conditions analysis
print("\nOptimal Growing Conditions Analysis:")
if 'Crop_Type' in df_clean.columns:
    try:
        # Define columns for optimal conditions analysis
        condition_cols = ['Temperature(C)', 'Humidity(%)', 'Soil_Moisture(%)', 'Soil_pH']
        available_condition_cols = []
        
        for col in condition_cols:
            if col in df_clean.columns:
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
                available_condition_cols.append(col)
        
        if available_condition_cols:
            conditions_data = df_clean[['Crop_Type'] + available_condition_cols].dropna()
            if len(conditions_data) > 0:
                optimal_conditions = conditions_data.groupby('Crop_Type')[available_condition_cols].agg(['min', 'max', 'mean']).round(2)
                print("Environmental ranges by crop type:")
                print(optimal_conditions)
            else:
                print("No valid data for optimal conditions analysis")
        else:
            print("No suitable columns for optimal conditions analysis")
    except Exception as e:
        print(f"Optimal conditions analysis not available: {str(e)}")
else:
    print("Crop_Type column not available for optimal conditions analysis")

# 8. EXPORT CLEANED DATASET
print("\n\n8. EXPORTING CLEANED DATASET")
print("=" * 50)

# Export cleaned dataset
output_filename = 'cleaned_precision_agriculture_data.csv'
df_clean.to_csv(output_filename, index=False)
print(f"Cleaned dataset exported as: {output_filename}")
print(f"Final dataset contains {len(df_clean)} records and {df_clean.shape[1]} variables")

# Summary of cleaning actions
print("\nData Cleaning Summary:")
print(f"• Original records: {len(df)}")
print(f"• Duplicates removed: {duplicates_removed}")
print(f"• Final records: {len(df_clean)}")
print(f"• Data quality: {(len(df_clean)/len(df)*100):.1f}% of original data retained")

print("\n=== ANALYSIS COMPLETE ===")
print("\nKey Findings Summary:")
if 'top_influencers' in locals() and top_influencers:
    top_vars = list(top_influencers.keys())[:2]
    print("1. Fertilizer recommendations are most influenced by:", ", ".join(top_vars))
else:
    print("1. Fertilizer recommendation influences: Analysis completed (see details above)")

if 'highest_moisture_crop' in locals() and 'highest_moisture_value' in locals():
    print(f"2. {highest_moisture_crop} has the highest average soil moisture ({highest_moisture_value}%)")
else:
    print("2. Crop moisture analysis: Completed (see details above)")

if 'high_temp_crops' in locals():
    print(f"3. {len(high_temp_crops)} records show temperatures above 30°C requiring irrigation adjustments")
else:
    print("3. High temperature irrigation analysis: Completed")

print(f"4. Dataset cleaned and exported with {len(df_clean)} quality records")
