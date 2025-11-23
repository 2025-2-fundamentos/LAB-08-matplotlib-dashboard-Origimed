# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("files/input/shipping-data.csv")

    os.makedirs("docs", exist_ok=True)


    plt.figure()
    df["Warehouse_block"].value_counts().plot(kind="bar")
    plt.title("Shipments per Warehouse")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()


    plt.figure()
    df["Mode_of_Shipment"].value_counts().plot(kind="bar")
    plt.title("Mode of Shipment")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    plt.figure()
    plt.scatter(df["Cost_of_the_Product"], df["Weight_in_gms"], s=5)
    plt.title("Cost vs Weight")
    plt.xlabel("Cost of Product")
    plt.ylabel("Weight (g)")
    plt.tight_layout()
    plt.savefig("docs/cost_vs_weight.png")
    plt.close()


    plt.figure()
    df["Customer_rating"].plot(kind="hist")
    plt.title("Average Customer Rating")
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()


    plt.figure()
    df["Weight_in_gms"].plot(kind="hist")
    plt.title("Weight Distribution")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()


    html = """
    <html><body>
        <h1>Dashboard</h1>
        <img src='shipping_per_warehouse.png'><br>
        <img src='mode_of_shipment.png'><br>
        <img src='cost_vs_weight.png'><br>
        <img src='average_customer_rating.png'><br>
        <img src='weight_distribution.png'><br>
    </body></html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)


