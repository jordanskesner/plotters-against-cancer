# About The Project

This project performs an exploratory data analysis on a Kaggle dataset that includeds an abundant set of socioeconomic and demographic factors.
The analysis will examine how these factors influence health outcomes.

# Getting Started

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

# Findings

1. Populations with higher median income have lower death rates.
![finding1](./results/figures/MedianIncome_ScatterReg.png)

2. Populations that have a greater percentage of people over 25 with a Bachelor's degree will see lower percentage of cancer deaths. The reverse is also moderately true. Populations that have a greater percentage of people over 25 with only a high school degree will see higher percentage of cancer deaths.
![finding2](./results/figures/BachelorDegree_ScatterReg.png)
![finding2](./results/figures/HighSchool_ScatterReg.png)

3. The South exhibits the highest cancer mortality rates across the United States.
![finding3](./results/figures/county_level_cancer_mortality_rates.png)
![finding3](./results/figures/region_level_cancer_mortality_rates.png)

4. Insurance coverage types may have a significant impact on cancer death rates, with public insurance showing a stronger positive correlation with higher cancer death rates.
![finding4](./results/figures/correlation_between_cancer_statistics_and_insurance_coverage.png)

5. The number of clinical trials per capita has a weak correlation with cancer statistics, suggesting that other factors may play a more significant role in influencing cancer outcomes.
![finding5](./results/figures/correlation_between_cancer_statistics_and_number_of_clinical_trials_per_capita_in_the_given_county.png)

6. There is a strong correlation between cancer incidence and median age, with a correlation coefficient of 0.63 overall, 0.59 for median male age, and 0.62 for median female age.
![finding6](./results/figures/age_incidence_correlations.png)
![finding6](./results/figures/age_incidence.png)

7. (GPT) There are varying correlations between average annual cancer count and racial demographics: a weak negative correlation of -0.14 with the percentage of the White population, a very weak positive correlation of 0.03 with the percentage of the Black population, a moderate positive correlation of 0.44 with the percentage of the Asian population, and a weak positive correlation of 0.21 with the percentage of other races.

![finding7](./results/figures/cancer_race_correlation_heatmap.png)

# Acknowledgments

This project utilizes the [Uncovering Trends in Health Outcomes and Socioeconomic Factors dataset](https://www.kaggle.com/datasets/thedevastator/uncovering-trends-in-health-outcomes-and-socioec/data) available on Kaggle.

Most of the data preparation process can be viewed [here](https://data.world/nrippner/cancer-trials).

# Contributors

![Contributors](https://contrib.rocks/image?repo=jordanskesner/plotters-against-cancer)
