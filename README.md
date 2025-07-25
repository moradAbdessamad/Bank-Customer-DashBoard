# Bank Customer Dashboard

An interactive data visualization dashboard for analyzing bank customer transactions and behavioral patterns using clustering analysis and machine learning insights.

## Project Overview

This project analyzes bank transaction data to identify customer segments and patterns through exploratory data analysis (EDA) and machine learning clustering techniques. The dashboard provides interactive visualizations to explore customer behaviors, transaction patterns, and utilization ratios across different demographics.

## Project Structure

```
.
├── README.md
├── .gitignore
├── dashboard/
│   └── app.py                          # Main Dash application
├── data/
│   ├── bank_transactions.csv           # Raw transaction data
│   └── bank_transactions_cleaned.csv   # Processed and cleaned data
└── EDA/
    └── main.ipynb                      # Exploratory Data Analysis notebook
```

## Dataset Features

**Dataset Source**: [Bank Customer Segmentation Dataset](https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation)

The cleaned dataset includes the following columns:
- `CustGender`: Customer gender (M/F)
- `CustLocation`: Customer location/city
- `CustAccountBalance`: Customer's account balance
- `TransactionDate`: Date of transaction
- `TransactionTime`: Time of transaction
- `TransactionAmount`: Transaction amount in INR
- `Age`: Customer age
- `UtilizationRatio`: Calculated utilization ratio
- `TransactionMonth`: Extracted month from transaction date
- Various cluster labels from ML analysis

## Features

### Data Analysis & Clustering
- **Customer Segmentation**: Multiple clustering algorithms applied to identify distinct customer groups
- **Balance-Transaction Clustering**: Segments customers based on account balance and transaction amounts
- **Age-Ratio Clustering**: Groups customers by age and utilization ratio patterns
- **Gender-Transaction Clustering**: Analyzes transaction patterns by gender demographics

### Interactive Dashboard
- **Real-time Filtering**: Month-based sliders for temporal analysis
- **Multiple Visualizations**: Scatter plots, bar charts, heatmaps, and pie charts
- **Key Metrics Display**: Total balances, transaction amounts, and customer statistics
- **Correlation Analysis**: Feature correlation heatmap for understanding relationships

### Key Metrics Tracked
- Total Customer Account Balance
- Total Transaction Amount
- Maximum Customer Account Balance
- Number of High-Transaction Locations
- Customer Distribution by Gender and Location
- Utilization Ratio Analysis by Age Groups

## Dataset Features

The cleaned dataset includes the following columns:
- `CustGender`: Customer gender (M/F)
- `CustLocation`: Customer location/city
- `CustAccountBalance`: Customer's account balance
- `TransactionDate`: Date of transaction
- `TransactionTime`: Time of transaction
- `TransactionAmount`: Transaction amount in INR
- `Age`: Customer age
- `UtilizationRatio`: Calculated utilization ratio
- `TransactionMonth`: Extracted month from transaction date
- Various cluster labels from ML analysis

## Installation & Setup

### Prerequisites
- Python 3.7+
- Required packages (install via pip):

```bash
pip install dash pandas plotly numpy matplotlib seaborn
```

### Running the Dashboard

1. Navigate to the dashboard directory:
```bash
cd dashboard
```

2. Run the Dash application:
```bash
python app.py
```

3. Open your browser and go to `http://127.0.0.1:8050`

## Key Insights from Analysis

### Customer Utilization Patterns
- Younger customers (ages 18-22) show higher utilization ratios compared to older customers
- Ages 20-21 have the highest mean utilization rates
- Ages 38-50 demonstrate lower utilization patterns

### Transaction Behavior
- Utilization ratios range from 0.00 to 100%, indicating varying resource utilization
- Strong correlation patterns between account balance, transaction amounts, and customer demographics
- Location-based analysis reveals geographic transaction patterns

### Clustering Results
- Multiple customer segments identified through PCA and K-means clustering
- Distinct patterns in balance vs. transaction amount relationships
- Age-based segmentation reveals behavioral differences across age groups

## Dashboard Components

### Tab 1: Cluster Analysis
- **First Cluster**: Customer Account Balance vs Transaction Amount
- **Second Cluster**: Age vs Utilization Ratio patterns
- **Third Cluster**: Transaction Amount vs Utilization Ratio

### Tab 2: Interactive Analysis
- **Utilization Ratio View**: Balance vs Transaction with utilization ratio sizing
- **Transaction Amount View**: Size-based transaction amount analysis
- **Transaction Count View**: Count-based transaction patterns

### Additional Visualizations
- Monthly transaction trends by gender
- Customer age distribution
- Geographic utilization ratio analysis
- Customer gender distribution pie chart

## Data Processing

The project includes comprehensive data cleaning and preprocessing:
- Handling missing values and outliers
- Feature engineering for utilization ratios
- Date/time processing for temporal analysis
- Clustering algorithm implementation with PCA

## Future Enhancements

- Real-time data integration
- Additional clustering algorithms
- Predictive modeling for customer behavior
- Advanced filtering and drill-down capabilities
- Export functionality for reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational and analytical purposes.