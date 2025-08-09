# train_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib, os

os.makedirs('models', exist_ok=True)
df = pd.read_csv('sample_data.csv')
X = df[['temp','humidity']].values
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)
joblib.dump(model, 'models/isolation_forest.pkl')
print('model saved to models/isolation_forest.pkl')
