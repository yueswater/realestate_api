def convert_to_roc_year(year: int) -> int:
    if year > 1000:
        year -= 1911
    return year