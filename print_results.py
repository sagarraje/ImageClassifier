#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Sagar Raje
# DATE CREATED:   31/01/2021  
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    #Print param value of function.
    
    #print("Param value of 1,2,3,4,5",results_dic,results_stats_dic,print_incorrect_dogs,print_incorrect_breed)
    
    #print model value 
    print("*******************************************************************")
    print("Print the result of model",model.upper().center(50))
    print("*******************************************************************")
    
    
    #Print the n_images and n_dogs_img
    #with the param value print result in format
    print("{:<20}: {:>3d}".format('correct img', results_stats_dic['n_images']))
    print("{:<20}: {:>3d}".format('Dog IMG', results_stats_dic['n_dogs_img']))
    print("{:<20}: {:>3d}".format('not dog images', results_stats_dic['n_notdogs_img'])) # print the count of not dog Images.
    
    
    
    
    #iterating through the results_stats dictionary printing out the statistic's name and value for all of the percentages (e.g. key that starts with       #the     #letter "p"). Recall that we had recommended that we used the same prefix (e.g. pct_) to all of the percentage statistics, so that they could all be             #printed out as a group.
    
    # Prints summary statistics (percentages) on Model Run
    print("Print  statistics in % on Model Run")
    #initialised for on stat dictionary 
    for count in results_stats_dic:
        if count.startswith('p'):
            print(count, results_stats_dic[count])
        #check if param value of print_incorrect_breed is true and n_correct_dogs is not n_correct_breed then print incorrect breed  
        #print_incorrect_breed - defaults to False
    if (print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) ):
        print("\nIn-correct Dog Breed Assignment:")
        
        # results dictionary, printing incorrectly classified dog breeds
        #User wants to print misclassifications:
        #print_incorrect_dogs == True
        #Some dogs were misclassified:
        #n_correct_dogs + n_correct_notdogs != n_images
        #If the check is True, then print the pet image and classifier labels for misclassified dogs when:
        #The labels disagree on whether or not an image is of a "dog"
        
        for count in results_dic:
            if (results_dic[count][3] == 1 and results_dic[count][4] == 0) or (results_dic[count][3] == 0 and results_dic[count][4] == 1): 
                print(results_dic[count][0], results_dic[count][1])
                
        if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) 
       ):
            print("\nINCORRECT Dog Breed Assignment:")    
            
         # print incoreect clasifier dog
        for val in results_dic:

            # the vlaue is dog but with incorrect classifier 
 
            if ( sum(results_dic[val][3:]) == 2 and results_dic[val][2] == 0 ):
                print("\ncorrect val: {:>26}   Dog Classifier: {:>30}".format(results_dic[val][0],results_dic[val][1])) 
                
