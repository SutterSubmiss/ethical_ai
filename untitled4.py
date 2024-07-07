# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:12:58 2024

@author: User
"""

from random import randint 

import mysql.connector as mys

mydb = mys.connect(
  host="localhost",
  user="root",
  password="",
  database="ai_base"
)
cursor1 = mydb.cursor(buffered=True)
input1 = input()
stuff = []
output1 = ""
class Something():
    weight = [[0,0],0,1]
    smell = ""
    gender = 0
    fitness = 0
    id1 = ""
    
iaa = input1.split(' ')
smell_words = ["smelly","stinky",'good']
probability_words = [["probably"]]
gender_words = [["boy","lad","man"],["girl","woman"],["","enby"]]
pronouns = ["He","She","They"]
weight_words = [["skinny","slim"],["chubby","overweight"],["fat","obese"]]
question_words = ["How","What","Why"]
question_second_words = ["much","did","is"]
speech_parts=[["noun",[]],["verb",[]],["adjective",[]],["adverb",[]],["determiner",[]]]
for part in speech_parts:
 cursor1.execute("Select * from "+part[0]+"s_meaning;")
 part[1] =cursor1.fetchall()
mydb.commit()
create = False
end = False
output_create = False
def delete_interpunction(i):
    if((chr(i[-1]) >=44 and chr(i[-1]) <=46) or chr(i[-1]) == 59 ):
      i.pop()
      if(i[-1] =="."):
          end = True
      return i
def add_new_word(i,iaa):
  
    if(iaa[iaa.index(i)+1] =="an" or iaa[iaa.index(i)+1] =="a"):
     identified = False
     
     for part in speech_parts:
       if(iaa[iaa.index(i)+2] == part[0]):
          cursor1.execute("Insert Into "+part[0]+"s_meaning("+part[0]+") values('"+iaa[iaa.index(i)-1]+"');")
          print("understood")
          identified = True
     #if(identified == False):
           #cursor1.execute("Insert Into "+part[0]+"s_meaning(category) values("+iaa[iaa.index(i)+2]+"');")
     mydb.commit() 
     
def create_meaning(i,iaa,i_placement):  
    this_part = ""
    for part in speech_parts:
      cursor1.execute("Update "+part+"s set meaning='"+iaa[i_placement:]+"' where "+part+"="+iaa[iaa.index(i)+1]+";")
      this_part = part
    for j in iaa[i_placement:]:
      if(speech_parts[0][1].contain(j)):
          ("Update "+part+"s set category='"+j+"' where "+part+"="+iaa[iaa.index(i)+1]+";")
      if(j == "low" or j=="bad"):
          cursor1.execute("Update "+this_part+"s set scale_placement=0 where "+this_part+"="+iaa[iaa.index(i)+1]+";")
      elif(j == "medium" or j=="neutral"):
          cursor1.execute("Update "+this_part+"s set scale_placement=1 where "+this_part+"="+iaa[iaa.index(i)+1]+";")
      elif(j == "high" or j=="good"):
          cursor1.execute("Update "+this_part+"s set scale_placement=2 where "+this_part+"="+iaa[iaa.index(i)+1]+";")
      mydb.commit() 
def get_data(stuff,i):
    cursor1.execute("Select * from adjective_meanings;")
    adjectives = cursor1.fetchall()
    for adject in adjectives:
        if(adject[0] == i):
              if(adject[2] == "weight"):
                stuff1.weight[0] = [(adject[4]+1)*40,(adject[4]+1)*70]
              if(adject[2] == "gender"):
                stuff1.gender[0] = adject[4]
              if(adject[2] == "smell"):
                stuff1.smell = adject[0]
              if(end == True):
                cursor1.execute("Insert Into stuff(weight,gender,smell) values("+str(stuff1.weight)+","+str(stuff1.gender)+",'"+str(stuff1.smell)+"');")
                mydb.commit() 
                cursor1.execute("Select Max(id)  from stuff");
                stuff1.id1 =  str(cursor1.fetchall()[0][0])
#cursor1.execute("Create table stuff(id int auto_increment primary key, weight int, smell varchar(100),gender int, fitness int);")
i_placement = 0;
for i in iaa:
  if(i == "is"):
        add_new_word(i,iaa)
  if(i == "means"):
         create_meaning(i,iaa,i_placement)
  if(create == True):
    delete_interpunction(i)  
    stuff1 = Something
    stuff.append(stuff1)
    
    get_data(stuff1,i)
    #for j in weight_words:
        #if(j.__contains__(i)):
            
           #stuff1.weight = (weight_words.index(j)+1)*randint(40,70)
    #for k in gender_words:
        #if(k.__contains__(i)):
           #stuff1.gender = gender_words.index(k)
            
           #create = False
    
    
    #if(smell_words.__contains__(i)):
        #stuff1.smell = i

  
    
  if(i == "a"):
        create = True
  i_placement +=1
  if(question_words.__contains__(i)):
      cursor1.execute("Select gender from stuff where id="+stuff1.id1+";")
      output1 += pronouns[int(str(cursor1.fetchall()[0][0]))]+" "
      output_create = True
  else:
      output1 ="Thank you, I understood"
  if(output_create == True):
      if(speech_parts[0][1].__contains__(i)):
       output1+=i+"s "
       if(i == "weigh"):
           cursor1.execute("Select gender from stuff where id="+stuff1.id1+";")
           output1 += str(cursor1.execute(cursor1.fetchall()[0][0]))+" kg"
       elif(i == "smell"):
          cursor1.execute("Select smell from stuff where id="+stuff1.id1+";")
          output1+=str(cursor1.fetchall()[0][0])
output1 +="."
print(output1)

        
