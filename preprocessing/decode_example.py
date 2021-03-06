from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

def decode_serialized_example(serialized_example, features_to_fetch, decode_image=True):
    """
    Args:
        serialized_example : A tfrecord example
        features_to_fetch : a list of tuples (feature key, name for feature)
    Returns:
        dictionary : maps name to parsed example
    """

    feature_map = {}
    for feature_key, feature_name in features_to_fetch:
        feature_map[feature_key] = {
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/colorspace': tf.FixedLenFeature([], tf.string),
            'image/channels': tf.FixedLenFeature([], tf.int64),
            'image/format': tf.FixedLenFeature([], tf.string),
            'image/filename': tf.FixedLenFeature([], tf.string),
            'image/id': tf.FixedLenFeature([], tf.string),
            'image/encoded': tf.FixedLenFeature([], tf.string),
            'image/extra': tf.FixedLenFeature([], tf.string),
            'image/class/label': tf.FixedLenFeature([], tf.int64),
            'image/class/text': tf.FixedLenFeature([], tf.string),
            'image/class/conf':  tf.FixedLenFeature([], tf.float32),
            'image/object/bbox/xmin': tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/xmax': tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/ymin': tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/ymax': tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/label': tf.VarLenFeature(dtype=tf.int64),
            'image/object/bbox/text': tf.VarLenFeature(dtype=tf.string),
            'image/object/bbox/conf': tf.VarLenFeature(dtype=tf.float32),
            'image/object/bbox/score' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/parts/x' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/parts/y' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/parts/v' : tf.VarLenFeature(dtype=tf.int64),
            'image/object/parts/score' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/count' : tf.FixedLenFeature([], tf.int64),
            'image/object/area' : tf.VarLenFeature(dtype=tf.float32),
            'image/object/id' : tf.VarLenFeature(dtype=tf.string)
        }[feature_key]

    features = tf.parse_single_example(
      serialized_example,
      features = feature_map
    )

    # return a dictionary of the features
    parsed_features = {}

    for feature_key, feature_name in features_to_fetch:
        if feature_key == 'image/height':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/width':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/colorspace':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/channels':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/format':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/filename':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/id':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/encoded':
            if decode_image:
                parsed_features[feature_name] = tf.image.decode_jpeg(features[feature_key], channels=3)
            else:
                parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/extra':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/class/label':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/class/text':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/class/conf':
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/object/bbox/xmin':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/xmax':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/ymin':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/ymax':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/label':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/text':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/conf':
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/bbox/score' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/parts/x' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/parts/y' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/parts/v' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/parts/score' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/count' :
            parsed_features[feature_name] = features[feature_key]
        elif feature_key == 'image/object/area' :
            parsed_features[feature_name] = features[feature_key].values
        elif feature_key == 'image/object/id' :
            parsed_features[feature_name] = features[feature_key].values

    return parsed_features