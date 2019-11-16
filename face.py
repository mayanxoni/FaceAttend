import cv2
import sqlite3

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


def getProfile(student_id, student_name):
    conn = sqlite3.connect("facebase.db")
    cmd = "SELECT * FROM students WHERE ID = " + student_id
    cursor = conn.execute(cmd)
    recordExists = 0
    for row in cursor:
        recordExists = 1
    if recordExists == 1:
        cmd = "UPDATE TABLE students SET Name = '" + str(student_name) + "' WHERE ID = " + student_id
    else:
        cmd = "INSERT INTO students(ID, Name) VALUES(" + student_id + ", '" + str(student_name) + "')"
        conn.execute(cmd)
        conn.commit()
        conn.close()


id = input("Enter User ID: ")
name = input("Enter Username: ")
ver = 0
getProfile(id, name)

while True:
    ret, img = cam.read()
    grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(grayscale_image, 1.3, 5)
    for(x, y, w, h) in faces:
        flipped_image = cv2.flip(grayscale_image, 1)
        cv2.imwrite("dataSet/"+str(name)+"." + str(id) + ".version." + str(ver) + ".jpg", flipped_image[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        ver = ver + 1
        cv2.waitKey(100)
    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if ver > 20:
        break

cam.release()
cv2.destroyAllWindows()
