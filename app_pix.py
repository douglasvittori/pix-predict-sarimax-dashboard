import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import joblib 

st.set_page_config(page_title="Previsão de Pix - Fintech", page_icon=":dollar:", layout="wide")

st.title("🎯 Dashboard de Previsão de Transações Pix")
st.markdown("Este aplicativo utiliza o modelo preditivo **SARIMAX** para projetar o volume diário de transações.")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("📊 Projeto Pix Predict")
    st.markdown(
        """
        Este projeto analisa e projeta o volume diário de transações Pix de uma Fintech. 
        O modelo **SARIMAX** foi ajustado para capturar a tendência de crescimento e as 
        fortes variações semanais do mercado financeiro.
        """
    )
    st.markdown("---") # Linha divisória para separar o resumo das configurações
    
    st.subheader("⚙️ Configurações da Previsão")
    # Permite ao usuário escolher quantos dias ele quer ver no futuro
    dias_previsao = st.sidebar.slider("Dias para prever no futuro:", min_value=7, max_value=30, value=15)

    botao_calcular = st.button("Calcular Previsão")

    st.markdown("---") # Linha divisória para organizar o espaço
    
    # Seção do Desenvolvedor 
    st.subheader("🛠️ Desenvolvedor")
    st.markdown("**Douglas Vittori**")
    st.caption("Cientista de Dados em Formação")
    
    # Botão e link destacado para o portfólio
    st.markdown("🔗 **Acesse meus projetos:**")
    st.markdown("[🚀 Meu Portfólio de Dados](https://douglasvittori-portfolio.lovable.app/)")


model_file = 'modelo/modelo_v2.pkl'
modelo = joblib.load(model_file)
# Aqui criamos um botão para disparar a previsão
if botao_calcular:
    
    # 1. O modelo gera as previsões brutas (já vem com as datas automáticas no índice!)
    previsoes_brutas = modelo.forecast(steps=dias_previsao)
    
    # 2. Pegamos o último valor real conhecido do treino
    ultimo_valor_real = 134.11 
    
    # 3. Fazemos a soma acumulada direto (o Pandas mantém as datas certinhas)
    previsoes_reais = ultimo_valor_real + np.cumsum(previsoes_brutas)
    
    # 4. Criando o DataFrame final 

    df_previsao = pd.DataFrame(previsoes_reais)
    df_previsao.columns = ["Volume Pix Previsto"] # Renomeia a coluna para o gráfico 
   
    st.subheader("📊 Resumo do Período Previsto")
    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(label="Volume Máximo Previsto", value=f"{df_previsao['Volume Pix Previsto'].max():.2f}")
    with m2:
        st.metric(label="Volume Mínimo Previsto", value=f"{df_previsao['Volume Pix Previsto'].min():.2f}")
    with m3:
        st.metric(label="Média Diária Projetada", value=f"{df_previsao['Volume Pix Previsto'].mean():.2f}")

    df_grafico_final = pd.DataFrame(df_previsao)

    df_grafico_final = df_previsao.index.name = "Data"
    
    # --- EXIBINDO OS RESULTADOS ---
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Gráfico de Tendência Futura")
        st.line_chart(df_previsao)
        
    with col2:
        st.subheader("📋 Tabela de Dados (Previsão)")
        df_tabela = df_previsao.copy()
        df_tabela.index = df_tabela.index.strftime('%d/%m/%Y')
        st.dataframe(df_tabela.style.format("{:.2f}"))

        csv = df_previsao.to_csv().encode('utf-8')
        st.sidebar.download_button(
            label="📥 Baixar Previsões (CSV)",
            data=csv,
            file_name='previsoes_pix.csv',
            mime='text/csv',
        )

        st.markdown("---")

    # --- NOVO: SEÇÃO 2: ALERTAS E INSIGHTS DE NEGÓCIO (FOCO PRÁTICO) ---
    st.subheader("💡 Alertas e Insights Operacionais")
    st.markdown("Avisos automáticos gerados com base nas projeções para apoiar a tomada de decisão:")
    
    # Calculando os dias de pico e de calmaria direto do resultado
    dia_pico = df_previsao["Volume Pix Previsto"].idxmax().strftime('%d/%m/%Y')
    dia_baixa = df_previsao["Volume Pix Previsto"].idxmin().strftime('%d/%m/%Y')
    
    col_ins1, col_ins2 = st.columns(2)
    
    with col_ins1:
        st.warning(
            f"""
            **🚀 Alerta de Pico de Demanda (TI & Infraestrutura):** O maior volume está previsto para o dia **{dia_pico}**.  
            *Recomendação:* Notificar o time de tecnologia para garantir que os servidores aguentem a alta concentração de acessos simultâneos sem instabilidade no app.
            """
        )
        
    with col_ins2:
        st.success(
            f"""
            **📉 Alerta de Janela de Manutenção:** O menor volume de transações está previsto para o dia **{dia_baixa}**.  
            *Recomendação:* Excelente oportunidade para agendar atualizações de sistema, manutenções programadas ou testes internos com o menor impacto possível para os clientes.
            """
        )

else:
    st.info("Clique no botão 'Calcular Previsão' na barra lateral para visualizar os resultados.")