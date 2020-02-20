'''
This file contains a function that generates a camera trajectory from an unreal engine simulation
'''

import csv
import os

def set_camera_traj(camera_traj_file,client):
    '''
    INPUT: 
    - camera_traj_file: name of csv file where the trajectroy will be saved into e.g 'camera_traj.csv'
    - client: generated by setting up a connection using unrealCV
    
    OUTPUT:
    - csv file containing the x,y,z locations and pitch,yaw,roll of the camera where every row is a specific location
    '''

    # Name of file where positions are saved into
    output = camera_traj_file

    #Getting input from user
    frames = int(input('How many frames do you want?'))

    #list to store positions
    loc_list = []
    rot_list = []

    i= 0 #counter
    #getting possitions
    while i<frames:
        loc = client.request('vget /camera/0/location') # x, y and z
        rot = client.request('vget /camera/0/rotation') #pitch, yaw, roll
        n_loc = loc.split(' ')
        n_rot = rot.split(' ')
        if n_loc not in loc_list and n_rot not in rot_list:
            loc_list.append(n_loc)
            rot_list.append(n_rot)
            i+=1
            
    #writing positions to csv file
    for i in range (0,len(loc_list)):
        x = loc_list[i][0]
        y= loc_list[i][1]
        z= loc_list[i][2]
        pitch = rot_list[i][0]
        yaw = rot_list[i][1]
        roll = rot_list[i][2]    
        if os.path.isfile(output): #if file exists don't add column header
            with open(output, mode='a', newline='') as csv_file:
                fieldnames = ['x', 'y','z','pitch','yaw','roll']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'x':x, 'y': y, 'z': z, 'pitch':pitch, 'yaw':yaw, 'roll':roll})
        else:  #if file does not exist then add column header
            with open(output, mode='w',newline='') as csv_file:
                fieldnames = ['x', 'y','z','pitch','yaw','roll']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({'x':x, 'y': y, 'z': z, 'pitch':pitch, 'yaw':yaw, 'roll':roll})