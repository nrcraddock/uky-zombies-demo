#This is a short text-based RPG created for assignment 36 in Zed Shaw's "Learn Python the Hard Way."

import sys
from time import sleep
from random import choice, randint

#starting flags and stat values. "flags" is an RPG term from the heyday of RPG Maker or OHRRPGCE or Sprite or any of those open source engines.
#When each scenario runs it checks the value of a flag. I prefer numbers to booleans because you can get more than one option.
#But, sometimes, booleans are better.

#player stats.
health = 100
max_health = 100
mana = 10
max_mana = 10
dam_min = 12
dam_max = 26
damage = range(dam_min, dam_max)
mana_cost = 2
heal = 40
exp = 0
level = 1
inv_serum = 0

#Enemy stats
weak_health = 50
weak_damage = range(10, 21)
weak_exp = 25
strong_health = 75
strong_damage = range(15, 26)
strong_exp = 50
boss_health = 500
boss_damage = range(50, 76)
boss_exp = 75

zombie_commuter = 0
zombie_fratboy = 0
zombie_barista = 0
zombie_instructor = 0
zombie_artist = 0
zombie_janitor = 0
zombie_techie = 0
joker = 0

bathroom = 0
mailbox = 0

#level up function. if this were a bit more complex I'd have more sophisticated stat growth formulas, 
#but since it's a 10-minute text RPG,
#why bother?
def levelup():
	global max_health, health, damage, heal, mana, level, exp
	max_health += (max_health * 0.12)
	health = max_health
	damage = range((dam_min + 7), (dam_max + 7))
	heal += (heal * 0.2)
	mana += 4
	level += 1
	exp -= 100
	print "You leveled up to level %s! You feel a bit bigger and badder, don't you?" % level

#starting inventory
inventory = ['umbrella', 'backpack', 'thesis', 'water bottle', 'car keys']

def intro():
	print """
	The streets of Lexington are oddly empty today.
	You wander cautiously out of Parking Structure 5 into the pedestrian bridge.
	As you look out the window you see those who you once called colleagues
	\t shuffling around aimlessly; they've been taken.
	But class is still in session. And your revised thesis is due in thirty minutes.
	Your advisor's office is on the other side of campus, and only 300 zombies stand
	\t between you and your Master's Degree.\n
	You need a weapon. Let's see what you've got:
	"""
	
	for i in inventory:
		print "You have: %r" % i
	
	print "What will you use?"
	
	weapon = raw_input('> ')
	#TODO: add code that changes your damage output depending on what you use as your weapon.
		
	print "So you went with the %r. Let's hope that works." % weapon
	sleep(1)
	stairwell()
		
def stairwell():
	print """
	You're in the stairwell, looking across the pedestrian bridge.
	The doorway to the parking structure is behind you.
	Will you go back to the parking structure or cross the bridge?
	"""
	next = raw_input('> ')
	
	if "parking structure" in next:
		garage()
	elif "bridge" in next:
		bridge()
	else:
		print "Not an option here."
		stairwell()

def garage():
	global zombie_commuter, inv_serum
	if zombie_commuter == 0:
		print "There's a zombie commuter lumbering towards you. 'BRAAAIINNSSSsss'..."
		#I ran into trouble with this function. I had to enclose the mob difficulty arg in quotes since it's in quotes in the fight function.
		fight("easy", "Zombie Commuter")
		print "One down."
		zombie_commuter = 1
		inventory.append('serum')
		inv_serum += 1
		print "The Zombie Commuter dropped a vial of antidote! Better hang on to that."
		sleep(1)
		stairwell()
	else:
		print "\n Not much going on here. Go back to the stairwell."
		sleep(1)
		stairwell()
		
def bridge():
	global zombie_commuter, inv_serum
	if zombie_commuter == 0:
		print "At the end of the bridge is a zombie commuter. Blood and pus is running down her tangled hair and jeggings."
		print "She doesn't seem to notice you. Do you want to fight her or try to avoid her?"
		next = raw_input('> ')
	
		if "fight" in next:
			fight ("easy", "Zombie Commuter")
			print "One down."
			zombie_commuter = 1
			inventory.append('serum')
			inv_serum += 1
			print "The Zombie Commuter dropped a vial of antidote! Better hang on to that."
			sleep(1)
			sidewalk()
		elif "avoid" in next:
			print "You slipped around her! Looks like she still had earbuds in."
			sleep(1)
			sidewalk()
		else:
			print "Make a decision!"
			sleep(1)
			next = raw_input('> ')
	else:
		print "Nothing to see here."
		sleep(1)
		sidewalk()

