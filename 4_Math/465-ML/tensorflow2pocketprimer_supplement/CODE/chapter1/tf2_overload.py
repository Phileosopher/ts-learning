import tensorflow as tf

@tf.function
def add(a):
  return a + a

print("Add 1:            ", add(1))
print("Add 2.3:          ", add(2.3))
print("Add string tensor:", add(tf.constant("abc")))

c = add.get_concrete_function(tf.TensorSpec(shape=None, dtype=tf.string))
c(a=tf.constant("a"))  
print("c:",c)

