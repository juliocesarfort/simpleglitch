#!/usr/bin/python
#
# simpleglitch.py: world's crappiest and slowest file format fuzzer used to
# generate image files that can hopefully be considered glitch art.
#
# This code mutates files at random in the byte level. New heuristics and
# increased word/byte/bit-level granularity should be added to create better
# glitches.
#
# by Julio Cesar Fort - julio@whatever.io
# made with <3 in Krakow, Poland

import sys
import os
import random
import time
import argparse
import glitchutils

# --- set defaults ---
ERROR = -1
DEFAULT_GLITCH_FACTOR = 0.0007
DEFAULT_SEED = time.time()
HEADER_LENGTHS = {'jpg':9, 'png':8}

# --- set globals ---
iteration = 0

def generate_glitch(input_file, glitch_factor, filetype):
    global iteration
    input_file_contents = []
    output_file_contents = []
    
    mutator = glitchutils.mutators()
    random.seed(time.time())
    index_ext = input_file.rfind('.')
    
    if index_ext == ERROR:
        print '[!] Error: missing file extension.'
        sys.exit(ERROR)

    orig_filename = input_file[:index_ext]
    orig_extension = input_file[index_ext:]

    output_file = orig_filename + '-glitch-' + str(iteration) + orig_extension
    
    try:
        skip_factor = HEADER_LENGTHS[filetype]
        fd_in = open(input_file, 'rb')
        fd_out = open(output_file, 'wb')
    except IOError as err:
        print '[!] Error opening file: %s' % str(err)
        sys.exit(ERROR)
    except KeyError:
        print '[!] Unknown file extension %s' % filetype
        sys.exit(ERROR)

    contents = list(fd_in.read())

    # copy the original file contents into a list
    for n in xrange(len(contents)):
        input_file_contents.append(contents[n])
    
    # save the header of the original input file
    for k in xrange(skip_factor):
        output_file_contents.append(input_file_contents[k])
    
    
    for i in xrange(len(input_file_contents) - skip_factor):
        if random.random() < glitch_factor / 100:
            output_file_contents.append(os.urandom(1))
        else:
            output_file_contents.append(input_file_contents[i])
    
    output_file_contents = ''.join(output_file_contents)    
    
    fd_out.write(output_file_contents)
    fd_in.close()
    fd_out.close()


def main():
    # file to be glitched, number of iteractions, heuristics, seed
    #parser = argparse.ArgumentParser(description="Glitch art generator")
    #parser.add_argument()
    generate_glitch('samples/Mona_Lisa.jpg', DEFAULT_GLITCH_FACTOR, 'jpg')

    
if __name__ == '__main__':
    main()