import tensorflow as tf

sess = tf.Session()

a = tf.constant(2)
b = tf.constant(3)

c = a + b

print(c)

print(sess.run(c))

print("Addition with constants : %i" % sess.run(a+b))
print("Subtraction with constants : %i" % sess.run(a-b))
print("Multiplication with constants : %i" % sess.run(a*b))
print("Division with constants : %f" % sess.run(a/b))
print("Quotient obtained from division with constants : %i" % sess.run(a/b))
print("Remainder obtained from division with constants : %i" % sess.run(a%b))