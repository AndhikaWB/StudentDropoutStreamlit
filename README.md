# Student Dropout Analysis

This repo contains 3 of my work:
1. Dashboard for analyzing dropout factor (Metabase)
2. Machine learning model to predict dropout status (Scikit Learn)
3. Interactive web app to access the machine learning model (Streamlit)

What I've learned:
- Model pipelining & ensembling
- Different effects of feature preprocessing

Result:
- Using ensemble model (combining tree, KNN, and linear based models), I can reach 86% prediction score (F1 macro)
- For screenshots and demo, see below

## Screenshots

### Dashboard

<details>
    <summary>Show screenshots</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/dashboard/dashboard_1.png"/>
        <img style="border: 1px solid black;" src="img/dashboard/dashboard_2.png"/>
        <img style="border: 1px solid black;" src="img/dashboard/dashboard_3.png"/>
        <img style="border: 1px solid black;" src="img/dashboard/dashboard_4.png"/>
    </p>
</details>

Metabase doesn't have box/violin plot yet, so I mostly use bar chart or line chart to substitute that. Detailed conclusion from the dashboard can be seen [here](dashboard/README.md) (in Bahasa Indonesia).

### Web App

<details>
    <summary>Show screenshots</summary>
    <p align="center">
        <img style="border: 1px solid white;" src="img/app/app_1.png"/>
        <img style="border: 1px solid white;" src="img/app/app_2.png"/>
    </p>
</details>

Web app can also be accessed on Streamlit Cloud [here](https://stud-evdgvjxrixagvawcczpydw.streamlit.app).

## Technical Comparisons

See also the [notebook](notebook.ipynb) to understand the context. There are some important notes there as well.

### Correlation Matrix

Scores below 0.2 and above -0.2 (e.g. -0.1) are shown as 0.

<details>
    <summary>Cramer's V + Pearson's R + correlation ratio</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/corr_matrix_cramer_mix.png"/>
    </p>
</details>

<details>
    <summary>Theil's U + Pearson's R + correlation ratio</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/corr_matrix_theil_mix.png"/>
    </p>
</details>

<details>
    <summary>Phi-K</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/corr_matrix_phik.png"/>
    </p>
</details>

### Feature Engineering

<details>
    <summary>Addition of 1st sem and 2nd sem curricular units</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_l2_add.png"/>
    </p>
</details>

<details>
    <summary>Average of 1st sem and 2nd sem curricular units</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_l2_avg.png"/>
    </p>
</details>

<details>
    <summary>Multiplication of 1st sem and 2nd sem curricular units</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_l2_mul.png"/>
    </p>
</details>

### Data Scaling

<details>
    <summary>Leave one out encoder + min-max scaler</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_minmax.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + quantile transformer</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_quant.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + robust scaler</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_robust.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + standard scaler</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_std.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + power transformer</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_pow.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + max normalizer</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_max.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + L1 normalizer</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_l1.png"/>
    </p>
</details>

<details>
    <summary>Leave one out encoder + L2 normalizer</summary>
    <p align="center">
        <img style="border: 1px solid black;" src="img/misc/pca_loo_l2_mul.png"/>
    </p>
</details>

---

[Data Source](data/README.md)