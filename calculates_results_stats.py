#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Sagar Raje
# DATE CREATED:   30/01/2021                                    
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    #empty dictionary for calculated result stat
    cal_results_stats_dic = dict()
    
    
    # Initialised value to o 
    #You will need to initialize all the counts to a value of zero before 
    #iterating through results dictionary. As you iterate through results dictionary, 
    #if certain criterion are met you will need to increment these counters by 1.
    
    cal_results_stats_dic['n_dogs_img'] = 0
    cal_results_stats_dic['n_match'] = 0
    cal_results_stats_dic['n_correct_dogs'] = 0
    cal_results_stats_dic['n_correct_notdogs'] = 0
    cal_results_stats_dic['n_correct_breed'] = 0 
    
    print("print value of result dictionary",results_dic)
    
    #iterate the result dictinary 
    
    for count in results_dic:
        if results_dic[count][2] == 1:
            cal_results_stats_dic['n_match'] += 1  # lables to match values.
        if results_dic[count][3] == 1 and results_dic[count][2] == 1:
            cal_results_stats_dic['n_correct_breed'] +=1 #Image lable is dog and count is correct bread
        if results_dic[count][3] == 1:
            cal_results_stats_dic['n_dogs_img'] += 1
            if results_dic[count][4] == 1:
                cal_results_stats_dic['n_correct_dogs'] += 1  #Image lable is dog and count correct dogs classification
            
        else:
            if results_dic[count][4] == 0:
                cal_results_stats_dic['n_correct_notdogs'] += 1 # correct not dog calssification    
                
                
        #print("geet",cal_results_stats_dic['n_correct_notdogs']) 
        #print("n_match",cal_results_stats_dic['n_match'])
        #print("cal_results_stats_dic",cal_results_stats_dic['n_correct_breed'])
        #print("n_dogs_img",cal_results_stats_dic['n_dogs_img'])
        #print("n_correct_dogs",cal_results_stats_dic['n_correct_dogs'])
        
      # count number of total images
    cal_results_stats_dic['n_images'] = len(results_dic) # calculate number of image   
    
    # count number of total images which are not dogs 
    cal_results_stats_dic['n_notdogs_img'] = (cal_results_stats_dic['n_images'] - 
                                      cal_results_stats_dic['n_dogs_img'])
    
    cal_results_stats_dic['pct_match'] = cal_results_stats_dic['n_match']/cal_results_stats_dic['n_images']*100
    
    #print("value of n n_dogs_img dogs",cal_results_stats_dic['n_dogs_img'])
    cal_results_stats_dic['pct_correct_dogs'] = cal_results_stats_dic['n_correct_dogs']/cal_results_stats_dic['n_dogs_img']*100
        
    cal_results_stats_dic['pct_correct_breed'] = cal_results_stats_dic['n_correct_breed']/cal_results_stats_dic['n_dogs_img']*100
    
    if cal_results_stats_dic['n_notdogs_img'] > 0:
        cal_results_stats_dic['pct_correct_notdogs'] = (cal_results_stats_dic['n_correct_notdogs'] /
                                                cal_results_stats_dic['n_notdogs_img'])*100.0
    else:
        cal_results_stats_dic['pct_correct_notdogs'] = 0.0

      
   
    return cal_results_stats_dic
