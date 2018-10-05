#Ex23 Strings, Bytes and Character Encodings

#Importation du module sys
import sys

#Unpacking
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() #read a line

    if line: #if the line is not empty (end of file)
        print_line(line, encoding, errors) #we run the function print_line
        return main(language_file,encoding, errors) #and we run the main function again


def print_line(line, encoding, errors):
    next_lang = line.strip() #stripping the line (removing \n)
    raw_bytes = next_lang.encode(encoding, errors=errors) #encoding the line to raw bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) #then decoding the raw bytes to a comprehensible string

    print(raw_bytes,"<===>", cooked_string) #printing the result



languages = open("languages.txt",encoding="utf-8") #open the file with uft-8 encoding

main(languages, input_encoding, error) #call the main function to start this module
