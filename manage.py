import os
import sys
from sklearn.datasets import load_files
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import joblib

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)

def my_model():
    train = load_files('C:/aclImdb//train')
    text_train, y_train = train.data, train.target

    test = load_files('C:/aclImdb//test')
    text_test, y_test = test.data, test.target

    cv = my_cv()

    X_train = cv.transform(text_train)
    #X_test = cv.transform(text_test)

    logit = LogisticRegression(n_jobs=-1, random_state=42)
    logit.fit(X_train, y_train)

    #print(logit.score(X_train, y_train), logit.score(X_test, y_test))
    
    return logit

def my_cv():
    train = load_files('C:/aclImdb//train')
    text_train = train.data
    cv = CountVectorizer()
    cv.fit(text_train)
    return cv


if __name__ == '__main__':

    model = my_model()
    cv = my_cv()
    filename_model = 'log_model'
    filename_cv = 'cv_model'
    joblib.dump(model, filename_model)
    joblib.dump(cv, filename_cv)

    main()
