import argparse
import os

import chainer
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def main():

    # Parse arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', **{
        'type': str,
        'help': 'The embeddings.npy file path.',
        'required': True
    })
    args = parser.parse_args()

    # Load embeddings file.
    embeddings = np.load(args.source)

    # Compress each embeddings to 2 dimension using PCA.
    pca = PCA()
    pca.fit(embeddings)

    # Load label data.
    _, val = chainer.datasets.get_mnist(ndim=3)
    labels = np.array([y for x, y in val])

    assert (len(labels) == len(embeddings))

    for label in range(10):
        indices = np.where(labels == label)
        x, y = np.ravel(embeddings[indices, 0]), np.ravel(embeddings[indices, 1])
        plt.scatter(x, y, label=str(label))
    plt.legend()
    head, ext = os.path.splitext(args.source)
    plt.savefig(f'{head}.png')


if __name__ == '__main__':
    main()