
In this section of the code, we will look at the correlation between the incidence rate of cancers
and the median age of a given population within a geographic region in the United States

Expectations:
We expect there to be a moderate to strong positive correlation between median age
and incidence of cancer within a given population, regardless of sex

Key Findings:
- Strong correlation of 0.63 between incidence and median age
- Strong correlation of 0.59 between incidence and median male age
- Strong correlation of 0.62 between incidence and median female age

Concludions:
As expected, there was a moderate to strong positive correlation between the median
age of the population and the incidence of cancer. Interestingly, this correlation
is slightly stronger among female populations. This could be explained as random noise
or could have a biological connection in differences between cancers that predominantly
affect one sex or the other, and which are more or less dependent on age of the affected
individual

Notes on data processing:
- All rows with NA values were dropped
- Outliers were trimmed individually from each data column using the 1.5*IQR method