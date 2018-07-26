import cv2
import numpy as np
import pdb


def find_contours(binary_image):
    _, contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours


def remove_contours(contours, cmin, cmax):
    large_contours = [c for c in contours if cmin < c.shape[0] < cmax]
    return large_contours


def get_corners(contours):
    remove_contours(contours, 100, 50000)
    cnt_corners = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True) * 0.02, True)
        if approx.shape[0] == 4 and cv2.isContourConvex(approx):
            cnt_corners.append(approx)
    return cnt_corners


def convert_corner_point(corner):
    points = []
    for p in corner:
        points.append([p[0][0], p[0][1]])
    return np.array(points, np.float32)


img = cv2.imread('/Users/apple/Downloads/test.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cnts = find_contours(binary)
corners = get_corners(cnts)
corner_img = np.copy(img)
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 0, 255)]
for c in corners:
    for i, point in enumerate(c):
        cv2.circle(corner_img, (point[0][0], point[0][1]), 10, colors[i % 4])
cv2.imwrite('/Users/apple/Downloads/cornered.jpg', corner_img)
# pdb.set_trace()
target_points = np.array([[0, 0], [0, 149], [149, 149], [149, 0]], np.float32)
for i, c in enumerate(corners):
    points = convert_corner_point(c)
    trans_mat = cv2.getPerspectiveTransform(points, target_points)
    output_img = cv2.warpPerspective(img, trans_mat, (150, 150))
    cv2.imwrite('/Users/apple/Downloads/output' + str(i) + '.jpg', output_img)
