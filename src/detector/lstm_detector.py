"""LSTM threat detector interface.

This lightweight version provides the same input/output interface used by
SecureSchedAI. Replace the simple scoring rule with a trained LSTM model
for full experimentation.
"""

def compute_anomaly_score(cpu_usage, syscall_rate, file_access_rate, network_rate):
    score = (
        0.30 * min(cpu_usage / 100, 1.0)
        + 0.25 * min(syscall_rate / 1000, 1.0)
        + 0.25 * min(file_access_rate / 500, 1.0)
        + 0.20 * min(network_rate / 1000, 1.0)
    )
    return round(score, 3)

def classify_threat(score, threshold=0.75):
    return "THREAT" if score >= threshold else "NORMAL"

if __name__ == "__main__":
    score = compute_anomaly_score(93, 850, 420, 650)
    print({"anomaly_score": score, "classification": classify_threat(score)})
