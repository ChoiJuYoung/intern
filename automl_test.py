import cv2
import tensorflow as tf

_pbPath = "automl_test"
_imgPath = "cloud.jpg"
img = cv2.imread(_imgPath)
flag, bts = cv2.imencode('.jpg', img)
inp = [bts[:,0].tobytes()]
loaded = tf.saved_model.load(export_dir=_pbPath)
infer = loaded.signatures["serving_default"]
out = infer(key=tf.constant('something_unique'), image_bytes=tf.constant(inp))

labels = [lbl.decode('utf-8') for lbl in out['labels'].numpy()[0]] 
print(labels)
scores = out['scores'].numpy()[0]
print(scores)

result = {keys: values for keys, values in zip(labels, scores)}
print(result)
prob = sorted(result.items(), key = lambda item: item[1], reverse = True) 

print("=" * 120)
print(prob) 
print("HIGHEST: " + prob[0][0])
print()