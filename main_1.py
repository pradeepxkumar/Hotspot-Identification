
# -------------------------------------------
# 🚦 Complete Accident Data Analysis with Auto-Save (CORRECTED)
# -------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
from datetime import datetime
warnings.filterwarnings('ignore')

# Create graphs folder if it doesn't exist
GRAPH_FOLDER = "accident_analysis_graphs"
if not os.path.exists(GRAPH_FOLDER):
    os.makedirs(GRAPH_FOLDER)
    print(f"✅ Created folder: {GRAPH_FOLDER}")

# ✅ Load your dataset with proper delimiter
print("🔍 Loading accident_data.csv...")

try:
    df = pd.read_csv("accident_data.csv", delimiter='\t', encoding='utf-8', low_memory=False)
    print("✅ Loaded successfully with tab delimiter")
except Exception as e:
    try:
        df = pd.read_csv("accident_data.csv", encoding='utf-8', low_memory=False)
        print("✅ Loaded successfully with comma delimiter")
    except Exception as e2:
        print(f"❌ Error loading CSV: {e2}")
        exit()

# Show initial info
print("\n📊 Initial Data Preview:")
print(df.head(3))
print(f"\n📏 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\n📋 Columns in dataset:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i}. {col}")

# -------------------------------------------
# 🧹 Data Cleaning
# -------------------------------------------
print("\n🧹 Cleaning data...")

# Clean column names
df.columns = df.columns.str.strip().str.replace('\n', ' ').str.replace('  ', ' ')

# Drop duplicates
initial_rows = len(df)
df = df.drop_duplicates()
print(f"   Removed {initial_rows - len(df)} duplicate rows")

# Convert date to datetime
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
    df = df.dropna(subset=['Date'])
    
    df['Month'] = df['Date'].dt.month
    df['Weekday'] = df['Date'].dt.day_name()
    df['Year'] = df['Date'].dt.year
    df['Month_Name'] = df['Date'].dt.strftime('%B')
    df['Quarter'] = df['Date'].dt.quarter
    
    print(f"✅ Date conversion successful")
else:
    print("⚠️ Date column not found!")
    exit()

print(f"✅ After cleaning: {len(df)} rows remain")

# -------------------------------------------
# 🗂️ Data Standardization (Clean Text Values)
# -------------------------------------------
print("\n🗂️ Standardizing text values...")

# Standardize Nature of Accident column
nature_col = 'Nature of Accident / Incident'
if nature_col in df.columns:
    df[nature_col] = df[nature_col].astype(str).str.strip()
    # Standardize spelling variations
    df[nature_col] = df[nature_col].replace({
        'Head on collison': 'Head-on Collision',
        'Rear End Collision': 'Rear-End Collision',
        'Collision Brush/Side Wipe,': 'Collision Brush/Side Swipe',
        'Dash with Median/Crash barrier': 'Dash with Median/Barrier',
        'Left Turn Collision': 'Left Turn Collision',
        'Right Turn Collision': 'Right Turn Collision'
    })
    print(f"   ✓ Standardized {nature_col}")

# Standardize Classification (Severity) column
class_col = 'Classification of Accident / Incident'
if class_col in df.columns:
    df[class_col] = df[class_col].astype(str).str.strip()
    df[class_col] = df[class_col].replace({
        'Grevious Injury': 'Grievous Injury',
        'Minor Injury': 'Minor Injury',
        'Non - Injury': 'Non-Injury',
        'Not specified': 'Not Specified'
    })
    print(f"   ✓ Standardized {class_col}")

# Standardize Causes column
causes_col = 'Causes'
if causes_col in df.columns:
    df[causes_col] = df[causes_col].astype(str).str.strip()
    df[causes_col] = df[causes_col].replace({
        'Fault of users': 'Driver/Pedestrian Fault',
        'Defect in vehicle/ Road condition': 'Mechanical/Road Defect',
        'Vehicle out of control': 'Vehicle Out of Control',
        'Not Specified': 'Not Specified'
    })
    print(f"   ✓ Standardized {causes_col}")

