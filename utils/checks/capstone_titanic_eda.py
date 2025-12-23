"""
Verification functions for Capstone Project 1: Titanic Dataset - Complete EDA
"""

from utils.checker import check
import numpy as np
import pandas as pd


def p0(g):
    """Verify library imports"""
    check.is_true('np' in g, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in g, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('plt' in g, "P0c: Matplotlib imported", "Import matplotlib.pyplot as plt")
    check.is_true('sns' in g, "P0d: Seaborn imported", "Import seaborn as sns")


def p1(df):
    """Verify Titanic dataset loaded correctly"""
    check.is_type(df, pd.DataFrame, "P1: Type check")
    check.is_true(len(df) > 800, "P1: Row count", "Should have more than 800 rows")
    check.contains_column(df, 'Survived', "P1: Has Survived column")


def p2(missing_df, df):
    """Verify missing data analysis"""
    check.is_type(missing_df, pd.DataFrame, "P2: Type check")
    check.contains_column(missing_df, 'missing_count', "P2: Has missing_count column")
    check.contains_column(missing_df, 'missing_pct', "P2: Has missing_pct column")
    check.is_true(missing_df.loc['Age', 'missing_count'] > 0, "P2: Age has missing values", "Age should have missing values")


def p3(survival_rate):
    """Verify overall survival rate calculation"""
    check.is_type(survival_rate, (int, float), "P3: Type check")
    check.value_in_range(survival_rate, 35, 42, "P3: Survival rate in expected range")


def p4(survival_by_gender):
    """Verify survival rate by gender"""
    check.is_type(survival_by_gender, pd.Series, "P4: Type check")
    check.is_true(survival_by_gender['female'] > survival_by_gender['male'], "P4: Female survival higher", "Females should have higher survival rate")
    check.is_true(survival_by_gender['female'] > 70, "P4: Female rate above 70%", "Female survival rate should be above 70%")


def p5(survival_by_class):
    """Verify survival rate by passenger class"""
    check.is_type(survival_by_class, pd.Series, "P5: Type check")
    check.has_length(survival_by_class, 3, "P5: Has 3 classes")
    check.is_true(survival_by_class.idxmax() == 1, "P5: Class 1 has highest survival", "First class should have highest survival rate")
    check.is_true(survival_by_class[1] > 60, "P5: Class 1 above 60%", "First class survival should be above 60%")


def p6(fig):
    """Verify survival by gender visualization"""
    check.is_not_none(fig, "P6: Figure created")


def p7(axes):
    """Verify age distribution analysis"""
    check.is_not_none(axes, "P7: Axes created")
    check.has_length(axes, 2, "P7: Has 2 subplots")


def p8(df_clean, missing_ages_after):
    """Verify missing age values handled"""
    check.is_type(df_clean, pd.DataFrame, "P8: Type check")
    check.is_true(missing_ages_after == 0, "P8: No missing ages", "All ages should be filled")
    check.is_true(df_clean['Age'].min() > 0, "P8: Positive ages", "All ages should be positive")


def p9(df_clean):
    """Verify age groups created"""
    check.contains_column(df_clean, 'age_group', "P9: Column created")
    check.is_true(df_clean['age_group'].nunique() == 4, "P9: Has 4 categories", "Should have 4 age group categories")


def p10(survival_by_age):
    """Verify survival by age group"""
    check.is_type(survival_by_age, pd.Series, "P10: Type check")
    check.has_length(survival_by_age, 4, "P10: Has 4 groups")
    check.is_true(survival_by_age['Child'] > 50, "P10: Children survival high", "Children should have >50% survival rate")


def p11(fare_by_survival):
    """Verify fare analysis"""
    check.is_type(fare_by_survival, pd.Series, "P11: Type check")
    check.has_length(fare_by_survival, 2, "P11: Has 2 elements")
    check.is_true(fare_by_survival[1] > fare_by_survival[0], "P11: Survivors paid more", "Survivors should have higher average fare")


def p12(df_clean):
    """Verify family size feature created"""
    check.contains_column(df_clean, 'family_size', "P12: Column created")
    check.is_true(df_clean['family_size'].min() == 1, "P12: Min is 1", "Minimum family size should be 1")
    check.is_true(df_clean['family_size'].max() > 5, "P12: Max above 5", "Maximum should be greater than 5")


def p13(survival_by_family):
    """Verify survival by family size"""
    check.is_type(survival_by_family, pd.Series, "P13: Type check")
    check.is_true(len(survival_by_family) > 1, "P13: Multiple family sizes", "Should have multiple family sizes")
    check.all_values_in_range(survival_by_family, 0, 100, "P13: Percentages valid")


def p14(survival_corr):
    """Verify correlation analysis"""
    check.is_type(survival_corr, pd.Series, "P14: Type check")
    check.all_values_in_range(survival_corr, -1, 1, "P14: Valid correlation range")


def p15(axes):
    """Verify summary dashboard created"""
    check.is_not_none(axes, "P15: Axes created")
    check.has_shape(axes, (2, 2), "P15: Correct shape")
