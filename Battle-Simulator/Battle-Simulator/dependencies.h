#ifndef dependencies_H
#define dependencies_H

// roll the dice
int rollDice(int diceType) {
	int diceSide = rand() % diceType;
	return diceSide;
}

// player class
class Player {
public:
	std::string name;
	std::string classType;
	int strength;
	int endurance;
	int id;
	int DT = 20;

	int getHP() { return (10 + ((strength + endurance) * 2)); }
	int getHit() { return rollDice(DT); }

	Player(std::string inpName, std::string inpClassType, int inpStrength, int inpEndurance, int inpId) {
		name = inpName;
		classType = inpClassType;
		strength = inpStrength;
		endurance = inpEndurance;
		id = inpId;
	}
	Player() = default;
};

// Enemies
class Enemy {
public:
	// var declaration
	std::string name;
	double AC;  // armor class ability to resist hits
	int DT;  // dice used to attack
	int eid;  // id for Enemies (Enemy id)
	int HP = round(HP * (1 + (AC * 10)));
	int getHit() { return rollDice(DT); }

	Enemy(std::string inpName, int inpHP, double inpAC, int inpDT, int inpEid) {
		name = inpName;
		HP = inpHP;
		AC = inpAC;
		DT = inpDT;
		eid = inpEid;
	}
	Enemy() = default;
};

std::istream& operator>>(std::istream& str, Player& player) {
	std::string line;
	if (std::getline(str, line)) {
		std::stringstream lineStream(line);

		std::string name;
		std::string classType;
		int         strength;
		int         endurance;
		int         id;

		if (lineStream >> name >> classType >> strength >> endurance >> id) {
			// Set up the player object.
			player = Player(name, classType, strength, endurance, id);
		}
		else {
			// Error when reading player characteristics from line.
			// Need to set the error state of the stream.
			str.setstate(std::ios::failbit);
		}
	}
	return str;
}

std::vector<Player> getPlayers() {
	std::ifstream                 playerFile("Player.txt");
	std::istream_iterator<Player> playerIter(playerFile);
	std::istream_iterator<Player> end;

	return std::vector<Player>(playerIter, end);
}

std::istream& operator>>(std::istream& str, Enemy& enemy) {
	std::string line;
	if (std::getline(str, line)) {
		std::stringstream lineStream(line);

		std::string name;
		int         HP;
		double      AC;
		int         DT;
		int         eid;

		if (lineStream >> name >> HP >> AC >> DT >> eid) {
			// Set up the enemy object.
			enemy = Enemy(name, HP, AC, DT, eid);
		}
		else {
			// Error when reading player characteristics from line.
			// Need to set the error state of the stream.
			str.setstate(std::ios::failbit);
		}
	}
	return str;
}

std::vector<Enemy> getEnemies() {
	std::ifstream                 enemyFile("Enemy.txt");
	std::istream_iterator<Enemy> enemyIter(enemyFile);
	std::istream_iterator<Enemy> end;

	return std::vector<Enemy>(enemyIter, end);
}

// Get context of the situation
std::string enemyContxt(int option) {
	int randNum = round(rand() % (9) + 1);

	static const std::string names[] = {
		"\nBruneor the ", "\nRichard the ", "\nFilbert the ", "\nLodric the ",
		"\nRuuker the ",  "\nKruger the ",  "\nCharles the ", "\nAaarl the ",
		"\nVasiilk the ", "\nGubl the " };

	static const std::string introductions[] = {
		" hits you with a blunt slinky ", " whacks you with a feather ",
		" pushes you into Tiny Tim ", " stabs you with a lamp ",
		" shoots you with an M16 catapult ", " summons a spirit to pester you ",
		" uses a rune-stothe enchantment ",
		" tries to curse you but explodes an unfourtunate chicken, due to a "
		"terrible mispronuncation of your name ",
		" simply does nothing ", " burps up a gnerm (a miniature knome) " };

	static const std::string transitions[] = {
		"and says 'Die, filthy swine!' ",
		"then trips on a gruubliyth. ",
		"and then, snarls! ",
		"and then begins to mutter an ancient curse! ",
		"then yells 'You hit like a Kerbb hehe!' ",
		"and says 'Die, filthy swine!' ",
		"then trips on a gruubliyth. ",
		"and then, snarls! ",
		"and then begins to mutter an ancient curse! ",
		"then yells 'You hit like a Uerbb hehe!' " };

	switch (option) {
	case 1:
		return names[randNum - 1];
	case 2:
		return introductions[randNum - 1];
	case 3:
		return transitions[randNum - 1];
	}
}

