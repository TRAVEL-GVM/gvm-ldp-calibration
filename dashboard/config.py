# Primary Colors (Dark to light green shades)
PRIMARY_COLORS = ["#2e7d32", "#43a047", "#66bb6a", "#a5d6a7"]

# Secondary Colors (Alternative green shades)
SECONDARY_COLORS = ["#388e3c", "#4caf50", "#81c784", "#c8e6c9"]

# Neutral Colors (Very light to medium green)
NEUTRAL_COLORS = ["#e8f5e9", "#c8e6c9", "#a5d6a7", "#81c784"]

# Accent Colors (Lime green shades)
ACCENT_COLORS = ["#689f38", "#8bc34a", "#aed581", "#dcedc8"]

# Extended Colors (For charts with many series)
EXTENDED_COLORS = ["#5d4037", "#8d6e63", "#0277bd", "#039be5", "#7b1fa2", "#9c27b0", "#ef6c00", "#f57c00"]

# Text Colors (Very dark to medium green for text)
TEXT_COLORS = ["#1b5e20", "#2e7d32", "#388e3c", "#43a047"]

# Background Colors (Very light green to white)
BACKGROUND_COLORS = ["#e8f5e9", "#f1f8e9", "#f9fbe7", "#ffffff"]

# Chart Colors (Main colors for visualizations with expanded options for multiple series)
CHART_COLORS = [
    PRIMARY_COLORS[0],
    SECONDARY_COLORS[0],
    ACCENT_COLORS[0],
    EXTENDED_COLORS[0],
    EXTENDED_COLORS[2],
    PRIMARY_COLORS[1],
    SECONDARY_COLORS[1],
    ACCENT_COLORS[1],
    EXTENDED_COLORS[1],
    EXTENDED_COLORS[3],
    EXTENDED_COLORS[4],
    EXTENDED_COLORS[6],
]

# Satisfaction Color Scale (Matching design doc exactly)
SATISFACTION_COLORS = {
    "Very Satisfied": "#179297",  # Dark green
    "Satisfied": "#66bb6a",  # Medium green
    "Neutral": "#ffeb3b",  # Yellow
    "Dissatisfied": "#ff9800",  # Orange
    "Very Dissatisfied": "#f44336",  # Red
}

# Housing Situation Colors (Using primary and accent colors)
HOUSING_COLORS = {
    "Arrendamento": PRIMARY_COLORS[0],  # Dark green
    "Casa Própria": SECONDARY_COLORS[0],  # Alternative green
    "Others": ACCENT_COLORS[0],  # Lime green
}

# Rent Burden Colors (Using a green to red gradient)
RENT_BURDEN_COLORS = {
    "≤30% (Affordable)": PRIMARY_COLORS[0],  # Dark green
    "31-50% (Moderate)": "#ffeb3b",  # Yellow
    "51-80% (High)": "#ff9800",  # Orange
    ">80% (Very High)": "#f44336",  # Red
    "Unknown": "#cccccc",  # Gray
}

# Color scales for different visualization types
COLOR_SCALES = {
    "sequential": [
        "#e8f5e9",
        "#c8e6c9",
        "#81c784",
        "#4caf50",
        "#2e7d32",
    ],  # Light to dark green
    "diverging": [
        "#f44336",
        "#ffeb3b",
        "#ffffff",
        "#66bb6a",
        "#2e7d32",
    ],  # Red to green
    "qualitative": [
        PRIMARY_COLORS[0],
        SECONDARY_COLORS[0],
        ACCENT_COLORS[0],
        EXTENDED_COLORS[2],
        EXTENDED_COLORS[4],
        EXTENDED_COLORS[6],
        PRIMARY_COLORS[1],
        SECONDARY_COLORS[1],
    ],  # Mix of color families
}

# Additional color combinations for specific visualizations
VISUALIZATION_COLORS = {
    "heatmap": "RdYlGn",  # Red-Yellow-Green colorscale
    "choropleth": "Greens",  # Green sequential colorscale
    "density": "Viridis",  # Default density colorscale
    "correlation": "RdBu",  # Red-Blue diverging colorscale
}


# https://bpstat.bportugal.pt/conteudos/quadros/1895

