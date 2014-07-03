from random import randint
from tkinter import *
from sys import platform
##Data Structure
###book data
Corp_list = {
	1:'Ai-Jin',
	2:'Comoros',
	3:'Eurasian Incorporated',
	4:'shi yukiro',
	5:'western federation',
	6:'other'}
Corp_languages = {
	'Ai-Jin':['Mandarin', 'Cantonese','Thai'],
	'Comoros':['Swahili', 'Hindi'],
	'Eurasian Incorporated':['English', 'Russian', 'German'],
	'shi yukiro':['Japanese','Mandarin'],
	'western federation':['English', 'Spanish', 'Military Sign']}
start_mon_list = {
	'Ai-Jin':7000,
	'Comoros':6000,
	'Eurasian Incorporated':10000,
	'shi yukiro':9000,
	'western federation':8000}
BookList = [Corp_list,Corp_languages,start_mon_list]
	###profile'
id = {
	'name':'',
	'corp':'',
	'rank':0,
	'prof':0,
	'divi':0,
	'leve':0}
hp = {
	'hp_total':0,
	'current':0,
	'mashing':0}
armour = {
	'armour':[],
	'move_speed':0}
shield = {
	'total':0,
	'current':0,
	'type':0}
advancement = {
	'cur_xp':0,
	'total_xp':0,
	'rank':0}
languige = []
hardware = {
	'ai':0,
	'credit':0,
	'slip':0,
	'hardware':[],
	'cybernetics':[]}
con_points = 0
agent_skills = {
	'training':[],
	'contacts':[],
	'licenses':[]}
stats = {
	'strength':5,
	'endurance':5,
	'agility':5,
	'reflexes':5,
	'perception':5,
	'intelligence':5,
	'presence':5}
psy_stats = {
	'assault':0,
	'biokinesis':0,
	'jump':0,
	'prescience':0,
	'psi_blade':0,
	'shield':0,
	'telekinesis':0,
	'total':0}
skills = {
	'art_and_culture':0,
	'assess_tech':0,
	'athletics':0,
	'athletics_tech':0,
	'attitude':0,
	'Business':0,
	'close_combat':0,
	'computers':0,
	'corp':0,
	'crime':0,
	'cyber':0,
	'drive':0,
	'hweapon':0,
	'lweapon':0,
	'looks':0,
	'lying':0,
	'mech':0,
	'medi':0,
	'obs':0,
	'pilot':0,
	'psych':0,
	'science':0,
	'stealth':0,
	'street':0,
	'sweapons':0,
	'tweapons':0,}
equiped_weap = {
	'name':'',
	'type':'',
	'r/c':'',
	'stat':'',
	'skill':'',
	'dammige':[1,10],
	'rate':0}
big_list = [id,hp,armour,shield,advancement,languige,hardware,con_points,agent_skills,stats,psy_stats,skills,equiped_weap]
#fuction
def diceScript(amount,type):
	i = 0
	total = 0
	while i != amount:
		total = total + randint(1,int(type))
	return total
#User interface START
def charCreate_ran():#create a random Chariter.
	WhileVal = 0
	count = 0
	name_text = ''
	CreateCorp = []
	for Corp in Corp_list.Values()
		CreateCorp.append(Corp)
	

def createCharUI():
	#mainCreate
	MainCreate = tk()
	MainCreate.geometry('200x200+600+400')
	if str(platform) is 'win32':
		MainCreate.mainloop()
	MainCreate.title('Create a Character')
	#elements
	buttonA = button(mainCreate,text='Random Genernation',command=charCreate_ran).place(x=100,y=50)
	buttonB = buttom(mainCreate,text='   Manual Imput   ',command=charCreate_man).place(x=150,y=50)	
def LockpickUI():
def equipUI():
def combatUI():
def gui_start():
	MainMenu = Tk()
	MainMenu.geometry('500x500+400+300')
	MainMenu.configure(background='black')
	if str(platform) is 'win32'
		MainMenu.mainloop()
	MainMenu.title('Main Menu')
	label1 = Label(MainMenu,text='Welcome to CorpHelper',font('Helvetica', 16)).pack()
	###
	buttonA = Button(MainMenu,text='Create a Character',command=createCharUI).place(x=100,y=10)
	buttonB	= Button(MainMenu,text='Lockpicking',command=LockpickUI).place(x=200,y=10)
	buttonC = Button(MainMenu,text='equipWeapon',command=equipUI).place(x=300,y=10)
	buttonD	= Button(MainMenu,text='Combat',command=combatUI).place(x=400,y=10)
#User Interface END
gui_start()