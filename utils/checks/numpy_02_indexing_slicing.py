from utils.checker import check
import numpy as np

def p1(elem):
    check.is_not_none(elem, "P1: Value check")
    check.is_true(elem == 3, "P1: Element value", "Should be the element at index 3")

def p2(last):
    check.is_not_none(last, "P2: Value check")
    check.is_true(last == 9, "P2: Last element value", "Should be the last element")

def p3(slice_arr):
    check.is_type(slice_arr, np.ndarray, "P3: Type check")
    check.has_length(slice_arr, 3, "P3: Length check")
    check.first_element_is(slice_arr, 2, "P3: First element")
    check.last_element_is(slice_arr, 4, "P3: Last element")

def p4(elem_2d):
    check.is_not_none(elem_2d, "P4: Value check")
    check.is_true(elem_2d == 6, "P4: Element value", "Should be the element at row 1, column 2")

def p5(row):
    check.is_type(row, np.ndarray, "P5: Type check")
    check.has_length(row, 4, "P5: Length check")
    check.first_element_is(row, 4, "P5: First element")
    check.last_element_is(row, 7, "P5: Last element")

def p6(col):
    check.is_type(col, np.ndarray, "P6: Type check")
    check.has_length(col, 3, "P6: Length check")
    check.first_element_is(col, 2, "P6: First element")
    check.last_element_is(col, 10, "P6: Last element")

def p7(every_other):
    check.is_type(every_other, np.ndarray, "P7: Type check")
    check.has_length(every_other, 5, "P7: Length check")
    check.first_element_is(every_other, 0, "P7: First element")
    check.last_element_is(every_other, 8, "P7: Last element")
    check.is_true(np.all(every_other % 2 == 0), "P7: Even numbers", "All elements should be even")

def p8(reversed_arr):
    check.is_type(reversed_arr, np.ndarray, "P8: Type check")
    check.has_length(reversed_arr, 10, "P8: Length check")
    check.first_element_is(reversed_arr, 9, "P8: First element")
    check.last_element_is(reversed_arr, 0, "P8: Last element")
    check.is_sorted(reversed_arr, "P8: Sorted check", ascending=False)

def p9(sub_arr):
    check.is_type(sub_arr, np.ndarray, "P9: Type check")
    check.has_shape(sub_arr, (2, 2), "P9: Shape check")
    check.first_element_is(sub_arr.flatten(), 1, "P9: First element")
    check.element_at_is(sub_arr, (1, 1), 6, "P9: Element at [1,1]")

def p10(greater_5):
    check.is_type(greater_5, np.ndarray, "P10: Type check")
    check.has_length(greater_5, 4, "P10: Length check")
    check.all_values_in_range(greater_5, 6, 10, "P10: Range check")
    check.first_element_is(greater_5, 6, "P10: First element")
    check.last_element_is(greater_5, 9, "P10: Last element")

def p11(between):
    check.is_type(between, np.ndarray, "P11: Type check")
    check.has_length(between, 4, "P11: Length check")
    check.all_values_in_range(between, 3, 6, "P11: Range check")
    check.first_element_is(between, 3, "P11: First element")
    check.last_element_is(between, 6, "P11: Last element")

def p12(fancy):
    check.is_type(fancy, np.ndarray, "P12: Type check")
    check.has_length(fancy, 3, "P12: Length check")
    check.first_element_is(fancy, 1, "P12: First element")
    check.element_at_is(fancy, 1, 3, "P12: Second element")
    check.last_element_is(fancy, 7, "P12: Last element")

def p13(fancy_2d):
    check.is_type(fancy_2d, np.ndarray, "P13: Type check")
    check.has_length(fancy_2d, 3, "P13: Length check")
    check.first_element_is(fancy_2d, 0, "P13: First element")
    check.element_at_is(fancy_2d, 1, 6, "P13: Second element")
    check.last_element_is(fancy_2d, 11, "P13: Last element")

def p14(replaced):
    check.is_type(replaced, np.ndarray, "P14: Type check")
    check.has_length(replaced, 10, "P14: Length check")
    check.first_element_is(replaced, 0, "P14: First element")
    check.element_at_is(replaced, 5, 5, "P14: Element at index 5")
    check.max_value_is(replaced, 5, "P14: Maximum value")
    check.min_value_is(replaced, -1, "P14: Minimum value")

def p15(even_indices):
    check.is_type(even_indices, np.ndarray, "P15: Type check")
    check.has_length(even_indices, 5, "P15: Length check")
    check.first_element_is(even_indices, 0, "P15: First element")
    check.last_element_is(even_indices, 8, "P15: Last element")
    check.is_true(np.all(even_indices % 2 == 0), "P15: Even indices", "All indices should be even")
