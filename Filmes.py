filmes = {
    "Ação": {
        "Piratas do caribe": "14/12/2025",
        "Duro de matar": "30/01/2026",
        "Homem aranha": "15/02/2026"
    },
    "Comédia": {
        "Um maluco no Golf": None,
        "Gente grande": None,
        "Derepente 30!": None
    }
}
for categoria, lista in filmes.items():
    print(f"\nMeus filmes de {categoria} favoritos:\n")
    for filme, data in lista.items():
        if data:
            print(f"{filme} - {data}")
        else:
            print(f"{filme}")

filmes["Comédia"]["Um maluco no Golf"] = "20/02/2026"

for categoria, lista in filmes.items():
    print(f"\nMeus filmes de {categoria} favoritos:\n")
    for filme, data in lista.items():
        if data:
            print(f"{filme} - {data}")
        else:
            print(f"{filme}")


