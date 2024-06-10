The categorical values listed on the journal appendix are different compared to the CSV file. To accurately map the values (from numeric to categorical), see either:

1. https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success
2. https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention

However, this is already done by me and the results are saved in `column_values` folder. Values from similar columns are also merged together:
- For example, not all mother's occupations are also listed on father's occupations, but I merged both values so father's occupations have the same number of jobs as mother's occupations
- This is the same for qualification as well (between father, mother, and previous qualification)