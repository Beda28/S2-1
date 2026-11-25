from src.load   import load, load_image
from src.visual import line

def main():
    date, price = load("data/car_price.csv")
    image       = load_image("data/sample.png")

    date = [date[2:].replace("-", ".") for date in date]

    line(
        date, price,
        "Car Price Dataset",
        "Date", "Price (10,000 KRW)",
        "outputs/car_price.png"
    )

if __name__ == "__main__":
    main()
