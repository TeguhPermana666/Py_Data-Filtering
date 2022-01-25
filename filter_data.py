#mengmbil sebuah data sesuai dengan kondisi yang ditentukan, kondisi yang di cek adalah pada kolom
#filltered_df=df[kondisi]

#defenisi data
import pandas as pd
data_nilai=({"Sandi":[70,50,64],"Sanda":[45,98,76],"Sunda":[60,75,98]})
df=pd.DataFrame.from_dict(data_nilai,orient="index",columns=["Matematika","Biologi","Fisika"])
print(df)

filtered= df[df["Matematika"]>50]
print(filtered)