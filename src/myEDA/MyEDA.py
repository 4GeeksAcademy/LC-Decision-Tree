import pandas as pd

class MyEDA:
    @staticmethod
    def explore(df):
        # Mostrar información básica
        print(f"\nRows (before cleanup): {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        # Detectar duplicados
        duplicates = df[df.duplicated()]
        if not duplicates.empty:
            print("\n🔴 Duplicate row(s) found and removed:\n")
            print(duplicates)
            df = df.drop_duplicates()
            print(f"\n✅ New shape after removing duplicates: {df.shape}")

        # Crear tabla resumen
        import pandas as pd

        # Crear tabla resumen
        summary = pd.DataFrame({
            "Non-Null Count": df.count(),
            "Null Count": df.isnull().sum(),
            "Data Type": df.dtypes
        })
        summary["Data Category"] = summary["Data Type"].apply(lambda x: "Categorical" if x == "object" else "Numeric")

        # Calcular el ancho máximo del índice (nombre de columna)
        max_index_length = max(len(str(index)) for index in summary.index)

        # Definir los anchos de las demás columnas
        col_widths = {
            "Non-Null Count": 16,
            "Null Count": 12,
            "Data Type": 10,
            "Data Category": 15
        }

        # Imprimir encabezado con separadores
        header = f"+{'-' * (max_index_length + 2)}+{'-' * col_widths['Non-Null Count']}+{'-' * col_widths['Null Count']}+{'-' * col_widths['Data Type']}+{'-' * col_widths['Data Category']}+"
        print(header)
        print(f"| {'':<{max_index_length}} | {'Non-Null Count':^{col_widths['Non-Null Count']}} | {'Null Count':^{col_widths['Null Count']}} | {'Data Type':^{col_widths['Data Type']}} | {'Data Category':^{col_widths['Data Category']}} |")
        print(header)

        # Imprimir filas del DataFrame alineadas
        for index, row in summary.iterrows():
            print(f"| {index:<{max_index_length}} | {row['Non-Null Count']:>{col_widths['Non-Null Count']-2}} | {row['Null Count']:>{col_widths['Null Count']-2}} | {str(row['Data Type']):>{col_widths['Data Type']-2}} | {row['Data Category']:>{col_widths['Data Category']-2}} |")

        # Imprimir línea final
        print(header)
        
    
        # Separar variables categóricas y numéricas
        categorical = list(df.select_dtypes(include=["object"]).columns)
        numerical = list(df.select_dtypes(exclude=["object"]).columns)

        return categorical, numerical, df
