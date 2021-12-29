from instabot import Bot
from time import sleep


print('███████╗██████╗  █████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     ')
print('██╔════╝██╔══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ')
print('███████╗██████╔╝███████║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ')
print('╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     ')
print('███████║██║     ██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗')
print('╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝')
print('                                                                          ')
print('██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗')
print('██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║')
print('██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║')
print('██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║')
print('██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║')
print('╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝')
print('STANDARD VERSION 1.0 BY CHICOSDU2')
print(" ")


attaqueUSER = input("Attaquant - USERNAME : ")
attaquePASSWORD = input("Attaquant - PASSWORD : ")
print(" ")
nombre = input("Nombres de messages à envoyer ?")
print("")
QuelMessage = input("Que souhaitez-vous envoyer à la victime ?")
print("")
Victimeinsta = input("Username de la victime ?")
print(" ")

print(f"Attaquant : {attaqueUSER} / {attaquePASSWORD} |")
print(f"Victime : {Victimeinsta} | Nombres de messages : {nombre} | Message : {QuelMessage} ")



bot = Bot()
bot.login(username=f"{attaqueUSER}", password=f"{attaquePASSWORD}", proxy="")
sleep(4)


print(" 20%|██        | 2/10")
sleep(2)
print(" 40%|████      | 4/10")
sleep(2)
print(" 60%|██████    | 6/10")
sleep(2)
print(" 80%|████████  | 8/10")
sleep(2)
print("100%|██████████| 10/10")


stop = 1

while True:
    if stop == 1:
        for i in range(int(nombre)+1):
            if i == int(nombre):
                stop = 0
                print("Successful, tout les messages ont bien été envoyés ! ")
                break
            else:
                bot = Bot()
                bot.login(username=f"{attaqueUSER}", password=f"{attaquePASSWORD}", proxy="")
                messageuser = Victimeinsta
                bot.send_message(f"{QuelMessage}",messageuser)
                bot.logout