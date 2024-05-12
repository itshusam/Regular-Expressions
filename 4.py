import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]


electronics_keywords = ["smartphone", "tablet", "laptop"]
apparel_keywords = ["t-shirt", "shirt", "jeans", "dress"]
kitchen_keywords = ["knife", "kitchen", "cookware"]


def tag_product(description):
    for keyword in electronics_keywords:
        if re.search(keyword, description, re.IGNORECASE):
            return "Electronics"
    for keyword in apparel_keywords:
        if re.search(keyword, description, re.IGNORECASE):
            return "Apparel"
    for keyword in kitchen_keywords:
        if re.search(keyword, description, re.IGNORECASE):
            return "Home & Kitchen"
    return "Other"


tagged_products = [tag_product(description) for description in descriptions]


for i, description in enumerate(descriptions):
    print(f"Product {i+1}: {description} - Tag: {tagged_products[i]}")