
def transform(records):
    for r in records:
        r["revenue"] = r["quantity"] * r["unit_price"]
    return records
