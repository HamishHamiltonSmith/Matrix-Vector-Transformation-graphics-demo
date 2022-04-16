def multiple(ihat,jhat,points):
    result = []

    for p in points:
        result.append([p[0]*ihat[0] + p[1]*jhat[0],p[0]*ihat[1] + p[1]*jhat[1]])

    return result

def get_determinent(ihat,jhat):
    return (ihat[0]*jhat[1])-(ihat[1]*jhat[0])