MAP_INDICATORS_METRICS = {
    "Autonomia Financeira": "%", "Financiamentos obtidos em percentagem do passivo": "%",
    "Custo dos financiamentos obtidos": "%", "VAB em percentagem da produção": "%",
    "Rendibilidade do ativo": "%", "Rendibilidade bruta dos capitais investidos": "%",
    "Cobertura dos gastos de financiamento": "Número", "Financiamentos obtidos em percentagem do ativo": "%",
    "Margem EBITDA em percentagem dos rendimentos": "%", "Rácio dos financiamentos obtidos sobre EBITDA": "Número",
    "Rendibilidade dos capitais próprios": "%", "Margem líquida em percentagem dos rendimentos": "%",
    "Capital próprio em percentagem do ativo": "%", "Liquidez geral": "%",
    "Margem bruta em percentagem dos rendimentos": "%", "Margem EBT em percentagem dos rendimentos": "%",
    "EBIT em percentagem do volume de negócios": "%", "Pressão financeira (Gastos de financiamento/EBITDA)": "%",
                          }


MEDIUM_ENTREPRISE_MAP_INDICATORS_KEYS = {
    "Autonomia Financeira": [12606603, 12626412, 12624219, 12615393, 12615893, 12613821,
            12593161, 12594593, 12609645, 12599760, 12594590, 12617758,
            12619173, 12598452, 12603026, 12593876, 12615662, 12605410],

    "Financiamentos obtidos em percentagem do passivo": [12588157, 12592900, 12611362, 12605698, 12616503, 12606153,
            12605683, 12623702, 12604657, 12603331, 12623253, 12630314,
            12612970, 12597354, 12590285, 12628627, 12629789, 12628715],

    "Custo dos financiamentos obtidos": [12612335, 12593500, 12608896, 12610840, 12596431, 12609405,
            12609493, 12590734, 12613387, 12614671, 12625006, 12609796,
            12608103, 12589334, 12587379, 12611131, 12623354, 12621660],

    "VAB em percentagem da produção": [12612589, 12612811, 12628208, 12620257, 12615236, 12612453,
            12628898, 12620057, 12597218, 12608368, 12627614, 12626589,
            12598081, 12626502, 12615835, 12598947, 12618903, 12624877],

    "Rendibilidade do ativo": [12607495, 12611290, 12612702, 12621539, 12593614, 12602954,
            12625639, 12601661, 12616424, 12617481, 12627572, 12613718,
            12597571, 12605675, 12622917, 12596501, 12608016, 12607110],

    "Rendibilidade bruta dos capitais investidos": [12623316, 12626582, 12607534, 12630050, 12594927, 12592064,
            12601321, 12609691, 12622392, 12611607, 12630124, 12610844,
            12614550, 12605483, 12598656, 12610608, 12621468, 12593266],

    "Cobertura dos gastos de financiamento": [12589560, 12590165, 12610993, 12596442, 12613398, 12630460,
            12625687, 12613530, 12597495, 12602769, 12622837, 12626607,
            12600650, 12613727, 12614024, 12599360, 12620024, 12622504],

    "Financiamentos obtidos em percentagem do ativo": [12618225, 12626771, 12594675, 12604367, 12600164, 12604023,
            12621221, 12617466, 12619655, 12604700, 12599784, 12602795,
            12630494, 12593336, 12601120, 12592977, 12629990, 12611805],

    "Margem EBITDA em percentagem dos rendimentos": [12607587, 12591042, 12602639, 12608438, 12626520, 12599617,
            12626541, 12623286, 12620620, 12601451, 12600978, 12615311,
            12593162, 12626480, 12602789, 12629066, 12610509, 12600162],

    "Rácio dos financiamentos obtidos sobre EBITDA": [12614436, 12599137, 12629039, 12609464, 12596422, 12607832,
            12621865, 12598899, 12623280, 12606129, 12603571, 12610001,
            12621742, 12588713, 12590354, 12617296, 12615069, 12607896],

    "Rendibilidade dos capitais próprios": [12595790, 12610787, 12614334, 12614277, 12630825, 12596754,
            12625046, 12594622, 12614836, 12607448, 12618716, 12627986,
            12601550, 12601732, 12627243, 12597557, 12610656, 12591462],

    "Margem líquida em percentagem dos rendimentos": [12594340, 12612743, 12594823, 12587798, 12617832, 12587716,
            12597214, 12624349, 12620651, 12604731, 12615522, 12616930,
            12598506, 12630224, 12612716, 12608678, 12618689, 12601245],

    "Capital próprio em percentagem do ativo": [12632138, 12632446, 12632099, 12632471, 12632410, 12632083,
            12632360, 12632375, 12632348, 12632255, 12632439, 12632168,
            12632502, 12632495, 12632142, 12632340, 12632111, 12632144],


    "Margem bruta em percentagem dos rendimentos": [12589512, 12614265, 12610611, 12628996, 12626627, 12603996,
            12624913, 12630172, 12589979, 12629045, 12589172, 12620524,
            12628135, 12604362, 12611027, 12594812, 12599913, 12630584],

    "Margem EBIT em percentagem dos rendimentos": [12596080, 12615969, 12607929, 12628128, 12607649, 12612604,
            12609360, 12616211, 12611759, 12610271, 12627495, 12604667,
            12621473, 12590914, 12607577, 12600795, 12619274, 12621406],

    "EBIT em percentagem do volume de negócios": [12598363, 12603493, 12621647, 12613063, 12603800, 12590596,
            12613955, 12614408, 12605133, 12626108, 12590520, 12627374,
            12617045, 12627545, 12601765, 12611341, 12604183, 12609638],

    "Pressão financeira (Gastos de financiamento/EBITDA)": [12617161, 12611543, 12602482, 12622145, 12611802, 12624386,
            12617223, 12630256, 12627205, 12594207, 12619703, 12625363,
            12626687, 12618561, 12620696, 12620907, 12604412, 12600841] ,

    "Liquidez geral": [12623026, 12588216, 12613258, 12611402, 12595465, 12596457,
            12590666, 12624134, 12590811, 12625238, 12628013, 12593728,
            12597459, 12613803, 12608407, 12623434, 12623066, 12605761]
                          }


