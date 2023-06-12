
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('img.png', 30)

colors_extracted = []
for color in colors:
    colors_extracted.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(colors_extracted)

[(251, 244, 248), (240, 249, 245), (13, 20, 78), (221, 151, 87), (32, 94, 158), (238, 228, 110), (134, 24, 54), (208, 80, 117), (191, 77, 27), (50, 28, 18), (19, 45, 140), (118, 178, 218), (15, 47, 27), (230, 73, 47), (3, 100, 35), (206, 131, 172), (166, 54, 85), (72, 22, 35), (22, 135, 49), (141, 213, 182), (251, 225, 0), (90, 202, 160), (169, 15, 8), (94, 112, 199), (85, 81, 19), (8, 175, 210), (17, 180, 141), (237, 167, 152)]
