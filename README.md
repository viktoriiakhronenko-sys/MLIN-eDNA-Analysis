# eDNA Biodiversity Analysis: Project "Mlyn" 

This repository contains the environmental DNA (eDNA) analysis results for the **Mlyn** station (Pavlivka River). The study combines data from **MegaBLAST** and **BOLD Systems** to provide a high-resolution map of local biodiversity.

## 📊 Research Results

### 1. General Taxonomic Structure
The chart below shows the dominant Phyla identified at the Mlyn station. Data has been filtered to include only high-confidence matches (Identity ≥ 97%).

![Main Composition](mlyn.pie_chart.png)

### 2. Rare Biosphere Analysis
To maintain scientific accuracy, we separately visualized groups that constitute less than 2% of the total sample. These "minority" taxa often include important bioindicator species.

![Minority Groups](mlyn.bar_chart.minoryty.png)

---

## 🔍 Data Quality Metrics (Mlyn Station)
Based on our latest processing:
- **Total Unique Sequences:** 7,924
- **Reliable Identifications (≥97%):** 7,895
- **Discarded (Low Confidence):** 29
- **Dominant Group:** *Annelida* (specifically *Stylaria lacustris*)

---

## 🛠 Methodology
1. **Bioinformatics Pipeline:** Sequences were processed via Galaxy Europe.
2. **Taxonomic Assignment:** Dual-database approach using MegaBLAST (NCBI) and BOLD Systems.
3. **Visualization:** Custom Python scripts (Pandas, Matplotlib) with automated "Others" category grouping for clarity.

## 📂 File Description
- `Final_Report_Mlyn.csv`: The master dataset with merged taxonomy and read counts.
- `visualize_edna.py`: Python script for generating research-grade visualizations.
- `main_composition.png` & `minority_details.png`: Generated visual reports.

---
*Analysis performed by Viktorija Khronenko, 2026.*
