import warnings
import joblib
import json

import streamlit as st
import pandas as pd

# ----------
# HELPER
# ----------

def _dict_key_from_val(dict_obj: dict, value: str) -> int:
    if value == None: return None
    # Get dict key from its value (inverse dict)
    # Will raise an error if value not found
    inv_dict = {v: k for k, v in dict_obj.items()}
    return int(inv_dict[value])

def _model_preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Don't modify reference directly
    df = df.copy()

    # Convert data types
    for col in df_cols:
        if type(df_cols[col]) == float: df[col] = df[col].astype('float')
        elif type(df_cols[col]) == int: df[col] = df[col].astype('int')

    # Combine features
    df['Curricular_units_all_sem_approved'] = df['Curricular_units_1st_sem_approved'] * df['Curricular_units_2nd_sem_approved']
    df['Curricular_units_all_sem_grade'] = df['Curricular_units_1st_sem_grade'] * df['Curricular_units_2nd_sem_grade']
    df = df.drop([
        'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade'
    ], axis = 1)

    # Reorder columns to be the same as model
    cols = list(df_cols)[:-4]
    cols += ['Curricular_units_all_sem_approved', 'Curricular_units_all_sem_grade']
    df = df[cols]

    return df

def _model_predict(df: pd.DataFrame, model) -> str | pd.DataFrame:
    '''Returns string (status) for single row, dataframe otherwise (index + status)'''
    df = _model_preprocess(df)
    prediction = model.predict(df)

    if len(df) == 1:
        if prediction == 0: return 'Dropout'
        return 'Enrolled/Graduate'
    else:
        # If more than 1 row, return dataframe
        temp = pd.DataFrame({'Status': prediction}, index = df.index)
        temp['Status'] = temp['Status'].astype('str')
        temp['Status'] = temp['Status'].replace({'0': 'Dropout', '1': 'Enrolled/Graduate'})
        return temp

def predict(df: pd.DataFrame, model):
    # Reset placeholder to initial state
    raw_data_placeholder.empty()
    result_placeholder.empty()

    # Get model prediction
    prediction = _model_predict(df, model)

    with raw_data_placeholder.expander('View Raw Data'):
        st.dataframe(df, use_container_width = True)
        st.write('**Note:** The leftmost column is the row id, and the prediction order is based on that.')

    with result_placeholder.expander('View Prediction', expanded = True):
        if len(df) == 1:
            # If only 1 student then don't show table
            if prediction == 'Enrolled/Graduate':
                # https://share.streamlit.io/streamlit/emoji-shortcodes
                st.success(
                    '# Congrats! :partying_face:\n'
                    'This student is more likely to stay/graduate.'
                )
                st.balloons()
            else:
                st.info(
                    '# Too bad! :cold_face:\n'
                    'This student is more likely to dropout.'
                )
                st.snow()
        else:
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                # Show prediction table (index + status)
                st.dataframe(prediction, use_container_width = True)
            with col2:
                # Show status value counts beside the table
                temp = prediction['Status'].value_counts()
                st.metric(label = f'**:green[{temp.index[0]}]**', value = temp.values[0]) # Graduate
                st.metric(label = f'**:red[{temp.index[1]}]**', value = temp.values[1]) # Dropout

                graduate_percent = round(temp.values[0] / (temp.values[0] + temp.values[1]) * 100)
                dropout_percent = 100 - graduate_percent

                # Show info box below the metric/value counts
                if graduate_percent > dropout_percent:
                    st.success(
                        '### Congrats! :partying_face:\n'
                        f'{graduate_percent}% students are more likely to stay/graduate.'
                    )
                    st.balloons()
                else:
                    st.info(
                        '### Too bad! :cold_face:\n'
                        f'{dropout_percent}% students are more likely to dropout.'
                    )
                    st.snow()

# ----------
# INIT
# ----------

# Model/pipeline to predict student dropout status
# This already includes most preprocessing steps
model = joblib.load('model/model.lz4')

# Columns required by the model (do not change order!)
# For numeric column, data type and max value must be specified
df_cols = {
    'Application_mode': None,
    'Course': None,
    'Debtor': None,
    'Tuition_fees_up_to_date': None,
    'Gender': None,
    'Scholarship_holder': None,
    'Age_at_enrollment': 100,
    # 1st sem and 2nd sem will be combined later
    # Max value should be 24 for 3 years study (Indonesia)
    'Curricular_units_1st_sem_approved': 24,
    'Curricular_units_2nd_sem_approved': 24,
    'Curricular_units_1st_sem_grade': 24.0,
    'Curricular_units_2nd_sem_grade': 24.0
}

# Get number-category mapping for some columns (e.g. course)
with open('data/column_values/all.json') as f:
    cat_dict = dict(json.load(f))

# ----------
# MAIN UI
# ----------

st.header('Student :blue[Dropout] Prediction', divider = 'rainbow')
tab1, tab2 = st.tabs(['Upload File', 'Fill Form'])

# Placeholder can only be replaced by 1 element
# To replace it with more than 1 element, use container/expander
raw_data_placeholder = st.empty()
result_placeholder = st.empty()

with tab1:
    with st.container(border = True):
        # https://fonts.google.com/icons
        st.warning('CSV file will not be sanitized, make sure to use the correct format!', icon = ':material/warning:')

        sample_csv = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv'
        csv_file = st.file_uploader(f'Upload a compatible CSV file (see [example]({sample_csv})).', type = 'csv')
        if csv_file:
            upload_df = pd.read_csv(csv_file, sep = ';')

        upload_error_placeholder = st.empty()
        pred_upload = st.button('Predict', type = 'primary', key = 123)

        if pred_upload and csv_file:
            upload_error_placeholder.empty()
            predict(upload_df, model)
            # # Reset data after each prediction
            # csv_file = None
        elif pred_upload:
            upload_error_placeholder.write(':red[No file uploaded!]')

with tab2:
    with st.container(border = True):
        # Initial dataframe
        form_df = pd.DataFrame()
        # Iterate all columns to make form
        for col in df_cols:
            if col in cat_dict:
                # Get number-category mapping for current column
                map_dict = cat_dict[col]
                # Show category in select box
                input_value = st.selectbox(
                    label = col.replace('_', ' '),
                    options = map_dict.values(),
                    index = None
                )
                # Convert category to number (inverse dict)
                input_value = _dict_key_from_val(map_dict, input_value)
            else:
                # If not in category dict then it's numeric value
                if type(df_cols[col]) == int:
                    input_value = st.number_input(
                        label = col.replace('_', ' '),
                        min_value = 0,
                        max_value = df_cols[col],
                        step = 1
                    )
                else:
                    input_value = st.number_input(
                        label = col.replace('_', ' '),
                        min_value = 0.0,
                        max_value = df_cols[col],
                        step = 1.0
                    )

            form_df[col] = [input_value]

        # Some form values are set to null (none) by default
        # This will check if any of the values are still null
        null_detected = form_df.isnull().values.any()

        form_error_placeholder = st.empty()
        pred_form = st.button('Predict', type = 'primary', key = 456)

        if pred_form and not null_detected:
            form_error_placeholder.empty()
            predict(form_df, model)
            # # Reset data after each prediction
            # form_df = pd.DataFrame()
        elif pred_form:
            form_error_placeholder.write(':red[There is at least 1 unfilled input!]')