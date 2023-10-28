
PLACEHOLDER = "[name]"

with open(r"day24\project\inputs\names\names.txt") as namesFiles:
  names = namesFiles.readlines()
  # print(names)
  
with open(r"day24\project\inputs\letters\starterLetter.docx") as letter:
  letterContent = letter.read()
  for name in names:
    strippedName = name.strip()
    newLetter = letterContent.replace(PLACEHOLDER,strippedName)
    # print(newLetter)
    with open(fr"day24\project\output\readyToSend\letterFor{strippedName}.docx",mode="w") as finalLetter:
      finalLetter.write(newLetter)
