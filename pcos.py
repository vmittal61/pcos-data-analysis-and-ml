import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\HP\Downloads\PCOS_data.csv")
print(df.corr(numeric_only=True)['PCOS (Y/N)'].sort_values(ascending=True))

df['BMI_data'] = pd.cut(
    df['BMI'],
    bins=[0,18.5,25,30,100],
    labels=['Underweight','Normal','Overweight','Obese'])
df['Avg_Follicle_No'] = pd.cut((df['Follicle No. (L)']+df['Follicle No. (R)'])/2, bins=[0,2,4,6,8,10,12,14,16,18,20,22])
df['Cycle(R/I)']=df['Cycle(R/I)'].replace(5, df['Cycle(R/I)'].mode()[0])
df['Marraige Status (Yrs)']=df['Marraige Status (Yrs)'].fillna(df['Marraige Status (Yrs)'].mean())

# num n cat cols separated
num=df.select_dtypes(include=['int64','float64']).columns
cat=df.select_dtypes(include=['object']).columns
print('numerical cols:')
print(num)
print('Categorical cols: ')
print(cat)

# null filled
df['Fast food (Y/N)']=df['Fast food (Y/N)'].fillna(df['Fast food (Y/N)'].mode()[0])

# dropped last col
df.drop(columns=['Unnamed: 44'], inplace=True)

# cycle relation
df['Cycle(R/I)']=df['Cycle(R/I)'].replace(5, df['Cycle(R/I)'].mode()[0])

# corresponding values for cycle and PCOS
print(pd.crosstab(df['Cycle(R/I)'], df['PCOS (Y/N)']))

# unsuccessful heatmap attempt
col=['BMI','PCOS (Y/N)']
sns.heatmap(df[col].corr(),annot=True, vmin=-0.3)

# BMI  VS   PCOS
plt.figure(figsize=(8,5))
sns.kdeplot(x="BMI", hue="PCOS (Y/N)", data=df, fill=True, common_norm=False, alpha=0.4, linewidth=2)

# Updated Cycle data
df['Cycle(R/I)']=df['Cycle(R/I)'].replace(5, df['Cycle(R/I)'].mode()[0])

# EVERY CORRELATION with PCOS
corr = df.corr(numeric_only=True)
plt.figure(figsize=(12,10))
sns.heatmap(corr, cmap='coolwarm')
corr['PCOS (Y/N)'].sort_values(ascending=False)

# BMI V Follicle R
sns.scatterplot(x='BMI', y='Follicle No. (R)', data=df)



