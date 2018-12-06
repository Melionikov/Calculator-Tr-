import cv2
import numpy as np 

cap = cv2.VideoCapture("vid2.mp4") #Cihan, attigin videoyu vid2 olarak kaydettim
kernelOpen = np.ones((2,2))
kernelClose = np.ones((55,55))
#tolerans gostermesi icin


while True:

    _, image = cap.read()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([49, 120, 190]) 
    upper_green = np.array([70, 255, 255])
    #yukaridaki iki boundary yesil icin

    mask = cv2.inRange(hsv, lower_green, upper_green)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    #Goruntelenecek seyleri en sona koymam gerektigini burdan ogrendim

    maskOpen = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    _, conts, h = cv2.findContours(maskClose.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #basa _ koymasam calismiyodu neden??!!
    #Value Error veriyordu.
    cv2.drawContours(image, conts, -1, (0, 0, 225), 2) 

    cv2.imshow("close", maskClose)
    cv2.imshow("open", maskOpen)
    mask2 = cv2.imshow("vid2.mp4", image)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27: #esc ye basinca cikar kendileri
        break

cap.release()
cv2.destroyAllWindows()