#TODO: finish scenarios
def sidewalk():
	global zombie_fratboy, inv_serum
	if zombie_fratboy == 0:
		print "The sidewalk forks up ahead. You see a pack of zombie frat boys in a cluster on the right fork."
		print "To your left is the sidewalk to the student union. There's a Starbucks in there."
		print "You might find some supplies at the Starbucks, but you'll have to get past the zombies to get to your advisor."
		print "Will you go to Starbucks or fight the zombies? You can head back to the stairwell, too..."
		next = raw_input('> ')
		if "fight" in next:
			fight("hard", "Zombie Fratboy")
			print "One down."
			zombie_fratboy = 1
			inventory.append('serum')
			inv_serum += 1
			print "The Zombie Fratboy dropped a vial of serum. Hang on to that!"
			sleep(1)
			whitehall()
		elif "starbucks" in next:
			print "Probably not a bad decision!"
			sleep(1)
			starbucks()
		elif "stairwell" in next:
			print "Right, you might have forgotten something."
			sleep(1)
			stairwell()
		else:
			print "Make a decision!"
			sleep(1)
			next = raw_input('> ')
	else:
		print "Not much going on here. Best head to Whitehall."
		whitehall()

def starbucks():
	global zombie_barista, inv_serum
	if zombie_barista == 0:
		print "You slip into the student union as quickly as possible and hang a right: there's the Starbucks."
		print "No one's around."
		print "The cooler is open and running, but it's too quiet."
		print "Do you want to grab a snack from the cooler, or do you want to go back outside?"
		next = raw_input('> ')
		if "snack" in next:
			print "Out of nowhere a Zombie Barista lunges toward you!"
			fight("hard", "Zombie Barista")
			print "Whew, that was close!"
			zombie_barista = 1
			inventory.append('serum')
			inv_serum += 1
			print "The Zombie Barista dropped a vial of antidote. Hang on to that!"
			sleep(1)
			sidewalk()
		elif "outside" in next:
			print "Probably not a bad idea... it's too quiet in here."
			sleep(1)
			sidewalk()
		else:
			print "Make a decision!"
			sleep(1)
			next = raw_input('> ')
	else:
		print "Not much going on here. Best head back outside."
		sleep(1)
		sidewalk()
		
def whitehall():
	global zombie_instructor, inv_serum
	if zombie_instructor == 0:
		print "There's a zombie instructor headed straight for you--it's one of your former department colleagues!"
		print "He must have been grading papers too late last night when the infection broke out."
		print "There's only one way through Whitehall: through him."
		fight("hard", "Zombie Instructor")
		print "Yikes, that was a tough one!"
		zombie_instructor = 1
		inventory.append('serum')
		inv_serum += 1
		print "The Zombie Instructor dropped a vial of antidote. Hang on to that!"
		sleep(1)
		finearts()
	else:
		print "Not much going on here. Best head on to the Fine Arts building."
		sleep(1)
		finearts()

#Here I want there to be two options that you have to do, but order doesn't matter. Can I do this in one function?
def finearts():
	global zombie_artist, zombie_janitor, inv_serum, bathroom, mailbox
	print "The Fine Arts building would be weird even if there weren't a zombie apocalypse going on."
	print "But, the final paperwork for your thesis proposal is in your mailbox."
	print "And you need to go to the bathroom... do you go to the bathroom first, or go to your mailbox?"
	next = raw_input('> ')
	if "bathroom" in next and bathroom == 0:
		bathroom = 1
		b_room()
	elif "mailbox" in next and mailbox == 0:
		mailbox = 1
		m_box()
	else:
		print "Not an option here!"

def b_room():
	global zombie_janitor, inv_serum, mailbox
	print "Ah, sweet relief. But no rest here--a zombie janitor is busy moping around! You know what to do."
	fight("easy", "Zombie Janitor")
	print "Guess he was already worn out."
	zombie_janitor = 1
	inventory.append('serum')
	inv_serum += 1
	print "The Zombie Janitor dropped a vial of antidote. Hang on to that!"
	if mailbox == 0:
		print "Go check your mailbox."
		sleep(1)
		m_box()
	else:
		print "Looks like you're done here. Head on over to the Fine Arts library."
		library()
	
	
def m_box():
	global zombie_artist, inv_serum, bathroom
	print "Your mailbox is right up ahead. You can't tell if that art major is a real zombie or is just dressed up for a flashmob!"
	print "Better be safe than sorry. Get to zombie fightin'!"
	fight("hard", "Zombie Artist")
	print "Well... let's hope she was the real thing."
	zombie_artist = 1
	inventory.append('serum')
	inv_serum += 1
	print "The Zombie Artist dropped a vial of antidote. Hang on to that!"
	sleep(1)
	if bathroom == 0:
		print "You still need to go to the bathroom."
		sleep(1)
		b_room()
	else:
		print "Looks like you're done here. Head on over to the Fine Arts library."
		library()

def library():
	global zombie_techie, inv_serum
	print "Your advisor's office is in the back of the Fine Arts Library. Normally you'd go to the front desk and wait to be shown back..."
	print "But today you'll have to fight your way through. There's a zombie work-study student running the circulation desk!"
	print "Get to gettin'!"
	fight("hard", "Zombie Techie")
	print "Whew, almost done."
	zombie_techie = 1
	inventory.append('serum')
	inv_serum += 1
	print "The Zombie Techie dropped a vial of antidote. Hang on to that!"
	sleep(1)
	print "Let's press onward!"
	advisor()

