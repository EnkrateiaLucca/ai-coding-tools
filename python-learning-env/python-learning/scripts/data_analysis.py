#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "pandas",
#   "matplotlib",
# ]
# ///

"""
Data analysis demonstration using pandas and matplotlib.
This script shows how to handle dependencies with uv script format.
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

def generate_sample_data():
    """Generate sample sales data for demonstration."""
    print("📊 Generating sample data...")
    
    # Generate random sales data
    start_date = datetime(2024, 1, 1)
    data = []
    
    products = ["Widget A", "Widget B", "Widget C", "Gadget X", "Gadget Y"]
    regions = ["North", "South", "East", "West", "Central"]
    
    for i in range(100):
        date = start_date + timedelta(days=random.randint(0, 365))
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'product': random.choice(products),
            'region': random.choice(regions),
            'sales': random.randint(100, 1000),
            'quantity': random.randint(1, 50)
        })
    
    return pd.DataFrame(data)

def analyze_data(df):
    """Perform basic data analysis."""
    print("\n🔍 Data Analysis Results:")
    print("=" * 40)
    
    # Basic statistics
    print(f"Total records: {len(df)}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Total sales: ${df['sales'].sum():,}")
    print(f"Average sale: ${df['sales'].mean():.2f}")
    
    # Group by product
    print("\n📦 Sales by Product:")
    product_sales = df.groupby('product')['sales'].sum().sort_values(ascending=False)
    for product, sales in product_sales.items():
        print(f"  {product}: ${sales:,}")
    
    # Group by region
    print("\n🌍 Sales by Region:")
    region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
    for region, sales in region_sales.items():
        print(f"  {region}: ${sales:,}")
    
    return product_sales, region_sales

def create_visualizations(df, product_sales, region_sales):
    """Create visualizations of the data."""
    print("\n📈 Creating visualizations...")
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Sales Data Analysis', fontsize=16, fontweight='bold')
    
    # 1. Sales by Product (Bar Chart)
    product_sales.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title('Sales by Product')
    ax1.set_ylabel('Sales ($)')
    ax1.tick_params(axis='x', rotation=45)
    
    # 2. Sales by Region (Pie Chart)
    region_sales.plot(kind='pie', ax=ax2, autopct='%1.1f%%')
    ax2.set_title('Sales Distribution by Region')
    ax2.set_ylabel('')
    
    # 3. Sales Timeline
    df['date'] = pd.to_datetime(df['date'])
    daily_sales = df.groupby('date')['sales'].sum()
    daily_sales.plot(kind='line', ax=ax3, color='green')
    ax3.set_title('Sales Over Time')
    ax3.set_ylabel('Daily Sales ($)')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. Quantity vs Sales Scatter
    ax4.scatter(df['quantity'], df['sales'], alpha=0.6, color='orange')
    ax4.set_title('Quantity vs Sales')
    ax4.set_xlabel('Quantity')
    ax4.set_ylabel('Sales ($)')
    
    plt.tight_layout()
    
    # Save the plot
    filename = 'sales_analysis.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Visualization saved as {filename}")
    
    # Show the plot
    plt.show()

def save_summary_report(df, product_sales, region_sales):
    """Save a summary report to CSV."""
    print("\n💾 Saving summary report...")
    
    # Create summary DataFrame
    summary = {
        'Metric': [
            'Total Records',
            'Total Sales',
            'Average Sale',
            'Top Product',
            'Top Region',
            'Date Range'
        ],
        'Value': [
            len(df),
            f"${df['sales'].sum():,}",
            f"${df['sales'].mean():.2f}",
            product_sales.index[0],
            region_sales.index[0],
            f"{df['date'].min()} to {df['date'].max()}"
        ]
    }
    
    summary_df = pd.DataFrame(summary)
    summary_df.to_csv('sales_summary.csv', index=False)
    print("✓ Summary report saved as sales_summary.csv")

def main():
    """Main function for data analysis demo."""
    print("🎯 Data Analysis Demo with Pandas & Matplotlib")
    print("=" * 50)
    
    try:
        # Generate sample data
        df = generate_sample_data()
        
        # Display first few rows
        print("\n📋 Sample Data (first 5 rows):")
        print(df.head())
        
        # Analyze data
        product_sales, region_sales = analyze_data(df)
        
        # Create visualizations
        create_visualizations(df, product_sales, region_sales)
        
        # Save summary report
        save_summary_report(df, product_sales, region_sales)
        
        print("\n✅ Analysis complete! Check the generated files.")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure the required packages are available.")
        print("This script uses uv to automatically manage dependencies.")

if __name__ == "__main__":
    main()