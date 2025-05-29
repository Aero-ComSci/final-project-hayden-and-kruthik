while True:
  question_1 = input("How many people are going to the beach? ")
  if question_1.isdigit() and int(question_1) > 0:
      question_1 = int(question_1)
      break
  else:
      print("Please enter a valid positive number.")

while True:
  question_2 = input("Will you be swimming? (yes/no) ").strip().lower()
  if question_2 in ["yes", "no"]:
      break
  else:
      print("Please enter 'yes' or 'no'.")

while True:
  question_3 = input("Are you staying overnight? (yes/no) ").strip().lower()
  if question_3 in ["yes", "no"]:
      break
  else:
      print("Please enter 'yes' or 'no'.")

while True:
  question_4 = input("Do you need to pack food? (yes/no) ").strip().lower()
  if question_4 in ["yes", "no"]:
      break
  else:
      print("Please enter 'yes' or 'no'.")
def print_list():
    packinglist = []
    packinglist.append("Sunglasses")
    packinglist.append("Beach hat")
    packinglist.append("Sunscreen")
    packinglist.append("Flip-flops")
    packinglist.append(f"Towels for {question_1} people")
    
    if question_2 == "yes":
        packinglist.append("Swimsuit")
        packinglist.append("Swim trunks")
        packinglist.append("Beach ball")
    if question_3 == "yes":
        packinglist.append("Sleeping bag")
        packinglist.append("Pillow")
        packinglist.append("Blanket")
    if question_4 == "yes":
        packinglist.append("Soda")
        packinglist.append("Pre packed sandwiches")
        packinglist.append("Portable Stove")
    for item in packinglist:
        print(f"You need to pack: {item}")
print_list()

while True:
    activity = input("Do you enjoy water activities or prefer to stay on land (water/land)").strip().lower()
    if activity in ["water", "land"]:
          break
    else:
          print("Please enter 'water' or 'land'.")
    
    
if activity == "water":
            print("You should try surfing, paddleboarding, or swimming.")
elif activity == "land":
            print("You should try hiking, biking, or birdwatching.")
