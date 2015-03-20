# I have not had the time to test this method yet
# so do not use it in its current state

import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curves(training_data, 
                         training_targets, 
                         test_data, 
                         test_targets,
                         classifier,
                         kind="training_size",
                         marker="o",
                         style="ggplot"):
    """
    Plots learning curves of a classifier

    Params:
            @training_data : matrix, shape=[n_samples, n_features]
            Feature matrix of the training dataset

            @training_targets : array, shape=[n_samples]
            True class labels of the training dataset

            @test_data : matrix, shape=[n_samples, n_features]
            Feature matrix of the test dataset

            @test_targets : array, shape=[n_samples]
            True class lables of the test dataset

            @classifier : object    (Must have a .fit and .predict  method)
            The object used to classify the data. 

            @kind : str             (Default: "training_size")
            "training_size" or "n_features"
            Plots missclassifications vs. training size or number of features

            @marker : str           (Default: "o")
            Marker for the line plot

            @style : str            (Default: "ggplot")
            The style of the plot, using plt.style method

    Returns:
            @(training_error, test_error) : tuple of lists
    """
    training_errors = []
    test_errors = []

    if kind not in ("training_size", "n_features"):
        raise ArgumentError("Kind must be 'training_size' or 'n_features'")
    
    if kind == "training_size":
        data_range = [int(i) for i in np.linspace(0, training_data.shape[0], 11)][1:][::-1]
        for r in data_range:
            classifier.fit(training_data[:r], training_targets[:r])

            train_predictions = classifier.predict(training_data[:r])
            train_misclassifications = (train_predictions != training_targets[:r]).sum()
            training_errors.append(train_misclassifications / training_data[:r].shape[0])

            test_predictions = classifier.predict(test_data)
            test_misclassifications = (test_predictions != test_targets).sum()
            test_errors.append(test_misclassifications / test_data.shape[0])

        plt.plot(np.arrange(10, 101, 10), training_errors, label="Training errors", marker=marker)
        plt.plot(np.arrange(10, 101, 10), test_errors, label="Test errors", marker=marker)
        plt.xlabel("Training set size in percent")
    
    if kind == "n_features":
        data_range = np.arrange(1, training_data.shape[1]+1)
        
        for r in data_range:
            classifier.fit(training_data[:, 0:r], training_targets]
            train_predictions = classifier.predict(training_data[:, 0:r])
            train_misclassifications = (train_predictions != training_targets).sum()
            training_errors.append(train_misclassifications / training_data.shape[0])

            test_predictions = classifier.predict(test_data[:, 0:r])
            test_misclassifications = (test_predictions != test_targets).sum()
            test_errors.append(test_misclassifications / test_data.shape[0])

        plt.plot(data_range, training_errors, label="Training errors", marker=marker)
        plt.plot(data_range, test_errors, label="Test errors", marker=marker)
        plt.xlabel("Number of features")

    if not style in plt.style.available:
        raise ArgumentError("style has to be on of the following: %s" % plt.style.available)
    else:
        plt.style.use(style)

    plt.ylabel("Number of misclassifications")
    plt.title("Learning curves")
    pl.ylim([0,1])
    plt.legend(loc=1)

    return (training_errors, test_errors)
