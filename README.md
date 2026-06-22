# SecureSchedAI

SecureSchedAI is a security-aware AI framework for Linux operating systems that integrates
DQN-based adaptive scheduling with LSTM-based intelligent threat detection.

This repository contains the dataset, paper figures, source-code modules, reproducibility scripts,
Docker support, and Kubernetes deployment manifests.

## Repository Structure

```text
SecureSchedAI/
├── dataset/
│   └── LASTD_2026_synthetic_linux_runtime_dataset.xlsx
├── figures/
│   ├── fig2_procfs_kernel_communication.png
│   ├── fig4_ubuntu_runtime_monitoring.png
│   ├── fig5_security_aware_enforcement.png
│   ├── fig6_runtime_logs.png
│   ├── fig7_confusion_matrix.png
│   ├── fig8_precision_recall_curve.png
│   ├── fig9_precision_recall_curve_large.png
│   └── fig10_kubernetes_deployment_demo.png
├── src/
│   ├── scheduler/dqn_scheduler.py
│   ├── detector/lstm_detector.py
│   ├── monitoring/runtime_monitor.py
│   └── enforcement/security_enforcement.py
├── scripts/
│   └── generate_paper_figures.py
├── docker/
│   └── docker-compose.yml
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
├── Dockerfile
└── main.py
```

## Python Version

Recommended Python version:

```bash
Python 3.11
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Reproducibility Demo

```bash
python main.py
```

The output metrics will be saved in:

```text
results/reproducibility_metrics.json
```

## Generate Paper Figures

```bash
python scripts/generate_paper_figures.py
```

The generated figures will be saved in the `figures/` folder.

## Docker Reproducibility

Build the Docker image:

```bash
docker build -t secureschedai .
```

Run the container:

```bash
docker run --rm -v $(pwd)/results:/app/results secureschedai
```

Or use Docker Compose:

```bash
cd docker
docker compose up --build
```

## Kubernetes Deployment

Build the local image:

```bash
docker build -t secureschedai:latest .
```

Apply Kubernetes manifests:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

Check pod status:

```bash
kubectl get pods
kubectl get deployments
```

Delete deployment:

```bash
kubectl delete -f kubernetes/
```

## Dataset

The LASTD-2026 dataset is provided in the `dataset/` folder. It contains Linux runtime samples
for normal and malicious activities and supports evaluation of adaptive scheduling and
intelligent threat detection.

## Paper Figure Mapping

- Fig. 2: `figures/fig2_procfs_kernel_communication.png`
- Fig. 4: `figures/fig4_ubuntu_runtime_monitoring.png`
- Fig. 5: `figures/fig5_security_aware_enforcement.png`
- Fig. 6: `figures/fig6_runtime_logs.png`
- Fig. 7: `figures/fig7_confusion_matrix.png`
- Fig. 8: `figures/fig8_precision_recall_curve.png`
- Fig. 9: `figures/fig9_precision_recall_curve_large.png`
- Fig. 10: `figures/fig10_kubernetes_deployment_demo.png`

## Citation

If you use this dataset or code, please cite the SecureSchedAI paper.
