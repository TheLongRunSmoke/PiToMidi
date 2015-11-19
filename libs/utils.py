import os
import glob

"""Some utility function are here.
"""

def is_number(s):
    """ Check is argument a number or not.
    Args:
        s: any unicode symbol.
    Returns:
        bool: True if number, otherwise False.
    Rises:
        TypeError, ValueError.
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def argv_resolver(argv):
    """Resolve command line args.
    Args:
        Argv: array of command line args getting with sys.argv().
    Returns:
        fromFile: text file contain input data.
        toFile: name for output file, must be *.mid.
        OR
        bool: False if problem occur.
        Errors: string with error message.
    """
    if len(argv) > 1:
        fromFile = argv[1]
        if not(argv[1][-4:] == '.txt'):
            return False, 'Error: input file must be *.txt'
        if not(os.path.isfile(fromFile)):
            return False, ' '.join(['Error: ', fromFile, 'file not found.'])
        if len(argv) == 3:
            if not(argv[2][-4:] == '.mid'):
                return False, 'Error: output file must be *.mid'
            toFile = argv[2];
        else:
            toFile = '.'.join([argv[1][0:-4], 'mid'])
    else:
        if (len(glob.glob("*.txt"))) > 0:
            fromFile = glob.glob("*.txt")[0]
            toFile = '.'.join([fromFile[0:-4], 'mid'])
        else:
            return False, usingHelp
    return fromFile, toFile

def compute_params( imgSize, paddingMin, fontSize, count, antialiasing ):
    """Calculate params for neat symbol positioning.
    Args:
        imgSize: tuple ( width, height ) of output image.
        paddingMin: minimal padding from image border.
        fontSize: font size in pt.
        count: tuple ( columns, row ) of symbol.
        antialiasing: oversampling size.
    Returns:
        padding: tuple ( x,y )
        interval: tuple ( x,y )
    """
    glyphX = fontSize*0.5*antialiasing
    glyphY = fontSize*0.6*antialiasing
    paddingX = (imgSize[0]*antialiasing - ((imgSize[0]*antialiasing-paddingMin*2*antialiasing)/count[0])*count[0])/2
    paddingY = (imgSize[1]*antialiasing - ((imgSize[1]*antialiasing-paddingMin*2*antialiasing)/count[1])*count[1])/2
    intervalX = (imgSize[0]*antialiasing-paddingX*2-glyphX*count[0])/float(count[0]-1)*0.99
    intervalY = (imgSize[1]*antialiasing-paddingY*2-glyphY*count[1])/float(count[1]-1)*0.96
    return ( paddingX, paddingY ), ( intervalX+glyphX, intervalY+glyphY )

"""Strings
"""
usingHelp = 'PiToMidi - convert txt to midi. Text file must contain numbers. Dots, commas, etc is allowed.\nUsing:\nPiToMidi input.txt\nor\nPiToMidi input.txt output.mid\nor\nJust place *.txt in current dir.'

def bar(x):
    return {
        0: '|',
        1: '/',
        2: '-',
        3: '\\',
    }[x]
