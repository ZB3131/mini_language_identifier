# mini_language_idenitifier

[![View on GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/ZB3131/mini_language_identifier)

This is a beginner-friendly implementation of a text classification model that identifies the language of a given text (short samples).
It uses character n-grams as features and is trained on a subset of the WiLI-2018 dataset. It is built with Python and NLTK and is trained on a Naive Bayes calssifier.
I have tried it on 11 languages (including ones with non-Latin script), but you can add more. In the model, I used it on 5 languages. The languages can be changed. Please refer to the "labels" .csv file for the language labels in the wiLI-2018 folder.
The model works by converting each sentence into small chunks of characters (n-grams), for example `"hallo"` with n=3 → `"hal"`, `"all"`, `"llo"`.
These n-grams are used as features to train a Naive Bayes classifier.
The model learns patterns of letters in different languages.
You can then type a sentence, and the model predicts the language.

The dataset used is the [WiLI-2018 dataset](https://zenodo.org/record/841984).
It contains text in 235 languages.
Due to size restrictions, the dataset is not included in the repository. Please download it from the previous link and extract the folder into the project directory.

Requirements:
- Python 3.x
- [NLTK](https://www.nltk.org/install.html)  

Clone the repository to your computer:
```bash
git clone https://github.com/ZB3131/mini_language_identifier_.git
```
Move into the project folder:
```
cd mini_language_identifier_
```
And install nltk:
```bash
pip install nltk
```
After cloning, you can open `language_identifier.py` in your desired code editor and make your own modifications (adjusting the feature extractor, classifier, languages, or test sample). Please make sure that the dataset files ("x_train", "y_test", etc.) are also in the folder; otherwise you will get the `No such file or directory` error.
Then run the script:
```bash
python language_identifier.py
```
Example output:
```bash
Input: "dobro jutro"
Predicted language: bos
```
Future Improvements:

- Trying different feature extractors (word n-grams, stopwords)

- Comparing performance with scikit-learn classifiers

- Modifying to handle longer text samples and multi-language texts

