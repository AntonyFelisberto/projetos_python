import cv2

image = cv2.imread("watermark/elfs.jpeg")
watermark_image = cv2.imread("watermark/watermark.png")

print(image.shape)
print(watermark_image.shape)

x = image.shape[1] - watermark_image.shape[1]
print(x)
y = image.shape[0] - watermark_image.shape[0]

watermark_place = image[y:,x:]
cv2.imwrite("watermark_place.jpeg",watermark_place)
print(watermark_place.shape)

blend = cv2.addWeighted(watermark_place,0.5,watermark_image,0.5,0)
cv2.imwrite("blend.jpeg",blend)

image[y:,x:] = blend
cv2.imwrite("elfs-watermark.jpeg",image)
