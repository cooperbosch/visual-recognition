import database
from node import *
import whispers
import TakePicture
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt
import numpy as np

'''
#take picture

TakePicture.take_pic()

#access database and find names for

#display w rectangles and names

from matplotlib.patches import Rectangle
fig,ax = plt.subplots()
ax.imshow(pic)

for r in rectangles:
    rect = Rectangle((r[0],r[1]),r[2],r[3],linewidth=1,edgecolor='r',facecolor='none')

    ax.add_patch(rect)



print("Number of faces detected: {}".format(len(detections)))
for k, d in enumerate(detections):
    # Get the landmarks/parts for the face in box d.
    shape = shape_predictor(pic, d)
    # Draw the face landmarks on the screen.
    for i in range(68):
        ax.plot(shape.part(i).x,shape.part(i).y,'+',color="blue")

#ask for names of unknowns

#ask user if they want to add to database
'''
def main():
    while input('take picture?\n') != 'q':
        picture = TakePicture.take_pic()
        fig, ax = plt.subplots()
        ax.imshow(picture)
        rectangles = TakePicture.find_rectangles(picture)
        for r in rectangles:
            rect = Rectangle((r[0], r[1]), r[2], r[3], linewidth=1, edgecolor='r', facecolor='none')

            ax.add_patch(rect)



if __name__ == "__main__":
    main()

