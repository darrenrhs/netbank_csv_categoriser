#!/usr/bin/python3

import datetime
import pytz
import sys

# Open the file and read it into memory, close after

try:
    print("Input file is " + str(sys.argv[1]))
except IndexError:
    print("No input file detected. Provide a file path as an argument when calling this script.")
else:
    csvfile = open(sys.argv[1], "r")
    lines = csvfile.readlines()
    csvfile.close

    # Set up categories

    from categories import categories

    # Create an output file to write to. Filename includes time, set to Melbourne by default.

    timenow = datetime.datetime.now(tz=pytz.timezone('Australia/Melbourne')).strftime("%Y_%m_%d-%H_%M_%S-%Z")
    filename = str("netbank-" + timenow + ".csv")
    print("Output file is " + filename)
    outfile = open(filename, "x")

    # Function for assigning categories to each line

    def search_cat(payload):
        cats = categories.items()
        for cat in cats:
            catlist = cat[1]
            cat = cat[0]
            for shop in catlist:
                if shop in payload:
                    return outfile.write(payload + ",\"" + cat + "\"\n")
        return outfile.write(payload + ",\"unknown\"" + "\n")

    # Loop through each line

    for line in lines:
        line = line.strip()
        search_cat(line)

    # Close output flie

    outfile.close