// Get context of the situation
std::string playerContxt(Player &player) {
	int randNum = round(rand() % (19) + 1);
	// pretty much the same thing with the function above
	std::string name = player.name;

	if (randNum == 1) return "\n" + name + " strikes with an evil Urrgleumbeck ";
	if (randNum == 2)
		return "\n" + name +
		" hits, but fails and hits a wall causing a rupture in time "
		"itself ";
	if (randNum == 3) return "\n" + name + " trips on an explosive turtle ";
	if (randNum == 4) return "\n" + name + " lunges at his enemy ";
	if (randNum == 5)
		return "\n" + name + " sneezes violently causing a worldwide pandemic ";
	if (randNum == 6)
		return "\n" + name + " swiftly hacks at his enemy using a knerm ";
	if (randNum == 7) return "\n" + name + " summons the almighty mega-knerm ";
	if (randNum == 8) return "\n" + name + " summons a crude writhe-golem ";
	if (randNum == 9) return "\n" + name + " casts an ancient curse";
	if (randNum == 10) return "\n" + name + " yells 'AVADA CADABRA!' ";
	if (randNum == 11) return "\n" + name + " falls painfully ";
	if (randNum == 12) return "\n" + name + " throws a strauug gas grenade ";
	if (randNum == 13) return "\n" + name + " fires a portable villkreek mortar ";
	if (randNum == 14)
		return "\n" + name + " strikes with a pirated knerm sword ";
	if (randNum == 15)
		return "\n" + name +
		" drinks a super-enchantment giving him the ability to eat apples "
		"10 times faster than normal ";
	if (randNum == 16)
		return "\n" + name + " summons Tiny Tim who calls upon his  liege ";
	if (randNum == 17)
		return "\n" + name + " calls upon a skeleton to do his bidding";
	if (randNum == 18) return "\n" + name + " strikes with a molten axe";
	if (randNum == 19)
		return "\n" + name + " hits a tree with his head causing it to fall ";
	if (randNum == 20)
		return "\n" + name + " calls upon the ancient curse of Ugaar ";
}

// fight an Enemy (option 1)
int fightEnemy(Player &player, Enemy &enemy) {
	int eHit = enemy.getHit();
	int pHit = player.getHit();
	int eHP = enemy.HP;
	int pHP = player.getHP();
	int playerLastRoll = pHit;
	int enemyLastRoll = eHit;
	int counter = 0;
	std::string name = enemyContxt(1);
	std::cout << "\n->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n";
	std::cout << "Welcome to the Arena!\n";
	std::cout << "Starting HP: \n" << player.name << "'s HP: " << pHP << "\n" << enemy.name << "'s HP: " << eHP << "\n";
	std::cout << "Begin Battle!\n";
	for (;;) {
		while (playerLastRoll == pHit || enemyLastRoll == eHit && counter != 0) {
			eHit = enemy.getHit();
			pHit = player.getHit();
		}
		std::cout << name << enemy.name << enemyContxt(2) << enemyContxt(3) << "Dealing " << eHit << " Damage!\n";
		pHP = pHP - eHit;
		if (pHP <= 0) {
			std::cout << "\n" << player.name << " is Dead!\n";
			std::cout << enemy.name << "'s HP left: " << eHP << "\n";
			std::cout << player.name << "'s HP left: " << pHP << "\n";
			break;
		}
		else {
			std::cout << "\n" << playerContxt(player) << " Dealing " << pHit << " Damage!\n";
			eHP = eHP - pHit;
			if (eHP <= 0) {
				std::cout << "\n" << enemy.name << " is Dead!\n";
				std::cout << enemy.name << "'s HP left: " << eHP << "\n";
				std::cout << player.name << "'s HP left: " << pHP << "\n";
				break;
			}
		}
		playerLastRoll = pHit;
		enemyLastRoll = eHit;
		counter++;
	}

	return 0;
}

