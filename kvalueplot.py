import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load transaction data into a Pandas dataframe
df = pd.read_csv('transaction_data.csv')

# Normalize the transaction amount
df['amount_norm'] = (df['amount'] - df['amount'].mean()) / df['amount'].std()

# Determine the optimal k-value using the elbow method
distortions = []
K = range(1, 10)
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df[['amount_norm']])
    distortions.append(kmeans.inertia_)
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('Elbow Method for Optimal k')
plt.show()

# Cluster the transaction data using the optimal k-value
k = 3 # set the optimal k-value based on the elbow method
kmeans = KMeans(n_clusters=k)
kmeans.fit(df[['amount_norm']])
df['cluster'] = kmeans.predict(df[['amount_norm']])

# Print the number of transactions in each cluster
print(df.groupby('cluster')['amount'].count())
