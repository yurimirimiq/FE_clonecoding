import pickle
profile_file = open("profile.pickle", "wb")

profile = {"이름" : "강유림", "나이" : 22, "취미" : ["영화", "독서"]}
print (profile)
pickle.dump(profile, profile_file)
profile_file.close()
