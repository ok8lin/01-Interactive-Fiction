#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "3EE7CCFD-7E2A-4A15-B3DE-67E592F6A873",
  "name": "interactive fiction",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631378297263,
  "passages": [
    {
      "name": "Apartment",
      "tags": "",
      "id": "1",
      "text": "You step out of your apartment. You can either drive or take the bus.\n[[DRIVE->Car]]\n[[BUS->Bus]]",
      "links": [
        {
          "linkText": "DRIVE",
          "passageName": "Car",
          "original": "[[DRIVE->Car]]"
        },
        {
          "linkText": "BUS",
          "passageName": "Bus",
          "original": "[[BUS->Bus]]"
        }
      ],
      "hooks": [],
      "cleanText": "You step out of your apartment. You can either drive or take the bus."
    },
    {
      "name": "Car",
      "tags": "",
      "id": "2",
	  "score":1, 
      "text": "You get in your car and start drving. Traffic is really bad and you are running late. You park at the stadium and wait for the bus into campus. You can either take the X bus or the W bus.\n[[X BUS->X Route]]\n[[W BUS->W Route]]",
      "links": [
        {
          "linkText": "X BUS",
          "passageName": "X Route",
          "original": "[[X BUS->X Route]]"
        },
        {
          "linkText": "W BUS",
          "passageName": "W Route",
          "original": "[[W BUS->W Route]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get in your car and start drving. Traffic is really bad and you are running late. You park at the stadium and wait for the bus into campus. You can either take the X bus or the W bus."
    },
    {
      "name": "Bus",
      "tags": "",
      "id": "3",
	  "score":5, 
      "text": "You get on the bus and meet a new friend. They're getting off at the sample gates. You can either get off or stay on the bus.\n[[GET OFF->Sample Gates]]\n[[STAY->Bus Route]]",
      "links": [
        {
          "linkText": "GET OFF",
          "passageName": "Sample Gates",
          "original": "[[GET OFF->Sample Gates]]"
        },
        {
          "linkText": "STAY",
          "passageName": "Bus Route",
          "original": "[[STAY->Bus Route]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get on the bus and meet a new friend. They're getting off at the sample gates. You can either get off or stay on the bus."
    },
    {
      "name": "Sample Gates",
      "tags": "",
      "id": "4",
	  "score":2,
      "text": "You get off at the sample gates. You and your new friend decide to go to the media school lobby to study. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get off at the sample gates. You and your new friend decide to go to the media school lobby to study. You can type YES to play again or QUIT to exit."
    },
    {
      "name": "Bus Route",
      "tags": "",
      "id": "5",
	  "score":1,
      "text": "You stay on the bus and let your friend get off. There are 3 more stops left. You can get off at the IMU, Psychology Building, or Library.\n[[IMU->IMU]]\n[[PSYCHOLOGY BUILDING->Psychology Building]]\n[[LIBRARY->Wells Library]]",
      "links": [
        {
          "linkText": "IMU",
          "passageName": "IMU",
          "original": "[[IMU->IMU]]"
        },
        {
          "linkText": "PSYCHOLOGY BUILDING",
          "passageName": "Psychology Building",
          "original": "[[PSYCHOLOGY BUILDING->Psychology Building]]"
        },
        {
          "linkText": "LIBRARY",
          "passageName": "Wells Library",
          "original": "[[LIBRARY->Wells Library]]"
        }
      ],
      "hooks": [],
      "cleanText": "You stay on the bus and let your friend get off. There are 3 more stops left. You can get off at the IMU, Psychology Building, or Library."
    },
    {
      "name": "X Route",
      "tags": "",
      "id": "6",
      "text": "The X bus is running late. You get on it 10 minutes after you would the W bus. You can get off at the Psychology Building, Wells Library or the Kelley School.\n[[PSYCHOLOGY BUILDING-> Psych Building]]\n[[WELLS LIBRARY->Library]]\n[[KELLEY SCHOOL->Hodge Hall]]",
      "links": [
        {
          "linkText": "PSYCHOLOGY BUILDING",
          "passageName": "Psych Building",
          "original": "[[PSYCHOLOGY BUILDING-> Psych Building]]"
        },
        {
          "linkText": "WELLS LIBRARY",
          "passageName": "Library",
          "original": "[[WELLS LIBRARY->Library]]"
        },
        {
          "linkText": "KELLEY SCHOOL",
          "passageName": "Hodge Hall",
          "original": "[[KELLEY SCHOOL->Hodge Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The X bus is running late. You get on it 10 minutes after you would the W bus. You can get off at the Psychology Building, Wells Library or the Kelley School."
    },
    {
      "name": "W Route",
      "tags": "",
      "id": "7",
	  "score":3,
      "text": "The W bus pickes you up quickly and you're not running late. You can either go to the IMU or Art Building.\n[[IMU->IMU]]\n[[ART BUILDING-> Eskenazi School]]",
      "links": [
        {
          "linkText": "IMU",
          "passageName": "IMU",
          "original": "[[IMU->IMU]]"
        },
        {
          "linkText": "ART BUILDING",
          "passageName": "Eskenazi School",
          "original": "[[ART BUILDING-> Eskenazi School]]"
        }
      ],
      "hooks": [],
      "cleanText": "The W bus pickes you up quickly and you're not running late. You can either go to the IMU or Art Building."
    },
    {
      "name": "IMU",
      "tags": "",
      "id": "8",
	  "score":5,
      "text": "You decide to order Starbucks when you get to the IMU. The Starbucks lobby isn't busy so you set your stuff down and study there. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to order Starbucks when you get to the IMU. The Starbucks lobby isn't busy so you set your stuff down and study there. You can type YES to play again or QUIT to exit."
    },
    {
      "name": "Psychology Building",
      "tags": "",
      "id": "9",
	  "score":5,
      "text": "You visit the colorful brain outside the building and take a couple of pictures with it. You decide to go inside and study there. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You visit the colorful brain outside the building and take a couple of pictures with it. You decide to go inside and study there. You can type YES to play again or QUIT to exit."
    },
    {
      "name": "Wells Library",
      "tags": "",
      "id": "10",
	  	"score":10,
      "text": "You get to the library and there are plenty of spaces avaliable for you to study. You decide to study there. Because it's so quiet there, you get a lot of work done. Good for you. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get to the library and there are plenty of spaces avaliable for you to study. You decide to study there. Because it's so quiet there, you get a lot of work done. Good for you. You can type YES to play again or QUIT to exit."
    },
    {
      "name": " Psych Building",
      "tags": "",
      "id": "11",
	  "score":1,
      "text": "You get to the psych building and barely have time to look at the colorful brain outside. Luckily there's still spots avaliable in the commons for you to sit. You decide to study there. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get to the psych building and barely have time to look at the colorful brain outside. Luckily there's still spots avaliable in the commons for you to sit. You decide to study there. You can type YES to play again or QUIT to exit."
    },
    {
      "name": "Library",
      "tags": "",
      "id": "12",
      "text": "You get to the library and try to find a place to study. Because you were running late, all the tables are full. You have to sit on a table outside and decide to study there. Your papers blow away because of the wind. Bummer. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get to the library and try to find a place to study. Because you were running late, all the tables are full. You have to sit on a table outside and decide to study there. Your papers blow away because of the wind. Bummer. You can type YES to play again or QUIT to exit."
    },
    {
      "name": "Hodge Hall",
      "tags": "",
      "id": "13",
      "text": "You get to Hodge and feel hungry. You can't order from the cafe because it's so busy. You barely find a spot to set your stuff down. You decide to study there, but don't get much work done. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get to Hodge and feel hungry. You can't order from the cafe because it's so busy. You barely find a spot to set your stuff down. You decide to study there, but don't get much work done. You can type YES to play again or QUIT to exit."
    },
    {
      "name": " Eskenazi School",
      "tags": "",
      "id": "14",
	  "score":2,
      "text": "You get to the Eskenazi School and visit the student exhibitions in the Grunwald Gallery of Art. You find an empty nook outside the hall and decide to study there. You can type YES to play again or QUIT to exit.\n[[YES->Apartment]]",
      "links": [
        {
          "linkText": "YES",
          "passageName": "Apartment",
          "original": "[[YES->Apartment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get to the Eskenazi School and visit the student exhibitions in the Grunwald Gallery of Art. You find an empty nook outside the hall and decide to study there. You can type YES to play again or QUIT to exit."
    }
  ]
}
  

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
	print("You are at the " + current_location["name"])
	print(current_location["cleanText"])

def get_input():
	response = input("What do you want to do? ")
	response = response.upper()
	response = response.strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label

	for link in current_location["links"]:
		if link["linkText"] == response:
			return link["passageName"]
			
	print("I didn't understand that. Please try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Apartment"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1	
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")
