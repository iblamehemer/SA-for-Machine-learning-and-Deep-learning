def map_class_to_bin(predicted_class: str) -> str:
    biodegradable = ["organic", "food_waste", "paper", "cardboard"]
    recyclable = ["plastic", "glass", "metal", "can", "bottle", "cloth"]
    hazardous = ["battery", "medical_waste", "e_waste", "chemical"]

    pc = predicted_class.lower().strip()

    if pc in biodegradable:
        return "🟢 Green Bin (Biodegradable)"
    elif pc in recyclable:
        return "🔵 Blue Bin (Recyclable)"
    elif pc in hazardous:
        return "🔴 Red Bin (Hazardous)"
    else:
        return "⚪ General Waste / Not Mapped"