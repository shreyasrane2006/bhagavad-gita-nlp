#with open("sample_verse.txt","r") as file:
#    lines = file.readlines()

#for line in lines:
#    print(line.strip())

#cleaned_lines = [line.strip().lower().replace(".", "") for line in lines]
#print(cleaned_lines)

#word_count = sum(len(line.split()) for line in cleaned_lines)
#char_count = sum(len(line) for line in cleaned_lines)

#print("Words:", word_count)
#print("Characters:", char_count)

#import shutil

with open("gita_intro.txt","r") as file:
    lines = file.readlines()

krishna_count = 0
arjuna_count  = 0
for line in lines:
    line = line.lower().replace(".", "")
    arjuna_count  = arjuna_count + line.count('arjuna')
    krishna_count = krishna_count + line.count('krishna')

print(krishna_count)
print(arjuna_count)


#shutil.copy("gita_intro.txt", "gita_cleaned.txt")
cleaned_lines = [line.strip().lower().replace(".", "") for line in lines]
for line in cleaned_lines:
    with open("gita_cleaned.txt", "w") as file:
        file.write(line)
    file.close()
