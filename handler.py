import pandas as pd

df = pd.read_csv("./Webpages_Classification_train_data.csv")
df[["url_len", "ip_add", "geo_loc", "tld", "who_is", "https", "label"]].to_csv("prec_data.csv", index=False)
#,url,url_len,ip_add,geo_loc,tld,who_is,https,js_len,js_obf_len,content,label
