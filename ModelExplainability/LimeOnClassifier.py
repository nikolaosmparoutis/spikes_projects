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

    @property
    def _pipe_random_forest(self):
        from sklearn.pipeline import Pipeline

        from sklearn.preprocessing import Normalizer
        from sklearn.decomposition import PCA

        makegray_step = self.PipeStep(lambda img_list: [rgb2gray(img) for img in img_list])
        flatten_step = self.PipeStep(lambda img_list: [img.ravel() for img in img_list])
        pipe_random_forest = Pipeline([('Step Make grayscale', makegray_step),
                                       ('Step Flatten the image', flatten_step),
                                       ('Step Normalize', Normalizer()),
                                       # ('Step Feature Selection: PCA', PCA(n_components=16).fit(self.x)),
                                       ('Step Classifier', self.classifier())])

        return pipe_random_forest

    def _data_preparation_classifier(self):
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, shuffle=True, stratify=self.y)
        self.x_y_splits = {'x_train': x_train, 'y_train': y_train, 'x_test': x_test, 'y_test': y_test}
        return self.x_y_splits

    # def _lime_image(self):
    #     from lime import lime_image
    #     from lime.wrappers.scikit_image import SegmentationAlgorithm
    #     explainer = lime_image.LimeImageExplainer(verbose=False)
    #     segmenter = SegmentationAlgorithm('quickshift', kernel_size=1, max_dist=200, ratio=0.2)
    #     return explainer, segmenter

    def train(self):
        self.x_y_splits = self._data_preparation_classifier()  # mutable object does not create new references.aka list, dicts
        from lime import lime_image
        from lime.wrappers.scikit_image import SegmentationAlgorithm
        explainer = lime_image.LimeImageExplainer(verbose=False)
        segmenter = SegmentationAlgorithm('quickshift', kernel_size=1, max_dist=200, ratio=0.2)

        self._pipe_random_forest.fit(self.x_y_splits['x_train'], self.x_y_splits['y_train'])
        # explainer, segmenter = self._lime_image()
        explanation = explainer.explain_instance(self.x_y_splits['x_test'][0],
                                                 classifier_fn=self._pipe_random_forest.predict_proba,
                                                 top_labels=10, hide_color=0, num_samples=10000,
                                                 segmentation_fn=segmenter)
        return self


from sklearn.ensemble import RandomForestClassifier
lm = LimeOnClassifier(RandomForestClassifier)
lm.load_data().train()

print(datetime.now() - start)