indicadores_ecb = {

    "GDP and expenditure components": {
        "Private final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1M.S1.D.P31._Z._Z._T.XDC.LR.GY",
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
        "Government final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S13.S1.D.P3._Z._Z._T.XDC.LR.GY",
        "Imports of goods and service": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.C.P7._Z._Z._Z.XDC.LR.GY",
        "Exports of goods and services": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.D.P6._Z._Z._Z.XDC.LR.GY",
        "Gross domestic product at market prices": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W2.S1.S1.B.B1GQ._Z._Z._Z.XDC_R_B1GQ.Y.GOY",
    },

    "Corporations": {
        "Net value added of Non financial corporations (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B1N._Z._Z._Z.XDC._T.S.V.GY._T",
        "Gross entrepreneurial income of Non financial corporations": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B4G._Z._Z._Z.XDC_R_B1G._T.S.V.N._T",
        "Debt securities and loans of Non financial corporations as a ratio of GDP": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.C.L.LE.F3T4.T._Z.XDC_R_B1GQ_CY._T.S.V.N._T",
        "Debt of Non financial corporations as a ratio of total financial liabilities": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.LE.FPT.T._Z.XDC_R_F._T.S.V.N._T",
        "Total financial assets of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.D.P51G._Z._Z._Z.XDC_R_B1G_CY._T.S.V.N._T"
    },

    "Households": {
        "Loans granted to households as a ratio of gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.LE.F4.T._Z.XDC_R_B6G_CY._T.S.V.N._T",
        "Gross saving of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B8G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Gross disposable income of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.GY._T",
        "Total financial assets of households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Loans granted to households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.F.F4.T._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P51G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Final consumption expenditure of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P3._Z._Z._Z.XDC._T.S.V.GY._T"
    },

    "Government finance statistics": {
        "Government deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government primary deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9P._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government debt (consolidated) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T"
    },

    "Labour market indicators": {
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
    }
}

# 
MAP_CATEGORIES_ECB_INDICADORS_URLS = {

    "GDP and expenditure components": {
        "Private final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1M.S1.D.P31._Z._Z._T.XDC.LR.GY",
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
        "Government final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S13.S1.D.P3._Z._Z._T.XDC.LR.GY",
        "Imports of goods and service": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.C.P7._Z._Z._Z.XDC.LR.GY",
        "Exports of goods and services": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.D.P6._Z._Z._Z.XDC.LR.GY",
        "Gross domestic product at market prices": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W2.S1.S1.B.B1GQ._Z._Z._Z.XDC_R_B1GQ.Y.GOY",
    },

    "Corporations": {
        "Net value added of Non financial corporations (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B1N._Z._Z._Z.XDC._T.S.V.GY._T",
        "Gross entrepreneurial income of Non financial corporations": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B4G._Z._Z._Z.XDC_R_B1G._T.S.V.N._T",
        "Debt securities and loans of Non financial corporations as a ratio of GDP": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.C.L.LE.F3T4.T._Z.XDC_R_B1GQ_CY._T.S.V.N._T",
        "Debt of Non financial corporations as a ratio of total financial liabilities": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.LE.FPT.T._Z.XDC_R_F._T.S.V.N._T",
        "Total financial assets of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.D.P51G._Z._Z._Z.XDC_R_B1G_CY._T.S.V.N._T"
    },

    "Households": {
        "Loans granted to households as a ratio of gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.LE.F4.T._Z.XDC_R_B6G_CY._T.S.V.N._T",
        "Gross saving of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B8G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Gross disposable income of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.GY._T",
        "Total financial assets of households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Loans granted to households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.F.F4.T._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P51G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Final consumption expenditure of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P3._Z._Z._Z.XDC._T.S.V.GY._T"
    },

    "Government finance statistics": {
        "Government deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government primary deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9P._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government debt (consolidated) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T"
    },

    "Labour market indicators": {
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
    }
}


