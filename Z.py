import amino

email=input("your email :")

password=input("your password :")

comId=input("your comId :")

client=amino.Client()

client.login(email=email,password=password)

sub_client=amino.SubClient(comId=comId,profile=client.profile)

chatId=input("give me chatId of group :")

userId=input("give userId of member of group for kick : ")

sub_client.kick(userId=userId,chatId=chatId,allowRejoin=True)
