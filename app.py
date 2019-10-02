from jamdict import Jamdict
import nagisa
import romkan

jmd = Jamdict()

lines = []
for line in open('l1.txt', 'r').readlines():
  words = nagisa.tagging(line.strip()).words
  words = [w for w in words if w != '\u3000']
  lines.append(words)

print('***********************************************') 
for i in range(0, 3):
  print('\n') 
print('***********************************************') 


for line in lines:
  for word in line:
    entries = jmd.lookup(word).entries
    if entries:
      entry = jmd.lookup(word).entries[0] 
      kana = entry.kana_forms[0].text if entry.kana_forms else ''
      romaji = romkan.to_roma(kana)
      sense = entry.senses[0].text(compact=True) if entry.senses else '?'
      print(word + '\t' + romaji + '\t' + sense)
    else:
      print(word + '\t-\t-')