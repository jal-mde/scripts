import pandas as pd
import sklearn
from sklearn.preprocessing import OrdinalEncoder

df_reviews = pd.read_csv("./Webpages_Classification_train_data.csv")
df_reviews = df_reviews[["url_len", "geo_loc", "tld", "who_is", "https", "label"]]

df_reviews['geo_loc'] = OrdinalEncoder().fit_transform(df_reviews.geo_loc.values.reshape(-1,1))
df_reviews['tld'] = OrdinalEncoder().fit_transform(df_reviews.tld.values.reshape(-1,1))
df_reviews['who_is'] = OrdinalEncoder().fit_transform(df_reviews.who_is.values.reshape(-1,1))
df_reviews['https'] = OrdinalEncoder().fit_transform(df_reviews.https.values.reshape(-1,1))
df_reviews['label'] = OrdinalEncoder().fit_transform(df_reviews.label.values.reshape(-1,1))

df_reviews = df_reviews.to_csv("prec_data_final.csv", index=False)
#,url,url_len,ip_add,geo_loc,tld,who_is,https,js_len,js_obf_len,content,label
