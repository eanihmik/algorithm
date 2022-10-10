# dtype object 아닌 경우는 다 continuous라는 가정 하에
mat = pd.DataFrame(index=data.columns, columns=data.columns)
for i in range(len(mat.columns)):
    for j in range(len(mat.columns)):
        if (data[mat.columns[i]].dtype != "object") & (data[mat.columns[j]].dtype != "object"):
            mat.iloc[i, j] = data[mat.columns[i]].corr(data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype == "object") & (data[mat.columns[j]].dtype == "object"):
            mat.iloc[i, j] = theils_u(data[mat.columns[i]], data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype == "object") & (data[mat.columns[j]].dtype != "object"):
            mat.iloc[i, j] = correlation_ratio(data[mat.columns[i]], data[mat.columns[j]])
        elif (data[mat.columns[i]].dtype != "object") & (data[mat.columns[j]].dtype == "object"):
            mat.iloc[i, j] = correlation_ratio(data[mat.columns[i]], data[mat.columns[j]])
mat
