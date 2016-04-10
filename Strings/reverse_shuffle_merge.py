string = raw_input()
string = string[::-1]
freq = [0]*26
positions = []
for i in range(26):
    positions.append([])
next_to_use = [0]*26
freq_seen = [0]*26
written = [0]*26

for i in range(len(string)):
    freq[ord(string[i])-ord('a')] = freq[ord(string[i])-ord('a')] + 1
  #  print "Val", ord(string[i])-ord('a')
    val = ord(string[i])-ord('a')
    positions[val].append(i)

#print freq
#print positions
for i in range(len(freq)):
    freq[i] = freq[i]/2
    next_to_use[i] = 0

needs = [0]*len(string)

for i in range(1, len(string)+1):
    j = len(string) - i
    hash_val = ord(string[j])-ord('a')
    needs[j] = freq[hash_val] - freq_seen[hash_val]
    freq_seen[hash_val] = min(freq_seen[hash_val]+1, freq[hash_val])
    

res = []
next_bottleneck = 0
last_pos = 0

while(len(res) != len(string)/2):
  #  print "Result", res
    while not written[ord(string[next_bottleneck])-ord('a')] < needs[next_bottleneck]:
        next_bottleneck = next_bottleneck + 1
 #   print "Bottleneck", next_bottleneck
    next_char = 0
 #  print "next_char", next_char
 #   print "Position", positions[next_char][next_to_use[next_char]]
    while written[next_char] == freq[next_char] or positions[next_char][next_to_use[next_char]] > next_bottleneck :
        next_char = next_char + 1
    str_pos = positions[next_char][next_to_use[next_char]]
  #  print "next_char", next_char
#    print "Str_pos", str_pos
    if str_pos:
        while last_pos != str_pos:
            
            next_to_use[ord(string[last_pos])-ord('a')] = next_to_use[ord(string[last_pos])-ord('a')] + 1
            last_pos = last_pos + 1
        
    while True:
        
        res.append(chr(next_char+ord('a')))
        #print res
        written[next_char] = written[next_char] + 1
        next_to_use[next_char] = next_to_use[next_char] + 1
        if not written[next_char] < needs[str_pos]:
            break
    last_pos = str_pos + 1

print ''.join(res)
