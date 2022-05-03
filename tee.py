import cv2
# import numpy as np

#cap = cv2.VideoCapture('rtsp://admin:btg$2021@10.140.128.209:554/Streaming/Channels/101')
#cap = cv2.VideoCapture('rtsp://admin:888888@192.168.1.52:10554/tcp/av0_0')
cap = cv2.VideoCapture('rtsp://Honeywell:Cctv!111@10.140.128.50:554')
# cap = cv2.VideoCapture('rtsp://admin:Honeywell123$@192.168.1.108:554')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Egg01.avi', fourcc, 20, (1280, 720))

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (1280, 720), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()