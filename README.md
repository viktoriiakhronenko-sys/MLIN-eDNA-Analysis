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

##  Ecological Diversity Analysis (Mlyn Station)

Beyond simple identification, we performed a mathematical analysis of the ecosystem's health using diversity indices. These metrics account for both the number of species and how evenly individuals are distributed among them.

### Biodiversity Metrics
![Diversity Analysis](ecolog.ind.mlyn.png)

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Species Richness** | [6] | Total number of unique species found |
| **Shannon Index (H)** | [0.087] | Measures uncertainty; higher values mean higher stability |
| **Simpson's Index (1-D)** | [0.031] | Probability that two random individuals belong to different species |

### Scientific Conclusion
A value of 0.087 is extremely low. This indicates that despite the presence of 6 different species, the community is heavily unbalanced. Almost all detected sequences belong to a single dominant taxon, while the other five species are present in negligible quantities. This suggests a "monoculture-like" state in this specific sample.
The score of 0.031 means there is only a 3.1% chance that two random organisms from this sample will be different species. In ecological terms, the sample is 96.9% dominated by one specific group. This low resistance to dominance often points to a highly specialized environment or a recent local ecological event that allowed one species to flourish while suppressing others.
Conclusion: Unlike the broader Pavlivka samples, the Mlyn station currently exhibits low taxonomic diversity and extreme dominance. With a Species Richness of only 6, the ecosystem here is significantly simplified. This data provides a crucial baseline for identifying why this specific location differs so drastically from the more balanced neighboring areas.
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
