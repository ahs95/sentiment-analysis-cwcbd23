# 🏏 Bangla Sentiment & Sarcasm Detection in Cricket Discourse

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/🤗_Model-Weights-ff6f61)](https://huggingface.co/ahs95/sentiment-sarcasm-detection-BanglaBERT)

Joint sentiment classification & sarcasm detection for severely imbalanced Bangla social media text. This repository contains the complete training pipeline, dynamic loss scheduling implementation, class-aware threshold calibration, and Gradio deployment for the paper:
> [Sentiment and Sarcasm Detection in Bangla: A Calibrated Multitask Framework for Imbalanced Cricket Discourse](https://zenodo.org/records/20307593)

---

## 📖 Overview
Social media discourse in low-resource languages like Bangla presents unique NLP challenges: severe class imbalance, domain-specific slang, and complex pragmatic phenomena (e.g., sarcasm, mixed sentiment). While sentiment analysis in Bangla has advanced, sarcasm detection remains underexplored, and most existing approaches treat the tasks in isolation or rely on static optimization that collapses minority-class recall.

This project introduces a **calibrated dual-head multitask framework** that:
- Leverages shared BanglaBERT representations for joint sentiment & sarcasm prediction
- Dynamically schedules focal loss (`α` inverse-frequency scaling + `γ` epoch decay) to prevent gradient starvation
- Optimizes per-class decision thresholds post-hoc to recover minority boundaries without retraining
- Augments rare classes via offline BanglaT5 paraphrasing
- Achieves **W-F1: 0.79 (Sentiment)** and **0.73 (Sarcasm)** under 5-fold stratified CV

---

## ✨ Key Features
| Component | Implementation |
|-----------|----------------|
| 🏗️ **Architecture** | Dual-head `csebuetnlp/banglabert_small` with 256-dim shared projection |
| ⚖️ **Loss Scheduling** | Fold-adaptive inverse-frequency `α` + linear `γ` decay (`2.5 → 0.8`) |
| 🎯 **Threshold Calibration** | Grid-searched per-class thresholds on validation folds (no test leakage) |
| 📝 **Augmentation** | BanglaT5 paraphrasing applied offline to minority classes |
| 📊 **Evaluation** | 5-fold stratified CV, 2,000 bootstrap CIs, macro/weighted F1 reporting |
| 🌐 **Deployment** | Gradio interface with 8-bit quantization & threshold-aware inference |

---

## 📊 Dataset
- **Size:** 6,507 manually annotated Bangla comments
- **Source:** Facebook & YouTube posts during Bangladesh's 2023 ICC Cricket World Cup campaign
- **Labels:** 
  - `Sentiment`: Positive, Neutral, Negative, Mixed
  - `Sarcasm`: Sarcastic, Non-Sarcastic
- **Distribution:** Highly skewed (Negative: 64.7%, Non-Sarcastic: 65.3%)
- **Inter-rater Agreement:** Cohen's κ = 0.79 (Sentiment), 1.00 (Sarcasm)

---

## 🛠️ Installation
```bash
# Clone repository
git clone https://github.com/ahs95/sentiment-analysis-cwcbd23.git
cd sentiment-analysis-cwcbd23

# Create & activate environment
conda create -n bangla-sarcasm python=3.10
conda activate bangla-sarcasm

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt**
```
torch>=2.0.0
transformers>=4.30.0
bitsandbytes>=0.41.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
iterative-stratification>=0.1.9
gradio>=4.0.0
openpyxl>=3.1.0
tqdm>=4.65.0
```

---

## 🚀 Quick Start

### 1. Training Pipeline
```bash
# Run full 5-fold training with dynamic loss & threshold calibration
python train.py --data_path data/Data_Cric23_BD.xlsx \
                --output_dir outputs/ \
                --num_epochs 5 \
                --batch_size 16 \
                --accumulation_steps 2 \
                --seed 42
```
*Outputs:* `model.pth`, `sent_thresholds.npy`, `sarc_thresholds.npy`, and error analysis CSV.

### 2. Inference (Calibrated)
```python
import torch
import numpy as np
from transformers import AutoTokenizer
from model_architecture import DualHeadModel

# Load artifacts
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglabert_small")
model = DualHeadModel(num_sentiment_classes=4, num_sarcasm_classes=2)
model.load_state_dict(torch.load("outputs/model.pth", map_location="cpu", weights_only=True))
model.eval()

sent_thresh = np.load("outputs/sent_thresholds.npy")
sarc_thresh = np.load("outputs/sarc_thresholds.npy")

# Prediction function (see `inference.py` for full threshold application logic)
from inference import predict
result = predict("বাংলাদেশ জিতবে ২০৫০ বিশ্বকাপ, তখন আমি আর থাকব না।", 
                 tokenizer, model, sent_thresh, sarc_thresh)
print(result)
# Output: {'sentiment': 'Negative', 'sarcasm': 'Sarcastic', 'confidence': {...}}
```

---

## 📈 Results
| Configuration | Sentiment W-F1 (±95% CI) | Sarcasm W-F1 (±95% CI) | Minority F1 (Sent/Sarc) |
|---------------|--------------------------|------------------------|--------------------------|
| Cross-Entropy | 0.690 [0.670–0.710]      | 0.610 [0.590–0.630]    | 0.00 / 0.41              |
| Weighted CE   | 0.729 [0.719–0.739]      | 0.760 [0.749–0.770]    | 0.55 / 0.67              |
| **Full Pipeline** | **0.794 [0.784–0.804]** | **0.729 [0.718–0.740]** | **0.59 / 0.62**          |

*All metrics computed via 5-fold stratified CV with 2,000 bootstrap resamples. Non-overlapping CIs confirm statistical significance.*

---

## 📜 Citation
If you use this code, dataset, or model in your research, please cite:
```bibtex
@article{banglasentimentsarcasm,
  title={Sentiment and Sarcasm Detection in Bangla: A Calibrated Multitask Framework for Imbalanced Cricket Discourse},
  author={Arshadul Hoque and Nasrin Sultana and Risul Islam Rasel},
  year={2026},
  publisher={Zenodo},
  doi={10.5281/zenodo.20307593}
}
```

## ⚖️ License & Contact
- 🔓 **Code:** Apache 2.0
- 🤝 **Model/Weights:** Apache 2.0 / CC-BY-NC 4.0
- 📧 **Correspondence:** `ahsbd95@gmail.com`
