
sed -n -i '1,+1000000p' Webpages_Classification_train_data.csv
sleep 3
sed -i 's/[^,]*,[^,]*,//' Webpages_Classification_train_data.csv
sleep 3
sed -i 's/bad/0/g' Webpages_Classification_train_data.csv
sleep 3
sed -i 's/good/1/g' Webpages_Classification_train_data.csv
sleep 3
sed -i 's/\(.*\),\(.*\),\(.*\),\(.*\),\(.*\),\(.*\),\(.*\),\(.*\),.*,\(.*\)/\1,\2,\3,\4,\5,\6,\7,\8,\9/' Webpages_Classification_train_data.csv

