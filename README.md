# Stress Detection System

## Overview

Stress Detection System is a Python-based application that analyzes user-entered text and determines whether the text indicates stress using sentiment analysis techniques.

The project uses the NLTK VADER (Valence Aware Dictionary and Sentiment Reasoner) sentiment analyzer to evaluate text sentiment and classify it as either "Stress" or "No Stress".

## Features

* Text-based stress detection
* Sentiment analysis using NLTK VADER
* Graphical User Interface (GUI) using Tkinter
* Real-time stress classification
* Easy-to-use interface

## Technologies Used

* Python
* Tkinter
* NLTK
* VADER Sentiment Analysis

## How It Works

1. User enters a caption or text message.
2. The VADER sentiment analyzer calculates sentiment scores.
3. If the compound sentiment score is less than or equal to -0.2, the text is classified as "Stress".
4. Otherwise, it is classified as "No Stress".

## Example

Input:
"I am overwhelmed with work and feeling exhausted."

Output:
Stress

Input:
"I had a great day and completed my tasks successfully."

Output:
No Stress

## Future Enhancements

* Machine Learning based stress prediction
* Voice-based stress detection
* Stress level percentage scoring
* Data visualization dashboard

## Author

Sujana
