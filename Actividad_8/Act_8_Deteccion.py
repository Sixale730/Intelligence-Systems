#Julio Alexis Gonzalez Villa       220839961
#Natalie Xiomara Moreno Bautista   220839996
#Miguel Alejaandro Medina Bravo

#---------------------------Actividad 8_ Detección de Números------------------------------
import numpy as np
import cv2
import pickle

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

model = pickle.load(open('act_8_numeros.sav','rb'))

while True:
    ret, frame = video.read()
    	
    if ret is False:
        break

    corners, ids, _ = detector.detectMarkers(frame)

    if len(corners) > 0 and len(ids)==1:
        points = np.asarray(corners)
        points = points.reshape(4,2)
        points = points.astype(int)
        
        p1 = points[0,:]
        p2 = points[1,:]
        p3 = points[2,:]
        p4 = points[3,:]
        
        frame = cv2.circle(frame,tuple(p1),5,(255,0,0),-1)
        frame = cv2.circle(frame,tuple(p2),5,(0,255,0),-1)
        frame = cv2.circle(frame,tuple(p3),5,(0,0,255),-1)
        frame = cv2.circle(frame,tuple(p4),5,(0,255,255),-1)
        
        d = 2*(abs(p3[0]-p4[0]))

        # frame[y:y+h,x:x+w]
        number = frame[p3[1]:p3[1]+d,p3[0]:p3[0]+d]

        # rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 10)
        frame = cv2.rectangle(frame, (p3[0],p3[1]), (p3[0]+d,p3[1]+d), (0,255,0), 2)
        
        number = cv2.cvtColor(number,cv2.COLOR_BGR2GRAY)
        _ , number = cv2.threshold(number,100,255,cv2.THRESH_BINARY_INV)
        number = cv2.resize(number,(28,28))
        
        pattern = number.reshape(1,784)        
        
        num_p = pattern.reshape(-1,1)
        
        data = [float(j) for j in num_p]
        data_array = np.asanyarray(data)
        
        y = model.predict(data_array.reshape(-1,784))
        
        print('Numero: ', y)

        number = cv2.resize(number,(100,100))
        cv2.imshow("Number", number)

    cv2.imshow("Image", frame)

    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break


cv2.destroyAllWindows()
video.release()