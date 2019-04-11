# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def export_plot(estimator, out_file):
    sns.set()

    gen = estimator.logbook.select("gen")
    score_max = estimator.logbook.chapters["score"].select("max")
    score_avg = estimator.logbook.chapters["score"].select("avg")

    test_max = estimator.logbook.chapters["test_score"].select("max")
    test_avg = estimator.logbook.chapters["test_score"].select("avg")

    test_all_zero = np.all(test_max == 0.0) and np.all(test_avg == 0.0)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Score")

    line1 = ax1.plot(gen, score_max, label='Maximum Score')
    line2 = ax1.plot(gen, score_avg, label='Average Score')

    if test_all_zero:
        lines = line1 + line2
    else:
        line3 = ax1.plot(gen, test_max, label='Maximum Test score')
        line4 = ax1.plot(gen, test_avg, label='Average Test score')

        lines = line1 + line2 + line3 + line4

    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="best")

    plt.savefig(out_file)
    plt.close()
