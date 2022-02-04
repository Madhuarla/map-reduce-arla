import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    model,year,price,transmission,mileage,mpg,engine = datalist

    # print intermediate key-value pairs to standard output
    print(model,"\t",price)