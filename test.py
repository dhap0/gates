import schemdraw
import schemdraw.elements as elm

#lbl = [ "A", "B", "C", "D", "I", "J", "K"]

def nparalel(el, n, d, lbl):
    nr = n//2
    nl = n - nr
    # right part
    dr = schemdraw.Drawing()
    dr.push()
    for i in range(nr):
        dr.add(elm.Line(d="right"))
        dr.push()
        dr.add(el(d="right", rgtlabel=lbl[i+nl]))
        #dr.add(elm.Dot(color="black"))
        dr.add(elm.Line(d="left"))
        dr.pop()
    dr.pop() 
    for i in range(nl):
        if n > 1:
            dr.add(elm.Line(d="left"))
        dr.push()
        dr.add(el(d="right", rgtlabel=lbl[nl-1-i]))
        #dr.add(elm.Dot(color="black"))
        if n > 1:
            dr.add(elm.Line(d="right"))
        if i == 0:
            xy=dr.here
        dr.pop()

    d.add(elm.ElementDrawing(dr))
    return d, xy

def nserie(el,n,d,xy):
    d.add(el(at=xy))
    for i in range(n-1):
        d.add(el)
    return d



def nand(d, inp=[]):
    pfet = elm.PFet
    nfet = elm.NFet
    n = len(inp)
    d, xy = nparalel(pfet, n, d, inp)

    d.add(elm.Line(at=xy, l=((n//2)+1)*3, rgtlabel="out"))
    d.add(elm.Arrowhead())
    d = nserie(nfet, n, d, xy)
    return d

    
if __name__ == "__main__":
    
    d = schemdraw.Drawing()

    d.add(elm.Vdd(label="Vdd"))
    nand(d, ["A", "B", "C" ])
    d.add(elm.Ground(botlabel="GND"))
    print(d.here)
    d.draw()
