#!/usr/bin/env python3

#Created by Lucas V. Araujo <lucas.vieira.ar@disroot.org>

import os
import optparse
from PIL import Image

def main():
    parser = optparse.OptionParser(usage='%prog [-o <out_dir>] [-q] <dir>')
    parser.add_option('-o', '--output-directory', dest='out_dir',
                      help='The directory to save the images')
    parser.add_option('-q', '--quiet', action='store_true', dest='verbose',
                      default=True, help="Don't print status messages")
    (options, args) = parser.parse_args()

    if (len(args) == 0):
        print('You must specify a directory containing image files!')
        exit(0)

    save_dir = options.out_dir or args[0]

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    if (save_dir == args[0]):
        confirm = input('The files will be overwritten. Are you sure? (y/n)')
        if (confirm.upper() != 'Y'):
            print('You can also specify an output directory with the -o .')
            print("If the directory doesn't exist, it will be created.")
            exit(0)

    for file in os.listdir(args[0]):
        fname = os.path.basename(file)
        oname = fname[:fname.rindex('.')] + '.jpeg'
        img = Image.open(os.path.join(args[0], file))
        img.save(os.path.join(save_dir, oname), dpi=(300.0, 300.0))
        if (options.verbose):
            print("[+] Converted %s" %fname)

if __name__ == '__main__':
    main()
