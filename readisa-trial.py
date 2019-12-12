import os
import errno
import isatools
import json
import requests

from isatools import isatab
from isatools.convert import isatab2json, json2isatab

# input_file_path = '/Users/philippe/Documents/git/elixir-europe/plant-brapi-to-isa/outputdir/POPYOMICS/'
# output_file_path = '/Users/philippe/Documents/git/elixir-europe/plant-brapi-to-isa/outputdir/POPYOMICS/' + "brapi2isa-test0-poppy" + '.json'

input_file_path = '/Users/philippe/Documents/git/ISAdatasets/tab/BII-I-1/'


JSON_INPUT_BIII1 = '/Users/philippe/Documents/git/ISAdatasets/json/BII-I-1/BII-I-1.json'
outputdirI1 = '/Users/philippe/Documents/git/ISAdatasets/json/massi-test/BII-I-1-conversion/'

JSON_INPUT_BIIS3 = '/Users/philippe/Documents/git/ISAdatasets/json/BII-S-3/BII-S-3.json'
outputdirS3 = '/Users/philippe/Documents/git/ISAdatasets/json/massi-test/BII-S-3-conversion/'

JSON_INPUT_BIIS7 = '/Users/philippe/Documents/git/ISAdatasets/json/BII-S-7/BII-S-7.json'
outputdirS7 = '/Users/philippe/Documents/git/ISAdatasets/json/massi-test/BII-S-7-conversion/'


input = os.path.join(input_file_path, 'i_investigation.txt')
# print("INPUT", input)




try:

    # my_isa_read = isatab.load(open(input))
    # print("reading in:", my_isa_read.studies)

    try:

        isa_json = isatab2json.convert(input_file_path, use_new_parser=True, validate_first=False)
        with open(outputdirI1, 'w') as out_fp:
            json.dump(isa_json, out_fp, indent=4)

    except Exception as excep:
        print(excep)

    try:
        # isa_tab = json2isatab.convert(output_file_path)
        # print("ISATAB: ", isa_tab)
        with open(JSON_INPUT_BIII1) as file_pointer:
            # print(file_pointer)
            # investigation = json.load(file_pointer)
            # try:
            #     json2isatab.convert(JSON_INPUT_BIIS7, outputdirS7, validate_first=True)
            # except IOError as ioe:
            #     print(ioe)

            #isatab.dump(
            json2isatab.convert(file_pointer, outputdirI1, validate_first=False)
                #, outputdirS7)

    except Exception as excep2:
        print(excep2)



except IOError as e:
    print(e)
