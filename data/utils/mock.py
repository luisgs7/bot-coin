"""Data Mock"""

DATA_MOCK = {
    "currencies": {
        "source": "BRL",
        "USD": {"name": "Dollar", "buy": 5.1567, "sell": 5.1581, "variation": -1.112},
        "EUR": {"name": "Euro", "buy": 5.182, "sell": 5.1834, "variation": -0.602},
        "GBP": {
            "name": "Pound Sterling",
            "buy": 5.978,
            "sell": None,
            "variation": -0.351,
        },
        "ARS": {
            "name": "Argentine Peso",
            "buy": 0.0365,
            "sell": None,
            "variation": -1.121,
        },
        "CAD": {
            "name": "Canadian Dollar",
            "buy": 3.9571,
            "sell": None,
            "variation": -0.664,
        },
        "AUD": {
            "name": "Australian Dollar",
            "buy": 3.5299,
            "sell": None,
            "variation": 0.293,
        },
        "JPY": {
            "name": "Japanese Yen",
            "buy": 0.0362,
            "sell": None,
            "variation": -0.071,
        },
        "CNY": {"name": "Renminbi", "buy": 0.7445, "sell": None, "variation": -0.642},
        "BTC": {
            "name": "Bitcoin",
            "buy": 116657.057,
            "sell": 116657.057,
            "variation": 10.316,
        },
    },
    "stocks": {
        "IBOVESPA": {
            "name": "BM&F BOVESPA",
            "location": "Sao Paulo, Brazil",
            "points": 112499.07,
            "variation": 2.35,
        },
        "IFIX": {
            "name": "Índice de Fundos de Investimentos Imobiliários B3",
            "location": "Sao Paulo, Brazil",
            "points": 2978.25,
            "variation": 0.13,
        },
        "NASDAQ": {
            "name": "NASDAQ Stock Market",
            "location": "New York City, United States",
            "points": 12105.31,
            "variation": 2.05,
        },
        "DOWJONES": {
            "name": "Dow Jones Industrial Average",
            "location": "New York City, United States",
            "points": 32096.87,
            "variation": 1.01,
        },
        "CAC": {
            "name": "CAC 40",
            "location": "Paris, French",
            "points": 6212.33,
            "variation": 1.41,
        },
        "NIKKEI": {
            "name": "Nikkei 225",
            "location": "Tokyo, Japan",
            "points": 28214.75,
            "variation": 0.53,
        },
    },
    "available_sources": ["BRL"],
    "bitcoin": {
        "blockchain_info": {
            "name": "Blockchain.info",
            "format": ["USD", "en_US"],
            "last": 21311.58,
            "buy": 21311.58,
            "sell": 21311.58,
            "variation": 10.159,
        },
        "coinbase": {
            "name": "Coinbase",
            "format": ["USD", "en_US"],
            "last": 21346.85,
            "variation": 10.36,
        },
        "bitstamp": {
            "name": "BitStamp",
            "format": ["USD", "en_US"],
            "last": 21311.0,
            "buy": 21315.0,
            "sell": 21312.0,
            "variation": 10.134,
        },
        "foxbit": {
            "name": "FoxBit",
            "format": ["BRL", "pt_BR"],
            "last": 351098.91,
            "variation": -1.885,
        },
        "mercadobitcoin": {
            "name": "Mercado Bitcoin",
            "format": ["BRL", "pt_BR"],
            "last": 110395.03,
            "buy": 110196.28041,
            "sell": 110355.0,
            "variation": 9.175,
        },
    },
    "taxes": [
        {
            "date": "2022-09-06",
            "cdi": 13.75,
            "selic": 13.75,
            "daily_factor": 1.00050788,
            "selic_daily": 13.65,
            "cdi_daily": 13.65,
        }
    ],
}
