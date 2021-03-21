import re
def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id = re.sub('[^a-z0-9-_.]','', new_id)
    
    #3단계
    new_id = re.sub('[.]+', '.', new_id)
           
    #4단계
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            #     if len(new_id)>0:
#         new_id = new_id.strip(.)
            
    

    

    #5단계
    if new_id == "":
        new_id = "a"
    #6단계
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    #7단계
    if len(new_id) <= 2:
        while len(new_id)<3:
            new_id+=new_id[-1]
        

    answer = new_id
    return answer


# import re
# def solution(new_id):
#     new_id = new_id.lower()

# #2
#     new_id = re.sub('[^a-z0-9-_.]', '', new_id)

#     #3
#     new_id = re.sub('[.]+', '.', new_id)

# # 5
#     if len(new_id) > 0:
#         new_id = new_id.strip(.)


# # 6
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         if new_id[-1] == '.':
#             new_id = new_id[:-1]
    
#     answer = new_id
#     return answer

#     #7단계
#     if len(new_id) <=2:
#         while len(new_id)<3:
#             new_id+=new_id[-1]


