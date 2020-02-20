'''
This file contains functions used to set the segmentation colours inside the unreal engine simulation
'''
import csv
import pandas
    
def get_class_dict(RGB_csv_file):
    '''
    INPUT:
    -RGB_csv_file: csv file containing objects from the simulation alongside the RGB colours that you want to labeled them as e.g
    inside the real engine simulation if all tree objects are named as tree_1,tree_2 and so on, in csv file add as a row the following           entry: tree,128,128,128
    - client: generated by setting up a connection using unrealCV
    
    OUTPUT:
    -this funcntion returns a dictionary for objects and their respective labelling colour
    '''
    # create a dictionary with classes and RGB colors associated to them from a CSV file
    class_color = pandas.read_csv(RGB_csv_file)
    
    class_dict = {}
    for line in range (len(class_color)-1):
        # adding into class dictionary
        r= str(class_color['r'][line])
        g= str(class_color['g'][line])
        b= str(class_color['b'][line])
        rgb = r+' '+g+' '+b

        class_dict.update( {class_color['class'][line] : rgb } )
        
    return class_dict


def set_colors(RGB_csv_file, client):
    '''
    INPUT:
    -RGB_csv_file: csv file containing objects from the simulation alongside the RGB colours that you want to labeled them as e.g
    inside the real engine simulation if all tree objects are named as tree_1,tree_2 and so on, in csv file add as a row the following           entry: tree,128,128,128
    - client: generated by setting up a connection using unrealCV
    
    OUTPUT:
    -this funcntion doesn't return anything but it uses unrealCV library to change the colours inside the simulation using 
    the class-colour dictionary provided by the csv file.
    '''
    
    #getting class dictionary
    class_dict= get_class_dict(RGB_csv_file)
    
    #getting list of all objects in simulation ['tree1', 'tree2',...]
    scene_objects = client.request('vget /objects').split(' ')
    
    for obj in scene_objects:

        for key in class_dict:
            if key in obj:
                rgb= class_dict[key]
                client.request('vset /object/'+obj+'/color '+rgb)
                break