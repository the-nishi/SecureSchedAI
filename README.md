## Dataset Location

```text
dataset/LASTD_2026_synthetic_linux_runtime_dataset.xlsx
```

## Linux Execution Guide

Clone the repository:

```bash
git clone https://github.com/the-nishi/SecureSchedAI.git
cd SecureSchedAI
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the reproducibility demo:

```bash
python main.py
```

Run runtime monitoring:

```bash
python src/monitoring/runtime_monitor.py
```

Run DQN scheduler demo:

```bash
python src/scheduler/dqn_scheduler.py
```

Run LSTM threat detector demo:

```bash
python src/detector/lstm_detector.py
```

Run security-aware enforcement demo:

```bash
python src/enforcement/security_enforcement.py
```

## Reproducibility

This repository contains:

* LASTD-2026 Dataset
* Source Code Modules
* Runtime Monitoring Scripts
* Security-Aware Enforcement Utilities
* Figure Generation Scripts
* Docker Configuration
* Kubernetes Deployment Manifests

to support reproducibility of the SecureSchedAI framework and facilitate future research on AI-assisted Linux operating systems.

## Experimental Reproduction

To reproduce the reported workflow:

1. Install all dependencies using `requirements.txt`.
2. Load the LASTD-2026 dataset from the `dataset/` directory.
3. Execute `main.py` to run the reproducibility pipeline.
4. Generate figures using `scripts/generate_paper_figures.py`.
5. Deploy the framework using Docker or Kubernetes if containerized evaluation is required.

## Repository Purpose

This repository accompanies the SecureSchedAI research paper and provides public access to:

* Dataset resources
* Source-code artifacts
* Runtime monitoring examples
* Linux enforcement demonstrations
* Figure generation scripts
* Deployment configurations

for transparency, validation, and reproducible experimentation.

## Citation

If you use this dataset, source code, figures, or deployment artifacts in your research, please cite the SecureSchedAI paper.
