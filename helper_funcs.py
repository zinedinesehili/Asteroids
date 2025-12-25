def truncate_float(num):
    """
    This function takes in a float and shortens the floating point
    values to 2 floating values
    """

    truncated = f"{num:.2f}"
    return float(truncated)