import cv2
cap_device = 2						# built-in camera of MacBook Pro 2018
cap = cv2.VideoCapture(cap_device)
print(cap.set(cv2.CAP_PROP_FPS, 120))
cfps = cap.get(cv2.CAP_PROP_FPS)
print(cfps)

# while cap.isOpened():
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
