# loops mini-project
### Recreating incorrect A/B test case study


## Introduction
In a case study presented on the loops website (see notes for link), an A/B test carried out by a customer led to misleading conclusions. An imbalance between the control and treatment groups, caused a bias in the results. Fortunately,  the mistake was found, the setup fixed, and a positive effect of the variant tested was discovered. In this project, I try to conceptually recreate this case study.

## Data Generation

I randomized data in python, using numpy and pandas packages, to try and get similar results to the ones discussed in paper (see notes). For the first and main stage, I created two tables:
1. "Original dataset"- users aresplit 50/50 into control and treatment
- control group: 0.8 high intent users
- treatment group: 0.2 high intent users
2. "Fixed dataset"- users are split 50/50 into control and treatment
- control group: 0.5 high intent users
- treatment group: 0.5 high intent users

## Analysis

I analyzed the two datasets in SQL, following the chronigical order described in the case study:
1. The first step was to naively check differences of KPI rates between control and treatment groups in dataset 1 (query 1 in SQL file). We get the following results:

|treat|	kpi_rate|	kpi_lift|
|-|-|-|
|0|	2.59|	NULL|
|1	|2.44|	-5.79%|

Similar to the first table presented in the case study. We observe a negative change in KPI.

2. Next we analyze in dataset 1 the splits of subgroups high and low intent, and control and treatment groups, and notice the imbalance between treatment groups (query 2 in SQL file)

3. We "redo" the A/B test to retrieve a fixed dataset, we make sure splits are correct (query 3 in SQL)
4. We can now analyze the dataset (since no imbalance was discovered) and get the following results (query 4 in SQL):

|treat|	kpi_rate|	kpi_lift|
|-|-|-|
|0|	2.34|	NULL|
|1	|2.53	|8.12%|

Here, like in the original study, we notice that indeed the treatment lifts the KPI.

5. We compare the changes in KPI across the two datasets, and notice the bias created by the imbalance in distribution in dataset 1 (query 5 in SQL)

6. For the last part of the project, I show that bias in results was created since intent of user affects both the treatments (imbalance) and outcome (KPI with different randomization parameters for low and high intent). For the last point I generated another 2 datasets, with the same split of 80/20 and 50/50 as in point 1, but this time data was generated such that effect of low and high intent on KPI is the same. We show that even though there is an imbalance in control and treatment, results stay the same in both datasets, since outcome is not affected by intent variable (query 6 in SQL).

###  Notes

1. https://www.getloops.ai/blog/flipping-a-hidden-a-b-test-setup-error-into-a-12-kpi-lift

2. Randomization was done using same seed. Parameters a,b,c,d were used for KPI probabilities, with values trying to mimic the ones in the case study.

3. Datasets lack real-world feeling, and obviously no dataset comes with ready made intent variable. But I wanted to conceptually show how bias could be created, in very simple terms.
