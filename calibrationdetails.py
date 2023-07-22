
meters = {
    "solar_meter": [
        { "raw": 0, "actual": 0.0 },
        # { "raw": 443, "actual": 100.0 },
        # { "raw": 500, "actual": 108.0 },
        # { "raw": 520, "actual": 114.0 },
        { "raw": 533, "actual": 110.0 },
        { "raw": 536, "actual": 112.0 },
    ],
    "dc_meter": [
        # From the handheld clamp meter
        # { "raw": (1984-1909), "actual": 9.0 },
        # { "raw": (2021-1909), "actual": 16.0 },
        # { "raw": (2045-1909), "actual": 13.6 },
        # { "raw": (2056-1909), "actual": 14.0 },

        # From Inverter's meter
        # { "raw": (1895-1909), "actual": 0.0 },
        # { "raw": (1932-1909), "actual": 5.5 },
        # { "raw": (2087-1909), "actual": 30.0 },

        # From the new solar meter
        { "raw": (1909-1909), "actual": 0.0 },
        # { "raw": (1921-1909), "actual": 3.74 },
        # { "raw": (1945-1909), "actual": 5.39 },
        # { "raw": (1946-1909), "actual": 5.53 },
        # { "raw": (1948-1909), "actual": 5.89 },
        # { "raw": (1949-1909), "actual": 5.69 },
        { "raw": (1957-1909), "actual": 6.39 },
    ],
    "grid_meter": [
        { "raw": 44, "actual": 1.98 },
        { "raw": 45, "actual": 2.2 },
        { "raw": 78, "actual": 3.0 },
        { "raw": 87, "actual": 3.16 },
        { "raw": 116, "actual": 3.84 },
        { "raw": 120, "actual": 4.0 },
        { "raw": 137, "actual": 4.01 },
        { "raw": 145, "actual": 4.7 },
        { "raw": 650, "actual": 14.2 },
    ],
    "load_meter": [
        # { "raw": 0, "actual": 1.0 },
        { "raw": 18, "actual": 1.6 },
        { "raw": 28, "actual": 1.72 },
        { "raw": 35, "actual": 2.25 },
        { "raw": 371, "actual": 8.72 },
        { "raw": 744, "actual": 15.32 },
    ]
}



def find_coefficients(meter_values):
    total = len(meter_values)
    first_half = total // 2

    dp_1 = {
        "raw": 0, "actual": 0
    }
    dp_2 = {
        "raw": 0, "actual": 0
    }

    total_raw, total_actual = 0, 0
    for idx in range(0, first_half):
        total_raw += meter_values[idx]["raw"]
        total_actual += meter_values[idx]["actual"]

    dp_1["raw"] = total_raw / first_half
    dp_1["actual"] = total_actual / first_half

    total_raw, total_actual = 0, 0
    for idx in range(first_half, total):
        total_raw += meter_values[idx]["raw"]
        total_actual += meter_values[idx]["actual"]

    dp_2["raw"] = total_raw / first_half
    dp_2["actual"] = total_actual / first_half


    m = (dp_2["actual"] - dp_1["actual"]) / (dp_2["raw"] - dp_1["raw"])
    c = dp_2["actual"] - m*dp_2["raw"]

    return (m*1000, c*1000)


if __name__ == "__main__":
    for meter in meters:
        print(f"{meter}: {find_coefficients(meters[meter])}")
