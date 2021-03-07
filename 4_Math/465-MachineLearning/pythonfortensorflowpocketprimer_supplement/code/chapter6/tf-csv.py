import tensorflow as tf

csv_file = './simple.csv'
dataset = tf.data.experimental.make_csv_dataset(csv_file, batch_size=2)
iter = dataset.make_one_shot_iterator()
next = iter.get_next()

# next is a dict with key=columns names and value=column data
print("next:",next) 
inputs, labels = next['text'], next['sentiment']

with tf.Session() as sess:
  sess.run([inputs, labels])
  print("inputs:",sess.run([inputs, labels]))

