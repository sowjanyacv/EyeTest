from PIL import Image, ImageFont, ImageDraw  

#This function is used for displaying Snellen Chart
def Snellen():
       image = Image.open(r'C:\Users\User\Desktop\Priy@\Python\Snellen.png')  
       image.show() 
       
#This function is used for displaying Tumbling E Chart
def Tumbling():
    image = Image.open(r'C:\Users\User\Desktop\Priy@\Python\Tumbling.jpg')  
    image.show() 

#This is the function which tells if you have myopia or no
def Calculateresult(line,age):
    if age<=4:
        l={
            '0': "You have Myopia\n",
            '1': "You have Myopia\n",
            '2': "You have Myopia\n",
            '3': "You have Myopia\n",
            '4': "You have Myopia\n",
            '5': "You do not have Myopia\n",
            '6': "You do not have Myopia\n",
            '7': "You do not have Myopia\n",
            '8': "You do not have Myopia\n"
          }
        print(l.get(line))
    
    if age==5:
        l1={
            '0': "You have Myopia\n",
            '1': "You have Myopia\n",
            '2': "You have Myopia\n",
            '3': "You have Myopia\n",
            '4': "You have Myopia\n",
            '5': "You have Myopia\n",
            '6': "You do not have Myopia\n",
            '7': "You do not have Myopia\n",
            '8': "You do not have Myopia\n"
          }
        print(l1.get(line))
        
        
    if age>5:
        l2={
            '0': "You have Myopia\n",
            '1': "You have Myopia\n",
            '2': "You have Myopia\n",
            '3': "You have Myopia\n",
            '4': "You have Myopia\n",
            '5': "You have Myopia\n",
            '6': "You have Myopia\n",
            '7': "You have Myopia\n",
            '8': "You do not have Myopia\n"
          }
        print(l2.get(line))
        
    if age<5:
        a1={
            '0': "You are legally blind\n",
            '1': "You need to go to the eye doctor immediately\n",
            '2': "You need to go to the eye doctor immediately\n",
            '3': "Eat foods rich in vitamin A, E and C\n",
            '4': "Eat foods rich in vitamin A, E and C\n",
            '5': "Good Work. Keep it up Mate\n",
            '6': "Good Work. Keep it up Mate\n",
            '7': "Good Work. Keep it up Mate\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a1.get(line))
        
        
    if age==5:
        a2={
            '0': "You are legally blind\n",
            '1': "You need to go to the eye doctor immediately\n",
            '2': "You need to go to the eye doctor immediately\n",
            '3': "Eat foods rich in vitamin A, E and C\n",
            '4': "Eat foods rich in vitamin A, E and C\n",
            '5': "Eat foods rich in vitamin A, E and C\n",
            '6': "Good Work. Keep it up Mate\n",
            '7': "Good Work. Keep it up Mate\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a2.get(line))
        
        
    if age in range(6,31):
        a3={
            '0': "You are legally blind\n",
            '1': "You need to go to opthamologist immediately\n",
            '2': "You need to go to opthamologist immediately\n",
            '3': "You need to go to opthamologist immediately\n",
            '4': "You need to go to opthamologist immediately\n",
            '5': "You need to go to opthamologist immediately\n",
            '6': "Eat foods rich in vitamin A, E and C\n",
            '7': "Eat foods rich in vitamin A, E and C\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a3.get(line))
        
    if age in range(31,51):
        a4={
            '0': "You are legally blind\n",
            '1': "You need to go to opthamologist immediately\n",
            '2': "You need to go to opthamologist immediately\n",
            '3': "You need to go to opthamologist immediately\n",
            '4': "You need to go to opthamologist immediately\n",
            '5': "Eat foods rich in vitamin A, E and C\n",
            '6': "Eat foods rich in vitamin A, E and C\n",
            '7': "Eat foods rich in vitamin A, E and C\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a4.get(line))
        
    if age in range(51,71):
        a5={
            '0': "You are legally blind\n",
            '1': "You need to go to opthamologist immediately\n",
            '2': "You need to go to opthamologist immediately\n",
            '3': "You need to go to opthamologist immediately\n",
            '4': "Eat foods rich in vitamin A, E and C\n",
            '5': "Eat foods rich in vitamin A, E and C\n",
            '6': "Eat foods rich in vitamin A, E and C\n",
            '7': "Eat foods rich in vitamin A, E and C\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a5.get(line))
 
    if age>71:
        a6={
            '0': "You are legally blind\n",
            '1': "You need to go to opthamologist immediately\n",
            '2': "Eat foods rich in vitamin A, E and C\n",
            '3': "Eat foods rich in vitamin A, E and C\n",
            '4': "Eat foods rich in vitamin A, E and C\n",
            '5': "Eat foods rich in vitamin A, E and C\n",
            '6': "Eat foods rich in vitamin A, E and C\n",
            '7': "Eat foods rich in vitamin A, E and C\n",
            '8': "Good Work. Keep it up Mate\n"
          }
        print(a6.get(line))
        
        
#main function
name=input("Enter Patient's Name: ")
age=int(input("Enter Patient's Age: "))

print("\nWhich chart do you want to Proceed with?\n")
print("1.Snellen Chart","2.Tumbling E Chart",sep="\n")
choice=input()

if choice=='1':
    Snellen()
elif choice=='2':
    Tumbling()
else:
    print("\nWrong Option")
    
line=input("Enter last line no. you can read: ")

print("\nName: ",name,end="\n")
print("Age : ",age,end="\n")

#This part tells your visual acuity
p= {
     '0': "You are considered legally blind\n",
     '1': "Visual Acuity: 20/200\n",
     '2': "Visual Acuity: 20/100\n",
     '3': "Visual Acuity: 20/70\n",
     '4': "Visual Acuity: 20/50\n",
     '5': "Visual Acuity: 20/40\n",
     '6': "Visual Acuity: 20/30\n",
     '7': "Visual Acuity: 20/25\n",
     '8': "Visual Acuity: 20/20\n"
}

print(p.get(line))

Calculateresult(line,age)
