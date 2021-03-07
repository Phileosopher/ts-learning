import tensorflow as tf

x = tf.Variable(10.)
#checkpoint = tf.train.Checkpoint()
checkpoint = tf.train.Checkpoint(x=x)
print("x:",x)  # => 10.0

# Assign a new value to x and save
x.assign(3.)   
print("x:",x)  # => 3.0
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/')

# Change the variable after saving.
x.assign(25.)  
print("x:",x)  # => 25.0

# Restore values from the checkpoint
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))
print("x:",x)  # => 3.0

