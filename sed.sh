
sed -n -i '1,+1000000p' Webpages_Classification_train_data.csv
sleep 2
sed -i 's/[^,]*,[^,]*,//' Webpages_Classification_train_data.csv
sleep 2
