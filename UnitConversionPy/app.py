import webview

class ConverterAPI:
    def __init__(self):
        self.length_units = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "dm": 10,
            "hm": 100,
            "km": 1000,
            "in": 0.0254,
            "ft": 0.3048,
            "yd": 0.9144,
            "mi": 1609.34
        }

    def convert(self, category, from_unit, to_unit, value):
        try:
            value = float(value)
        except:
            return "Invalid input"

        if category == "length":
            base = value * self.length_units[from_unit]
            return round(base / self.length_units[to_unit], 6)

        if category == "temperature":
            c = self.to_celsius(value, from_unit)
            return round(self.from_celsius(c, to_unit), 6)

        return "Error"

    def to_celsius(self, value, unit):
        if unit == "c":
            return value
        if unit == "f":
            return (value - 32) * 5 / 9
        if unit == "k":
            return value - 273.15

    def from_celsius(self, value, unit):
        if unit == "c":
            return value
        if unit == "f":
            return value * 9 / 5 + 32
        if unit == "k":
            return value + 273.15


if __name__ == "__main__":
    webview.create_window(
        "Unit Converter",
        "app.html",
        js_api=ConverterAPI(),
        width=420,
        height=520
    )
    webview.start()
