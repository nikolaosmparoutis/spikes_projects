from datetime import datetime

start = datetime.now()
import numpy as np
# pip install scikit-image
from skimage.color import gray2rgb, rgb2gray, label2rgb  # since the code wants color images
from sklearn.datasets import fetch_openml
from matplotlib import pyplot as plt


def _set_lime():
    import os, sys
    try:
        import lime
    except:
        sys.path.append(os.path.join('..', '..'))  # add the current directory
        import lime


class LimeOnClassifier:

    def __init__(self, classifier):
        self.x = []
        self.y = []
        self.x_y_splits = {}  # keys: x_train, y_train, x_test, y_test
        self.classifier = classifier
        self.estimator = None
        _set_lime()

    def load_data(self):
        mnist = fetch_openml('mnist_784')
        # make each image color so lime_image works correctly
        g2rgb = []
        for img in mnist.data.values.reshape((-1, 28, 28)):
            g2rgb.append(gray2rgb(img))
        # trick: mutable object can referenced without new creation of reference
        self.x = np.stack(g2rgb, 0).astype(np.uint8)
        self.y = mnist.target.astype(np.uint8)
        x_vec = self.x
        y_vec = self.y

        fig, ax1 = plt.subplots(1, 1)
        ax1.imshow(x_vec[0], interpolation='none')
        ax1.set_title('Digit: {}'.format(y_vec[0]))
        return self

    class PipeStep(object):
        """
        Wrapper for turning functions into pipeline transforms (no-fitting)
        """

        def __init__(self, step_func):
            self._step_func = step_func

        def fit(self, *args):
            return self

        def transform(self, X):
            return self._step_func(X)

    def _pipeline_classifier(self):
        from sklearn.pipeline import Pipeline

        from sklearn.preprocessing import Normalizer
        from sklearn.decomposition import PCA

        makegray_step = self.PipeStep(lambda img_list: [rgb2gray(img) for img in img_list])
        flatten_step = self.PipeStep(lambda img_list: [img.ravel() for img in img_list])
        pipe_random_forest = Pipeline([('Step Make grayscale', makegray_step),
                                       ('Step Flatten the image', flatten_step),
                                       ('Step Normalize', Normalizer()),
                                       # ('Step Feature Selection: PCA', PCA(n_components=16)),
                                       ('Step Classifier', RandomForestClassifier())])

        return pipe_random_forest

    def _data_split(self):
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, shuffle=True, stratify=self.y)
        return {'x_train': x_train, 'y_train': y_train, 'x_test': x_test, 'y_test': y_test}

    def train(self):
        self.x_y_splits = self._data_split()  # mutable object does not create new references.aka list, dicts
        self.estimator = self._pipeline_classifier().fit(self.x_y_splits['x_train'], self.x_y_splits['y_train'])
        return self

    def get_explainability(self):
        """Local Interpretable Model Agnostic Explanations"""
        self.x_y_splits = self._data_split()  # mutable object does not create new references.aka list, dicts
        self.estimator = self._pipeline_classifier().fit(self.x_y_splits['x_train'], self.x_y_splits['y_train'])
        from lime import lime_image
        from lime.wrappers.scikit_image import SegmentationAlgorithm
        explainer = lime_image.LimeImageExplainer(verbose=False)
        segmenter = SegmentationAlgorithm('quickshift', kernel_size=1, max_dist=200, ratio=0.2)

        explanation = explainer.explain_instance(self.x_y_splits['x_test'][0],
                                                 classifier_fn=self.estimator.predict_proba,
                                                 top_labels=10, hide_color=0, num_samples=10000,
                                                 segmentation_fn=segmenter)

        temp, mask = explanation.get_image_and_mask(self.x_y_splits['y_test'][0], positive_only=True, num_features=10,
                                                    hide_rest=False,
                                                    min_weight=0.01)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
        ax1.imshow(label2rgb(mask, temp, bg_label=0), interpolation='nearest')
        ax1.set_title('Positive Regions for {}'.format(self.x_y_splits['y_test'][0]))
        temp, mask = explanation.get_image_and_mask(self.x_y_splits['y_test'][0], positive_only=False, num_features=10,
                                                    hide_rest=False,
                                                    min_weight=0.01)
        ax2.imshow(label2rgb(3 - mask, temp, bg_label=0), interpolation='nearest')
        ax2.set_title('Positive/Negative Regions for {}'.format(self.x_y_splits['y_test'][0]))

from sklearn.ensemble import RandomForestClassifier

lm = LimeOnClassifier(RandomForestClassifier)
lm.load_data().train().get_explainability()
plt.show()
print(datetime.now() - start)

