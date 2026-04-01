# ── Importações ──────────────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Configurações visuais
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

print("✅ Bibliotecas importadas com sucesso!")

# ── Criação do Dataset ───────────────────────────────
np.random.seed(42)

produtos = {
    "Dom Casmurro":       ("Literatura", 35.90),
    "O Pequeno Príncipe": ("Infantil",   29.90),
    "Sapiens":             ("Ciências",   54.90),
    "Python para Dados":  ("Tecnologia", 89.90),
    "Clean Code":         ("Tecnologia", 95.00),
    "Harry Potter Vol.1": ("Fantasia",   49.90),
    "Atomic Habits":      ("Autoajuda",  44.90),
    "A Arte da Guerra":   ("Filosofia",  32.00),
    "Cosmos":             ("Ciências",   62.50),
    "Cem Anos de Solidão":("Literatura", 39.90),
}

vendedores = ["Ana Lima", "Carlos Mendes", "Bruno Costa", "Fernanda Rocha"]
regioes    = ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
datas      = pd.date_range("2024-01-01", "2024-06-30", periods=50)

nomes_prod = np.random.choice(list(produtos.keys()), 50)

dados = {
    "id_venda":   range(1, 51),
    "data":       datas.strftime("%Y-%m-%d"),
    "produto":    nomes_prod,
    "categoria":  [produtos[p][0] for p in nomes_prod],
    "quantidade": np.random.randint(1, 6, 50),
    "preco_unit": [produtos[p][1] for p in nomes_prod],
    "vendedor":   np.random.choice(vendedores, 50),
    "regiao":     np.random.choice(regioes, 50),
}

df = pd.DataFrame(dados)
df["total_venda"] = df["quantidade"] * df["preco_unit"]


# 5 linhas com valores nulos
novas_linhas_nulas = pd.DataFrame({
    "id_venda": range(51, 56),
    "data": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
    "produto": ["Dom Casmurro", None, "Sapiens", None, "Cosmos"],
    "categoria": ["Literatura", "Infantil", "Ciências", "Tecnologia", None],
    "quantidade": [1, 2, None, 4, 5],
    "preco_unit": [35.90, 29.90, 54.90, None, 62.50],
    "vendedor": ["Ana Lima", None, "Bruno Costa", "Fernanda Rocha", "Carlos Mendes"],
    "regiao": ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
})

df = pd.concat([df, novas_linhas_nulas], ignore_index=True)

print(" Novas linhas com valores nulos adicionadas!")


# linhas nulas
novas_linhas_nulas = pd.DataFrame({ ... })
df = pd.concat([df, novas_linhas_nulas], ignore_index=True)
df.to_csv("vendas_livraria.csv", index=False)
df.to_csv("vendas_livraria.csv", index=False)

print(f" Dataset criado! Shape: {df.shape}")
print(f"   Colunas: {list(df.columns)}")
df.head()

print("\n🔎 Onde estão os valores nulos?")
print(df.isnull().sum())

# ── Exploração Inicial ───────────────────────────────
df = pd.read_csv("vendas_livraria.csv")
print("\n🔍 VALORES NULOS ENCONTRADOS:")
print(df.isnull().sum())
df["produto"] = df["produto"].fillna("Não Informado")
df["quantidade"] = df["quantidade"].fillna(1)

print("═" * 45)
print("📋 INFORMAÇÕES DO DATASET")
print("═" * 45)
print(f"Linhas:   {df.shape[0]}")
print(f"Colunas:  {df.shape[1]}")

print("\n📊 TIPOS DE DADOS:")
print(df.dtypes)

print("\n🔍 VALORES NULOS:")
print(df.isnull().sum())

print("\n📈 ESTATÍSTICAS DESCRITIVAS:")
df[["quantidade", "preco_unit", "total_venda"]].describe().round(2)

# ── Análise de Vendas ────────────────────────────────

# 1. Total faturado
total = df["total_venda"].sum()
print(f"💰 Faturamento Total: R$ {total:,.2f}")

# 2. Faturamento por categoria
print("\n📦 Faturamento por Categoria:")
cat_fat = (df.groupby("categoria")["total_venda"]
             .sum()
             .sort_values(ascending=False))
print(cat_fat.apply(lambda x: f"R$ {x:,.2f}"))

