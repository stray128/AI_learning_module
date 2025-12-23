"""
Script to download public datasets for the learning module.
Run this once to set up the datasets.
"""
import os

# Create directories if they don't exist
os.makedirs('public', exist_ok=True)
os.makedirs('synthetic', exist_ok=True)

try:
    import pandas as pd
    import numpy as np

    print("Downloading datasets...")

    # 1. Titanic Dataset (from seaborn or a public URL)
    try:
        import seaborn as sns
        titanic = sns.load_dataset('titanic')
        titanic.to_csv('public/titanic.csv', index=False)
        print("✓ Titanic dataset saved")
    except:
        # Fallback to direct URL
        titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
        titanic.to_csv('public/titanic.csv', index=False)
        print("✓ Titanic dataset saved (from URL)")

    # 2. Iris Dataset
    try:
        import seaborn as sns
        iris = sns.load_dataset('iris')
        iris.to_csv('public/iris.csv', index=False)
        print("✓ Iris dataset saved")
    except:
        from sklearn.datasets import load_iris
        iris_data = load_iris()
        iris = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
        iris['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
        iris.to_csv('public/iris.csv', index=False)
        print("✓ Iris dataset saved (from sklearn)")

    # 3. Tips Dataset
    try:
        import seaborn as sns
        tips = sns.load_dataset('tips')
        tips.to_csv('public/tips.csv', index=False)
        print("✓ Tips dataset saved")
    except:
        tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
        tips.to_csv('public/tips.csv', index=False)
        print("✓ Tips dataset saved (from URL)")

    # 4. Create synthetic datasets
    np.random.seed(42)

    # Simple numeric dataset
    simple = pd.DataFrame({
        'id': range(1, 101),
        'value_a': np.random.randint(1, 100, 100),
        'value_b': np.random.randn(100) * 10 + 50,
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'flag': np.random.choice([True, False], 100)
    })
    simple.to_csv('synthetic/simple_data.csv', index=False)
    print("✓ Simple synthetic dataset saved")

    # Dataset with missing values (for cleaning exercises)
    messy = pd.DataFrame({
        'id': range(1, 51),
        'name': ['Person_' + str(i) for i in range(1, 51)],
        'age': [np.random.randint(18, 65) if np.random.random() > 0.1 else np.nan for _ in range(50)],
        'salary': [np.random.randint(30000, 100000) if np.random.random() > 0.15 else np.nan for _ in range(50)],
        'department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing', None], 50),
        'hire_date': pd.date_range('2020-01-01', periods=50, freq='W').astype(str).tolist()
    })
    messy.to_csv('synthetic/messy_data.csv', index=False)
    print("✓ Messy synthetic dataset saved (for cleaning exercises)")

    # Sales dataset (for groupby/aggregation)
    sales = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=200, freq='D').repeat(3)[:500],
        'product': np.random.choice(['Widget', 'Gadget', 'Gizmo', 'Doohickey'], 500),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 500),
        'quantity': np.random.randint(1, 50, 500),
        'price': np.random.uniform(10, 100, 500).round(2)
    })
    sales['revenue'] = (sales['quantity'] * sales['price']).round(2)
    sales.to_csv('synthetic/sales_data.csv', index=False)
    print("✓ Sales synthetic dataset saved (for groupby exercises)")

    print("\n✅ All datasets downloaded successfully!")
    print(f"\nDatasets available in:")
    print(f"  - public/titanic.csv")
    print(f"  - public/iris.csv")
    print(f"  - public/tips.csv")
    print(f"  - synthetic/simple_data.csv")
    print(f"  - synthetic/messy_data.csv")
    print(f"  - synthetic/sales_data.csv")

except ImportError as e:
    print(f"Error: {e}")
    print("Please install required packages: pip install pandas numpy seaborn scikit-learn")
