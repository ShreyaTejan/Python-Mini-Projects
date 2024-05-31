
import camelot as ct
#input pdf to extract tables
input_pdf = ct.read_pdf("Shreya_Python.pdf", flav='lattice', pages= '1,2')
input_pdf
for n in input_pdf:
    print(n)

input_pdf[2].df
df= input_pdf[2].df.loc[11:14,1:3]
df
df= df.reset_index(drop =True)
df.columns = ['Speed','Driver','Car']
df.to_csv("packet_output.csv")
df.to_excel("table_from_pdf.xlxs")
import pandas as p
df2= pd.read_csv("packet_output.csv")
df2
import seaborn as sea
df_melted = df.melt('Speed', var_name = 'Driver', value_name='Car')
sea.barplot(x="Driver", y='Car', hue="Speed", data+ df_melted)
