import matplotlib.pyplot as plt
import numpy as np
from node import *

def histogram(db):
    same_x=list()
    diff_x=list()
    vals=[i.arr for i in list(db.values())]
    for v in vals:
        arr=v.arr
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                same_x.append(np.linalg.norm(arr[i]-arr[j]))
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            for v1 in vals[i]:
                for v2 in vals[j]:
                    diff_x.append(np.linalg.norm(v1-v2))
    bins=np.linspace(0,2,20)  
    plt.hist(same_x,bins,alpha=0.5,label="same")
    plt.hist(diff_x,bins,alpha=0.5,label="different")


def make_graph(dlist, thresh):
    graph=list()
    for i in range(len(dlist)):
        nlist=list()
        for j in range(len(dlist)):
            if i!=j:
                if np.linalg.norm(dlist[i]-dlist[j]) < thresh:
                    nlist.append(j)
        graph.append(Node(i,nlist,dlist[i])
    return graph
