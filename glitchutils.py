#!/usr/bin/python
#
# glitchutils.py: part of simpleglitch.py, world's crappiest and slowest file
# format fuzzer used to generate image files that can hopefully be considered
# glitch art.
#
# by Julio Cesar Fort - julio@whatever.io

import os
import random
import string
import time

global glitch_factor

class mutators:
    def __init__(self, seed=time.time()):
        self.seed = seed
        random.seed(self.seed)

    def swap_bytes(self, left, right):
        new_left = right
        new_right = left
        return (new_left, new_right)
        
    def append_random_character(self, orig_bytes):
        return orig_bytes.append(self._random_character())
    
    def append_random_byte(self, orig_bytes):
        return orig_bytes.append(self._random_byte())
    
    def append_random_string(self, orig_bytes, n_bytes):
        return orig_bytes.append(self._random_string(n_bytes))
    
    def add_byte_random_location(self, orig_bytes):
        orig_bytes[random.choice(range
                                 (len(orig_bytes)))] = self._random_byte()
        return orig_bytes
        
    def add_bytes_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            orig_bytes[random.choice(range(len(orig_bytes)))] = self._random_byte()
        return orig_bytes

    def add_character_random_location(self, orig_bytes):
        orig_bytes[random.choice(range
                                 (len(orig_bytes)))] = self._random_character()
        return orig_bytes
    
    def add_characters_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            orig_bytes[random.choice
                       (range(len(orig_bytes)))] = self._random_character()
        return orig_bytes  

    def add_string_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            return
    
    def delete_last_bytes(self, orig_bytes, n_bytes):
        for i in xrange(n_bytes):
            orig_bytes.pop()
        return orig_bytes
    
    def delete_random_bytes(self, orig_bytes, n_bytes):
        for i in xrange(n_bytes):
            orig_bytes.remove(orig_bytes[random.choice(range(len(orig_bytes)))])
        return orig_bytes

    def replicate_byte_chunks_random_location(self, orig_bytes, n_bytes,
                                              times=1):
        copied_bytes = []
        copy_from_byte = random.randrange(len(orig_bytes))
        
        if copy_from_byte + n_bytes < len(orig_bytes):
            copied_bytes = orig_bytes[copy_from_byte:copy_from_byte + n_bytes]
        else:
            copied_bytes = orig_bytes[:copy_from_byte]
        
        for i in xrange(times):
            replicate_from_byte = random.randrange(len(orig_bytes))
            orig_bytes = orig_bytes[:replicate_from_byte] + copied_bytes + orig_bytes[replicate_from_byte:]
         
        return orig_bytes

    ''' NOT WORKING PROPERLY '''
    def replace_byte_chunks_random_location(self, orig_bytes, n_bytes, times=1):
        copied_bytes = []
        copy_from_byte = random.randrange(len(orig_bytes))
        
        if copy_from_byte + n_bytes < len(orig_bytes):
            copied_bytes = orig_bytes[copy_from_byte:copy_from_byte + n_bytes]
        else:
            copied_bytes = orig_bytes[:copy_from_byte]
        
        print "copied_bytes: %s" % copied_bytes
        print "copy_from_byte: %d" % copy_from_byte
            
        for i in xrange(times):
            replace_from_byte = random.randrange(len(orig_bytes))
            print "replace from byte: %d" % replace_from_byte
            for j in xrange(len(copied_bytes)):
                if replace_from_byte + len(copied_bytes) < len(orig_bytes):
                    orig_bytes[replace_from_byte + j] = copied_bytes[j]
        
        return orig_bytes

    # shuffler probably messes images up very very badly
    def shuffler(self, orig_bytes):
        return random.shuffle(orig_bytes)
    
    '''
    These are support functions that are not called directly.
    Used to generate fixed and random characters, bytes, strings.
    '''
    def _random_character(self):
        return random.choice(string.printable)
    
    def _random_byte(self):
        return os.urandom(1)
    
    def _random_string(self, n_bytes):
        string_list = []
        
        if n_bytes > 0:
            for i in xrange(n_bytes):
                string_list.append(random.choice(string.printable))
        
        return ''.join(string_list)
        
    def _not_random_string(self, character, n_bytes):
        ret_string = ''
        
        if n_bytes > 0:
            for i in xrange(n_bytes):
                ret_string += character
        
        return ret_string
    
    # _gen_random_list function is used for debugging and testing only
    def _gen_random_list(self):
        random_list = []
        for i in xrange(random.randrange(4, 8)):
            random_list.append(self._random_string(random.randrange(4, 8)))
            
        return random_list