import cv2
faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)




while (True):
    ret, videoGoruntu = cam.read()
    videoGoruntu = cv2.flip(videoGoruntu, 1)
    gray_video = cv2.cvtColor(videoGoruntu, cv2.COLOR_BGR2GRAY)
    faces = faces_cascade.detectMultiScale(gray_video, 1.1, 10)
   
    
    for (x, y, width, height) in faces:
        cv2.rectangle(videoGoruntu, (x, y), (x+width, y+height),(0, 175, 200), 3)
   
    
    cv2.imshow("Bilgisayar_Kamerasi", videoGoruntu)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

