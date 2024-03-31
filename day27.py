print("""
|----------------------------------------------------------------------------------|
|::::::::::-->>>         ____  __. __________  _________            <<<--::::::::::|  
|::::::::::-->>>         |    |/ _| \______   \ \_   ___ \          <<<--::::::::::| 
|::::::::::-->>>         |      <    |    |  _/ /    \  \/          <<<--::::::::::|
|::::::::::-->>>         |    |  \   |    |   \ \     \____         <<<--::::::::::|
|::::::::::-->>>         |____|__ \  |______  /  \______  /         <<<--::::::::::|
|::::::::::-->>>                 \/         \/          \/          <<<--::::::::::|
|===============================KAUN BANEGA KARODEPATI=============================|
|----------------------------------------------------------------------------------|""")
quizes=["1. Which one of the following river flows between Vindhyan and Satpura ranges?","2. The Central Rice Research Station is situated in?","3. Who among the following wrote Sanskrit grammar?","4. Which among the following headstreams meets the Ganges in last?","5. The metal whose salts are sensitive to light is?","6. Patanjali is well known for the compilation of –","7. River Luni originates near Pushkar and drains into which one of the following?","8. Which one of the following rivers originates in Brahmagiri range of Western Ghats?","9. The country that has the highest in Barley Production?","10. Tsunamis are not caused by","11. Chambal river is a part of –","12. D.D.T. was invented by?","13. Volcanic eruption do not occur in the","14. Indus river originates in –","15. The hottest planet in the solar system?","16. With which of the following rivers does Chambal river merge?"]
optionslist=["(a) Narmada (b) Mahanadi (c) Son (d) Netravati","(a) Chennai (b) Cuttack (c) Bangalore (d) Quilon","(a) Kalidasa (b) Charak (c) Panini (d) Aryabhatt","(a) Alaknanda (b) Pindar (c) Mandakini (d) Bhagirath","(a) Zinc (b) Silver(c) Copper (d) Aluminum","(a) Yoga Sutra (b) Panchatantra (c) Brahma Sutra (d) Ayurveda","(a) Rann of Kachchh (b) Arabian Sea (c) Gulf of Cambay (d) Lake Sambhar","(a) Pennar (b) Cauvery (c) Krishna (d) Tapti","(a) China (b) India (c) Russia (d) France","(a) Hurricanes (b) Earthquakes (c) Undersea landslides (d) Volcanic eruptions","(a) Sabarmati basin (b) Ganga basin (c) Narmada basin (d) Godavari basin","(a) Mosley (b) Rudolf (c) Karl Benz (d) Dalton","(a) Baltic sea (b) Black sea (c) Caribbean sea (d) Caspian sea","(a) Kinnaur (b) Ladakh (c) Nepal (d) Tibet","(a) Mercury (b) Venus (c) Mars (d) Jupiter","(a) Banas (b) Ganga (c) Narmada (d) Yamuna"]
ans=["a","b","c","d","b","a","a","b","c","a","c","a","d","b","d"]
prize=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
print("::kya aap tayar hai Kaun Banega Crorepati ke iss safar mai ::\n")
a=input()
if a=="bilkul suru kijiye" or a=="start" or a=="ho jaye suru":
    quiznum=16
    finalSum=0
    sum=0
    lifelines=[1,1]
    while(quiznum>0):
        print("Q"+quizes[16-quiznum]+"\n")
        print(optionslist[16-quiznum]+"\n")
        print("ENTER YOUR OPTION")
        sel=input()
        if lifelines[0]==1 or lifelines[1]==1 :
            print("WANT TO LOCK THE OPTION ?\nANSWER IN ->YES ->NO")
            op1=input()
            if op1=="YES" or op1=="yes":
               print("PROCEED")
            else:
                print("CHOOSE THE LIFELINE\n(1)expert advice  (2)50-50 ")
                op2=int(input())
                if op2==1 and lifelines[0]==1:
                    print("suggested option is feeded")
                    sel=ans[16-quiznum]
                    lifelines[0]=0
                if op2==2 and lifelines[1]==1:
                    print("choose option now")
                    sel="d"
                    lifelines[1]=0
        print("ARE U SURE or want to quit\n")
        buzz=input()
        if buzz=="sure":
            if sel==ans[16-quiznum]:
                sum=prize[16-quiznum]
                if (17-quiznum)==5 or (17-quiznum)==10 or (17-quiznum)>5:
                    finalSum=sum
        if buzz=="quit":
            finalSum=sum              
        quiznum=quiznum-1          
    print("CONGRATULATIONS YOU WON::")
    print(finalSum)    
    