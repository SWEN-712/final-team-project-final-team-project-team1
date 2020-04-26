import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
from collections import Counter

im = cv2.imread('./static/uploads/t5.jpg')
bbox, label, conf = cv.detect_common_objects(im)
print(label)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()


def object_detect(filename):
    """
    This function will detect objects in image
    """
    just_fname = filename.split(".")[0]
    im = cv2.imread('./static/uploads/'+filename)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)

    plt.savefig(os.path.join('./static/output/', just_fname+'.png'))
    # Image.open('testplot.png').save('testplot.jpg','JPEG')
    # plt.show()
    d = Counter(label)
    # labelstr = ' '.join([str(elem) for elem in label])
    labelstr = ", ".join('{} {}'.format(v, k) for k, v in d.items())

    return labelstr
