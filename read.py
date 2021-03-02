import cv2 as cv


def rescaleFrame(frame, scale=0.10):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#---Reading Images---
img = cv.imread('photos/dog.jpg')

cv.imshow('Dog', img)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)


#---Reading Videos---
capture = cv.VideoCapture('videos/boats.mp4') # 0 = webcam


while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



