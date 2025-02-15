# Viral Infections Tracker Dashboard
[CLick here to see the dahsboard live] ()
## Overview
An interactive dashboard that tracks and visualizes viral infection data from around the world using data from the World Health Organization (WHO). The dashboard includes various visualizations such as choropleth maps, line charts, pie charts, and top 10 rankings to provide comprehensive insights into viral infection patterns.

## Features
- Real-time data updates through daily web scraping of WHO's FluNet database
- Interactive world map showing infection distribution
- Comparative analysis tools for different viruses and regions
- Time series analysis of infection trends
- Top 10 rankings of most affected countries
- Positive/negative test rate visualization by country

## Prerequisites
- Python 3.12+
- pip3 (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/viral-infections-tracker.git
cd viral-infections-tracker
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
viral-infections-tracker/
├── app.py                 # Main dashboard application
├── scraping.py           # Data scraping script
├── ploomber-cloud.yaml   # Ploomber Cloud configuration
├── requirements.txt      # Project dependencies
├── data_flunet.csv    #scraped data
├──map.py
├──pie.py
├──TOP10.py
├──topweek.py
├──line_chart.py
├──map.json     
└── assets/
    └── style.css        # Dashboard styling
```

## Running Locally

1. Start the data scraper:
```bash
python scraping.py
```

2. Launch the dashboard:
```bash
python app.py
```

3. Open your web browser and navigate to `http://localhost:8050`

## Deployment on Ploomber Cloud

1. Ensure you have a Ploomber Cloud account and the Ploomber CLI installed:
```bash
pip install ploomber-cloud
```

2. Login to Ploomber Cloud:
```bash
ploomber-cloud login
```

3. Deploy the application:
```bash
ploomber-cloud deploy
```

The deployment configuration will:
- Run the data scraper daily at 00:00 UTC
- Update the dashboard daily at 00:15 UTC
- Make the dashboard accessible via a provided URL

## Dashboard Components

### 1. Positive and Negative Tests Rate
- Pie chart showing the distribution of test results by country
- Updated weekly with the latest available data

### 2. Top 10 Weekly Infections
- Bar chart displaying the countries with highest infection rates
- Filterable by virus type
- Weekly updates based on new data

### 3. Global Distribution Map
- Choropleth map showing infection distribution
- Color-coded by infection intensity
- Filterable by virus type

### 4. Time Series Analysis
- Line chart showing infection trends over time
- Multiple country and virus selection
- Regional filtering options

### 5. Annual Statistics
- Top 10 most affected countries in the current year
- Total reported cases by country

## Data Sources
- World Health Organization's FluNet database
- Data is automatically updated daily through web scraping

## Contributors
- [AGODE M.](https://moise-agode.github.io/)
- [BETE E.](https://eden-bete.github.io/portfolio/)
- [DENIS T.](https://www.theo-denis.com/Portfolio%20-%20English.html)
- [MIEMO B.](https://borgiamiemo.github.io/Portfolio/)
- [SORO C.](https://christelle-soro.github.io/portfolio/)


## Troubleshooting

### Common Issues

1. Data not updating:
   - Check internet connection
   - Verify WHO's FluNet website accessibility
   - Check scraping script logs

2. Dashboard not loading:
   - Ensure all dependencies are installed
   - Verify data file exists and is not corrupted
   - Check console for error messages

### Support
For issues and feature requests, please open an issue on the GitHub repository.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request