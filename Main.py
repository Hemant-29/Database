import json
import os
user_details=[]

if os.path.exists("./user_data.json"):
	with open("./user_data.json") as json_object:
		user_details=json.load(json_object)

citynames=[]
with open ("./cities.txt") as file_object:
	lines=file_object.readlines()
	for cities in lines:
		cities=cities.rstrip()
		cities=cities.lower()
		citynames.append(cities)


def input_details():
	global citynames
	while True:
		name=input("Please enter your name.\n-> ")
		if name=="":
			print("Please enter a valid name.\n")
		elif name.isalpha()==True:
			name=name.title()
			break
		else:
			print("name must contain alphabets only.\n")

	while True:
		age=input(f"What is your age {name}?\n-> ")
		if age=="":
			print("Please enter a valid age.\n")
		if age.isnumeric()==True:
			break
		else:
			print("please enter numbers only.\n")

	while True:
		city=input(f"{name}. You come from which city?\n-> ")
		if city=="":
			print("Please enter a valid name.\n")
		elif city not in citynames:
			print("Your city name is not recognized by us.")
			match=find_match(city,citynames)
			if match:
				city=match.title()
				break
			else:
				pass
		elif city.isalpha()==True:
			city=city.title()
			break
		else:
			print("city name must contain alphabets only.\n")
	print()
	return [name,age,city]


def main_menu():
	print("Press ENTER to add another user.\nType- S to show user's details.\nType- Q to quit.\n")
	inp=input("->")
	print()
	if inp.lower()=="q":
		None
	elif inp.lower()=="s":
		if user_details==[]:
			print("No details found in the database")
		else:
			curr_num=0
			for i in user_details:
				curr_num+=1
				print(f"{curr_num})",i[0],i[1],i[2])
		print()
		main_menu()
	else:
		val=input_details()
		user_details.append(val)
		dump_details()
		main_menu()
		

def find_match(name,name_list):
	match_ratios=[]
	for city in name_list:
		match_words=0
		for j in name.lower():
			if j in city.lower():
				match_words+=1
		match_ratio = match_words/len(city)
		match_ratios.append(match_ratio)
	match_index=match_ratios.index(max(match_ratios))
	match_city = name_list[match_index]
	print("Do you mean",match_city,"?")
	a=input("->")
	if a.lower()=="y" or a.lower() == "yes":
		return match_city
	else:
		return None

def dump_details():
	with open("./user_data.json",'w') as json_object:
		json.dump(user_details,json_object)

main_menu()
dump_details()
