import streamlit as st
import pandas as pd
df = pd.read_csv('country_profile_variables.csv')

country_list = list(df['country'])

#Clean Dataframe Spliat columns with more than 1 value into 2 columns
df[['Labour force Participation female %', 'Labour force Participation male %']] = df['Labour force participation (female/male pop. %)'].str.split("/", expand = True)
df.drop('Labour force participation (female/male pop. %)', axis=1, inplace = True)

df[['Pop. using improved drinking water (urban, %)', 'Pop. using improved drinking water (rural, %)']] = df['Pop. using improved drinking water (urban/rural, %)'].str.split("/", expand = True)
df.drop('Pop. using improved drinking water (urban/rural, %)',  axis=1, inplace = True)

df[['Education: Primary gross enrol. ratio (female per 100 pop.)', 'Education: Primary gross enrol. ratio (male per 100 pop.)']] = df['Education: Primary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
df.drop('Education: Primary gross enrol. ratio (f/m per 100 pop.)',  axis=1, inplace = True)

df[['Education: Secondary gross enrol. ratio (female per 100 pop.)', 'Education: Secondary gross enrol. ratio (female per 100 pop.)']] = df['Education: Secondary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
df.drop('Education: Secondary gross enrol. ratio (f/m per 100 pop.)',  axis=1, inplace = True)

df[['Education: Tertiary gross enrol. ratio (female per 100 pop.)', 'Education: Tertiary gross enrol. ratio (male per 100 pop.)']] = df['Education: Tertiary gross enrol. ratio (f/m per 100 pop.)'].str.split("/", expand = True)
df.drop('Education: Tertiary gross enrol. ratio (f/m per 100 pop.)',  axis=1, inplace = True)

#Convert everything to numbers
indicators = df.columns
indicators = indicators[2:]
for s in indicators:
    df[s] = pd.to_numeric(df[s], errors = 'coerce')

selected_countries = ['Benin','Haiti','Bangladesh','Mali','France']
#MultiSelect
selected_countries = st.multiselect("Select Countries", country_list)
#st.write("You selected", len(selected_countries), "options: ", selected_countries)


#pd.pivot_table(df, columns = 'country')[['Algeria', 'Angola']]
df_pivot = pd.pivot_table(df, columns = 'country')[selected_countries]
df_pivot.index.names=['indicator']
st.write(df_pivot)

#Select Box
indicator = 'GDP per capita (current US$)'
indicator = st.selectbox("Select an Indicator", indicators)
st.write("you selected this option ",indicator)

st.bar_chart(df_pivot.loc[indicator])

#df_pivot.loc[indicator].plot(x='country', kind = 'bar')
#df_pivot.loc['Agricultural production index (2004-2006=100)'].plot(x='country', kind = 'bar')
#df[df['country'].isin(selected_countries)]
#df[df['country'].isin(selected_countries)]
#df[df['country']=='Andorra']