def advisor():
	global inv_serum, weapon
	print "You make your way back to your advisor's office, only to discover that he's been taken, too!"
	print "But, he's on your committee! Maybe there's a way to get him back to normal. Do you have a few vials of antidote?"
	if inv_serum <= 4:
		print "Looks like you need more antidote! Head back outside PDQ!"
		sleep(1)
		sidewalk()
	else:
		print "You've got enough to heal him!"
		print "\'ERrrrghhghannghhhaa......aghhat....thhhhhhank... thank you!\'"
		print "He comes out of his zombified stupor. Beaming, you hand him your thesis."
		print "\'Glad to have your thesis... but... one thing I need you to take care of for me...\'"
		print "\'All this started when Joker Phillips got fired. He's something of a zombie himself now! Can you take care of him?\'"
		print "You nod and grasp your %s tightly. Joker was an awful football coach!" % weapon
		finale()

def finale():
	print "You run across Avenue of Champions to Memorial Coliseum."
	print "Zombies are strangely absent... so you head on into the gymnasium."
	print "Joker's here! Best sneak up on him quick."
	fight("boss", "Disgruntled Joker Phillips")
	sleep(1)
	inventory.append("Joker's Paycheck")
	print "\'Gah! If only they would have let me finish my contract...\' Joker disappears in a blast of smoke and heat!"
	sleep(1)
	print "You found Joker's last paycheck! He won't be needing it... looks like your student loans are taken care of!"
	print "Looks like your work here is done. Congratulations on your Master's!"
	sleep(1)
	exit()

#function that asks player if they want to fight.
def fight(diff, mob):
	while True:
		fight = raw_input('> ').lower()
		
		if "fight" in fight or "attack" in fight:
			combat(diff, mob)
			break
		elif "flee" in fight or "run" in fight:
			stairwell()
		else:
			print "You have to fight or flee!"

#Combat engine.
def combat(diff, mob):
	global health, mana, exp
	
	#checks difficulty and sets stats accordingly.
	if diff == "easy":
		mob_health = weak_health
		mob_damage = weak_damage
		mob_exp = weak_exp
	elif diff == "hard":
		mob_health = strong_health
		mob_damage = strong_damage
		mob_exp = strong_exp
	elif diff == "boss":
		mob_health = boss_health
		mob_damage = boss_damage
		mob_exp = boss_exp
	else:
		print "Something went horribly awry. Goodbye!"
		exit()
	
	print "\nYou're taking on a %s. You have %s HP; the %s has %s HP." % (mob, health, mob, mob_health)
	print "Type 'attack' to attack the %s, or 'heal' to heal yourself. It costs %s chutzpah to heal." % (mob, mana_cost)
	
	#Combat continues as long as everyone is above 0 health.
	while mob_health > 0 and health > 0:
		print ""
		
		while True:
			action = raw_input('> ')
			
			#checks for user action.
			#If attack:
			if "attack" in action:
				dam = choice(damage)
				mob_health -= dam
				break
			#if heal:
			elif "heal" in action:
				if health >= max_health:
					print "You're good to go! Get to zombie hunting."
				elif max_health - health <= heal:
					heals = max_health - health
					health = max_health
					mana -= mana_cost
					print "You healed %s; you're up to %s of %s; you're out %s chutzpah, leaving you with %s left." % (heals, health, max_health, mana_cost, mana)
					break
				#If you have lost more health than you will heal:
				else:
					health += heal
					mana -= mana_cost
					print "%s healed. You've got %s left and %s chutzpah left." % (heal, health, mana)
					break
			elif "heal" in action and mana <= 1:
				print "Oy gevalt, you're low on chutzpah! Find some coffee to recover."
			else:
				print "Attack or heal, buddy!"
		
		#Runs after the user input loop is done. Checks for mob health.
		if mob_health <= 0:
			print "You deal %s damage to the %s! It crumples in a heap." % (dam, mob)
			break
		elif mob_health > 0 and "attack" in action:
			print "You deal %s damage to the %s! It has %s left." % (dam, mob, mob_health)
		sleep(1)
		
		#Enemy turn.
		dam = choice(mob_damage)
		health -= dam
		
		if health <= 0:
			print "The %s deals %s damage to you. Oy, what a meshuggenich! You're kaput!" % (mob, dam)
			break
		else:
			print "The %s deals %s damage to you. You have %s left." % (mob, dam, health)
		sleep(1)
		#Continues loop if it hasn't been broken yet.
	
	#Information on the outcome of the fight. Runs after previous loop is broken.
	if mob_health <= 0:
		print "\nYou win! What a mensch! You gained %s experience points." % mob_exp
		mana = max_mana
		exp += mob_exp
		checkexp()
	elif health <= 0:
		print "\nOy vey, you lost! I don't think brains are kosher."
		mana = max_mana
		sleep(1)
		ress()
	else:
		print "Whoops, no one lost the fight. Uhhhh... aborting!"
		exit()

#Checks experience after a battle to see if it's time to level up!
def checkexp():
	global exp
	if exp >= 100:
		levelup()
	else:
		exp = exp
		
def ress():
	global health
	print "You died. What a schmuck! Let's give this another shot; that thesis isn't going to turn itself in. \n"
	health = max_health
	stairwell()

intro()