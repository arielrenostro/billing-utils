# Billing Utils

Simple Python project to help me to categorize my credit card billing.

## Nubank Bill Report

Usage:
```shell
python nubank-bill-report/main.py {report.csv}
```

Output:
```table
+------------+------------------------------------+---------+--------------+
|    Date    | Description                        |   Value | Category     |
+------------+------------------------------------+---------+--------------+
| 07/10/2024 | Mercadolivre*3produto              |  101.98 | Verificar    |
| 08/10/2024 | Mercadolivre*5produto              |  129.52 | Verificar    |
| 08/10/2024 | Panvel Farmacias                   |  131.85 | Verificar    |
| 08/10/2024 | Mercadolivre*5produto              |   16.11 | Verificar    |
| 14/10/2024 | Mercadolivre*Guitroni              |   38.99 | Verificar    |
| 15/10/2024 | Mercadolivre*3produto              |   12.88 | Verificar    |
| 15/10/2024 | Mercadolivre*3produto              |   53.57 | Verificar    |
| 01/11/2024 | Madeiro Neumarkt                   |  107.25 | Verificar    |
| 02/10/2024 | Giassi Farmacia                    |  155.26 | Desconhecido |
| 03/10/2024 | Raia2785                           |   37.28 | Desconhecido |
| 08/10/2024 | Estorno de "Mercadolivre*3produto" | -101.98 | Desconhecido |
| 11/10/2024 | Caroline Salvador                  |   50.00 | Desconhecido |
| 12/10/2024 | Safe Park Maxi Flora               |   12.00 | Desconhecido |
| 13/10/2024 | sem Parar                          |  250.00 | Desconhecido |
| 13/10/2024 | Galo Ko                            |   12.99 | Desconhecido |
| 19/10/2024 | Oliv Restaurante                   |  363.33 | Desconhecido |
| 30/10/2024 | Ccg Farmacia e Drogari             |   28.64 | Desconhecido |
| 07/10/2024 | Paypal *Vibra                      |  317.17 | Carro        |
| 08/10/2024 | Posto Almirante                    |  302.83 | Carro        |
| 20/10/2024 | Posto Almirante                    |    3.00 | Carro        |
| 20/10/2024 | Posto Almirante                    |  119.04 | Carro        |
| 22/10/2024 | Paypal *Shellbox                   |  288.78 | Carro        |
| 21/10/2024 | Paygo*Kenko                        |  113.70 | Delivery     |
| 14/10/2024 | Mp *Melimais                       |   27.99 | Contas casa  |
| 16/10/2024 | Telecom Unif*Unifique              |  149.90 | Contas casa  |
+------------+------------------------------------+---------+--------------+
```
