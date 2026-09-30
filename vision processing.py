import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
     print("Error: Could not open webcam")
     exit()

print("Webcam started")
print("Press 'q' to stop")

while True:

   
     ret, frame = cap.read()

     if not ret:
         print("Error: Could not read frame")
         break

    
     frame = cv2.resize(frame, (640, 480))

    
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     cv2.imshow("Original Video", frame)

    
     cv2.imshow("Processed Frame", gray)


     if cv2.waitKey(1) & 0xFF == ord("q"):
         break


cap.release()


cv2.destroyAllWindows()

print("Webcam stopped")

