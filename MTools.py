def Regionalizacion(R):
    Regiones = {
    'ARICA': 'Región de Arica y Parinacota',
    'TARAP':'Región de Tarapacá',
    'ANTO':'Región de Antofagasta',
    'ATAC':'Región de Atacama',
    'COQ':'Región de Coquimbo',
    'VALP':'Región de Valparaíso',
    'SANTI':'Región Metropolitana de Santiago',
    'METRO':'Región Metropolitana de Santiago',
    "HIG":"Región del Libertador General Bernardo O'Higgins",
    'MAUL':'Región del Maule',
    'ÑUB':'Región de Ñuble',
    'BIOB':'Región del Biobío',
    'BÍOB':'Región del Biobío',
    'ARAU':'Región de La Araucanía',
    'LOS R':'Región de Los Ríos',
    'LAGOS':'Región de Los Lagos',
    'AYS':'Región de Aysén del General Carlos Ibáñez del Campo',
    'MAGA':'Región de Magallanes y de la Antártica Chilena'}

    K = list(Regiones.keys())

    L = list(zip([m in R for m in K], K))

    return Regiones.get([x[1] for x in L if x[0]][0])


def Comunizador(comuna):
    comuna = str(comuna)
    comuna = comuna.upper().replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U').strip()
    
    L_comunas = ['FUTALEUFU', 'QUIRIHUE', 'LOS ANDES', 'CURANILAHUE', 'PETORCA', 'TALCA', 'CHILLAN', 'CHANCO', 'PADRE LAS CASAS', 'LO PRADO', 'MACHALI',
     'CHAÑARAL', 'NEGRETE', 'SAN BERNARDO', 'LAGO RANCO', 'ALTO HOSPICIO', 'LLANQUIHUE', 'CALDERA', 'PAPUDO', 'LOS VILOS', 'PELARCO', 'VILLARRICA',
     'PUNTA ARENAS', 'FUTRONO', 'JUAN FERNANDEZ', 'PELLUHUE', 'ANTARTICA', 'TALAGANTE',
     'COLCHANE', 'PAILLACO', 'MARIQUINA', 'SANTIAGO', 'CODEGUA', 'ALTO DEL CARMEN', 'INDEPENDENCIA', 'CAÑETE', 'OVALLE', 'GRANEROS', 'BUIN',
     'ÑUÑOA', "O'HIGGINS", 'ROMERAL', 'SAN RAFAEL', 'SAN PEDRO', 'COCHAMO', 'RIO NEGRO', 'PADRE HURTADO', 'PUCON', 'CASABLANCA', 'SAGRADA FAMILIA',
     'PUCHUNCAVI', 'EL CARMEN', 'POZO ALMONTE', 'VALPARAISO', 'YERBAS BUENAS', 'ALTO BIOBIO', 'RANQUIL', 'RENCA', 'CHAITEN', 'RANCAGUA', 'CURACO DE VELEZ',
     'LO BARNECHEA', 'LONQUIMAY', 'MOSTAZAL', 'VILLA ALEGRE', 'TENO', 'FREIRE', 'SAN PABLO', 'SAN JAVIER', 'FRUTILLAR', 'LIMACHE', 'QUINTERO',
     'CORONEL', 'DOÑIHUE', 'PAREDONES', 'MAFIL', 'QUEMCHI', 'ESTACION CENTRAL', 'OLLAGÜE', 'RIO CLARO', 'CABO DE HORNOS', 'FREIRINA', 'TIRUA',
     'AYSEN', 'REQUINOA', 'LICANTEN', 'RECOLETA', 'CAUQUENES', 'CURACAVI', 'VILCUN', 'SANTA MARIA', 'GUAITECAS', 'PANGUIPULLI', 'CORRAL', 'LONGAVI',
     'PUMANQUE', 'PALENA', 'MULCHEN', 'LOS ALAMOS', 'SAN MIGUEL', 'YUNGAY', 'MARCHIHUE', 'MELIPEUCO', 'LA CRUZ', 'TOCOPILLA', 'ERCILLA', 'LITUECHE', 'HUALQUI',
     'COINCO', 'COBQUECURA', 'SAN FABIAN', 'LA REINA', 'CALBUCO', 'MELIPILLA', 'PUNITAQUI', 'COLTAUCO', 'RIO BUENO', 'HIJUELAS', 'SAN JUAN DE LA COSTA', 'COELEMU',
     'CHILLAN VIEJO', 'PARRAL', 'CERRO NAVIA', 'IQUIQUE', 'NANCAGUA', 'VIÑA DEL MAR', 'LAUTARO', 'ANTUCO', 'OLMUE', 'PORTEZUELO', 'VICUÑA', 'SAN VICENTE', 'VALDIVIA',
     'CURARREHUE', 'COLLIPULLI', 'CERRILLOS', 'CONSTITUCION', 'QUILICURA', 'MONTE PATRIA', 'ÑIQUEN', 'NOGALES', 'SAN FELIPE', 'TUCAPEL', 'PERALILLO', 'QUILLECO', 'COIHUECO',
     'EL BOSQUE', 'COPIAPO', 'TALTAL', 'SIERRA GORDA', 'CONCEPCION', 'TEMUCO', 'TRAIGUEN', 'NINHUE', 'SAN PEDRO DE LA PAZ', 'COCHRANE', 'LAGUNA BLANCA', 'LOS MUERMOS',
     'ARAUCO', 'PICHILEMU', 'MARIA PINTO', 'MARIA ELENA', 'PENCAHUE', 'PITRUFQUEN', 'PENCO', 'NAVIDAD', 'ALGARROBO', 'OSORNO', 'LA GRANJA', 'TEODORO SCHMIDT', 'NACIMIENTO',
     'VALLENAR', 'SAN PEDRO DE ATACAMA', 'PEUMO', 'CHIMBARONGO', 'RENGO', 'COMBARBALA', 'TREGUACO', 'PUERTO VARAS', 'HUALAIHUE', 'PROVIDENCIA', 'LAMPA', 'CAMIÑA', 'MALLOA',
     'PANQUEHUE', 'PERQUENCO', 'SANTA JUANA', 'PEMUCO', 'RAUCO', 'SAN NICOLAS', 'PUENTE ALTO', 'CONTULMO', 'LOS LAGOS', 'CURICO', 'LUMACO', 'QUEILEN', 'SAN JOSE DE MAIPO',
     'LA LIGUA', 'QUILLOTA', 'HUALAÑE', 'LANCO', 'SANTO DOMINGO', 'ALHUE', 'BULNES', 'NUEVA IMPERIAL', 'SAN CLEMENTE', 'CARTAGENA', 'ZAPALLAR', 'GALVARINO', 'LOLOL', 'PEÑAFLOR',
     'LA SERENA', 'SANTA CRUZ', 'QUILLON', 'PORVENIR', 'HUECHURABA', 'SANTA BARBARA', 'CASTRO', 'PUYEHUE', 'CALERA DE TANGO', 'CUREPTO', 'RINCONADA', 'LA FLORIDA', 'CATEMU',
     'RENAICO', 'ILLAPEL', 'NATALES', 'SAN CARLOS', 'ARICA', 'CHOLCHOL', 'VILLA ALEMANA', 'LA PINTANA', 'MAULE', 'LA UNION', 'PIRQUE', 'COLBUN', 'LA HIGUERA', 'LONCOCHE',
     'PUQUELDON', 'RIO IBAÑEZ', 'CABRERO', 'HUALPEN', 'LOTA', 'GENERAL LAGOS', 'TORTEL', 'VICTORIA', 'TALCAHUANO', 'CAMARONES', 'PUTRE', 'CHIGUAYANTE', 'QUINCHAO', 'PLACILLA',
     'FLORIDA', 'CONCHALI', 'LO ESPEJO', 'SALAMANCA', 'SAN ESTEBAN', 'QUINTA NORMAL', 'LAJA', 'PAIHUANO', 'SAN RAMON', 'CALLE LARGA', 'ANGOL', 'LEBU', 'PUREN', 'MACUL', 'TIMAUKEL',
     'SAN ANTONIO', 'HUARA', 'EL TABO', 'RETIRO', 'PRIMAVERA', 'MAULLIN', 'PUERTO OCTAY', 'PUDAHUEL', 'PEDRO AGUIRRE CERDA', 'ISLA DE PASCUA', 'RIO VERDE', 'LOS SAUCES', 'HUASCO',
     'LINARES', 'MOLINA', 'SAN GREGORIO', 'ANDACOLLO', 'PICHIDEGUA', 'ANTOFAGASTA', 'QUINTA DE TILCOCO', 'PUTAENDO', 'QUILPUE', 'EL QUISCO', 'CHONCHI', 'CABILDO', 'LA ESTRELLA',
     'EL MONTE', 'FRESIA', 'RIO HURTADO', 'CHEPICA', 'ISLA DE MAIPO', 'PAINE', 'LOS ANGELES', 'SAN ROSENDO', 'GORBEA', 'QUILACO', 'COQUIMBO', 'CUNCO', 'LAGO VERDE', 'PICA',
     'MAIPU', 'LAS CABRAS', 'VITACURA', 'SAN JOAQUIN', 'SAN FERNANDO', 'PUERTO MONTT', 'LAS CONDES', 'COYHAIQUE', 'PURRANQUE', 'DALCAHUE', 'YUMBEL', 'PINTO', 'DIEGO DE ALMAGRO',
     'TOME', 'LA CALERA', 'OLIVAR', 'CISNES', 'SAAVEDRA', 'PEÑALOLEN', 'CHILE CHICO', 'CARAHUE', 'CURACAUTIN', 'TOLTEN', 'LLAY-LLAY', 'COLINA', 'TIL TIL', 'CALAMA', 'LA CISTERNA', 
     'CONCON', 'ANCUD', 'QUELLON', 'TORRES DEL PAINE', 'EMPEDRADO', 'TIERRA AMARILLA', 'VICHUQUEN', 'SAN IGNACIO', 'MEJILLONES', 'PALMILLA', 'CANELA']
    
    return comuna in L_comunas
    
    
