import pandas as pd
from app.utils.logger import logger


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Cleaning dataset...")

    df = df.dropna(subset=["Invoice", "Quantity", "Price"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    df = df[df["Quantity"] > 0]
    df = df[df["Price"] > 0]

    df["TotalAmount"] = df["Quantity"] * df["Price"]

    logger.info(f"Cleaned rows count: {len(df)}")
    return df


def generate_summary(df: pd.DataFrame) -> dict:
    logger.info("Generating aggregate summary...")

    summary = {
        "total_revenue": round(df["TotalAmount"].sum(), 2),
        "total_orders": int(df["Invoice"].nunique()),
        "top_country": df.groupby("Country")["TotalAmount"].sum().idxmax(),
        "top_products": (
            df.groupby("Description")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .to_dict()
        ),
    }

    return summary
