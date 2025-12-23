from utils.checker import check
import numpy as np

def p1(fig, axes):
    check.is_not_none(fig, "P1a: Figure created")
    check.is_not_none(axes, "P1b: Axes array created")
    check.is_true(hasattr(axes, 'shape') and axes.shape == (2, 2), "P1c: Correct shape", "Axes should be 2x2 array")

def p2(fig_size):
    check.is_not_none(fig_size, "P2: Figure size retrieved")
    check.is_true(tuple(fig_size) == (10.0, 6.0), "P2: Correct size", "Figure should be 10x6 inches")

def p3(num_axes):
    check.is_type(num_axes, int, "P3: Type check")
    check.is_true(num_axes == 3, "P3: Correct number of subplots", "Should have 3 subplots")

def p4(suptitle):
    check.is_type(suptitle, str, "P4: Type check")
    check.is_true(suptitle == 'My Figure Title', "P4: Correct title", "Super title should be 'My Figure Title'")

def p5(axes):
    check.is_not_none(axes, "P5: Shared y-axis subplots created")

def p6(tick_labels):
    check.is_not_none(tick_labels, "P6: Tick labels retrieved")
    check.is_true(tick_labels == ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], "P6: Correct labels", "Tick labels should match the days of the week")

def p7(rotation):
    check.is_not_none(rotation, "P7: Rotation retrieved")
    check.is_true(rotation == 45.0, "P7: Correct rotation", "Labels should be rotated 45 degrees")

def p8(title_fontsize):
    check.is_not_none(title_fontsize, "P8: Font size retrieved")
    check.is_true(title_fontsize == 16.0, "P8: Correct font size", "Title font size should be 16")

def p9(style_used):
    check.is_true(style_used == 'ggplot', "P9: Style used", "Should use 'ggplot' style")

def p10(text):
    check.is_not_none(text, "P10: Text annotation added")

def p11(ax_inset):
    check.is_not_none(ax_inset, "P11: Inset axes created")

def p12(file_exists):
    check.is_true(file_exists, "P12: File saved", "File should be saved")

def p13(ax1, ax2, ax3):
    check.is_not_none(ax1, "P13a: First subplot created")
    check.is_not_none(ax2, "P13b: Second subplot created")
    check.is_not_none(ax3, "P13c: Third subplot created")

def p14(ax2):
    check.is_not_none(ax2, "P14: Twin axes created")

def p15(y_scale):
    check.is_not_none(y_scale, "P15: Scale type retrieved")
    check.is_true(y_scale == 'log', "P15: Correct scale", "Y-axis should be logarithmic")

def p16(file_exists, file_size):
    check.is_true(file_exists, "P16a: File saved", "File should be saved")
    check.is_true(file_size > 10000, "P16b: High DPI file size", "High DPI file should be reasonably large")
