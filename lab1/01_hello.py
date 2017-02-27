import tensorflow as tf

# Create a Constant op (operation)
hello = tf.constant('Hello, TensorFlow!') 

# Print hello
print(hello)	# Output : Tensor("Const:0", shape=(), dtype=string)

# Start tf session
sess = tf.Session()

# Print sess.run
print(sess.run(hello))	# Output : b'Hello, TensorFlow!'

print(type(sess.run(hello)))	# Output : <class, 'bytes'>

print(tf.Session().run(hello).decode(encoding='utf-8'))	# Output : Hello, TensorFlow!

print(type(tf.Session().run(hello).decode(encoding='utf-8')))	# Output : <class, 'str'>

# Close tf session
sess.close()