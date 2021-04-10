import face_recognition
import numpy as np
import cv2
import os
from django.shortcuts import render
from django.utils import timezone
import datetime


def static_rec(image_to_test):

    test_image = face_recognition.load_image_file(image_to_test)

    known_face_encodings = []
	known_face_names = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
	
	base_dir = os.getcwd()
	image_dir = os.path.join(base_dir,"{}/{}/{}".format('media','images','case'))
	print(image_dir)
	names = []

    for root,dirs,files in os.walk(image_dir):
		for file in files:
			if file.endswith('jpg') or file.endswith('png'):
				path = os.path.join(root, file)
				img = face_recognition.load_image_file(path)
				label = file[:len(file)-4]
				img_encoding = face_recognition.face_encodings(img)[0]
				known_face_names.append(label)
				known_face_encodings.append(img_encoding)

     
	face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    #looping through the face locations and the face embeddings
    for current_face_location,current_face_encoding in zip(face_locations,face_encodings):
        #splitting the tuple to get the four position values of current face
        top_pos,right_pos,bottom_pos,left_pos = current_face_location
        
        
        #find all the matches and get the list of matches
        all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)
    
        #string to hold the label
        name_of_person = 'Unknown face'
        
        #check if the all_matches have at least one item
        #if yes, get the index number of face that is located in the first index of all_matches
        #get the name corresponding to the index number and save it in name_of_person
        if True in all_matches:
            first_match_index = all_matches.index(True)
            name_of_person = known_face_names[first_match_index]
            name = name_of_person
        else:
            print("No match")

    return name
        
        """ #draw rectangle around the face    
        cv2.rectangle(original_image,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)
        
        #display the name as text in the image
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(original_image, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)
        
        #display the image
        cv2.imshow("Faces Identified",original_image) """