from Cricket_navam import *

from datetime import datetime


key = 'Your_Personal_Bot_API_Key'

url_comm = 'https://www.cricbuzz.com/live-cricket-scores/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'
url = 'https://www.cricbuzz.com/live-cricket-scorecard/33810/eng-vs-nz-2nd-test-new-zealand-tour-of-england-2021'

cric = Cricket(url_comm,url)
cric.get_playing_11()

cric.Update()
import telebot
bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def start(message):
	mess = "Hey, I'm Goti, your cricket companion. \n"
	mess += "Bhavesh and Navam have asked me to give users information about current live matches. \n"
	mess += "If you want know the current score, you can ask me by sending '/score' . \n"
	mess += "Looking forward to helping you. *Smile* :) "
	bot.reply_to(message, mess)


@bot.message_handler(commands=['score'])
def score(message):
	cric.Update()
	sc = 'Score : ' + cric.get_curr_team_score() + '\n\n'
	bats = cric.get_bats_for_bot()
	bat_mess = 'Batsmen : \n'
	bat_mess += bats[0][0] + ' is playing at ' + bats[0][1] + ' runs after ' + bats[0][1] + ' balls \n'
	bat_mess += bats[1][0] + ' is playing at ' + bats[1][1] + ' runs after ' + bats[1][1] + ' balls \n\n'
	# print(sc)
	# print(bats)
	bowl = cric.get_bowl_for_bot()
	bowl_mess = 'Bowler : \n'
	bowl_mess += bowl['name'] + ' has taken ' + bowl['wickets'] + ' wickets in ' + bowl['over'] 
	bowl_mess += ' overs and has given ' + bowl['runs'] + ' runs.' 

	mess = sc + bat_mess + bowl_mess
	bot.reply_to(message, mess)
	# bot.reply_to(message, '\n'.join(bats))
	# bot.reply_to(message, bowl)

@bot.message_handler(commands=['full'])
def full_score(message):
	cric.Update()
	mess = cric.get_full_score()
	bot.reply_to(message, mess)

bot.polling()

