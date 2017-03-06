import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add = tf.add(a, b)
sub = tf.sub(a, b)
mul = tf.mul(a, b)
div = tf.div(a, b)
rem = tf.mod(a, b)

with tf.Session() as sess:
	print("Addition with constants : %i" % sess.run(add, feed_dict={a:2, b:3}))
	print("Subtraction with constants : %i" % sess.run(sub, feed_dict={a:2, b:3}))
	print("Multiplication with constants : %i" % sess.run(mul, feed_dict={a:2, b:3}))
	print("Division with constants : %f" % sess.run(div, feed_dict={a:2, b:3}))
	print("Remainder from division with constants : %i" % sess.run(rem, feed_dict={a:2, b:3}))