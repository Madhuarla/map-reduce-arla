# map-reduce-arla
practice on mapping and reducing

## Type of data
I like bmw cars because of their sporty look and comfort inside. I personally prefer to buy an used car rather than new car. So, I took data related to used bmw cars to know which model has the highest number of sales.
I took the data from kaagle. link to my data https://www.kaggle.com/mysarahmadbhat/bmw-used-car-listing

## how to run the script
> 1.clone down the repo
> 2.open the code in vs code which is popularly used. or you can run using powershell.
> 3.type the below commands to get the results. 
> mapping :

``` cat bmw.csv | Python 02mapper.py > ArlaOutput01.txt
> reducing:

``` cat bmw.csv | Python 02mapper.py | sort | Python 02reducer.py > ArlaOutput02.txt
## Data problem
I would like to get the number of cars sold in each bmw model.

##  Data story
I have analyzed the data and sorted accoring to the sales of each bmw model. As per the data that shown bmw series 3 have the highest number of sales. 

![image](https://github.com/Madhuarla/map-reduce-arla/blob/main/finaloutput.PNG)
