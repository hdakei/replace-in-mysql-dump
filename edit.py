address = input("Enter main address without http/thhps/www: ")
change = input("what is change string: ")
dbname= str(input("the name of db (default is multishop.sql) : ") or "multishop.sql")
ishttps= str(input("is replace with https? (default is no) : ") or "no")
iswww= str(input("is replace with www? (default is no) : ") or "no")	
rwholetext = change
mwholetext = address

#concatenates with main address
mcchttpswww = "https://www."+address
mcchttps = "https://"+address
mcchttpwww = "http://www."+address
mcchttp = "http://"+address
#concatenates replace domain www with httpsaddress
rcchttpswww = "https://www."+change
#concatenates replace domain without wwww with httpsaddress
rcchttps = "https://"+change
#concatenates replace domain www with httpaddress
rcchttpwww = "http://www."+change
#concatenates replace domain without wwww with httpaddress
rcchttp = "http://"+change



	
	
def changehttpswithwww():
		#close the input file
		#read input file
		fin = open(dbname, "rt")
		#read file contents to string
		data = fin.read()

		#replace all occurrences of the required string
		occurrences = data.count(mcchttpswww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpswww,rcchttpswww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttps)
		print(f"Number of occurrences of the word {mcchttps}: ", occurrences)
		data = data.replace(mcchttps,rcchttpswww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpwww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpwww,rcchttpswww) 		
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttp)
		print(f"Number of occurrences of the word {mcchttp}: ", occurrences)
		data = data.replace(mcchttp,rcchttpswww) 	
		
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

		


def changehttpswithoutwww():
		#read input file
		fin = open(dbname, "rt")
		#read file contents to string
		data = fin.read()

				
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpswww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpswww,rcchttpswww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttps)
		print(f"Number of occurrences of the word {mcchttps}: ", occurrences)
		data = data.replace(mcchttps,rcchttpswww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpwww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpwww,rcchttpswww) 		
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttp)
		print(f"Number of occurrences of the word {mcchttp}: ", occurrences)
		data = data.replace(mcchttp,rcchttpswww) 	
		
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





def changehttpwithwww():
		#read input file
		fin = open(dbname, "rt")
		#read file contents to string
		data = fin.read()

	
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpswww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpswww,rcchttpwww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttps)
		print(f"Number of occurrences of the word {mcchttps}: ", occurrences)
		data = data.replace(mcchttps,rcchttpwww) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpwww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpwww,rcchttpwww) 		
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttp)
		print(f"Number of occurrences of the word {mcchttp}: ", occurrences)
		data = data.replace(mcchttp,rcchttpwww) 	
		
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


def changehttpwithoutwww():
		#read input file
		fin = open(dbname, "rt")
		#read file contents to string
		data = fin.read()

		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpswww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpswww,rcchttp) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttps)
		print(f"Number of occurrences of the word {mcchttps}: ", occurrences)
		data = data.replace(mcchttps,rcchttp) 
		
		#replace all occurrences of the required string
		occurrences = data.count(mcchttpwww)
		print(f"Number of occurrences of the word {mcchttpswww}: ", occurrences)
		data = data.replace(mcchttpwww,rcchttp) 		
		
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


if ishttps == "yes" and iswww == "yes":
	changehttpswithwww()
elif ishttps == "yes" and iswww == "no":
	changehttpswithoutwww()
elif ishttps == "no" and iswww == "yes":
	changehttpwithwww()
elif ishttps == "no" and iswww == "no":
	changehttpwithoutwww()
