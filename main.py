import TakePicture
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt
import numpy as np
import os.path
import pickle
from database import *

'''
#take picture
@ -38,15 +42,74 @@ for k, d in enumerate(detections):
#ask user if they want to add to database
'''
def main():
    th = .39
    font = {
            'color': 'white',
            }
    db=None
    if (os.path.exists('database.dict')):
        try:
            savefile = open('database.dict', 'rb')
            db = pickle.load(savefile)
            savefile.close()
        except:
            db=dict()
    else:
        db=dict()
    while input('take picture?\n') != 'q':
        picture = TakePicture.take_pic()
        fig, ax = plt.subplots()
        ax.imshow(picture)
        rectangles = TakePicture.find_rectangles(picture)

        for r in rectangles:
            rect = Rectangle((r[0], r[1]), r[2], r[3], linewidth=1, edgecolor='r', facecolor='none')

            ax.add_patch(rect)
        ax.imshow(picture)




        ds = TakePicture.get_descriptor(picture)
        unknowns=list()
        for ind, d in enumerate(ds):
            r=rectangles[ind]
            name = match_face(d,db,th)
            plt.text(r[0]+40,r[1]+30,name,fontdict=font)
            if name == 'unknown':
                unknowns.append(ind)
            else:
                db[name](ds[ind])

        plt.show()
        plt.clf()

        for ind in unknowns:
            r = rectangles[ind]
            fig, ax = plt.subplots()
            ax.imshow(picture)
            rect = Rectangle((r[0], r[1]), r[2], r[3], linewidth=1, edgecolor='y', facecolor='none')
            ax.add_patch(rect)
            plt.text(r[0], r[1] +r[3]+ 40, 'Enter name into console', fontdict=font)
            plt.show()
            newname = input('Who was that?\n (leave empty to not add)')
            if len(newname) > 0:
                desc=ds[ind]
                if newname in db:
                    db[newname](desc)
                else:
                    db[newname]=Profile(newname, np.array([desc]))
            plt.clf()

        savefile = open('database.dict', 'wb')
        pickle.dump(db, savefile)
        savefile.close()

def match_face(descriptor, db, th):
    for name, d in db.items():
        if np.linalg.norm(d.mean_descriptor-descriptor) < th:
            return name
    return 'unknown'