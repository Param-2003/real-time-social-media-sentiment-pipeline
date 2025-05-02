# 🏏 IPL Tweet Sentiment Analysis (2020–2022)

This project analyzes Twitter sentiment around the Indian Premier League (IPL) using **PySpark** and **VADER NLP**, handling over 100k tweets across 3 seasons.

---

## 📈 Features

- 🔥 PySpark-based big data processing
- 🔍 VADER sentiment analysis (positive, neutral, negative)
- 📊 Visualizations (bar + pie)
- 📁 Clean CSV output for dashboards
- ✅ Ready for Looker / Tableau / Power BI

---

## 🛠️ Tech Stack

| Component        | Tool                     |
|------------------|---------------------------|
| ETL & Processing | PySpark (DataFrame API)   |
| NLP              | VADER Sentiment Analyzer  |
| Visualization    | Seaborn + Matplotlib      |
| Dashboard        | Looker Studio / Power BI  |
| Environment      | Jupyter + Anaconda        |

---

## 📂 Dataset

- Tweets collected across **IPL 2020, 2021, 2022**
- Cleaned for nulls & irrelevant fields
- ~100K tweets analyzed

---

## 📊 Visuals

### Sentiment Distribution
![bar](visualizations/sentiment_bar_chart.png)

### Sentiment Share
![pie](visualizations/sentiment_pie_chart.png)

---

## 📁 Output

Final sentiment-tagged tweets: http://localhost:8889/files/ipl_sentiment_final.csv?_xsrf=2%7C7c29b734%7C367a81522f655a42e332f04b2d1ba7e0%7C1745982402

