import streamlit as st
from pandas import DataFrame
import pickle
from playsound import playsound
# Ler dados do modelo treinado
modelo = pickle.load(open('modelo_eleicao_municipal.pkl', 'rb'))
logit = modelo['resultados']
escala = modelo['escala']

# Titulo do APP
st.title("Previsão de eleição de candidatos a vereador no estado da Paraíba")
st.markdown('''
    <style>
    .stApp {
        background-image: url("https://imagens.ebc.com.br/CfhTMvy3MruuywXxD5B36DvEQxE=/1170x700/smart/https://agenciabrasil.ebc.com.br/sites/default/files/atoms/image/urna_menor.jpg?itok=ff-VZfrA");
        background-size: Cover;
        background-repeat: no-repeat;  
        background-position: center;
    }
    .stButton > button, .stTextInput, .stSelectbox, .stNumberInput, .stExpander > .stButton, .stMarkdown, .stExpander .stMarkdown {
        background-color: rgba(255, 255, 255, 0.95); 
        border-radius: 5px;
        border: none;
        padding: 10px;
    }
    .stExpander > .stButton {
        font-size: 18px; 
        font-weight: bold; 
    }
     .stExpander > .stButton {
        font-size: 20px;
        font-weight: bold; 
        color: #333; 
        background-color: #f9f9f9;
        box-shadow: 0 2px 12px rgba(0,0,0,0.1); 
    }
    </style>
''', unsafe_allow_html=True)




with st.expander('Modelo', expanded=False):

    st.markdown('''
                
            ## Apresentação do Protótipo
            Este Aplicativo possibilita que se faça previsões sobre a eleição ou não de um candidato a vereador no estado da Paraíba
            a partir de dados das eleições de 2020 usando uma modelagem de `Machine Learning`.

            ## Modelo canônico
            Regressão logística
            
            $$P(Y=1) = \dfrac{exp(Xb+u)}{1+exp(Xb+u)}$$

            ''')

st.header("Dados de Entrada")
# Formulário
sexo = st.selectbox("Informe seu sexo:", ['Feminino', 'Masculino'])
idade = st.number_input("Informe sua idade:", value=30)
gastos = st.number_input("Informe o valor que ira destinar a campanha:", value=0)
reeleição = st.selectbox("Você é candidato a reeleição?", ['Sou', 'Não sou'])

idade_n = (idade - escala[1]['IDADE'][0])/(escala[1]['IDADE'][1] - escala[1]['IDADE'][0])

gastos_n = (gastos - escala[0]['VR_DESPESA_MAX_CAMPANHA'][0])/(escala[0]['VR_DESPESA_MAX_CAMPANHA'][1] - escala[0]['VR_DESPESA_MAX_CAMPANHA'][0])

st.write(f"Tenho {idade} anos. Meu sexo é {sexo}. Meu orçamento na campanha será de R$ {gastos}. {reeleição} candidato a reeleição.")

# Data frame: atributos do modelo treinado