# BMI AND CYCLE    +  data
bmi_cycle=pd.crosstab(
    [df['BMI_data'], df['Cycle(R/I)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(bmi_cycle[1])
sns.catplot(
    data=df,
    x='BMI_data',
    hue='PCOS (Y/N)',
    col='Cycle(R/I)',
    kind='count')




# BMI and FOLLICLE  +  data
bmi_f=pd.crosstab(
    [df['BMI_data'], df['Avg_Follicle_No']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(bmi_f[1])
#---1
pivot = df.pivot_table(
    values='PCOS (Y/N)',
    index='BMI_data',
    columns='Avg_Follicle_No',
    aggfunc='mean')
sns.heatmap(pivot, cmap='Blues', annot=True)


#---2 (PCOS=1)
df['Avg_follicle_no.']=(df['Follicle No. (L)']+df['Follicle No. (R)'])/2
sns.kdeplot(
    x='BMI',
    y='Avg_follicle_no.',
    data=df[df['PCOS (Y/N)']==1],
    fill=True)



# BMI n SkinD   +  data
bmi_skind =pd.crosstab(
    [df['BMI_data'], df['Skin darkening (Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(bmi_skind[1])
sns.catplot(
    x='BMI_data',
    hue='PCOS (Y/N)',
    col='Skin darkening (Y/N)',
    kind='count',
    data=df)



# HairG+SkinD +  Data
hairg_skind = pd.crosstab(
    [df['hair growth(Y/N)'], df['Skin darkening (Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(hairg_skind[1])
a=hairg_skind.plot(kind='bar', stacked=True)
for n in a.containers:
    a.bar_label(
        n,
        fmt='%.1f%%',
        label_type='center')
a.legend(
    title='PCOS (Y/N)',
    loc='upper right',
    bbox_to_anchor=(1.005, 1),)
plt.tight_layout()
plt.xlabel(' ')
plt.ylabel('Percentage')
plt.title('PCOS Prevalence (%)')



# Follicle+skind  +  Data
f_skind=pd.crosstab(
    [df['Avg_Follicle_No'], df['Skin darkening (Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(f_skind)
a=sns.catplot(
    x='Avg_Follicle_No',
    hue='PCOS (Y/N)',
    col='Skin darkening (Y/N)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()




# Follicle+WeightG  +  Data
f_wg=pd.crosstab(
    [df['Avg_Follicle_No'], df['Weight gain(Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(f_wg[1])
a=sns.catplot(
    x='Avg_Follicle_No',
    hue='PCOS (Y/N)',
    col='Weight gain(Y/N)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()




# Follicle+HairG  +  Data
f_hg=pd.crosstab(
    [df['Avg_Follicle_No'], df['hair growth(Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(f_hg[1])
a=sns.catplot(
    x='Avg_Follicle_No',
    hue='PCOS (Y/N)',
    col='hair growth(Y/N)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()




# follicle+cycle  +  Data
f_cycle=pd.crosstab(
    [df['Avg_Follicle_No'], df['Cycle(R/I)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(f_cycle[1])
a=sns.catplot(
    x='Avg_Follicle_No',
    hue='PCOS (Y/N)',
    col='Cycle(R/I)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()




# SkinD+HairG  +  Data
skind_hg=pd.crosstab(
    [df['Skin darkening (Y/N)'], df['hair growth(Y/N)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(skind_hg[1])
a=sns.catplot(
    x='Skin darkening (Y/N)',
    hue='PCOS (Y/N)',
    col='hair growth(Y/N)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()




# SkinD+Cycle  +  Data
skind_cycle=pd.crosstab(
    [df['Skin darkening (Y/N)'], df['Cycle(R/I)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(skind_cycle[1])
a=sns.catplot(
    x='Skin darkening (Y/N)',
    hue='PCOS (Y/N)',
    col='Cycle(R/I)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()


# Follicle, skinD, HairGrowth, WeightGain, Cycle, FastFood, Pimples, Weight, BMI, HairLoss

wg_cycle=pd.crosstab(
    [df['Weight gain(Y/N)'], df['Cycle(R/I)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(wg_cycle[1])
a=sns.catplot(
    x='Weight gain(Y/N)',
    hue='PCOS (Y/N)',
    col='Cycle(R/I)',
    kind='count',
    data=df)
sns.move_legend(a, loc='upper right')
plt.tight_layout()


age_cycle=pd.crosstab(
    [df[' Age (yrs)'], df['Cycle(R/I)']],
    df['PCOS (Y/N)'],
    normalize='index')*100
print(age_cycle.xs('I', level='Cycle(R/I)')[1])
pivot = df.pivot_table(
    values='PCOS (Y/N)',
    index=' Age (yrs)',
    columns='Cycle(R/I)',
    aggfunc='mean')
sns.heatmap(pivot, cmap='Blues', annot=True)
plt.show()


df.to_csv("PCOS_cleaned.csv", index=False)

with pd.ExcelWriter("All_Insights.xlsx") as writer:

    bmi_skind.to_excel(writer,
                       sheet_name="bmi_skind")

    bmi_cycle.to_excel(writer,
                        sheet_name="bmi_cycle")

    bmi_f.to_excel(writer,
                        sheet_name="bmi_f")
    hairg_skind.to_excel(writer,
                        sheet_name="hairg_skind")
    f_skind.to_excel(writer,
                        sheet_name="f_skind")
    f_wg.to_excel(writer,
                        sheet_name="f_wg")
    f_hg.to_excel(writer,
                        sheet_name="f_hg")
    f_cycle.to_excel(writer,
                        sheet_name="f_cycle")
    skind_hg.to_excel(writer,
                        sheet_name="skind_hg")
    skind_cycle.to_excel(writer,
                        sheet_name="skind_cycle")
    wg_cycle.to_excel(writer,
                        sheet_name="wg_cycle")



df=pd.read_csv("PCOS_cleaned.csv")
df["II    beta-HCG(mIU/mL)"] = df["II    beta-HCG(mIU/mL)"].astype(str).str.replace(r"\.$", "", regex=True)
df["II    beta-HCG(mIU/mL)"] = pd.to_numeric(df["II    beta-HCG(mIU/mL)"],errors="coerce")
df["AMH(ng/mL)"] = pd.to_numeric(df["AMH(ng/mL)"],errors="coerce")
df["AMH(ng/mL)"] = df["AMH(ng/mL)"].fillna(df["AMH(ng/mL)"].median())
df["II    beta-HCG(mIU/mL)"] = df["II    beta-HCG(mIU/mL)"].fillna(df["II    beta-HCG(mIU/mL)"].median())

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


X = df.drop(["Patient File No.", "Sl. No", "PCOS (Y/N)","BMI_data", "Avg_Follicle_No", "Follicle No. (R)", "Follicle No. (L)"], axis=1)
y=df["PCOS (Y/N)"]
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)

model=XGBClassifier()
model.fit(X_train,y_train)
predictions=model.predict(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
lr = LogisticRegression(max_iter=5000)
lr.fit(X_train_scaled, y_train)
y_pred = lr.predict(X_test_scaled)

rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Accuracy XGB:", accuracy_score(y_test, predictions)*100)
print("Accuracy LR:", accuracy_score(y_test, y_pred)*100)
print("Accuracy RF:", accuracy_score(y_test, y_pred_rf)*100)


importance = pd.DataFrame({"Feature": X.columns, "Importance": model.feature_importances_})
importance = importance.sort_values(by="Importance", ascending=False)
print(importance.head(15))
from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))

for c in X.columns:
    print(c)

from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
from xgboost import plot_importance
plot_importance(model)
plt.show()

X = df.drop(["Patient File No.", "Sl. No", "PCOS (Y/N)","BMI_data", "Avg_Follicle_No", "Follicle No. (R)", "Follicle No. (L)"], axis=1)
y=df["PCOS (Y/N)"]
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)
model=XGBClassifier()
model.fit(X_train,y_train)
predictions=model.predict(X_test)

from xgboost import plot_importance
plot_importance(model)
plt.show()

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
print(cm)

from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

