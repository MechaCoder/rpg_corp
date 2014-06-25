#Complete Redersigning
from random import randint
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
#Chariter 
#char DATA:

def fileSave():
	FileControl = open('User.txt','w')
	FileControl.write(big_list)
def diceScript(amount,type):
	i = 0
	total = 0
	while i != amount:
		total = total + randint(1,int(type))
		i += 1
	return total
def charCreate():
	whileVal = 0
	count1 = 0
	#start name
	id['name'] = input('pleses enter the name of your agent? ')
	# end name
	print('_________________________________________________________')
	# corp script
	print('pleses select your Corperation ? (list bellow)')
	for corps in Corp_list.values():
		count1 += 1
		print('> ', count1, ' - ', corps)
	while whileVal == 0:
		inputval = input('enter the number of your corperation: ')
		if int(inputval) < 7:
			whileVal = 1
			id['corp'] = Corp_list[int(inputval)]
	StatsAssign()
	char_mathbased()
def StatsAssign():
	pool = 14
	x = 0
	statsArray = ['strength','endurance','agility','reflexes','perception','intelligence','presence']
	#inputVal = input('Would you like to define your stats (y/n) ? ')
	if inputVal is 'n':
		while pool > 0:
			int_temp = randint(0, (len(stats) - 1))
			stats[statsArray[int_temp]] += 1
			pool -= 1
			#print(pool)
	else:
		print('err')
	for stat in stats.values():
		print(statsArray[x], ' - ', stat)
		x += 1
def char_mathbased():
	languige.append(Corp_languages[id['corp']])
	psy_stats['total'] = (stats['presence'] + stats['perception'] + stats['intelligence']) + 10
	armour['move_speed'] = stats['strength'] + stats['endurance'] + stats['agility']
	hardware['ai'] = 1
	armour['armour'].append('flack jacket')
	con_points = 2
	advancement['rank'] = 10
	hardware['credit'] = start_mon[id['corp']]
def CharAssignSkills():
	tempInt = 0
	max_int = 0 #skill_Points_list
	tempInt2 = 0
	max_int2 = 0 #skill_dict_list
	temp_skills = {'art_and_culture':0,'assess_tech':0,'athletics':0,'athletics_tech':0,'attitude':0,'Business':0,'close_combat':0,'computers':0,'corp':0,'crime':0,'cyber':0,'drive':0,'hweapon':0,'lweapon':0,'looks':0,'lying':0,'mech':0,'medi':0,'obs':0,'pilot':0,'psych':0,'science':0,'stealth':0,'street':0,'sweapons':0,'tweapons':0}
	skill_Points_list = [8,7,6,5,5,5,4,4,4,3,3,3,2,2,2,1,1,1,1]
	skill_dict_list = ['art_and_culture','assess_tech','athletics','athletics_tech','attitude','Business','close_combat','computers','corp','crime','cyber','drive','hweapon','lweapon','looks','lying','mech','medi','obs','pilot','psych','science','stealth','street','sweapons','tweapons']
	###
	'''print(len(skill_Points_list))
	print(len(skill_dict_list))
	print(len(temp_skills))'''
	###
	while skill_Points_list != []:
		max_int = len(skill_Points_list) - 1
		max_int2 = len(skill_dict_list) - 1
		tempInt = randint(0, max_int) #randint for list
		tempInt2 = randint(0, max_int2) # randint for dict
		#############
		if max_int == 0:
			max_int += 1
		if max_int2 == 0:
			max_int2 += 1
		temp_skills[skill_dict_list[tempInt2]] = skill_Points_list[tempInt]
		'''print(skill_dict_list[tempInt2])
		print(skill_Points_list[tempInt])'''
		skill_dict_list.pop(tempInt2)
		skill_Points_list.pop(tempInt)
	skills = temp_skills
def lockpicking():
	LockType.upper()
	check = 0
	whileVal = 1
	i = 0
	bonus = 0
	returnVal = 0
	modi = 0
	print('1 - Crude Lock')
	print('2 - Normal Lock')
	print('3 - Good Lock')
	print('4 - Advanced lock')
	print('5 - elite Lock')
	
	modi = input('enter number of the type lock that is being used : ')
	if LockType is 'M':
		for item in hardware['hardware']: 
			if item is 'lockpicks':
				check = 4
	elif LockType is 'E':
		for item in hardware['hardware']:
			if item is 'Sercurity Bypass Device':
				check = 4
	
	if modi is 1:
		int_value = stats['intelligence'] + skills['crime'] + check + 2
	if modi is 2:
		int_value = stats['intelligence'] + skills['crime'] + check
	if modi is 3:
		int_value = stats['intelligence'] + skills['crime'] + check - 4
	if modi is 4:
		int_value = stats['intelligence'] + skills['crime'] + check - 8
	if modi is 5:
		int_value = stats['intelligence'] + skills['crime'] + check - 12
	roll = diceScript(2,10)
	if roll < int_value:
		return('Unlocked')
	else:
		return('Locked')		
