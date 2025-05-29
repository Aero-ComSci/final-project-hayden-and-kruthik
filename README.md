[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DpCY8B3G)


Description: This program can be used by people of all ages and genders. It can be used as a basic checklist for a day at the beach or a vacation. It automates making a checklist based on the activites you want to do. 

```
    packinglist = []
    packinglist.append("Sunglasses")
    packinglist.append("Beach hat")
    packinglist.append("Sunscreen")
    packinglist.append("Flip-flops")
    packinglist.append(f"Towels for {question_1} people")

```
```while True:
  question_1 = input("How many people are going to the beach? ")
  if question_1.isdigit() and int(question_1) > 0:
      question_1 = int(question_1)
      break
  else:
      print("Please enter a valid positive number.")

```
def print_list():
