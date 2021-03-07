import tensorflow as tf

filenames = ["comments.txt"]

ds = tf.data.Dataset.from_tensor_slices(filenames)

# Use Dataset.flat_map() to transform each file 
# as a separate nested ds, then concatenate their 
# contents sequentially into a single "flat" ds.
# Skip the first line (header row)
# Filter out lines beginning with "#" (comments)

ds = ds.flat_map(
    lambda filename: (
      tf.data.TextLineDataset(filename)
      .skip(1)
      .filter(lambda line: tf.not_equal(tf.strings.substr(line,0,1),"#"))))

for value in ds.take(2):
  print("value:",value)

