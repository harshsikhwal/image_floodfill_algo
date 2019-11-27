from cv2 import *
import numpy
import queue

old_color = 127
new_color = 120
white_image = r"Resources\white.jpg"
maze = r"Resources\maze.jpg"
referencePointer = []
onKeyPress = False


# Registering a Left Button Double Click Event
# which will start the flood fill

def on_click(event, x, y, flags, param):
    global onKeyPress
    global referencePointer
    if event == cv2.EVENT_LBUTTONDBLCLK:
        referencePointer = [x, y]
        onKeyPress = True


def display_image(image, _time):
    imshow("Test", image)
    waitKey(_time)


# Recursion causes Stack Overflow in most of the cases (even for the smallest flood-fill).
# Therefore I am using loop and maintaining a queue that tracks the pixels and
# perform EnQueue/DeQueue operation accordingly

def flood_fill(row, col, old_col, new_col, image):
    q = queue.Queue(image.shape[0] * image.shape[1])
    q.put([row, col])
    while q.empty:
        display_image(image, 1)
        tup = q.get()
        row = tup[0]
        col = tup[1]
        if row - 1 >= 0 and image[row - 1, col] > old_col:
            image[row - 1, col] = new_col
            q.put([row - 1, col])
        if row + 1 < image.shape[0] and image[row + 1, col] > old_col:
            image[row + 1, col] = new_col
            q.put([row + 1, col])
        if col - 1 >= 0 and image[row, col - 1] > old_col:
            image[row, col - 1] = new_col
            q.put([row, col - 1])
        if col + 1 < image.shape[1] and image[row, col + 1] > old_col:
            image[row, col + 1] = 120
            q.put([row, col + 1])
        if row - 1 >= 0 and col - 1 >= 0 and image[row - 1, col - 1] > old_col:
            image[row - 1, col - 1] = new_col
            q.put([row - 1, col - 1])
        if row + 1 < image.shape[0] and col + 1 < image.shape[1] and image[row + 1, col + 1] > old_col:
            image[row + 1, col + 1] = new_col
            q.put([row + 1, col + 1])
        if col - 1 >= 0 and row + 1 < image.shape[0] and image[row + 1, col - 1] > old_col:
            image[row + 1, col - 1] = new_col
            q.put([row + 1, col - 1])
        if col + 1 < image.shape[1] and row - 1 >= 0 and image[row - 1, col + 1] > old_col:
            image[row - 1, col + 1] = new_col
            q.put([row - 1, col + 1])


def flood_fill_image(image):
    global referencePointer
    global onKeyPress
    global old_color
    global new_color
    while True:
        imshow("Test", image)
        key = waitKey(1)
        if onKeyPress:
            break
    flood_fill(referencePointer[1], referencePointer[0], old_color, new_color, image)


def main():
    # read Image
    image = imread(maze)
    # convert to grayscale
    image = cvtColor(image, COLOR_BGR2GRAY)
    namedWindow("Test")
    setMouseCallback("Test", on_click)
    flood_fill_image(image)
    display_image(image, 200)


if __name__ == '__main__':
    main()
