import tensorflow as tf


def expression(f_d):
    with g.as_default():
        x = tf.multiply(tf.add(tf.pow(f_d['a'], 2), f_d['b']), f_d['c']) #(a^2+b)*c
        sess = tf.Session(graph=g)  # session is run on the graph g
        op = sess.run(x)
        print(op)
        sess.close()

g = tf.Graph()

feed_dict = {"a": 2, "b": 3, "c": 5}
expression(feed_dict)