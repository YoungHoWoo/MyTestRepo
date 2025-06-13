import pandas as pd
import plotly.express as px
import plotly.offline as pyo

SPREADSHEET_ID = "1oWu5j9FzCiT2P9a32iw5qplwO0MbVstYUuptodBU4zw/"
SPREADSHEET_CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}export?format=csv"
)

# Specify columns corresponding to projects in the Google Sheet
PROJECT_COLUMNS = ["Project A", "Project B"]
DATE_COLUMN = "Date"


def load_data(url: str) -> pd.DataFrame:
    """Load CSV data from Google Sheets"""
    return pd.read_csv(url, parse_dates=[DATE_COLUMN])


def generate_plot(df: pd.DataFrame) -> str:
    """Generate a Plotly line chart HTML"""
    melted = df.melt(id_vars=[DATE_COLUMN], value_vars=PROJECT_COLUMNS, var_name="Project", value_name="Value")
    fig = px.line(melted, x=DATE_COLUMN, y="Value", color="Project", title="Project Comparison")
    fig.update_layout(template="plotly_white")
    return pyo.plot(fig, output_type="div", include_plotlyjs="cdn")


def main():
    data = load_data(SPREADSHEET_CSV_URL)
    plot_div = generate_plot(data)
    html = f"""
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Project Comparison</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; }}
            h1 {{ text-align: center; }}
            .chart {{ max-width: 800px; margin: auto; }}
        </style>
    </head>
    <body>
        <h1>Project Comparison</h1>
        <div class=\"chart\">{plot_div}</div>
    </body>
    </html>
    """
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated output.html")


if __name__ == "__main__":
    main()
