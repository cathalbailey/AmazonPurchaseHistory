import pandas as pd


def calculate_amazon_spending(csv_file_path):
    # Load the CSV data into a DataFrame
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
        return None

    # Filter out orders with 'Item Total' column and 'Shipment Date' column
    df = df[['Shipment Date', 'Item Total']]

    # Convert 'Item Total' column to a numeric type (removing '$' sign)
    df['Item Total'] = df['Item Total'].str.replace('$', '').astype(float)

    # Group by shipment date and sum the spending for each date
    spending_by_date = df.groupby('Shipment Date')['Item Total'].sum()

    # Calculate total spending
    total_spending = spending_by_date.sum()

    return total_spending


if __name__ == "__main__":
    csv_file_path = "path/to/your/amazon_purchase_history.csv"
    total_spending = calculate_amazon_spending(csv_file_path)

    if total_spending is not None:
        print(f"Total spending on Amazon: ${total_spending:.2f}")
