# Collecting Data from SARB's Web-Based API

I will be collating python code for collecting various types of data from the SARB's web page here.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Files](#files)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [License](#license)

## Project Overview

This project began as a simple guide to assist "non-tech" financial professionals overcome the hurdle of using API's
For now it contains a simple example of how to collect bond market data from the South African Reserve Bank's web-based API
The article can be found on my Linkedin Page: www.linkedin.com/in/tlhogi

I will be adding code for collecting and cleaning the other data here as I tackle related projects over time

## Prerequisites

Python 3.x

The project also assumes you ave already installed the necessary libraries used in order to facilitate the following imports:
* import requests
* import pandas as pd
* import xml.etree.ElementTree as ET
* import os
* import datetime

## Files

* notebooks/: Jupyter notebooks with python code used for collecting data - annotated for your understanding
* .py files/: Python files with pure python code without annotations and intermediate print-outs
* README.md : This file, providing an overview of the project.

## Usage

To collect data from the South African Reserve Bank's web-based API, follow these steps:

1. Download the `.py` file from the repository.

2. Open the `.py` file and update the working directory to match your setup if necessary.

3. Run the script using your preferred Python environment.

4. The script will collect data and save it as a CSV file.

5. You can now access and use the collected data for your analysis or applications.

## License

This project is licensed under the Apache License 2.0
