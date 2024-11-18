from sklearn.neighbors import LocalOutlierFactor

def detect_outliers(df, columns, contamination=0.1):
    # Use Local Outlier Factor (LOF) instead of IsolationForest
    lof = LocalOutlierFactor(contamination=contamination)
    
    # Fit the model and predict outliers
    df['outlier'] = lof.fit_predict(df[columns])
    
    # Map LOF output: -1 means an outlier, 1 means an inlier
    # We map them to 1 (outlier) and 0 (inlier) for consistency with your test cases
    df['outlier'] = df['outlier'].map({-1: 1, 1: 0})
    
    return df
