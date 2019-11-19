import cv2
import sqlite3

image_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_feed = cv2.VideoCapture(0)


def get_profile(student_id, student_name):
    connection = sqlite3.connect("database/facebase.db")
    command = "SELECT * FROM students WHERE ID = " + student_id
    cursor = connection.execute(command)
    record_exists = 0
    for row in cursor:
        record_exists = 1
    if record_exists == 1:
        command = "UPDATE TABLE students SET Name = '" + str(student_name) + "' WHERE ID = " + student_id
    else:
        command = "INSERT INTO students(ID, Name) VALUES(" + student_id + ", '" + str(student_name) + "')"
        connection.execute(command)
        connection.commit()
        connection.close()


student_id = input("Enter User ID: ")
student_name = input("Enter Username: ")
image_version = 0
get_profile(student_id, student_name)

while True:
    ret, image = video_feed.read()
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = image_classifier.detectMultiScale(grayscale_image, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.imwrite("dataset/" + str(student_name) + "." + str(student_id) + ".version." + str(image_version) + ".jpg", grayscale_image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        image_version = image_version + 1
        cv2.waitKey(100)
    cv2.imshow("Face", image)
    cv2.waitKey(1)
    if image_version > 20:
        break

video_feed.release()
cv2.destroyAllWindows()
