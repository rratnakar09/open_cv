# setting camera parameter i.e reshape the width and height of capturing video stream
# writing date time on video stream

import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# setting the width and height of cap frame
cap.set(3, 1208)  # 3 for width
cap.set(4, 720)  # 4 for height

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        # write the date_time on video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width " + str(cap.get(3)) + " Height " + str(cap.get(4))
        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, date_time, (10, 50), font, 1,
                            (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
