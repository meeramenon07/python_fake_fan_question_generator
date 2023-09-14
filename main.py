print("Fake Fan Finder")
anime = input("What is your favourite anime?: ")
if anime == "Attack on Titan":
  print("Oh really!? Name the main character? ")
  mainCharacter = input("main character ")
  if mainCharacter == "Titan":
    print("You just got that by pure fluke! Ok, then, tell me a bit more details about Titan? ")
    moreDetails = input("more details about Titan ")
    if moreDetails == "Man-eating humanoid":
      print("Ok,then, they existed for how many years on earth? ")
      years = input("how many years on earth ")
      if years == "more than 2000 years":
        print("You are not a fake fan!")
      else:
        print("See here !A fake Titan fan!")
  else:
    print("Seems like you don't know a thing!")
  
        
elif anime == "Dragon Ball":
 print("Oh, scary one that!")
else:
  print("Yup, that's pretty awesome and fun...")