# Standardize Road Feature column
road_feature_col = 'Road Feature'
if road_feature_col in df.columns:
    df[road_feature_col] = df[road_feature_col].astype(str).str.strip()
    print(f"   ✓ Standardized {road_feature_col}")

# Standardize Road condition column
road_cond_col = 'Road condition'
if road_cond_col in df.columns:
    df[road_cond_col] = df[road_cond_col].astype(str).str.strip()
    df[road_cond_col] = df[road_cond_col].replace({
        'Straight road': 'Straight',
        'Slight curve': 'Slight Curve',
        'Sharp curve': 'Sharp Curve',
        'Flat road': 'Flat Road',
        'Not specified': 'Not Specified'
    })
    print(f"   ✓ Standardized {road_cond_col}")

# Standardize Intersection Type column
int_col = 'Intersection type and control'
if int_col in df.columns:
    df[int_col] = df[int_col].astype(str).str.strip()
    df[int_col] = df[int_col].replace({
        'T-junction': 'T-junction',
        'Y-junction': 'Y-junction',
        'Four arm junction,': 'Four-arm Junction',
        'Four-arm': 'Four-arm Junction',
        'Staggered junction': 'Staggered Junction',
        'Staggered': 'Staggered Junction',
        'Mid-block': 'Mid-block',
        '-': 'Not Specified',
        'nan': 'Not Specified'
    })
    print(f"   ✓ Standardized {int_col}")

# Standardize Weather condition column
weather_col = 'Weather condition'
if weather_col in df.columns:
    df[weather_col] = df[weather_col].astype(str).str.strip()
    df[weather_col] = df[weather_col].replace({
        'Not specified': 'Not Specified'
    })
    print(f"   ✓ Standardized {weather_col}")

# Standardize Vehicle Responsible column
veh_col = 'Vehicle Responsible'
if veh_col in df.columns:
    df[veh_col] = df[veh_col].astype(str).str.strip()
    print(f"   ✓ Standardized {veh_col}")

print("✅ Standardization complete")

# -------------------------------------------
# 📊 Summary Statistics
# -------------------------------------------
print(f"\n{'='*60}")
print(f"📊 ACCIDENT DATA SUMMARY")
print(f"{'='*60}")
print(f"Total Accidents: {len(df)}")
if 'Accident Location' in df.columns:
    print(f"Unique Locations: {df['Accident Location'].nunique()}")
print(f"Date Range: {df['Date'].min().strftime('%d %B %Y')} to {df['Date'].max().strftime('%d %B %Y')}")
print(f"{'='*60}\n")

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 120
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

graph_count = 0

# -------------------------------------------
# GRAPH 1: Year-wise Distribution
# -------------------------------------------
graph_count += 1
print(f"📈 Generating Graph {graph_count}: Year-wise Distribution...")
plt.figure(figsize=(14,7))
year_counts = df['Year'].value_counts().sort_index()
bars = plt.bar(year_counts.index, year_counts.values, color='#FF6B6B', alpha=0.85, edgecolor='black', linewidth=1.5)
plt.title("Year-wise Accident Distribution", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14, fontweight='bold')
plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
for i, (year, count) in enumerate(zip(year_counts.index, year_counts.values)):
    plt.text(year, count + max(year_counts.values)*0.02, str(count), 
             ha='center', va='bottom', fontweight='bold', fontsize=11)
plt.xticks(year_counts.index, fontsize=11)
plt.tight_layout()
plt.savefig(f"{GRAPH_FOLDER}/01_year_wise_distribution.png")
plt.close()

