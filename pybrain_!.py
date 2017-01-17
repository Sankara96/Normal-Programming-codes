from pybrain.tools.shortcuts import buildNetwork
import simpleai
net = buildNetwork(2, 3, 1)
print net.activate([2,1])
print net