from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE
ppt = Presentation()

styles = ppt.styles
chart_styles = [s for s in styles if s.type == XL_CHART_TYPE.__members__]

for style in chart_styles:
    print(style.name)