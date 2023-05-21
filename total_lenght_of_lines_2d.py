class LineTo:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class PathLines:
    def __init__(self, *elements):
        self.segments = [LineTo(0, 0)]
        if elements:
            for el in elements:
                self.segments.append(el)
    
    def get_path(self):
        return self.segments
    
    def get_length(self):
        coord_lines = ((self.segments[i-1], self.segments[i]) for i in range(1, len(self.segments)))
        full_lenght = list(map(lambda c: (((c[0].x - c[1].x) ** 2 + (c[0].y - c[1].y) ** 2) ** 0.5), coord_lines))
        
        return sum(full_lenght)
    
    def add_line(self, line):
        self.segments.append(line
        
#line1 = LineTo(1, 1)
#line2 = LineTo(2, 2)
#line3 = LineTo(4, 4)

#p = PathLines(line1, line2, line3)
#print(round(sum(p.get_length()), 2))

#p.add_line(LineTo(5, 5))
#print(round(sum(p.get_length()), 2))