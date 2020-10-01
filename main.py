import json
import argparse

def draw(key, expr):
    inp = []
    for i in expr[key]:
        if type(i) is dict:
            inp.append(i+"_"+draw(i,expr[key]).join('_'))
        else:
            inp.append(i)

    return inp
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="echo the string you use here")
    args = parser.parse_args()
    
    with open(args.file) as file:
        expr = json.load(file)
        

        for key in expr:
            print(draw(key, expr.get(key)))
        
        
            