data = DataFrame({
    'VR_DESPESA_MAX_CAMPANHA': [gastos_n],
    'IDADE': [idade_n],
    'NR_PARTIDO_11': [False],
    'NR_PARTIDO_12': [False],
    'NR_PARTIDO_13': [False],
    'NR_PARTIDO_14': [False],
    'NR_PARTIDO_15': [False],
    'NR_PARTIDO_16': [False],
    'NR_PARTIDO_17': [False],
    'NR_PARTIDO_18': [False],
    'NR_PARTIDO_19': [False],
    'NR_PARTIDO_20': [False],
    'NR_PARTIDO_22': [False],
    'NR_PARTIDO_23': [False],
    'NR_PARTIDO_25': [False],
    'NR_PARTIDO_27': [False],
    'NR_PARTIDO_28': [False],
    'NR_PARTIDO_29': [False],
    'NR_PARTIDO_33': [False],
    'NR_PARTIDO_35': [False],
    'NR_PARTIDO_36': [False],
    'NR_PARTIDO_40': [False],
    'NR_PARTIDO_43': [False],
    'NR_PARTIDO_45': [False],
    'NR_PARTIDO_50': [False],
    'NR_PARTIDO_51': [False],
    'NR_PARTIDO_55': [False],
    'NR_PARTIDO_65': [False],
    'NR_PARTIDO_70': [False],
    'NR_PARTIDO_77': [False],
    'NR_PARTIDO_80': [False],
    'NR_PARTIDO_90': [False],
    'CD_GENERO_4': [sexo=="Feminino"],
    'CD_COR_RACA_2': [False],
    'CD_COR_RACA_3': [False],
    'CD_COR_RACA_4': [False],
    'CD_COR_RACA_5': [False],
    'CD_COR_RACA_6': [False],
    'ST_REELEICAO_S': [reeleição=="Sim"],
    'SG_UE_19011': [False],
    'SG_UE_19020': [False],
    'SG_UE_19038': [False],
    'SG_UE_19046': [False],
    'SG_UE_19054': [False],
    'SG_UE_19062': [False],
    'SG_UE_19070': [False],
    'SG_UE_19089': [False],
    'SG_UE_19097': [False],
    'SG_UE_19100': [False],
    'SG_UE_19119': [False],
    'SG_UE_19127': [False],
    'SG_UE_19135': [False],
    'SG_UE_19143': [False],
    'SG_UE_19151': [False],
    'SG_UE_19160': [False],
    'SG_UE_19178': [False],
    'SG_UE_19186': [False],
    'SG_UE_19194': [False],
    'SG_UE_19208': [False],
    'SG_UE_19216': [False],
    'SG_UE_19224': [False],
    'SG_UE_19232': [False],
    'SG_UE_19240': [False],
    'SG_UE_19259': [False],
    'SG_UE_19267': [False],
    'SG_UE_19275': [False],
    'SG_UE_19283': [False],
    'SG_UE_19291': [False],
    'SG_UE_19305': [False],
    'SG_UE_19313': [False],
    'SG_UE_19321': [False],
    'SG_UE_19330': [False],
    'SG_UE_19348': [False],
    'SG_UE_19356': [False],
    'SG_UE_19364': [False],
    'SG_UE_19372': [False],
    'SG_UE_19380': [False],
    'SG_UE_19399': [False],
    'SG_UE_19402': [False],
    'SG_UE_19410': [False],
    'SG_UE_19429': [False],
    'SG_UE_19437': [False],
    'SG_UE_19445': [False],
    'SG_UE_19453': [False],
    'SG_UE_19461': [False],
    'SG_UE_19470': [False],
    'SG_UE_19488': [False],
    'SG_UE_19496': [False],
    'SG_UE_19500': [False],
    'SG_UE_19518': [False],
    'SG_UE_19526': [False],
    'SG_UE_19534': [False],
    'SG_UE_19542': [False],
    'SG_UE_19550': [False],
    'SG_UE_19569': [False],
    'SG_UE_19577': [False],
    'SG_UE_19585': [False],
    'SG_UE_19593': [False],
    'SG_UE_19607': [False],
    'SG_UE_19615': [False],
    'SG_UE_19623': [False],
    'SG_UE_19631': [False],
    'SG_UE_19640': [False],
    'SG_UE_19658': [False],
    'SG_UE_19666': [False],
    'SG_UE_19674': [False],
    'SG_UE_19682': [False],
    'SG_UE_19690': [False],
    'SG_UE_19704': [False],
    'SG_UE_19712': [False],
    'SG_UE_19720': [False],
    'SG_UE_19739': [False],
    'SG_UE_19747': [False],
    'SG_UE_19755': [False],
    'SG_UE_19763': [False],
    'SG_UE_19771': [False],
    'SG_UE_19780': [False],
    'SG_UE_19798': [False],
    'SG_UE_19801': [False],
    'SG_UE_19810': [False],
    'SG_UE_19828': [False],
    'SG_UE_19836': [False],
    'SG_UE_19844': [False],
    'SG_UE_19852': [False],
    'SG_UE_19860': [False],
    'SG_UE_19879': [False],
    'SG_UE_19887': [False],
    'SG_UE_19895': [False],
    'SG_UE_19909': [False],
    'SG_UE_19917': [False],
    'SG_UE_19925': [False],
    'SG_UE_19933': [False],
    'SG_UE_19941': [False],
    'SG_UE_19950': [False],
    'SG_UE_19968': [False],
    'SG_UE_19976': [False],
    'SG_UE_19984': [False],
    'SG_UE_19992': [False],
    'SG_UE_20001': [False],
    'SG_UE_20010': [False],
    'SG_UE_20036': [False],
    'SG_UE_20052': [False],
    'SG_UE_20079': [False],
    'SG_UE_20095': [False],
    'SG_UE_20117': [False],
    'SG_UE_20133': [False],
    'SG_UE_20150': [False],
    'SG_UE_20176': [False],
    'SG_UE_20192': [False],
    'SG_UE_20214': [False],
    'SG_UE_20230': [False],
    'SG_UE_20257': [False],
    'SG_UE_20273': [False],
    'SG_UE_20290': [False],
    'SG_UE_20311': [False],
    'SG_UE_20338': [False],
    'SG_UE_20354': [False],
    'SG_UE_20370': [False],
    'SG_UE_20397': [False],
    'SG_UE_20419': [False],
    'SG_UE_20435': [False],
    'SG_UE_20451': [False],
    'SG_UE_20478': [False],
    'SG_UE_20494': [False],
    'SG_UE_20516': [False],
    'SG_UE_20532': [False],
    'SG_UE_20559': [False],
    'SG_UE_20575': [False],
    'SG_UE_20591': [False],
    'SG_UE_20613': [False],
    'SG_UE_20630': [False],
    'SG_UE_20656': [False],
    'SG_UE_20672': [False],
    'SG_UE_20699': [False],
    'SG_UE_20710': [False],
    'SG_UE_20737': [False],
    'SG_UE_20753': [False],
    'SG_UE_20770': [False],
    'SG_UE_20796': [False],
    'SG_UE_20818': [False],
    'SG_UE_20834': [False],
    'SG_UE_20850': [False],
    'SG_UE_20877': [False],
    'SG_UE_20893': [False],
    'SG_UE_20915': [False],
    'SG_UE_20931': [False],
    'SG_UE_20958': [False],
    'SG_UE_20974': [False],
    'SG_UE_20990': [False],
    'SG_UE_21016': [False],
    'SG_UE_21032': [False],
    'SG_UE_21059': [False],
    'SG_UE_21075': [False],
    'SG_UE_21091': [False],
    'SG_UE_21113': [False],
    'SG_UE_21130': [False],
    'SG_UE_21156': [False],
    'SG_UE_21172': [False],
    'SG_UE_21199': [False],
    'SG_UE_21210': [False],
    'SG_UE_21237': [False],
    'SG_UE_21253': [False],
    'SG_UE_21270': [False],
    'SG_UE_21296': [False],
    'SG_UE_21318': [False],
    'SG_UE_21334': [False],
    'SG_UE_21350': [False],
    'SG_UE_21377': [False],
    'SG_UE_21393': [False],
    'SG_UE_21415': [False],
    'SG_UE_21431': [False],
    'SG_UE_21458': [False],
    'SG_UE_21474': [False],
    'SG_UE_21490': [False],
    'SG_UE_21512': [False],
    'SG_UE_21539': [False],
    'SG_UE_21555': [False],
    'SG_UE_21571': [False],
    'SG_UE_21598': [False],
    'SG_UE_21610': [False],
    'SG_UE_21636': [False],
    'SG_UE_21652': [False],
    'SG_UE_21679': [False],
    'SG_UE_21695': [False],
    'SG_UE_21717': [False],
    'SG_UE_21733': [False],
    'SG_UE_21750': [False],
    'SG_UE_21776': [False],
    'SG_UE_21792': [False],
    'SG_UE_21814': [False],
    'SG_UE_21830': [False],
    'SG_UE_21857': [False],
    'SG_UE_21873': [False],
    'SG_UE_21890': [False],
    'SG_UE_21911': [False],
    'SG_UE_21938': [False],
    'SG_UE_21954': [False],
    'SG_UE_21970': [False],
    'SG_UE_21997': [False],
    'SG_UE_22012': [False],
    'SG_UE_22039': [False],
    'SG_UE_22055': [False],
    'SG_UE_22071': [False],
    'SG_UE_22098': [False],
    'SG_UE_22110': [False],
    'SG_UE_22136': [False],
    'SG_UE_22152': [False],
    'SG_UE_22179': [False],
    'SG_UE_22195': [False],
    'SG_UE_22217': [False],
    'SG_UE_22233': [False],
    'SG_UE_22250': [False],
    'SG_UE_22276': [False],
    'SG_UE_22292': [False],
    'SG_UE_22314': [False],
    'SG_UE_22330': [False],
    'SG_UE_22357': [False],
    'SG_UE_22373': [False],
    'SG_UE_22390': [False],
    'SG_UE_22411': [False],
    'SG_UE_22438': [False]
})

colunas = ['VR_DESPESA_MAX_CAMPANHA', 'IDADE', 'CD_GENERO_4', 'ST_REELEICAO_S']

#st.table(data[colunas])

# Convertendo o DataFrame para HTML
html = data[colunas].to_html(index=False)

# Adicionando estilo com CSS
css_styling = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #cccccc;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #004682;  /* Cor de fundo do cabeçalho */
        color: white;
    }
    tr:nth-child(even) {background-color: #f2f2f2;}  /* Linhas pares */
    tr:hover {background-color: #ddd;}  /* Hover de linhas */
</style>
"""

# Exibindo a tabela estilizada no Streamlit
st.markdown(css_styling + html, unsafe_allow_html=True)

if st.button('Simular'):
    st.header('Resultados')
    classe = logit.predict(data)
    probabilidade = logit.predict_proba(data)

    r = DataFrame({'Probabilidade': probabilidade[0],
                   'Classe': ['Não Eleito', 'Eleito']})

    resposta = "Não será Eleito"
    if classe==1:
        resposta = " será Eleito"
        st.balloons()
    st.write(f"Você {resposta.upper()}")
    st.bar_chart(data=r, x="Classe", y="Probabilidade",
                 color=["#FF0000"])
    
    
