# detect_live.py
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

model_path = 'models/isolation_forest.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError('Train the model first using train_model.py')

model = joblib.load(model_path)
df = pd.read_csv('sample_data.csv')
X = df[['temp','humidity']].values
pred = model.predict(X)
df['anomaly'] = (pred == -1)
print(df.tail())

plt.figure(figsize=(6,4))
colors = df['anomaly'].map({True:'red', False:'blue'})
plt.scatter(df['temp'], df['humidity'], c=colors, s=10)
plt.xlabel('temp'); plt.ylabel('humidity')
plt.title('Anomalies: red')
plt.tight_layout()
plt.savefig('anomaly_scatter.png')
print('saved anomaly_scatter.png')
