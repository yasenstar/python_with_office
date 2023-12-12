from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE

print(len(MSO_AUTO_SHAPE_TYPE.__members__))

for shape in MSO_AUTO_SHAPE_TYPE.__members__:
    print(shape.value, shape.name)