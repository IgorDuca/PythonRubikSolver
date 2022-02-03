from pprint import pprint

def checkWhiteCross(blocks):
    for face in blocks:
        if face[1].startswith("W") and face[3].startswith("W") and face[4].startswith("W") and face[5].startswith("W") and face[7].startswith("W"):
            pprint("Face {} is matching as a whitecross.".format(face))
        else: pprint("Face {} doesn't match as a whitecross.".format(face))