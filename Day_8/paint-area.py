def calc_paint(width, height, cover):
    width=float(width)
    height=float(height)
    cover=float(cover)
    ans=(width*height)/cover
    return ans

print(calc_paint(10,5,5))