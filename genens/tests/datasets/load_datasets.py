# -*- coding: utf-8 -*-

import pandas as pd
from functools import partial

from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from sklearn.preprocessing import LabelEncoder


def load_wilt(random_state=42):
    filename = 'wilt-train.csv'
    data = pd.read_csv(filename, sep=',')
    data = shuffle(data, random_state=random_state)
    train_X = data[data.columns[1:]]
    train_y = data[data.columns[0]]
    le = LabelEncoder()

    ix = train_y.index
    train_y = pd.Series(le.fit_transform(train_y), index=ix)

    test_filename = 'wilt-test.csv'

    data = pd.read_csv(test_filename, sep=',')

    test_X = data[data.columns[1:]]
    test_y = data[data.columns[0]]
    le = LabelEncoder()

    ix = test_y.index
    test_y = pd.Series(le.fit_transform(test_y), index=ix)

    return train_X, train_y, test_X, test_y


def load_from_sklearn(load_func, random_state=42):
    data, target = load_func(return_X_y=True)
    train_X, test_X, train_y, test_y = train_test_split(data, target,
                                                        test_size=0.33, random_state=random_state)
    return train_X, test_X, train_y, test_y


load_functions = {
    'iris': partial(load_from_sklearn, load_iris),
    'digits': partial(load_from_sklearn, load_digits),
    'wine': partial(load_from_sklearn, load_wine),
    'breast_cancer': partial(load_from_sklearn, load_breast_cancer),
    'wilt': load_wilt
}


def load_dataset(dataset_name, random_state=42):
    """
    # TODO
    classification: 'wine' 'breast_cancer' 'digits' 'iris' ...
    regression: 'diabetes' 'boston' 'california (fetch)' ...
    """

    if dataset_name in load_functions:
        train_X, test_X, train_y, test_y = load_functions[dataset_name](random_state)
    else:
        raise ValueError("Invalid dataset name.")

    return train_X, train_y, test_X, test_y
