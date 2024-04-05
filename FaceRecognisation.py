# Install the library first: pip install face_recognition

import face_recognition
import cv2

# Load an image with known faces
known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load an unknown image
unknown_image = face_recognition.load_image_file("unknown_face.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the encodings
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("Match! The faces belong to the same person.")
else:
    print("No match. These faces are different.")

# Display the images (optional)
cv2.imshow("Known Face", known_image)
cv2.imshow("Unknown Face", unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
