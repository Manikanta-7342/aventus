import cv2
from pyzbar import pyzbar
import numpy as np
from collections import Counter
import time

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
def open_camera_for_long():
# Open the camera
    # Check if the camera was successfully opened
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera.")
        exit()
    data=[]
    all_codes=[]
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
        if len(data)>=10:
            most_common = most_common_element(data)
            all_codes.append(most_common)


            display_text = True
            start_time = time.time()

        # Display the frame in an OpenCV window

            # Display text on the window for 2 seconds
            while(display_text):
                elapsed_time = time.time() - start_time
                if elapsed_time < 2:
                    cv2.putText(frame, "Scanned", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.imshow("Barcode Scanner", frame)
                else:
                    display_text = False
            time.sleep(3)
            data=[]



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # # Display the frame with detected barcodes
        # cv2.imshow("Barcode Scanner", frame)
        # Wait for the 'q' key to exit

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
    return all_codes

print(open_camera_for_long())