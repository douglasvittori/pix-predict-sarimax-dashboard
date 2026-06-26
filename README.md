# 🎯 Pix Predict: Dashboard de Previsão de Transações Pix para Fintech

[![Streamlit App](https://static.streamlit.io/badge_穩定.svg)](https://SEU-LINK-AQUI.streamlit.app/)

Este projeto foi desenvolvido para resolver um problema real de planejamento e operações em uma Fintech: **prever o volume diário de transações via Pix**. 

A solução consiste em um modelo preditivo especializado em séries temporais acoplado a um dashboard interativo desenvolvido em **Streamlit**. O grande diferencial da aplicação é traduzir previsões matemáticas complexas em **alertas e recomendações práticas de negócio** para as equipes de TI (Infraestrutura) e Operações.

---

## 📊 O Aplicativo em Ação

O dashboard permite que qualquer gestor ou diretor da empresa defina uma janela de projeção futura (de 7 a 30 dias) através de uma barra lateral interativa. 

Ao calcular a previsão, o sistema gera automaticamente:
1. **Métricas de Resumo:** Volumes máximos, mínimos e médias diárias projetadas para o período.
2. **Gráfico de Tendência Futura:** Visualização interativa do comportamento da demanda ao longo dos dias.
3. **Alertas Operacionais Inteligentes:** Identificação automática dos dias de pico (para prevenção de quedas de servidor) e janelas de calmaria (oportunidades para manutenções programadas).
4. **Exportação de Dados:** Botão integrado para baixar as previsões geradas diretamente em formato CSV.

---

## 🧠 Abordagem Técnica e Modelagem

Os dados de transações financeiras possuem um comportamento complexo de dependência temporal e forte ritmo semanal. O desenvolvimento seguiu as seguintes etapas:

* **Análise Exploratória:** Identificação de uma clara tendência de crescimento ao longo dos meses e uma forte **sazonalidade de 7 dias** (picos expressivos nas sextas-feiras e quedas acentuadas nos finais de semana).
* **Modelagem Preditiva:** Evolução de um modelo de base (ARIMA) para o **SARIMAX**, permitindo que o algoritmo compreendesse as variáveis sazonais e o ritmo dos dias da semana.
* **Otimização:** O modelo foi ajustado diretamente com diferenciação zerada ($d=0$) no treinamento após estabilização, reduzindo a margem de erro (RMSE) de **33.42** para apenas **28.48**, aproximando a simulação ao máximo da realidade do mercado.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando o ecossistema técnico de Ciência de Dados em Python:

* **Python 3**
* **Streamlit** (Interface e deploy da aplicação)
* **Statsmodels** (Algoritmo estatístico SARIMAX)
* **Pandas** e **NumPy** (Manipulação, engenharia de recursos e soma acumulada)
* **Joblib** (Persistência e carregamento do modelo treinado em arquivo `.pkl`)

---

## 🚀 Como Rodar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/pix-predict-sarimax-dashboard.git](https://github.com/seu-usuario/pix-predict-sarimax-dashboard.git)
   cd pix-predict-sarimax-dashboard

   1.Crie e ative um ambiente virtual:

   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate

   2.Instale as dependências:

   pip install -r requirements.txt

   3. Execute o aplicativo:

   streamlit run app.py

   Desenvolvedor

    Douglas Vittori - Cientista de Dados em Formação

    🔗 Conecte-se comigo no LinkedIn

    🚀 Conheça meu Portfólio de Dados