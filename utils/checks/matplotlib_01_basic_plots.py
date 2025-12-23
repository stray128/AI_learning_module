from utils.checker import check
import numpy as np

def p1(fig, ax):
    check.is_not_none(fig, "P1a: Figure created")
    check.is_not_none(ax, "P1b: Axes created")

def p2(title_text):
    check.is_type(title_text, str, "P2: Type check")
    check.is_true(title_text == 'Quadratic Function', "P2: Correct title", "Title should be 'Quadratic Function'")

def p3(scatter):
    check.is_not_none(scatter, "P3: Scatter plot created")

def p4(bars):
    check.is_not_none(bars, "P4: Bar chart created")

def p5(line_color):
    check.is_not_none(line_color, "P5: Line color set")
    check.is_true(line_color in ['red', 'r'], "P5: Correct color", "Line should be red")

def p6(line_style):
    check.is_not_none(line_style, "P6: Line style set")
    check.is_true(line_style in ['--', 'dashed'], "P6: Correct style", "Line should be dashed")

def p7(num_lines):
    check.is_type(num_lines, int, "P7: Type check")
    check.is_true(num_lines == 2, "P7: Correct number of lines", "Should have 2 lines (sin and cos)")

def p8(legend):
    check.is_not_none(legend, "P8: Legend created")

def p9(scatter):
    check.is_not_none(scatter, "P9: Colored scatter plot created")

def p10(bars):
    check.is_not_none(bars, "P10: Horizontal bar chart created")

def p11(xlim, ylim):
    check.is_true(xlim == (0, 5), "P11a: X-axis limits", "X-axis should be [0, 5]")
    check.is_true(ylim == (-2, 2), "P11b: Y-axis limits", "Y-axis should be [-2, 2]")

def p12(scatter):
    check.is_not_none(scatter, "P12: Scatter with variable sizes created")

def p13(bars1, bars2):
    check.is_not_none(bars1, "P13a: First bar group created")
    check.is_not_none(bars2, "P13b: Second bar group created")

def p14(bars_bottom, bars_top):
    check.is_not_none(bars_bottom, "P14a: Bottom bars created")
    check.is_not_none(bars_top, "P14b: Top bars created")

def p15(marker):
    check.is_not_none(marker, "P15: Marker set")
    check.is_true(marker == 'o', "P15: Correct marker", "Marker should be 'o' (circle)")

def p16(grid_on):
    check.is_type(grid_on, bool, "P16: Type check")
    check.is_true(grid_on, "P16: Grid enabled", "Grid should be visible")

def p17(annotation):
    check.is_not_none(annotation, "P17: Annotation created")