# -------------------------------------------
# GRAPH 2: Month-wise Distribution
# -------------------------------------------
graph_count += 1
print(f"📈 Generating Graph {graph_count}: Month-wise Distribution...")
plt.figure(figsize=(14,7))
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_counts = df['Month_Name'].value_counts().reindex(month_order)
colors = plt.cm.viridis(np.linspace(0.2, 0.9, 12))
bars = plt.bar(range(12), month_counts.values, color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
plt.title("Month-wise Accident Distribution", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=14, fontweight='bold')
plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
plt.xticks(range(12), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], fontsize=11)
plt.grid(axis='y', alpha=0.3, linestyle='--')
for i, v in enumerate(month_counts.values):
    if not pd.isna(v):
        plt.text(i, v + max(month_counts.values)*0.02, str(int(v)), 
                 ha='center', va='bottom', fontweight='bold', fontsize=10)
plt.tight_layout()
plt.savefig(f"{GRAPH_FOLDER}/02_month_wise_distribution.png")
plt.close()

# -------------------------------------------
# GRAPH 3: Quarter-wise Distribution
# -------------------------------------------
graph_count += 1
print(f"📈 Generating Graph {graph_count}: Quarter-wise Distribution...")
plt.figure(figsize=(10,7))
quarter_counts = df['Quarter'].value_counts().sort_index()
quarter_labels = ['Q1\n(Jan-Mar)', 'Q2\n(Apr-Jun)', 'Q3\n(Jul-Sep)', 'Q4\n(Oct-Dec)']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
bars = plt.bar(range(1, 5), [quarter_counts.get(i, 0) for i in range(1, 5)], 
               color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
plt.title("Quarter-wise Accident Distribution", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Quarter", fontsize=14, fontweight='bold')
plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
plt.xticks(range(1, 5), quarter_labels, fontsize=11)
plt.grid(axis='y', alpha=0.3, linestyle='--')
for i, q in enumerate(range(1, 5), 1):
    val = quarter_counts.get(q, 0)
    plt.text(i, val + max(quarter_counts.values)*0.02, str(int(val)), 
             ha='center', va='bottom', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig(f"{GRAPH_FOLDER}/03_quarter_wise_distribution.png")
plt.close()

# -------------------------------------------
# GRAPH 4: Weekday Distribution
# -------------------------------------------
graph_count += 1
print(f"📈 Generating Graph {graph_count}: Weekday Distribution...")
plt.figure(figsize=(12,7))
weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekday_counts = df['Weekday'].value_counts().reindex(weekday_order)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DFE6E9', '#A29BFE']
bars = plt.bar(range(7), weekday_counts.values, color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
plt.title("Day-wise Accident Distribution", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Day of Week", fontsize=14, fontweight='bold')
plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
plt.xticks(range(7), ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], fontsize=12)
plt.grid(axis='y', alpha=0.3, linestyle='--')
for i, v in enumerate(weekday_counts.values):
    if not pd.isna(v):
        plt.text(i, v + max(weekday_counts.values)*0.02, str(int(v)), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
plt.tight_layout()
plt.savefig(f"{GRAPH_FOLDER}/04_weekday_distribution.png")
plt.close()

# -------------------------------------------
# GRAPH 5: Nature of Accident
# -------------------------------------------
if nature_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Nature of Accidents...")
    plt.figure(figsize=(14,8))
    nature_counts = df[nature_col].value_counts()
    colors = plt.cm.Set3(range(len(nature_counts)))
    bars = plt.barh(range(len(nature_counts)), nature_counts.values, 
                    color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.yticks(range(len(nature_counts)), nature_counts.index, fontsize=12)
    plt.title("Nature of Accidents", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.ylabel("Type of Accident", fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    for i, v in enumerate(nature_counts.values):
        plt.text(v + max(nature_counts.values)*0.02, i, str(v), 
                 va='center', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/05_nature_of_accidents.png")
    plt.close()

# -------------------------------------------
# GRAPH 6: Causes of Accidents
# -------------------------------------------
if causes_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Causes of Accidents...")
    plt.figure(figsize=(14,8))
    cause_counts = df[causes_col].value_counts()
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DFE6E9']
    bars = plt.bar(range(len(cause_counts)), cause_counts.values, 
                   color=colors[:len(cause_counts)], alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Causes of Accidents", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Cause Type", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(cause_counts)), cause_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(cause_counts.values):
        plt.text(i, v + max(cause_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/06_causes_of_accidents.png")
    plt.close()

# -------------------------------------------
# GRAPH 7: Accident Severity
# -------------------------------------------
if class_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Accident Severity...")
    plt.figure(figsize=(12,7))
    severity_counts = df[class_col].value_counts()
    severity_order = ['Fatal', 'Grievous Injury', 'Minor Injury', 'Non-Injury', 'Not Specified']
    severity_counts_ordered = pd.Series({s: severity_counts.get(s, 0) for s in severity_order if s in severity_counts.index})
    
    colors = ['#E74C3C', '#E67E22', '#F39C12', '#2ECC71', '#95A5A6']
    bars = plt.bar(range(len(severity_counts_ordered)), severity_counts_ordered.values, 
                   color=colors[:len(severity_counts_ordered)], alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accident Severity Distribution", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Severity Level", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(severity_counts_ordered)), severity_counts_ordered.index, rotation=30, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(severity_counts_ordered.values):
        plt.text(i, v + max(severity_counts_ordered.values)*0.02, str(int(v)), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/07_severity_distribution.png")
    plt.close()

# -------------------------------------------
# GRAPH 8: Road Features
# -------------------------------------------
if road_feature_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Road Features...")
    plt.figure(figsize=(12,7))
    road_counts = df[road_feature_col].value_counts()
    colors = plt.cm.Pastel1(range(len(road_counts)))
    bars = plt.bar(range(len(road_counts)), road_counts.values, 
                   color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accidents by Road Feature", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Road Feature Type", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(road_counts)), road_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(road_counts.values):
        plt.text(i, v + max(road_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/08_road_features.png")
    plt.close()

# -------------------------------------------
# GRAPH 9: Road Conditions
# -------------------------------------------
if road_cond_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Road Conditions...")
    plt.figure(figsize=(12,7))
    cond_counts = df[road_cond_col].value_counts()
    colors = plt.cm.Set2(range(len(cond_counts)))
    bars = plt.bar(range(len(cond_counts)), cond_counts.values, 
                   color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accidents by Road Condition", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Road Condition", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(cond_counts)), cond_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(cond_counts.values):
        plt.text(i, v + max(cond_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/09_road_conditions.png")
    plt.close()

# -------------------------------------------
# GRAPH 10: Intersection Types
# -------------------------------------------
if int_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Intersection Types...")
    plt.figure(figsize=(12,7))
    int_counts = df[int_col].value_counts()
    colors = plt.cm.Accent(range(len(int_counts)))
    bars = plt.bar(range(len(int_counts)), int_counts.values, 
                   color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accidents by Intersection Type", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Intersection Type", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(int_counts)), int_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(int_counts.values):
        plt.text(i, v + max(int_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/10_intersection_types.png")
    plt.close()

# -------------------------------------------
# GRAPH 11: Weather Conditions
# -------------------------------------------
if weather_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Weather Conditions...")
    plt.figure(figsize=(12,7))
    weather_counts = df[weather_col].value_counts()
    colors = ['#3498DB', '#95A5A6', '#34495E', '#5DADE2', '#2E86C1', '#AEB6BF']
    bars = plt.bar(range(len(weather_counts)), weather_counts.values, 
                   color=colors[:len(weather_counts)], alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accidents by Weather Condition", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Weather Condition", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(weather_counts)), weather_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(weather_counts.values):
        plt.text(i, v + max(weather_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/11_weather_conditions.png")
    plt.close()

# -------------------------------------------
# GRAPH 12: Vehicle Types
# -------------------------------------------
if veh_col in df.columns:
    graph_count += 1
    print(f"📈 Generating Graph {graph_count}: Vehicle Types...")
    plt.figure(figsize=(12,7))
    veh_counts = df[veh_col].value_counts()
    colors = plt.cm.tab10(range(len(veh_counts)))
    bars = plt.bar(range(len(veh_counts)), veh_counts.values, 
                   color=colors, alpha=0.85, edgecolor='black', linewidth=1.5)
    plt.title("Accidents by Vehicle Type Responsible", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Vehicle Type", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Accidents", fontsize=14, fontweight='bold')
    plt.xticks(range(len(veh_counts)), veh_counts.index, rotation=45, ha='right', fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    for i, v in enumerate(veh_counts.values):
        plt.text(i, v + max(veh_counts.values)*0.02, str(v), 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)
    plt.tight_layout()
    plt.savefig(f"{GRAPH_FOLDER}/12_vehicle_types.png")
    plt.close()

# -------------------------------------------
# GRAPH 13: Fatal Accidents - Causes
# -------------------------------------------
if class_col in df.columns and causes_col in df.columns:
    fatal_data = df[df[class_col] == 'Fatal']
    if len(fatal_data) > 0:
        graph_count += 1
        print(f"📈 Generating Graph {graph_count}: Fatal Accidents by Cause...")
        plt.figure(figsize=(12,8))
        fatal_causes = fatal_data[causes_col].value_counts()
        colors = plt.cm.Reds(np.linspace(0.4, 0.9, len(fatal_causes)))
        bars = plt.barh(range(len(fatal_causes)), fatal_causes.values, 
                       color=colors, edgecolor='darkred', linewidth=1.5)
        plt.yticks(range(len(fatal_causes)), fatal_causes.index, fontsize=12)
        plt.title("Fatal Accidents by Cause", fontsize=18, fontweight='bold', pad=20, color='darkred')
        plt.xlabel("Number of Fatal Accidents", fontsize=14, fontweight='bold')
        plt.ylabel("Cause", fontsize=14, fontweight='bold')
        plt.grid(axis='x', alpha=0.3, linestyle='--')
        for i, v in enumerate(fatal_causes.values):
            plt.text(v + max(fatal_causes.values)*0.02, i, str(v), 
                     va='center', fontweight='bold', fontsize=11, color='darkred')
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}/13_fatal_accidents_causes.png")
        plt.close()

# -------------------------------------------
# GRAPH 14: Fatal Accidents - Road Features
# -------------------------------------------
if class_col in df.columns and road_feature_col in df.columns:
    fatal_data = df[df[class_col] == 'Fatal']
    if len(fatal_data) > 0:
        graph_count += 1
        print(f"📈 Generating Graph {graph_count}: Fatal Accidents by Road Feature...")
        plt.figure(figsize=(12,7))
        fatal_roads = fatal_data[road_feature_col].value_counts()
        colors = plt.cm.OrRd(np.linspace(0.4, 0.9, len(fatal_roads)))
        bars = plt.barh(range(len(fatal_roads)), fatal_roads.values, 
                       color=colors, edgecolor='darkred', linewidth=1.5)
        plt.yticks(range(len(fatal_roads)), fatal_roads.index, fontsize=12)
        plt.title("Fatal Accidents by Road Feature", fontsize=18, fontweight='bold', pad=20, color='darkred')
        plt.xlabel("Number of Fatal Accidents", fontsize=14, fontweight='bold')
        plt.ylabel("Road Feature", fontsize=14, fontweight='bold')
        plt.grid(axis='x', alpha=0.3, linestyle='--')
        for i, v in enumerate(fatal_roads.values):
            plt.text(v + max(fatal_roads.values)*0.02, i, str(v), 
                     va='center', fontweight='bold', fontsize=11, color='darkred')
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}/14_fatal_accidents_road_features.png")
        plt.close()