def reco_open(File):
    import pandas as pd
    
    Hojas = pd.ExcelFile(File).sheet_names
    
    # Import hoja ReconA
    
    recoa = pd.read_excel('RECO.xlsx', sheet_name = Hojas[0])

    recoa_cols = ['REGION CONTROL FRONTERIZO','AVANZADA O LUGAR DONDE SE MATERIALIZÓ LA RECONDUCCIÓN ','FECHA DE LA RECONDUCCIÓN DEL INDIVIDUO',
                  'AUTORIDAD QUE SORPRENDE EL INTENTO DE INGRESO AL PAÍS','NACIONALIDAD', 'SEXO ','EDAD', 'SITUACIÓN EXTRANJERO ']

    ['region', 'avanzada', 'fecha', 'autoridad', 'nacionalidad', 'sexo', 'edad', 'situacion']
    
    recoa = recoa[recoa_cols]

    recoa['grupo'] = 'Adulto'

    recoa.columns = ['region', 'avanzada', 'fecha', 'autoridad', 'nacionalidad', 'sexo', 'edad', 'situacion', 'grupo']
    
    # Import hoja RecoNNA
    
    reconna = pd.read_excel('RECO.xlsx', sheet_name = Hojas[1])

    reconna = reconna[['REGION','AVANZADA', 'FECHA','NACIONALIDAD', 'SEXO ', 'EDAD ']]

    reconna['situacion'] = 'RECONDUCCIÓN MATERIALIZADA'

    reconna['grupo'] = 'NNA'

    reconna['autoridad'] = 'NNA'

    reconna = reconna[['REGION', 'AVANZADA', 'FECHA', 'autoridad', 'NACIONALIDAD', 'SEXO ', 'EDAD ', 'situacion', 'grupo']]

    reconna.columns = ['region', 'avanzada', 'fecha', 'autoridad', 'nacionalidad', 'sexo', 'edad', 'situacion', 'grupo']
    
    # Import NoRecoA
    
    Noreco = pd.read_excel('RECO.xlsx', sheet_name = Hojas[2])


    Noreco_cols = ['REGION CONTROL FRONTERIZO','AVANZADA O LUGAR DONDE FUE SORPRENDIDO ',
                   'FECHA DEL INTENTO DE INGRESO AL PAÍS','AUTORIDAD QUE SORPRENDE EL INTENTO DE INGRESO AL PAÍS','NACIONALIDAD', 'SEXO ','EDAD ','SITUACIÓN EXTRANJERO ']

    Noreco = Noreco[Noreco_cols]

    Noreco['grupo'] = 'Adulto'

    Noreco.columns = ['region', 'avanzada', 'fecha', 'autoridad', 'nacionalidad', 'sexo', 'edad', 'situacion', 'grupo']
    
    # Import NoRecoNNA
    
    Noreconna = pd.read_excel('RECO.xlsx', sheet_name = Hojas[3])

    Noreconna_cols = ['REGION', 'AVANZADA EVADIDA','FECHA DEL HECHO', 'NACIONALIDAD (PAÍS)', 'SEXO ', 'EDAD ']

    Noreconna = Noreconna[Noreconna_cols]

    Noreconna['situacion'] = 'NO MATERIALIZADA'

    Noreconna['grupo'] = 'NNA'

    Noreconna['autoridad'] = 'NNA'

    Noreconna = Noreconna[['REGION', 'AVANZADA EVADIDA', 'FECHA DEL HECHO', 'autoridad', 'NACIONALIDAD (PAÍS)', 'SEXO ', 'EDAD ', 'situacion', 'grupo']]

    Noreconna.columns = ['region', 'avanzada', 'fecha', 'autoridad', 'nacionalidad', 'sexo', 'edad', 'situacion', 'grupo']
    
    # DF final
    
    df = pd.concat([recoa,reconna,Noreco,Noreconna])

    df['avanzada'] = df['avanzada'].str.replace('(AVANZADA|PASO)', '', regex = True).str.strip()
    #df['region'] = df['region'].str.replace('(REGIÓN\s*DE\s*)', '', regex = True).str.strip()
    df['sexo'] = df['sexo'].str.upper().str.strip()
    
    df['region'] = df['region'].apply(regiones)
    
    return df

def barPlot(df,X, Y, Umbral = 0.01, Otro = 'OTRA',
            Max_color = '#eb4034', Other_color = '#d4cadb',
            Title = 'Some Text:'):
  
  import pandas as pd
  import matplotlib.pyplot as plt
  
  _ = df
  T = _[Y].sum()
  Z = list(zip(_[X], [t/T for t in _[Y]]))
  Z = [z[0] if z[1] > Umbral else Otro for z in Z ]

  _['RECO'] = Z

  _['COLORS'] = [Other_color] * (len(_[X])-1) + [Max_color]

  fig, ax = plt.subplots()
  ax.barh(_['RECO'], _[Y], color = _['COLORS'])
  ax.set_title(Title)
  ax.set_ylabel(X)
  ax.set_xlabel(Y)
  
  return [_, fig]
