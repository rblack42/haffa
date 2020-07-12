from svgelements import *
from Shapes import paths, boxes
from svgelements import Path

SVGDIR = "svg"


class Badge(object):

    def __init__(self, height):
        """ load shape and position data"""
        print("Generating SVG file for height %d" % height)
        self.paths = paths
        self.boxes = boxes

    def normalize(self, path):
        """ normalize path to height of 1000"""
        box = path.bbox()
        x1, y1, x2, y2 = box
        dx = x2 - x1
        dy = y2 - y1
        scale = 1000 / dy
        t = "translate(%s,%s)" % (-x1, -y1)
        s = "scale(%s)" % scale
        tp = path * t
        sp = tp * s
        return sp

    def transform(self, shape, x, y, w, h):
        print("transforming", x, y, w, h)
        bbox = shape.bbox()
        print(bbox)
        x1, y1, x2, y2 = bbox
        bdx = x2 - x1
        bdy = y2 - y1
        scalex = w/bdx
        scaley = h/bdy
        print(bdx, bdy)
        s = 'scale(%s,%s)' % (scalex, scaley)
        t = 'translate(%s,%s)' % (x, y)
        print(s, t)
        sc = shape * s
        tc = sc * t
        return tc

    def gen_raw_svg(self):
        """generate standard view of shapes"""
        for s in self.paths:
            shape_path = paths[s]
            sp = Path(shape_path)
            sp = self.normalize(sp)
            bb = sp.bbox()
            x1, y1, x2, y2 = bb
            dx = x2 - x1
            dy = y2 - y1
            sp = self.transform(sp, 20, 20, dx*0.6, dy*0.6)
            d = sp.d()
            db = "M 20,20 h %s v %s H 20 V 20 Z" % (dx*0.6, dy*0.6)
            svg = """<svg width="%d" height="%d"
                xmlns="http://www.w3.org/2000/svg" >""" % (dx, dy)
            svg += """ <path style="fill:none"
  stroke="black" stroke-width="3" d="%s" />""" % db
            svg += """
   <path style="fill:none" stroke="red" stroke-width="3" d="%s" />""" % d
            svg += """"
</svg>"""
            fname = "%s/raw_%s.svg" % (SVGDIR, s)
            with open(fname, "w") as fout:
                fout.write(svg)

    def gen_placement(self):
        cx1, cy1, cx2, cy2 = self.boxes["canvas"]
        width = cx2 - cx1 + 10
        height = cy2 - cy1 + 10
        svg = """<svg width="%d" height="%d"
  xmlns="http://www.w3.org/2000/svg"
>""" % (width, height)

        for b in self.boxes:
            if b == "canvas":
                continue
            shape = b
            if len(b) == 2:
                shape = shape[0]
            print("placing ", b, " with shape: ", shape)
            path = self.paths[shape]
            x1, y1, x2, y2 = self.boxes[b]
            w = x2 - x1
            h = y2 - y1
            print(x1, y1, x2, y2, w, h)
            sp = Path(path)
            sp = self.normalize(sp)
            sp = self.transform(sp, x1, y1, w, h)
            print("shape box:", sp.bbox())
            d = sp.d()
            svg += """
  <rect x="%d" y="%d"
    width="%d" height="%d"
    stroke="black" stroke-width="2"
    fill="none" />""" % (x1, y1, w, h)
            svg += """
  <path style="fill:none" stroke="red" stroke-width="3" d="%s" />""" % d

        svg += "</svg>"
        with open("svg/layout.svg", "w") as fout:
            fout.write(svg)

    def get_logo_placement(self, size):
        """calculate scale and x,y to fit in circle of radius=size"""
        x1, y1, x2, y2 = boxes["canvas"]
        width = x2 - x1
        height = y2 - y1
        ar = width / height

if __name__ == "__main__":
    l = Logo(1000)
    heart = paths["heart"]
    bbox = boxes["heart"]
    print(heart)
    p = Path(heart)
    print(p.d())
    print(p.bbox())
    x1, y1, x2, y2 = bbox
    print(x1, y1, x2, y2)
    l.gen_raw_svg()
    l.gen_placement()

