import tensorflow as tf

with tf.name_scope("my_scope"):
    with tf.variable_scope("sadasd"):
        v1 = tf.get_variable("var1", [1], dtype=tf.float32)
        v2 = tf.Variable(1, name="var2", dtype=tf.float32)
        a = tf.add(v1, v2)

print(v1.name)  # var1:0
print(v2.name)  # my_scope/var2:0
print(a.name)   # my_scope/Add:0