MAP_CATEGORIES_ECB_INDICADORS = {

    "GDP and expenditure components": [
        "Private final consumption", "Government final consumption",
        "Imports of goods and service", "Exports of goods and services", "Gross domestic product at market prices"
    ],

    "Corporations": [
        "Net value added of Non financial corporations (growth rate)",
        "Gross entrepreneurial income of Non financial corporations",
        "Debt securities and loans of Non financial corporations as a ratio of GDP",
        "Debt of Non financial corporations as a ratio of total financial liabilities",
        "Total financial assets of Non financial corporations as a ratio of total financial assets",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added"
    ],

    "Households": [
        "Loans granted to households as a ratio of gross disposable income",
        "Gross saving of households as a ratio of adjusted gross disposable income",
        "Gross disposable income of households (growth rate)",
        "Total financial assets of households as a ratio of total financial assets",
        "Loans granted to households as a ratio of total financial assets",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income",
        "Final consumption expenditure of households (growth rate)"
        ],

    "Government finance statistics": [
        "Government deficit(-) or surplus(+) (as % of GDP)",
        "Government primary deficit(-) or surplus(+) (as % of GDP)",
        "Government debt (consolidated) (as % of GDP)"],

}

MAP_OTHER_BPSTAT_INDICATORS = {
    "CPI (Consumer Price Index) MA12": {
        'url': 5721550
        }
    }

MAP_OTHER_ECB_INDICATORS = {
        "Unemployment rate":{
            'periodicity': "Monthly",
            'url': "https://data.ecb.europa.eu/data/datasets/LFSI/LFSI.M.PT.S.UNEHRT.TOTAL0.15_74.T"
            },
        "Labour Productivity (per persons)": {
            'url': "https://data.ecb.europa.eu/data/datasets/MNA/MNA.Q.S.PT.W0.S1.S1._Z.LPR_PS._Z._T._Z.XDC.LR.GY",
            'periodicity': "Quarterly"
            }
    }


ldp_sectors = ['All', 'Agricult & fishing', 'Mining and quarrying', 'Manufacturing', 'Electricity and gas', 'Water and waste',
               'Construction', 'Trade', 'Transport and storage', 'Hotels and similar', 'Information and communication', 'Real estate', 
               'Administrative activities', 'Education', 'Health and social', 'Shows and sports', 'Professional and scientific']

medium_all_columns = ['Date', 
       'Capital ratio-Medium-%',
       'Financial debt (% liabilities)-Medium',
       'Cost of financial debt-Medium-%',
       'GVA (% output)-Medium',
       'Return on assets-Medium-%',
       'EBITDA / invested capital-Medium-%',
       'Financing expenses coverage ratio-Medium',
       'Financial debt (% assets)-Medium',
       'EBITDA margin (% income)-Medium',
       'Financial debt over EBITDA-Medium',
       'Return on equity-Medium-%',
       'Net income (% income)-Medium',
       'Equity (% assets)-Medium',
       'Gross profit (% income)-Medium',
       'EBIT margin (% income)-Medium',
       'EBITDA (% turnover )-Medium',
       'Financial pressure-Medium-%',
       'Current ratio-Medium-%']


container_style_html = """
    <style>
        .gpt-container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .gpt-button {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border: none;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 0;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .gpt-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            background: linear-gradient(135deg, #5e7cea, #9d68e1);
        }
        .gpt-textarea {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 15px;
            font-size: 16px;
        }
        .gpt-toggle {
            margin: 15px 0;
        }
        .gpt-response {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            border-left: 5px solid #6e8efb;
        }
    </style>"""