# 3. Melhor vendedor
print("\n🏆 Ranking de Vendedores:")
vend_rank = (df.groupby("vendedor")["total_venda"]
               .sum()
               .sort_values(ascending=False))
print(vend_rank.apply(lambda x: f"R$ {x:,.2f}"))

# 4. Produto mais vendido (em quantidade)
print("\n📚 Top 3 Produtos (qtd vendida):")
top_prod = (df.groupby("produto")["quantidade"]
              .sum()
              .sort_values(ascending=False)
              .head(3))
print(top_prod)

# 5. Venda média por região
print("\n🗺️  Ticket Médio por Região:")
reg_media = (df.groupby("regiao")["total_venda"]
               .mean()
               .sort_values(ascending=False)
               .round(2))
print(reg_media.apply(lambda x: f"R$ {x:,.2f}"))



# evolução do faturamento mês a mês

df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month
vendas_por_mes = df.groupby("mes")["total_venda"].sum()
print("\nDinheiro que entrou por mês:")
print(vendas_por_mes.round(2))



# gráfico de linha mostrando a tendência de vendas

plt.figure(figsize=(10, 4))
plt.plot(vendas_por_mes.index, vendas_por_mes.values,
         color="green", linewidth=2, marker="o")
plt.title("Gráfico de Vendas da livraria")
plt.xlabel("Meses (1 a 6)")
plt.ylabel("Dinheiro que entrou (R$)")
plt.grid(True)
plt.show()



#  Vendedor com o maior Ticket Médio

ticket_dos_vendedores = df.groupby("vendedor")["total_venda"].mean()
ticket_ordenado = ticket_dos_vendedores.sort_values(ascending=False)
print("\nMédia de valor por venda de cada um:")
print(ticket_ordenado.round(2))
vendedor_campeao = ticket_ordenado.index[0]
valor_campeao = ticket_ordenado.iloc[0]
print(f"\n O vencedor do Ticket Médio foi {vendedor_campeao}!")
print(f"A média das vendas dele foi de R$ {valor_campeao.round(2)}")



# Análise de Vendas de Alto Valor

vendas_caras = df[df["total_venda"] > 200]
quantidade_vendas_caras = len(vendas_caras)
print("Quantidade de vendas acima de 200 reais:")
print(quantidade_vendas_caras)
categorias_caras = vendas_caras.groupby("categoria")["total_venda"].count()
categorias_ordenadas = categorias_caras.sort_values(ascending=False)
print("\nAs categorias que mais vendem caro são:")
print(categorias_ordenadas)
top_produto_caro = vendas_caras.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
nome_do_campeao = top_produto_caro.index[0]
print("\nO produto que mais gerou vendas grandes foi:")
print(nome_do_campeao)

# ── Visualizações ────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Dashboard: Livraria 2024",
             fontsize=14, fontweight="bold", y=1.02)

# --- Gráfico 1: Faturamento por Categoria (barras) ---
ax1 = axes[0]
cores = ["#e84b1a" if i==0 else "#c8bfaa" for i in range(len(cat_fat))]
ax1.barh(cat_fat.index, cat_fat.values, color=cores)
ax1.set_title("Faturamento por Categoria", fontweight="bold")
ax1.set_xlabel("Receita (R$)")
ax1.xaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))

# --- Gráfico 2: Ranking Vendedores (barras verticais) ---
ax2 = axes[1]
ax2.bar(vend_rank.index, vend_rank.values,
        color=["#1a6ee8","#4a90e8","#8ab8f0","#c8d8f0"])
ax2.set_title("Ranking de Vendedores", fontweight="bold")
ax2.set_ylabel("Total Vendido (R$)")
ax2.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda y, _: f"R${y/1000:.0f}k"))
ax2.tick_params(axis="x", rotation=15)

# --- Gráfico 3: Distribuição das Regiões (pizza) ---
ax3 = axes[2]
reg_total = df.groupby("regiao")["total_venda"].sum()
ax3.pie(reg_total, labels=reg_total.index,
        autopct="%1.1f%%",
        colors=["#e84b1a","#1a6ee8","#c9a84c","#28a745","#6f42c1"],
        startangle=90,
        wedgeprops={"edgecolor":"white", "linewidth":2})
ax3.set_title("Participação por Região", fontweight="bold")

plt.tight_layout()
plt.savefig("dashboard_livraria.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Gráficos salvos em dashboard_livraria.png")