def equipWeapon():
	equiped_weap['name'] = input("pleses enter weapon's name  : ")
	equiped_weap['type'] = input("pleses enter weapon's type  : ")
	equiped_weap['r/c'] = input("pleses enter weapon's R/C   : ")
	if equiped_weap['r/c'] is 'r':
		equiped_weap['stat'] = 'perception'
	elif equiped_weap['r/c'] is c:
		equiped_weap['stat'] = 'agility' #equiped_weap['stat'] = input("pleses enter weapon's stat : ") #Automize if r (ranged) runs of preception if c will run off agillity.
	equiped_weap['skill'] = input("pleses enter the weapon's Class")
def CombatBase():
	init = stats['reflexs'] + diceScript(1,10)
	if equiped_weap['r/c'].lower() is 'r':
		if stat[equiped_weap['stat']] + skills[equiped_weap['skill']] < diceScript(2,10):
			roll = diceScript(equiped_weap['dammige'[0]],equiped_weap['dammige'[1]])
			return(roll)
	elif equiped_weap['r/c'].lower() is 'c':
		if stat[equiped_weap['stat']] + skills[equiped_weap['skill']] < diceScript(2,10):
			OppDefence = input("Enter the opponent's Defence : ")
			roll = diceScript(equiped_weap['dammige'[0]],equiped_weap['dammige'[1]])
def SniperShot():
	total = CombatBase()
	print('COVER')
	print('Pleses enter the number for the type of cover')
	print('1 - lamp Post  ')
	print('2 - low wall   ')
	print('3 - car        ')
	print('4 - High Wall  ')
	print('5 - Total cover')
	cover = input('enter number here > ') * 2
	if cover is 10:
		return('No Target')
	print('Target Shot')
	t_size ={
		'coin':'-12',
		'egg':'-8',
		'can':'-6',
		'ball':'-4',
		'pack':'-2',
		'man':'-0',
		'door':'+2',
		'car':'+4',
		'van':'+6',
		'lorr':'+8',
		'House':'+12',}
	print('enter the size of size target')
	for item in t_size.keys():
		print(' : ', item)
	string = input('what is the size of the target picked of the list above')
	modi = t_size(string)
	
"""def expi(argNum):
	arg = ['add_xp','improve_skills','improve_stats','Learn_Lingo']
	if argNum is '':
		for its in arg:
			print(i, ' - ', its)
			i += 1
		inVal = input('enter the number of thing you wish to do : ')
	elif argNum is 'add_xp':
		inputVal = input('enter the number of exp point you wish to add : ')
		int(inputVal)
		advancement['cur_xp'] = advancement['cur_xp'] + inputVal
		advancement['total_xp'] = advancement['total_xp'] + inputVal
	elif argNum is 'improve_skills':
		i = 0
		key = []
		for s in skills.keys():
			key.append(s)
		for k in key:
			print(i,' - ',k)
		inV = input('Enter the number of the skill you want to improve : ')
		if skills[key[inVal]] is 0:
			skills[key[inVal]] = skills[key[inVal]] + 1
			advancement['cur_xp'] = advancement['cur_xp'] - 2
		elif skills[key[inVal]] < 10 and skills[key[inVal]] > 0:
			advancement['cur_xp'] = advancement['cur_xp'] - skills[key[inVal]]
			skills[key[inVal]] = skills[key[inVal]] + 1
		elif skills[key[inVal]] >= 10:
			print('sorry you can not improve you score')
	elif argNum is 'improve_stats':
		i = 0
		list=[]
		for s in stats.keys():
			list.append(s)
			print(i,' - ',s)
		inVal = input('enter choice : ')
		stats[list[inVal]] += 1
		advancement['cur_total'] = advancement['cur_total'] - (advancement['cur_total'] * 2)
	elif argNum is 'Learn_Lingo':
		list1 = []
		list2 = []
		for e in Corp_languages.values():
			i = 0
			while i != len(e):
				list1.append(e[i])
				i += 1 
		for e in list1:
			if e != list2:
				list2.append(x)
		posLings = []
		i = 0
		for e in list2:
			if e != languige:
				posLings.append(e)
		for e in posLings:
                        print(i, e)"""