// fight a Player (option 2)
int fightPlayer(Player &player1, Player &player2) {
	int pHit1 = player1.getHit();
	int pHit2 = player2.getHit();
	int pHP1 = player1.getHP();
	int pHP2 = player2.getHP();
	int playerLastRoll1 = pHit1;
	int playerLastRoll2 = pHit2;
	int counter = 0;
	std::cout << "\n->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n";
	std::cout << "Welcome to the Arena!\n";
	std::cout << "Starting HP: \n" << player1.name << "'s HP: " << pHP1 << "\n" << player2.name << "'s HP: " << pHP2 << "\n";
	std::cout << "Begin Battle!\n";
	for (;;) {
		while (playerLastRoll1 == pHit1 ||
			playerLastRoll2 == pHit2 && counter != 0) {
			pHit1 = player1.getHit();
			pHit2 = player2.getHit();
		}
		std::cout << "\n" << playerContxt(player1) << " Dealing " << pHit1 << " Damage!\n";
		pHP2 = pHP2 - pHit1;
		if (pHP2 <= 0) {
			std::cout << "\n" << player2.name << " is Dead!\n";
			std::cout << player1.name << "'s HP left: " << pHP1 << "\n";
			std::cout << player2.name << "'s HP left: " << pHP2 << "\n";
			break;
		}
		else {
			std::cout << "\n" << playerContxt(player2) << " Dealing " << pHit2 << " Damage!\n";
			pHP1 = pHP1 - pHit2;
			if (pHP1 <= 0) {
				std::cout << "\n" << player1.name << " is Dead!\n";
				std::cout << player1.name << "'s HP left: " << pHP1 << "\n";
				std::cout << player2.name << "'s HP left: " << pHP2 << "\n";
				break;
			}
		}
		playerLastRoll1 = pHit1;
		playerLastRoll2 = pHit2;
		counter++;
	}

	return 0;
}

int entityComboCheck(int id1, int id2, std::vector<Player> &allPlayers, std::vector<Enemy> &allEnemies, int option) {
	bool found = false;
	if (option == 1) {
		std::vector<Player>::iterator player_iter = allPlayers.begin();
		std::vector<Enemy>::iterator enemy_iter;

		// try to find player
		while (player_iter != allPlayers.end() && !found) {
			if (player_iter->id == id1)
				found = true;
			else
				player_iter++;
		}

		// when player has been found, try to find enemy
		if (found) {
			found = false;
			enemy_iter = allEnemies.begin();

			while (enemy_iter != allEnemies.end() && !found) {
				if (enemy_iter->eid == id2)
					found = true;
				else
					enemy_iter++;
			}

			// if both have been found call function fightEnemy
			if (found) fightEnemy(*player_iter, *enemy_iter);
			return 0;
		}
		return 0;
	}

	if (option == 2) {
		std::vector<Player>::iterator player_iter1 = allPlayers.begin();
		std::vector<Player>::iterator player_iter2;

		// try to find player 1
		while (player_iter1 != allPlayers.end() && !found) {
			if (player_iter1->id == id1)
				found = true;
			else
				player_iter1++;
		}

		// when player has been found, try to find player 2
		if (found) {
			found = false;
			player_iter2 = allPlayers.begin();

			while (player_iter2 != allPlayers.end() && !found) {
				if (player_iter2->id == id2)
					found = true;
				else
					player_iter2++;
			}

			// if both have been found call function fightPlayer
			if (found) fightPlayer(*player_iter1, *player_iter2);
			return 0;
		}
	}
}

#endif