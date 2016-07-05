import numpy as np
import os, sys, pickle
import time
import matplotlib.pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'
# plt.rcParams['image.cmap'] = 'gray'
os.environ['GLOG_minloglevel'] = '2'
import caffe
caffe_root = '/Users/mo/caffe/'
caffe.set_mode_cpu()

dataset = 'day_left'
prepath = './' 
images = [f for f in os.listdir(prepath) if f.endswith('.jpg')]
images = images[:1]

def disp():
	d = 17 #size: must be an odd number
	temp1 = np.zeros( (400, d, d) )
	temp1[:384,(d-13)/2:(d+13)/2,(d-13)/2:(d+13)/2] = \
		net.blobs['conv3'].data[0]
	temp2 = np.zeros( (20*d,20*d) )
	for i in range(20):
		for j in range(20):
			temp2[d*i:d*(i+1),d*j:d*(j+1)]=temp1[j+20*i]
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	ax1.imshow(np.uint8(temp2*2))
	ax2 = fig.add_subplot(5,5,22)
	ax2.imshow(image)
	plt.axis('off')
	plt.show()

t1 = time.time()
""" load net weights and allocate memory """
print 'loading the net weigths...'
net = caffe.Net('pconv.prototxt','wconv', caffe.TEST)
net.blobs['data'].reshape(len(images), 3, 227, 227)

""" pre-processing for input """
print 'preparing for pre-processing...'
blob = caffe.proto.caffe_pb2.BlobProto()
data = open('avg','rb')
blob.ParseFromString(data.read())
mu = np.array(caffe.io.blobproto_to_array(blob))[0]
BGRmean = mu.mean(1).mean(1)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', BGRmean)
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))

""" forward step """
print 'loading the data...'
for i in range(len(images)):
  image = caffe.io.load_image(prepath+images[i])
  net.blobs['data'].data[i] = transformer.preprocess('data', image)
print 'loaded. moving forward...'
net.forward()
print 'net forward completed'
t2 = time.time()
print 'total time: %f secs, %d image(s)' %(t2-t1,len(images))

# disp()


















