# Band name generator
import random


titles = ["gigantic", "sour", "steamy", "gross", "stupid", 
	      "ironic", "greasy", "tangy", "smelly", "small",
	      "Inventive", "Spherical", "spiritual", "green",
	      "Blue", "pot bellies", "pickled", prickly"]
	      
adjs = ["tiny", "fat", "shiny", "electric", "fluffy", "bright", 
        "corrupt", "agressive", "alarming", "amazing", "magical",
        "courageous", "fierce", "colorless", "red", "thoughtless"
        "smart", "delirious", "fabulous", "fergalicious", "dangerous"]
        
plural_nouns = ["apples", "oranges", "kiwis", "clementines"
                "wildebeasts", "mammoths", "rabbits", "sloth", "crashes"
                "spices", "herbs", "eggs", "pony tails", "bears" 
                "unicorns", "Kermit", "Sighs", "indians", "cowboys]
            
def title():
	''' This function chooses a random title for the name '''
	return random.choice(titles)
	
def adj():
	'''This function chooses a random adj for the band '''
	return random.choice(adjs)
	
def plural_noun():
	return random.choice(plural_nouns)
	
def main():
	while True:
		name = raw_imput("Enter your name: ")
		if name == "q"
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()
		
main()