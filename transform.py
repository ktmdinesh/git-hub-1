
def transform(records):
    cleaned = []
    for r in records:
        if r.get("quantity") is None or r.get("unit_price") is None:
            continue
        r["revenue"] = r["quantity"] * r["unit_price"]
        cleaned.append(r)
    return cleaned
