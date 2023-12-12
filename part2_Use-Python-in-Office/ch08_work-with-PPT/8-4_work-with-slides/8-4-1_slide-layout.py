from pptx import Presentation

ppt = Presentation()

print(len(ppt.slide_layouts))

for layout in ppt.slide_layouts:
    print(type(layout), layout.name)