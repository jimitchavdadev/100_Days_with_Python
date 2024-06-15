def calc_paint(width, height, cover):
    """Calculates the amount of paint needed."""
    width = float(width)
    height = float(height)
    cover = float(cover)
    ans = (width * height) / cover
    return ans

# Test the function with float arguments
print(calc_paint(10.0, 5.0, 5.0))