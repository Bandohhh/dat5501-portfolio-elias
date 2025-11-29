📘 DAT5501 Portfolio — Weekly Labs & Projects

Author: Elias Bandoh
Module: DAT5501 

This repository contains weekly lab exercises, projects and independent/group tasks completed for DAT5501.
Each week focuses on a new Python or data-analysis concept, progressing from programming fundamentals to applied machine learning and automation.

**Week 1 — Version Control & Unit Testing**

Files:

version_control_practice.py

unit_testing.py

Summary:
Introduced Git basics (commits, branches) and Python’s built in unittest module.
Scripts demonstrate defining simple arithmetic or logical functions and testing them for correctness.

Packages: unittest, math (stdlib)
Techniques: version control, assertions, test-driven development.

**Week 2 — Compound Interest & Financial Modelling**

File: week_2/comp_int.py

Summary:
A financial calculator that computes compound interest and time required for an investment to double using logarithmic functions.
Demonstrates loops, functions, and user input.

Packages: math
Techniques:

Function decomposition (compound_interest(), investment_double_time())

For loops and formatted string output

Real world formula implementation


**Week 3 — Calendar & Date Utilities**

Folder: week_3/

Summary:
Worked with date/time modules and basic GUI design using Tkinter.
Created simple programs to print or display calendars interactively.

Packages: datetime, calendar, tkinter
Techniques: CLI design, GUI layout, function reuse.

**Week 5 — GUI Development & Data Analysis**
Creating a duration caluclator and a Graphical User Interface (GUI) 
US election analysis, creating charts and a user interface that would show the proportion of votes each candidates in the US election recieved in each state
Folders:

week_5/duration_task/

week_5/us_election/

Summary:

Duration Task: built a Tkinter + tkcalendar GUI to calculate the number of days between two dates.

US Election Analysis: analysed voting data from CSV files, plotted histograms, and summarised results.

Packages: tkinter, tkcalendar, pandas, matplotlib
Techniques:

GUI event handling and widget control

Reading & cleaning CSV data

Plotting histograms and bar charts



**Week 8 — Algorithm Performance & Forecasting**
Plotting and predictting gold prices and using the chi squared values for projections of data, doing forcasting and projectting future gold prices using polynomials.

Project for chi squared values is under the thurs folder within week 8

Files:

price_sort.py

HistoricalData_1762772785970.csv

thurs/ (supporting scripts)

Summary:
Analysed the computational performance of sorting operations compared to the theoretical n log n complexity.
Performed polynomial fitting and forecasting using stock or population data.

Packages: numpy, pandas, matplotlib, time
Techniques:

Complexity analysis and timing functions

Polynomial fitting & model evaluation (χ², BIC) chi^2

Data visualisation and interpretation

**Week 10 — Machine Learning & Decision Trees**
Ceaning and sorting data and using machiene learning techniques to create a decision tree based of student results and predicting wether they would pass an exam or not.

Files:

decision_tree.py

real_estate_ml.py

Datasets: student-por.csv, real_estate_valuation_data set.csv

Summary:
Implemented two small ML pipelines:

Student Performance Classifier — predicts pass/fail outcomes using a decision tree.

Real Estate Valuation Model — regression model predicting house prices.

Both include data loading, preprocessing, model training, and accuracy evaluation.

Packages: pandas, scikit-learn, matplotlib
Techniques:

DecisionTreeClassifier & Regression

Train/test split, accuracy evaluation

Feature importance and visualisation (plot_tree)

Data ethics: no personal data; open UCI datasets used

**Labs (Practice Work)**

Folder: labs/

lab-02-unit-testing/: reinforces TDD and assertions

Misc .vscode/ config (editor setup)

Summary:
A collection of additional lab exercises and exploratory code used to strengthen understanding of Python fundamentals and testing.




