first_installment = 'Parcela 1\/'
not_first_installment = 'Parcela (?!1\/)[0-9]*\/'
refund_regex = 'Estorno de "(.+)"'

first_installment_regex = '^.+ - Parcela 0*1\/[0-9]+$'
has_installment_regex = '^.+ - Parcela [0-9]+\/[0-9]+$'

categories_to_ignore = {'Pessoal', 'Reembolso', 'Reembolso automático', 'Parcela', 'Ignorado'}

nubank_date_col_idx = 0
nubank_desc_col_idx = 1
nubank_value_col_idx = 2
nubank_csv_header = ['date','title','amount']

nubank_categories_by_place = {
  "Pg *Foco Radical": 'Pessoal',
  "Giassi Supermercados": 'Mercado',
  "Pg *Ton Sorveteria C": 'Verificar',
  "Cafe Cultura": 'Verificar',
  "regexp:^Ifd\\*.*": 'Delivery',
  "Super Imperatriz": 'Mercado',
  "Baogui": 'Delivery',
  "Google Tinder": 'Pessoal',
  "Paypal *Shellbox": 'Carro',
  "Apple.Com/Bill": 'Pessoal',
  "Amazon": 'Verificar',
  "Google Youtube Member": 'Pessoal',
  "Cooper Filial Vila Nov": 'Mercado',
  "Posto Almirante": 'Carro',
  "Pinballspace": 'Verificar',
  "Posto Ilha Bela": 'Carro',
  "Cooper Filial Itoupava": 'Mercado',
  "IOF de \"Paypal *Crunchyroll\"": 'Pessoal',
  "Recarga de celular": 'Pessoal',
  "Paypal *Crunchyroll": 'Pessoal',
  "Airbnb * Hm3z2a8wyp": 'Verificar',
  "Crunch Mama Paes e Piz": 'Delivery',
  "Bacio Di Latte-Lj3008": 'Reembolso',
  "Estacionamento Catedra": 'Reembolso',
  "Google Youtubepremium": 'Pessoal',
  "Mp *Hbomaxassin": 'Contas casa',
  "Telecom Unif*Unifique": 'Contas casa',
  "Rei do Mate Aeroporto": 'Reembolso',
  "Uber* Trip": 'Verificar',
  "Rede de Postos R4": 'Carro',
  "Mp *Melimais": 'Contas casa',
  "Hoepers Auto Mecanica": 'Carro',
  "Panvel Farmacias": 'Verificar',
  "Saldo restante da fatura anterior": 'Ignorado',
  "Pagamento recebido": "Ignorado",
  "Nubank - Tarifa de assinatura": 'Pessoal',
  "Claro Flex": 'Reembolso automático',
  "Cappta *Evandro Marcel": 'Delivery',
  "Auto Posto Br H": 'Carro',
  "Pag*Renner": 'Verificar',
  "Bokas": 'Delivery',
  "Azul Seguro Auto": 'Pessoal',
  "Farmacia Vila Nova Blu": 'Verificar',
  "Nubank Celular Seguro": 'Pessoal',
  'Porao Comedy': 'Viagem',
  'Choperiabiervila': 'Delivery',
  'Portus Artesanal': 'Delivery',
  'Mini Kalzone Neumarkt': 'Delivery',
  'Dva Pneus': 'Carro',
  'Paygo*Kenko': 'Delivery',
  'Paypal *Vibra': 'Carro',
  "Aliexpress": 'Verificar',
  "regexp:^Ebn\\*Cambly.*": 'Pessoal',
  "regexp:^Pag\\*Steam.*": 'Pessoal',
  "regexp:^App\\*Muscleboss.*": 'Verificar',
  "regexp:^Sportime Comercio de.*": 'Pessoal',
  "regexp:^Via Laser S e L.*": 'Pessoal',
  "regexp:^Oticas Carol.*": 'Pessoal',
  "regexp:^Mercadolivre\\*.+": 'Verificar',
  'Madeiro Neumarkt': 'Verificar',
  'Café Frente Vila': 'Delivery',
}

nubank_categories_translate = {
    'Blumenausthshp': 'Madeiro Neumarkt',
    'Dorapanltda': 'Café Frente Vila',
}