import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np





st.markdown("# Evolution de la Data science au fil des années")
st.markdown("## Comment le big data a-t-il apparu ? ")
st.image('The-data-revolution-explained-by-data-complexity-both-intrinsic-the-data-per-se.png')
st.markdown("Ceci est un paragraphe de texte **formaté** en utilisant *Markdown*.")
st.markdown("Le terme \'data science\' est apparu dans les années 2000 pour décrire un domaine multidisciplinaire qui combine des compétences en mathématiques, statistiques et programmation pour analyser et interpréter les données. L'explosion du Big Data a été un tournant décisif, car les entreprises ont été confrontées à des volumes massifs de données provenant de diverses sources. L'avènement du Big Data a donné naissance à de nouvelles technologies et techniques pour traiter et analyser ces données. L\'apprentissage automatique (machine learning) et l\'intelligence artificielle (IA) sont devenus des domaines clés des data sciences, permettant d\'extraire des connaissances et des modèles à partir des données. La data science a également connu une adoption croissante dans de nombreux domaines et industries, car elle permet d\'améliorer la prise de décision, de prédire des tendances et de résoudre des problèmes complexes. Les data scientists sont devenus des professionnels recherchés, et de nombreuses entreprises ont investi dans la création de départements et de laboratoires de data science. Aujourd\'hui, les data sciences continuent d\'évoluer avec l\'émergence de nouvelles technologies et techniques. Des domaines tels que l\'apprentissage profond (deep learning), l\'analyse prédictive, l\'analyse des réseaux sociaux et l\'analyse des données non structurées sont devenus des domaines de recherche et d\'application importants. En résumé, l\'évolution des data sciences a été marquée par l\'explosion du Big Data, l\'utilisation de l\'apprentissage automatique et de l\'IA, ainsi que par une adoption croissante dans divers domaines. Les data sciences continuent de se développer avec de nouvelles technologies et techniques émergentes pour répondre aux défis et opportunités liés à l\'analyse des données.")

salaries = pd.read_csv('salaries.csv')

salaries['work_year'] = pd.to_datetime(salaries['work_year'], format='%Y')
annees = salaries['work_year'].dt.year.unique().tolist()

selected_year = st.sidebar.selectbox('Sélectionnez une année', annees)

salaries_filtered = salaries[salaries['work_year'].dt.year == selected_year]



salaries_avg = salaries.groupby(salaries['work_year'].dt.year)['salary_in_usd'].mean()
st.title("Evolution des outils big data en fonction du temps")
st.image('evolution_visualisations.png')

st.title('Évolution moyenne des salaires en fonction du temps')

st.bar_chart(salaries_avg)

result_merged = pd.read_csv('result_merged.csv')
result_merged['work_year']=  pd.to_datetime(result_merged['work_year'], format='%Y')
region_mean = result_merged.groupby(['region_name', 'work_year']).agg('mean')
region_mean = region_mean.reset_index()
regions_to_keep = ['Amerique', 'Europe']
years_to_keep = ['2021', '2022', '2023']
region_mean = region_mean[region_mean['region_name'].isin(regions_to_keep)]
region_mean = region_mean[region_mean['work_year'].isin(salaries_filtered['work_year'])]
salaries_by_region_year = region_mean.groupby(['region_name', region_mean['work_year'].dt.year])['salary_in_usd'].mean()


salaries_by_region_year = salaries_by_region_year.unstack()




salaries_by_region_year.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Région')
plt.ylabel('Salaire moyen')
plt.title('Évolution des salaires par région et année')
plt.legend(title='Année')
st.pyplot(plt)

st.markdown('## Les métiers de la Data Science sont désormais parmis les métiers les mieux payés')
st.markdown('Les moyennes des salaires en France pour un débutant')
st.image('projet4.png')

st.markdown('## Sommes investies dans le domaine du big data depuis 01/05/2020')
investissements = pd.read_csv('investissements.csv', delimiter=';')



st.dataframe(investissements)

pays_liste = investissements['Country'].unique().tolist()
selected_pays = st.sidebar.selectbox('Sélectionnez un pays', pays_liste)

data_filtered = investissements[investissements['Country'] == selected_pays]

colonnes_trimestres = [col for col in data_filtered.columns]
colonnes_trimestres = np.delete(colonnes_trimestres,0)
colonnes_trimestres = np.delete(colonnes_trimestres,-1)


valeurs_par_colonne = {}

for colonne in colonnes_trimestres:
    valeurs_par_colonne[colonne] = data_filtered[colonne].values[0]

fig, ax = plt.subplots()
ax.bar(valeurs_par_colonne.keys(), valeurs_par_colonne.values())
ax.set_title(f'Valeurs par colonne pour le pays {selected_pays}')
ax.set_xlabel('Trimestre')
ax.set_ylabel('Valeur')
st.pyplot(fig)


offres = pd.read_csv('series_offres_difusees_ds.csv', delimiter=';')
offres = offres.reset_index()
offres['Nombre d\'offres diffusées'] = offres['Nombre d\'offres diffusées'].astype(int)
offres_groupes = offres.groupby('Année')['Nombre d\'offres diffusées'].sum()
offres_groupes.reset_index()


fig, ax = plt.subplots()
offres_groupes.plot(kind='bar', ax=ax)
ax.set_title('Nombre d\'offres par année')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre d\'offres')

st.pyplot(fig)

st.image('PROJEY3.png')

st.markdown("Répartition des profils recherchés par type de métier")
st.image('PROJET3.png')











