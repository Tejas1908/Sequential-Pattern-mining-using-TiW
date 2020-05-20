import matplotlib.pyplot as plt

def is_none(l, length):
	if l is None:
		return [None for ii in range(length)]
	else:
		assert len(l), length
		return l

# no. pattern vs threshold for delta = 0.5 0.7 0.9
def plt_graphs(xss, yss, labels=None, colors=None, markers=None, x_label="x - axis", y_label="y - axis"):
	l = len(xss)
	assert l, len(yss)

	labels = is_none(labels, l)
	markers = is_none(markers, l)
	colors = is_none(colors, l)

	for ll in range(l):
		plt.plot(xss[ll], yss[ll], label=labels[ll], color=colors[ll], marker=markers[ll])
	plt.legend()
	plt.show()


plt_graphs([[1, 2]], [[2, 2]])
