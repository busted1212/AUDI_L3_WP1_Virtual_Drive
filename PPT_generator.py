# -*- coding: utf-8 -*-

import pptx


template_BSV = pptx.Presentation('checkbox-test.pptm')
sld = template_BSV.slides
sld_0 = sld[0]
print(type(sld_0))
sld_0.add_slide()
sld_0.shapes.add_picture('BSV1/lat=116.4544lng=39.959347.jpeg', 200, 200)
template_BSV.save('new-checkbox-test.pptm')
