# -*- coding: utf-8 -*-

import pptx
from pptx.util import Inches, Pt

# prs = pptx.Presentation('checkbox-test.pptm')
# # select a layout template
# graph_slide_layout = prs.slide_layouts[6]
# # use the selected layout to create a new slide
# slide_1 = prs.slides.add_slide(graph_slide_layout)
# print(type(slide_1.shapes))
# slide_2 = prs.slides.add_slide(graph_slide_layout)
# prs.save('checkbox-test_new.pptm')


prs = pptx.Presentation('checkbox-test.pptm')
first_slide = prs.slides[0]
first_slide_layout = first_slide.slide_layout
for shape in first_slide.placeholders:
    print(shape.placeholder_format.idx)
    print(shape.name)
    #print('%d %s' % (shape.placeholder_format.idx, shape.name))
placeholder_1 = first_slide.placeholders[13]

#slide_1 = prs.slides.add_slide(first_slide)
# do something with the content of the slides
#prs.save('new-file-name.pptm')