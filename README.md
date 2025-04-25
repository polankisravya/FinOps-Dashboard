
# 💰 FinOps Dashboard (Offline Version)

This project is a simple FinOps (Financial Operations) dashboard built using **Python**, **SQLite**, and **Grafana** — fully offline, without any cloud or Docker setup.

## 🧠 Objective

To simulate and visualize daily cloud cost data for multiple services using local tools. This project helps understand cost visibility and tracking without relying on actual cloud billing APIs.

## 📦 Tools Used

- **Python 3**: To generate mock billing data.
- **SQLite**: Lightweight embedded database to store usage data.
- **Grafana**: Open-source visualization tool to create dashboards.

## 📁 Project Files

- `mock_usage.py`: Python script to generate mock usage data.
- `usage.db`: SQLite database file with generated data.
- `FinOps_Report.pdf`: Final 1-page report for submission.
- `README.md`: This file!

## 🧪 How It Works

1. Run the Python script:
   ```bash
   python mock_usage.py
   ```
   This creates a SQLite database (`usage.db`) with simulated usage data for:
   - Compute Engine
   - Cloud Storage
   - Cloud Functions

2. Open **Grafana** at [http://localhost:3000](http://localhost:3000)
3. Add `usage.db` as a **SQLite data source**
4. Create a dashboard using this SQL:
   ```sql
   SELECT date, SUM(amount) as total FROM usage GROUP BY date ORDER BY date;
   ```
5. Visualize as a bar chart or line graph.

## 📸 Sample Output

> Insert a screenshot of your Grafana dashboard here (optional)

## ✅ Deliverables

- ✔️ Working Python script
- ✔️ Database with mock data
- ✔️ Grafana dashboard showing daily cost trends
- ✔️ Report PDF with all details

## 📚 Learning Outcomes

- Hands-on experience with Grafana
- Simulated cost visibility without cloud setup
- Understanding of FinOps basics and dashboarding

---

**Project by:** *[Your Name]*  
**Date:** *April 2025*
