# Using Large Language Models as Data Annotators

## Introduction

The project aims to estimate the performance and reliability of using large language models (LLMs) as data annotators. We are addressing the challenge of annotating customer reviews based on their references to various product features. Traditionally, this task involves multiple human annotators, but as the volume and complexity of the data increase, more time and resources are required to achieve a consistently reliable annotation. This is where LLMs come into play, providing a fast and efficient alternative for data annotation.

## Project Structure

The project consists of the following files:

### Data Scraping and Annotation

- **Scrapping_code.py**: Contains the code used to scrape user comments from the internet.
- **Annotation_Guidelines.pdf**: Provides the annotation guidelines that need to be considered while annotating the data for both human and LLM annotators.

### Human Annotation

- **Human_annotations.csv**: Generated manually by annotating the labels for scraped reviews according to the annotation guidelines.

### LLM Annotation

- **annotate_llm.ipynb**: Jupyter notebook used to annotate the scraped reviews using Large Language Models (LLMs). The models used here are GPT-4 and GPT-4o-mini.
- **LLM_annotations_gpt-4o-mini.csv**: Generated using `annotate_llm.ipynb`. Contains GPT-4o-mini annotated labels for the scraped customer reviews data.
- **LLM_annotations_gpt_4.csv**: Also generated using `annotate_llm.ipynb`. Contains GPT-4 annotated labels for the scraped customer reviews data.

### Analysis and Modeling

- **Project_code.ipynb**: Jupyter notebook containing all the code used for this project, including analysis, data interpretation, and model creation.

### Report

- **Data annotaion project report.pdf**: This is a 2 page project report that shows the project overview, methids, experiments, results and analysis.

## Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Anshkumardev/Data-Annotation-using-LLMs

2. **Run the Scrapping code.py file**: This will scrape data from the internet about customer reviews for a given product. Make sure to change the URL and product name in the code according to your needs.
3. **Run the annotate_llm.ipynb**: Once you manually annotate the data as in the `Human_annotations.csv file`, you can use this notebook to annotate your data using a given LLM model. Make sure to change the API key of the model and also specify the model you want to use in the code for the annotation task.
4. **Run the Project_code.ipynb**: Finally, run this notebook to get all the analysis and results discussed in the project report. This notebook uses the human and LLM annotated data and shows the analyses done on them. Additionally, there is a section that demonstrates a basic classification model for the annotated labels and evaluates their performance.
