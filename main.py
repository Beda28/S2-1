from src.load   import load, load_image
from src.visual import line, plot
from src.math   import (unit_circle, rotation, scaling, shearing, transform)

def main():
    date, price = load("data/car_price.csv")
    image       = load_image("data/sample.png")

    date = [d[2:].replace("-", ".") for d in date]

    line(
        date, price,
        "Car Price Dataset",
        "Date", "Price (10,000 KRW)",
        "outputs/car_price.png"
    )

    circle = unit_circle()

    matrices = {
        "rotation": rotation(45),
        "scaling" : scaling(2, 0.5),
        "shearing": shearing(1)
    }

    for name, matrix in matrices.items():
        result = transform(circle, matrix)

        plot(
            circle, result, name.capitalize(),
            f"outputs/{name}.png"
        )

if __name__ == "__main__":
    main()
