# 📊 Google Trends Analyzer

A Python-based tool that analyzes Google search trends using the **Pytrends** API to extract, visualize, and interpret keyword insights over time, region, and related queries.

## 🚀 Features

- **Interest Over Time**: Analyze keyword popularity trends over a specified timeframe.  
- **Historical Hourly Interest**: Fetch hourly interest data for deeper time-specific analysis.  
- **Interest by Region**: Identify which regions search for a keyword the most.  
- **Top Charts**: Discover the most searched topics for a given year.  
- **Related Queries**: Explore related search terms for a given keyword.  
- **Keyword Suggestions**: Get keyword suggestions to expand your search analysis.  

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/rohitinu6/Google-Trends-Analyser.git
cd Google-Trends-Analyser
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 📊 Usage

Run the script to fetch Google Trends data:

```bash
python main.py
```

### Example Output:
- **Interest Over Time**: View keyword popularity over a period.  
- **Interest by Region**: Identify the top regions searching for the keyword.  
- **Related Queries**: Get insights on related searches.  
- **Keyword Suggestions**: Discover alternative keywords.

## 📂 Project Structure

```
Google-Trends-Analyser/
├── main.py             # Main script to analyze Google Trends
└── requirements.txt    # Python dependencies
```

## 📌 Requirements

- Python 3.10+
- `pytrends`
- `pandas`
- `matplotlib`
- `requests`

## 📣 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## 📄 License

This project is licensed under the **Apache 2.0 License**.
