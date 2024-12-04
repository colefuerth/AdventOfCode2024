# day folder format is dayxx
# where xx is the day number
# create the new day folder and copy the contents of the template folder into it

# get the day number
day_num=$(ls -d day* | wc -l)
day_num=$(($day_num + 1))
day_num=$(printf "%02d" $day_num)

# create the new day folder
mkdir day$day_num
cp -r template/* day$day_num