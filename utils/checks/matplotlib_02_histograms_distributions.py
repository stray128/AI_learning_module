from utils.checker import check
import numpy as np

def p1(n, bins):
    check.is_not_none(n, "P1a: Histogram counts returned")
    check.is_not_none(bins, "P1b: Bin edges returned")

def p2(num_bins):
    check.is_type(num_bins, int, "P2: Type check")
    check.is_true(num_bins == 20, "P2: Correct bin count", "Should have exactly 20 bins")

def p3(bp):
    check.is_not_none(bp, "P3: Box plot created")

def p4(wedges):
    check.is_not_none(wedges, "P4: Pie chart created")

def p5(green_value):
    check.is_not_none(green_value, "P5: Color extracted")
    check.is_true(green_value > 0.4, "P5: Green component", "Should be green color")

def p6(edge_sum):
    check.is_not_none(edge_sum, "P6: Edge color extracted")
    check.is_true(edge_sum < 0.1, "P6: Black edge color", "Edge color should be black (sum close to 0)")

def p7(bp):
    check.is_not_none(bp, "P7: Multiple box plots created")

def p8(area):
    check.is_not_none(area, "P8: Area calculated")
    check.is_true(abs(area - 1.0) < 0.01, "P8: Area sums to 1", "Area should be approximately 1.0")

def p9(n1, n2):
    check.is_not_none(n1, "P9a: First histogram created")
    check.is_not_none(n2, "P9b: Second histogram created")

def p10(wedges):
    check.is_not_none(wedges, "P10: Exploded pie chart created")

def p11(bp):
    check.is_not_none(bp, "P11: Notched box plot created")

def p12(bp):
    check.is_not_none(bp, "P12: Horizontal box plot created")

def p13(vp):
    check.is_not_none(vp, "P13: Violin plot created")

def p14(bins):
    check.is_not_none(bins, "P14a: Bins created")
    check.is_true(len(bins) == 7, "P14b: Correct number of bin edges", "Should have 7 bin edges")
    check.is_true(all(bins == [-3, -2, -1, 0, 1, 2, 3]), "P14c: Bins match custom", "Bins should match custom_bins list")

def p15(h):
    check.is_not_none(h, "P15: 2D histogram created")

def p16(autotexts):
    check.is_not_none(autotexts, "P16: Pie chart with percentages created")

def p17(n):
    check.is_not_none(n, "P17: Step histogram created")
