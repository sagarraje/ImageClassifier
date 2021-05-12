#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sagar Raje
# DATE CREATED:  31/01/2021                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # image_dir this variable is predefined in code.
    inputimg_files = listdir(image_dir)
    #Python method listdir() returns a list containing the names of the entries in the directory given by path
    
    
    # for the Pet Image filenames (as keys) and a List that contains the filenames associated labels (as values) we are going to use dictionary.
    # Creates  dictionary with varible results_dic
    results_dic = dict()
    
    # calculate number of items in dictionary
    dictionary_items = len(results_dic)
    
    
    for count in range (0, len(inputimg_files), 1):
        if inputimg_files[count][0] != ".": # to skip file which starts with "."
            petname_label = ""
            petname_image = inputimg_files[count]  #take file name 1 by 1
            petname_image_in_lowercase = petname_image.lower()   #places letters in lower case only.
            list_pet_image = petname_image_in_lowercase.split("_")
            # returns a list of words from a string, where the words have been separated (split)
            #by the delimiter provided to the split function. If no delimiter is provide, splits on whitespace.
            for worditr in list_pet_image:
                if worditr.isalpha(): #check the value is alphabetic char
                    petname_label += worditr + " "
            petname_label = petname_label.strip() #returns a string with leading & trailing characters removed. If no characters are provided, strips leading
            
        if inputimg_files[count] not in results_dic:
            results_dic[inputimg_files[count]] = [petname_label]
        else:
            print("The Key=", inputimg_files[count],
               "already exists in return_disc please refer following value =",
               results_dic[inputimg_files[count]])
            
    
    print("\nthe values of dictionary return_disc ")
    for val in results_dic:
        print("Filename value", val, "   labelname =", results_dic[val][0])
    
    return results_dic
