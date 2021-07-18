address = input("Enter main address without http/thhps/www: ")
change = input("what is change string: ")
dbname= str(input("the name of db (default is multishop.sql) : ") or "multishop.sql")

#read input file
fin = open(dbname, "rt")
#read file contents to string
data = fin.read()

#concatenates with main address
mcchttpswww = "https://www."+address
mcchttps = "https://"+address
mcchttpwww = "http://www."+address
mcchttp = "http://"+address
mwholetext = address


#concatenates with replace domain address
rcchttpswww = "https://www."+change
rcchttps = "https://"+change
rcchttpwww = "http://www."+change
rcchttp = "http://"+change
rwholetext = change


#replace all occurrences of the required string
occurrences = data.count(mcchttpswww)
print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
data = data.replace(mcchttpswww,rcchttpswww) 

#replace all occurrences of the required string
occurrences = data.count(mcchttps)
print(f"Number of occurrences of the word {mcchttps}: ", occurrences)
data = data.replace(mcchttps,rcchttps)


#replace all occurrences of the required string
occurrences = data.count(mcchttpwww)
print(f"Number of occurrences of the word {mcchttpwww}: ", occurrences)
data = data.replace(mcchttpwww,rcchttpwww)


#replace all occurrences of the required string
occurrences = data.count(mcchttp)
print(f"Number of occurrences of the word {mcchttp}: ", occurrences)
data = data.replace(mcchttp,rcchttp)


#replace all occurrences of the required string
occurrences = data.count(mwholetext)
print(f"Number of occurrences of the word {mwholetext}: ", occurrences)
data = data.replace(mwholetext,rwholetext)



#close the input file
fin.close()
#open the input file in write mode
fin = open(dbname, "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

