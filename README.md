# Project Title

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
   git clone https://github.com/yourusername/yourproject.git

2. **Run the Scrapping code.py file**: This will scrap the data from the internet about customer reviews for a given product. Make sure to change the url and product name in there accoerding to the need.
3. **Run the annotate_llm.ipynb**: Once you mannually annotate the data as in `Human_annotations.csv` file you can use this file to annotate your data using a given LLM model. Make sure to change the api_key of the model and also mention the model you want to use in the code for the annotation task.
4. 
