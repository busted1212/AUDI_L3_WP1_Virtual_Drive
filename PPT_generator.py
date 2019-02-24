# -*- coding: utf-8 -*-

import pptx


template_BSV = pptx.Presentation('checkbox-test.pptm')
sld = template_BSV.slides
sld_0 = sld[0]
sld.add_slide()
sld.shapes.add_picture('BSV1/lat=116.4544lng=39.959347.jpeg', 200, 200)
template_BSV.save('new-checkbox-test.pptm')
