import matplotlib.pyplot as plt
import numpy as np
from node import *
import collections

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
        graph.append(Node(i,nlist,dlist[i]))
    return graph

def whispers_algor(graph):

    adj = np.zeros(len(graph),len(graph))
    llist=tuple(i.label for i in graph)
    prev=tuple(-1 for i in range(len(graph)))
    count=0
    while llist!=prev and count<100:
        for index,nd in enumerate(graph):
            mostCommon = collections.Counter(nd.neighbors).most_common(1)[0]
            nd.label = mostCommon
            adj[index,nd.label] = 1
            adj[nd.label,index] = 1
        prev=llist
        llist=tuple(i.label for i in graph)
        count+=1
    print(count)

    plot_graph(graph,adj)





