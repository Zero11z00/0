print("\033[1;31m \$$$$$$$   \$$$$$$    \$$$$    \033[1;32m script by \033[1;36mJoker.a.1.3  ")  

print('\n\033[0m')              

client=amino.Client()

ss=0

sz=25

nuum=0

tst=False

while tst==False:

    try:

        email=input("\033[1;93m# your email : \033[0m")

        password=getpass.getpass("\033[1;93m# your password : \033[0m")

        client.login(email=email,password=password)

        tst=True

    except:

        tst=False

        print("\033[1;93m# verify email or password\033[0m")

        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")

        if exx=='n' or exx=='N' or exx=='no':

            os._exit(1)

            

tst=False

while tst==False:

    try:

        infoos=input("\033[1;93m#give me url of group : \033[0m")

        infoo=client.get_from_code(infoos)

        tst=True

        if infoo.objectType!=12:

            print ("\033[1;93m#not chat url !\033[0m")

            tst=False

    except:

        tst=False

        print("\033[1;93m# verify your url \033[0m")

    if tst==False:

        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")

        if exx=='n' or exx=='N' or exx=='no':

            os._exit(1)
            
            chatId=infoo.objectId

comId=infoo.path[1:infoo.path.index("/")]

sub_client=amino.SubClient.kick(comId=comId,profile=client.profile)

swich=0

tst=False

while tst==False:

   tst:

    tst = صحيح
