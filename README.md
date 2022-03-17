# Cat Prediction

# Data

Setup Postgres

```console
cd data
docker compose up -d
```


# DBT

Setup dbt

```console
cd cat_predict_dbt
export DBT_PROFILES_DIR=$(pwd)
dbt debug

-- documentation
dbt docs generate
dbt docs serve
```


# Notebooks
```console
cd notebooks
```

## Setup


Ensure Python 3, `virtualenv` and `pip` are installed.

```console
which python3

virtualenv -p `which python3` venv
source venv/bin/activate
python --version
pip --version
pip install -r requirements.txt 
```

## Running JupyterLab

```console
jupyter lab
```

## Streamlit


```console
streamlit run cat_predictor_app_simple.py
```

## References

https://towardsdatascience.com/how-to-visualize-a-decision-tree-from-a-random-forest-in-python-using-scikit-learn-38ad2d75f21c

https://builtin.com/machine-learning/streamlit-tutorial
