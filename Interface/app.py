import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for matplotlib
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the base directory and datasets folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_FOLDER = os.path.join(BASE_DIR, "static", "datasets")

# Updated dataset file paths
datasets = {
    "KDDCUP99": os.path.join(DATASET_FOLDER, "KDDCUP99.csv"),
    "NSL-KDD": os.path.join(DATASET_FOLDER, "NSL-KDD.csv"),
    "CICIDS2017": os.path.join(DATASET_FOLDER, "CICIDS2017.csv")
}

# Metrics data for models (keys in lowercase to match HTML values)
metrics_data = {
    "accuracy": {"SVM": 99.54, "DT": 97.98, "KNN": 98.62},
    "precision": {"SVM": 99.54, "DT": 97.98, "KNN": 98.62},
    "recall": {"SVM": 99.79, "DT": 99.80, "KNN": 99.79},
    "f1-score": {"SVM": 99.68, "DT": 99.57, "KNN": 99.61}
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/models', methods=['GET', 'POST'])
def models():
    # Get selected metric and dataset; defaults are 'accuracy' and 'KDDCUP99'
    selected_metric = request.form.get('metric', 'accuracy')
    selected_dataset = request.form.get('dataset', 'KDDCUP99')

    # Generate a bar chart for the selected metric using matplotlib
    metric_values = metrics_data.get(selected_metric, metrics_data["accuracy"])
    plt.figure(figsize=(6, 4))
    plt.bar(metric_values.keys(), metric_values.values(), color=['blue', 'green', 'red'])
    plt.xlabel("ML Models")
    plt.ylabel(selected_metric.capitalize())
    plt.title(f"{selected_metric.capitalize()} for ML Models")
    # Save the graph to the static folder so it can be served to the client
    graph_path = os.path.join("static", "graph.png")
    plt.savefig(graph_path)
    plt.close()

    # Load the selected dataset CSV from src/datasets and extract the top 10 rows
    dataset_path = datasets.get(selected_dataset)
    if dataset_path and os.path.exists(dataset_path):
        df = pd.read_csv(dataset_path).head(10)
        table_html = df.to_html(classes='table table-striped', index=False)
    else:
        table_html = "<p>Dataset not found.</p>"

    return render_template(
        'models.html',
        metric=selected_metric,
        dataset=selected_dataset,
        graph=graph_path,
        table=table_html
    )

# AJAX endpoint to update the dataset preview without reloading the page
@app.route('/get_dataset')
def get_dataset():
    dataset_name = request.args.get('name', 'KDDCUP99')
    dataset_path = datasets.get(dataset_name)
    if dataset_path and os.path.exists(dataset_path):
        df = pd.read_csv(dataset_path).head(10)
        table_html = df.to_html(classes='table table-striped', index=False)
        return table_html
    else:
        return "<p>Dataset not found.</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
