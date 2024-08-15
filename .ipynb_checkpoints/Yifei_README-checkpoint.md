
# YifeiProject1

## Overview

This project focuses on analyzing the relationship between cancer statistics, various types of health insurance coverage, and access to clinical trials across different counties in the United States. The analysis includes data cleaning, correlation analysis, and visual exploration to understand how these factors relate to cancer death rates and overall cancer statistics.

## Project Structure

- **YifeiProject1.ipynb**: The main Jupyter notebook where the data cleaning, analysis, and visualization are performed.
- **Data Files**:
  - `avg-household-size.csv`
  - `cancer_reg.csv`
- **Figures**: Individual figures generated from the analysis are stored in the `figures` folder.

## Data Cleaning

Missing values in the dataset were handled by filling in the blanks with the mean of the respective columns. This approach ensured that no rows were eliminated from the dataset, preserving as much information as possible for analysis.

## Analysis and Visualization

The analysis includes:
- **Figure 1: Correlation Heatmap**: A heatmap that identifies relationships between cancer statistics and insurance coverage.
![Figure 1](./results_figures/Fig.1_Correlation_Between_Cancer_Statistics_and_Insurance_Coverage.png)
- **Figure 2: Correlation Heatmap**: A heatmap showing the relationship between cancer statistics and access to clinical trials.
![Figure 2](./results_figures/Fig.2_Correlation_Between_Cancer_Statistics_and_Clinical_Trials.png)
- **Linear Regression Plots**: To explore the strength and direction of the relationships between key variables.
- **Box Plots with Data Points**: To visualize the distribution and potential outliers in the insurance coverage data.
- **Skewness and Kurtosis Analysis**: To confirm that the observed correlations are not the result of skewed data distributions.

## Supplementary Information

To ensure the robustness of the correlations observed, supplementary figures and analyses were included to verify that the relationships identified were not artifacts of skewed data or missing values.

## Instructions for Running the Notebook

1. Load the notebook `YifeiProject1.ipynb` in Jupyter.
2. Ensure that the data files (`avg-household-size.csv` and `cancer_reg.csv`) are in the same directory as the notebook.
3. Run the notebook cells sequentially to perform the data cleaning, analysis, and generate the visualizations.

## How to Save Figures

Each figure generated in the notebook can be saved as an individual file. To do this, add the following line after each plotting command:

```python
plt.savefig('figures/figure_name.png')
```

## Installation

### For Unix (Linux/MacOS)

1. Open your terminal.
2. Run the following command:
```bash
git clone https://github.com/jordanskesner/plotters-against-cancer.git
```

## Usage
1. Start Jupyter Notebook from the project directory.
2. Open the relevant `.ipynb` notebook files to explore and run the analysis.

## Findings

- The cancer mortality rate shows a moderate negative correlation with the percentage of private insurance coverage, suggesting that better insurance coverage is associated with lower cancer death rates.
- Clinical trials per capita show a weak to moderate correlation with cancer statistics, indicating a potential impact on mortality but requiring further investigation.

## Acknowledgments

This project utilizes the [Uncovering Trends in Health Outcomes and Socioeconomic Factors dataset](https://www.kaggle.com/datasets/thedevastator/uncovering-trends-in-health-outcomes-and-socioec/data) available on Kaggle.

Most of the data preparation process can be viewed [here](https://data.world/nrippner/cancer-trials).

## Contributors

![Contributors](https://contrib.rocks/image?repo=jordanskesner/plotters-against-cancer)
