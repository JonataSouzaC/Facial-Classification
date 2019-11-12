# import libraries
import cv2
import matplotlib.pyplot as plt
import cvlib as cv

image_path = 'teste3.jpeg'
im = cv2.imread(image_path)

# nova = im[325:363, 92:140]
# plt.imshow(nova)
# plt.show()
#plt.imshow(im)
#plt.show()

faces, confidences = cv.detect_face(im)
# loop through detected faces and add bounding box
for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]
    # draw rectangle over face
    cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2)


    print('oi')
# display output
plt.imshow(im)
plt.show()