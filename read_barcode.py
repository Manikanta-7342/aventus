import cv2
from pyzbar import pyzbar
from collections import Counter

# Function to get the most common element in the list
def most_common_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None


# Function to scan barcodes in the frame
def scan_barcodes(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use the ZBar library to detect and decode barcodes
    barcodes = pyzbar.decode(gray)

    # Loop over detected barcodes
    for barcode in barcodes:
        # Extract the barcode data as a string
        barcode_data = barcode.data.decode("utf-8")

        # Draw a rectangle around the barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw the barcode data and type on the image
        text = f"{barcode_data} ({barcode.type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Print the barcode data to the console
        return barcode_data
        # print("Barcode Data:", barcode_data)
def open_camera():
# Open the camera
    # Check if the camera was successfully opened
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera.")
        exit()
    data=[]

    # Loop over frames from the camera
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if a frame was successfully read
        if not ret:
            print("Failed to capture frame.")
            # cv2.CAP_V4L2
            break

        # Scan for barcodes in the frame
        item=scan_barcodes(frame)
        # print(item)
        if item==None:
            # Display the frame with detected barcodes
            cv2.imshow("Barcode Scanner", frame)
        else:
            # Display the frame with detected barcodes
            cv2.imshow("Barcode Scanner", frame)
            data.append(item)
            # print(item)

        # # Display the frame with detected barcodes
        # cv2.imshow("Barcode Scanner", frame)
        # Wait for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q') or len(data)>=10:
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
    most_common = most_common_element(data)
    return most_common


# print(open_camera())