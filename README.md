# Animal recognition and class classification

Celem projektu jest przeanalizowanie zbioru danych o zwierzętach z zoo. Jedna część składa się z modeli predykcyjnych, które mają za zadanie przewidzieć gromadę zwierzęcia, a druga część to program w stylu Akinatora, który zadaje pytania użytkownikowi i zgaduje konkretne zwierzę.

## About the dataset

abc

## How to run this project

### Setting up virtual environment and installing requirements

After cloning the repository set up virtual environment and install requirements

```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

### Runing the project using DVC

This project uses DVC (Data Version Control) to run data processing pipelines.

Run the "evaluate_model" stage to see performance of the best model
```
dvc repro evaluate_model
```

To see the accuracy of the best model run
```
dvc accuracy show
dvc plots show
```

### Seeing the results

To see the results of the ML-pipeline run the following commands:
```
dvc metrics show
dvc plots show
```

## About the models

| Used models        |
|--------------------|
| K-means            |
| kNN                |
| Random Forest      |
| Decision Tree      |
| Gradient Boosting  |
| SVC                |

Coś o modelach?

## About Animal Guesser app

Aplikacja służy do rozpoznania nazwy zwierzęcia na podstawie zadawanych pytań. Należy wymyślić sobie zwierzę (istniejące w datasecie) i odpowiadać poprawnie na pytania, a program po kilku z nich poda ostateczną predykcję lub poda kilka jeśli ich parametry są identyczne.

### How to use Animal Guesser app

Run Animal_Guesser_app.py

![Gif 1](gif1.gif)

## About Class Guesser app

Aplikacja służy do rozpoznania gromady zwierzęcia na podstawie dostępnych parametrów w datasecie. Do predykcji zostaje wybrany najlepszy model według pliku 'accuracy.json'.

### How to use Animal Class Guesser app

Run Class_Guesser_app.py

![Gif 2](gif2.gif)