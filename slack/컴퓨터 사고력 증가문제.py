box = [7,4,2,0,0,6,0,7,0]
total_box=[]
for j in range(len(box)):
  box_in_room=[]
  for i in range(len(box)):
    if box[i] > 0:
      b =1 
      box_in_room.append(b)
    if box[i] <= 0:
      b = 0
      box_in_room.append(b)
    box[i]-=1
  total_box.append(box_in_room)
total_box=list(reversed(total_box))
for j in range(len(total_box)):
  print(total_box[j])
c=[]
for i in range(len(total_box)):
  # print(total_box[i])
  c_0 = 0
  for j in range(len(total_box[i])):
    if total_box[i][j] == 0:
      c_0 += 1
  if c_0 <= 8:
    # print(c_0)
    c.append(c_0)
  if c_0 == 9:
    continue
# print(c)
max_v = 0
for i in c:
    if max_v < i:
        max_v = i
print(max_v)