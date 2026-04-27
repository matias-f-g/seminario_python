"""This module is a quiz implemented in Streamlit about protected areas of Argentina."""

import streamlit as st
import random


# A dict with two elements: reserved_areas and national_parks_only
PROTECTED_AREAS = {'reserved_areas' : {'Costa Atlántica de Tierra del Fuego': 762166,
                                        'La Calera': 136225,
                                        'Paraná Guazú': 7541,
                                        'Ingeniero Barney': 500,
                                        'Pehuen Có - Monte Hermoso': 572244,
                                        'Islote de la Gaviota Cangrejera': 2925,
                                        'Arroyo Los Gauchos': 7413,
                                        'Manzano - Portillo de Piuquenes': 3152446,
                                        'Olaroz - Cauchari': 2073205,
                                        'Los Andes': 15248404,
                                        'Puerto Dalmacia': 3072,
                                        'Vicente López': 27,
                                        'Baterías - Charles Darwin': 10113,
                                        'Bahía Blanca, Bahía Falsa y Bahía Verde': 2563758,
                                        'Caverna de las Brujas': 1305,
                                        'Barranca Norte': 1054,
                                        'Chasicó': 78258,
                                        'Caleta de los Loros': 90786,
                                        'Punta Bermeja': 18968,
                                        'Restinga del Faro': 7062,
                                        'Mbotaby': 132,
                                        'Península de San Julián': 74177,
                                        'Isla de los Estados y Archipiélago de Año Nuevo': 502056,
                                        'Caleta Olivia': 1027,
                                        'Humedal Caleta Olivia': 2737,
                                        'Barco Hundido': 111322,
                                        'Nahuel Huapi': 2376718,
                                        'Cabo Blanco': 36568,
                                        'Ría de Puerto Deseado': 75554,
                                        'Península Valdés': 3913939,
                                        'Punta León': 3412,
                                        'Urugua-í': 31493,
                                        'La Humada': 60500,
                                        'Punta Loma': 16507,
                                        'Punta Buenos Aires': 80078,
                                        'Patagonia Azul': 30553073,
                                        'Punta Tombo': 2370,
                                        'Lago Puelo': 83516,
                                        'Cabo dos Bahías': 2579,
                                        'Monte Loayza': 76062,
                                        'Arroyo Zabala': 23786,
                                        'Bahía Laura': 51895,
                                        'Bahía San Blas': 5193196,
                                        'Isla Pingüinos': 1579355,
                                        'Embalse Casa de Piedra': 89439,
                                        'Santa María del Aguaray Miní': 236,
                                        'Tomo': 15097,
                                        'Cuartel Victoria': 4382,
                                        'El Paraíso': 4382,
                                        'Yaguaroundí': 4026,
                                        'Cerro Azul': 3846,
                                        'Julián Freaza': 6016,
                                        'Valle del Arroyo Cuñá Pirú': 54920,
                                        'Guardia del Juncal': 1304,
                                        'Limay Mahuida': 71735,
                                        'Parque Luro': 96772,
                                        'La Reforma': 82908,
                                        'Tupá Pojá': 446,
                                        'Estricta San Antonio': 4786,
                                        'Pereyra Iraola': 102958,
                                        'Rincón Nazarí': 49,
                                        'Alejandro Orloff - Saltitos': 2278,
                                        'Isla Martín García': 1935,
                                        'del Pilar': 2190,
                                        'Rincón de Santa María': 71378,
                                        'Laguna de Guatraché': 54620,
                                        'Arroyo El Durazno': 4433,
                                        'Lagunas de San Vicente': 7187,
                                        'Ñochilei-co': 247695,
                                        'Salitral Encantado': 968644,
                                        'Puerto Península': 83625,
                                        'Yabotí': 2294965,
                                        'San Guillermo': 9467763,
                                        'Alto Iguazu': 655,
                                        'Guaraní': 52155,
                                        'Laguna Salada Grande': 2859775,
                                        'Papel Misionero': 104807,
                                        'Isla Botija': 48267,
                                        'Bahía de Samborombón': 3990013,
                                        'Colonia Benítez': 75,
                                        'Pichi Mahuida': 70207,
                                        'Iguazú': 71884,
                                        'Corpus': 8731,
                                        'La Ponderosa': 1989,
                                        'Boca de la Laguna Herradura': 1146,
                                        'Estancia Santa Catalina': 10143,
                                        'Arroyo Ramírez': 1867,
                                        'Apipé Grande': 47436,
                                        'Lago del Desierto': 561950,
                                        'Laguna Negra': 13394,
                                        'Bosque Petrificado Ea. La Urbana': 320789,
                                        'Río Valdez': 27428,
                                        'El Gato y Lomas Limpias': 997755,
                                        'Escuela Rural Juan B. Alberdi': 150,
                                        'Laguna La Felipa': 12761,
                                        'Cerro Colorado': 28154,
                                        'La Quebrada': 42186,
                                        'Pampa de Achala': 1544801,
                                        'Chancaní': 50043,
                                        'Tucu - Tucu': 1824571,
                                        'Pinturas Rupestres Río Chalia o Shehuen': 132457,
                                        'Laguna Azul': 13034,
                                        'Meseta Espinosa y El Cordón': 2635015,
                                        'Laguna Hú': 14308,
                                        'Agua Dulce': 79300,
                                        'San Lorenzo': 213348,
                                        'Campo Garabato': 26548,
                                        'Aguas Chiquitas': 33448,
                                        'Islote Municipal': 163,
                                        'Quebrada del Portugués': 76903,
                                        'Laguna Brava': 798,
                                        'Playa Larga': 632,
                                        'La Pirámide': 67269,
                                        'Ciudad Universitaria - Costanera Norte': 219,
                                        'El Bagual': 32249,
                                        'San Justo': 140,
                                        'Isla de las Damas': 14345,
                                        'Laguna Nimez': 565,
                                        'Arroyo Saladillo': 1879966,
                                        'Arroyo Sauce-Pavón': 799576,
                                        'Federico Wildermuth': 16481,
                                        'Granja Esperanza': 654,
                                        'El Fisco': 15932,
                                        'Isleta Linda': 222381,
                                        'Potrero 7b': 20149,
                                        'La Loca': 21754,
                                        'La Ascensión': 145765,
                                        'Laguna La Salina': 36872,
                                        'Boca del Río Bermejo': 3458,
                                        'Piedra del Fraile': 44829,
                                        'Bañado la Estrella': 3732850,
                                        'Ascochinga': 33973,
                                        'Laguna Oca del Río Paraguay': 1014276,
                                        'Patagonia': 385440,
                                        'El Rincón': 150005,
                                        'Riacho Teuquito': 896943,
                                        'Estancia Ralicó': 152479,
                                        'Formosa': 89984,
                                        'La Angostura': 16717,
                                        'Los Sosa': 26998,
                                        'Meseta Lago Strobel': 121268,
                                        'Santa Ana': 172610,
                                        'Los Escarchados': 21036,
                                        'Punta Gruesa': 23171,
                                        'Aves Migratorias': 58548,
                                        'Monte León': 65516,
                                        'Salinas Grandes': 2220773,
                                        'Quebrada del Condorito': 108030,
                                        'Perito Moreno': 320022,
                                        'Los Glaciares': 1898269,
                                        'Corazón de la Isla': 1717655,
                                        'Isla del Cerrito': 121896,
                                        'Isla El Tala': 69292,
                                        'Don Carmelo': 399691,
                                        'Río Xibi - Xibi': 331,
                                        'de Barrancas': 16455,
                                        'Lote 5B Carabajal': 10995,
                                        'Batea Mahuida': 20428,
                                        'Ñacunán': 129486,
                                        'Los Palmares': 141779,
                                        'Auca Mahuida': 764364,
                                        'Bosque Petrificado Sarmiento': 18863,
                                        'Piedra Parada': 1310,
                                        'Castillos de Pincheira': 4697,
                                        'Telteca': 384324,
                                        'Ñacunán (Lote 11)': 79337,
                                        'Ñacunán (Lote 9)': 152453,
                                        'Sierra Pintada': 46313,
                                        'Punta Marqués': 966,
                                        'Lagunas de Epulafquen': 306566,
                                        'El Manzano Histórico': 9340,
                                        'Lagunas del Atuel': 1295899,
                                        'de la Quebrada de Cafayate': 953140,
                                        'Las Lancitas': 110828,
                                        'Laguna de Llancanelo': 889507,
                                        'Inversora Juramento': 126391,
                                        'Bosques Protectores': 18414,
                                        'Acambuco': 80995,
                                        'El Mangrullo': 87517,
                                        'Chañy': 49793,
                                        'Fracciones 50 y 51 del Lote Fiscal 3': 74870,
                                        'Garrapata': 43527,
                                        'Lotes 32 y 33 porcion W': 200061,
                                        'Laguna de los Pozuelos': 3777444,
                                        'de las Yungas': 13488705,
                                        'Altoandina de la Chinchilla': 3170373,
                                        'Finca Las Costas': 108087,
                                        'Divisadero Largo': 5081,
                                        'Laguna del Diamante': 1968190,
                                        'Laguna Aleusco': 10158,
                                        'Pizarro': 84887,
                                        'Lago Epuyén': 188580,
                                        'Lotes 1703-1704-4325-4326-4336-19866': 251927,
                                        'Serranías del Zapla': 371319,
                                        'Lanín': 1933017,
                                        'Lago Baggilt': 17290,
                                        'Nant y Fall (Arroyo Las Caídas)': 3613,
                                        'Andino Norpatagónica': 23573774,
                                        'Río Turbio': 713446,
                                        'Parque Costero del Sur': 261465,
                                        'Villavicencio': 624292,
                                        'El Nogalar de los Toldos': 32739,
                                        'Rincón de Ajó': 13995,
                                        'Iberá-Núcleo Carambola': 75177,
                                        'Copo': 1966112,
                                        'Isla Monte Leon': 4734,
                                        'Delta del Paraná': 1029920,
                                        'Islas de Victoria': 4352305,
                                        'Reserva Natural Otamendi': 41346,
                                        'Costanera Sur': 3321,
                                        'Iberá': 10687229,
                                        'Laguna Blanca': 6494213,
                                        'Los Alerces': 1885277,
                                        'Península de Magallanes': 454793,
                                        'Punta Lara': 55845,
                                        'Iberá-Rincón del Socorro/Iberá': 312879,
                                        'Mar Chiquita': 90020,
                                        'Mar Chiquita - Dragones de Malvinas': 18615,
                                        'Parque Atlántico Mar Chiquita': 286255,
                                        'Cabo Vírgenes': 26174,
                                        'Uspallata': 415969,
                                        'Bañados del Río Dulce y Laguna de Mar Chiquita': 10726532,
                                        'Campo San Juan': 57234,
                                        'Ansenuza': 4839670,
                                        'Manantiales': 3712676},
               'national_parks_only': {'Perito Moreno': 953034,
                                        'Monte León': 562692,
                                        'Chaco': 149308,
                                        'Nahuel Huapi': 4783064,
                                        'Lago Puelo': 189193,
                                        'Lihuel Calel': 327341,
                                        'Iguazú': 513122,
                                        'Islas de Santa Fe': 35210,
                                        'Patagonia': 524093,
                                        'Mburucuyá': 177189,
                                        'El Impenetrable': 1278233,
                                        'Traslasierra': 278364,
                                        'Bosques Petrificados de Jaramillo': 634930,
                                        'Quebrada del Condorito': 245790,
                                        'Los Glaciares': 5336408,
                                        'Iberá-Núcleo Carambola': 103123,
                                        'Iberá - Núcleo San Nicolás/San Alonso': 1070780,
                                        'Iberá - Núcleo Cambyretá': 234818,
                                        'Tierra del Fuego': 699878,
                                        'Pre-Delta': 26787,
                                        'El Rey': 398197,
                                        'El Palmar': 84978,
                                        'Talampaya': 2132167,
                                        'El Leoncito': 902265,
                                        'Los Cardones': 646695,
                                        'Calilegua': 773152,
                                        'Baritú': 682349,
                                        'Los Arrayanes': 17856,
                                        'Sierra de las Quijadas': 745001,
                                        'Lanín': 2182554,
                                        'Río Pilcomayo': 510557,
                                        'Aconquija': 1250357,
                                        'Campos del Tuyú': 30485,
                                        'Ciervo de los Pantanos': 56098,
                                        'San Guillermo': 1650043,
                                        'Ansenuza': 1776194,
                                        'Islotes Lobos': 195383,
                                        'Laguna El Palmar': 55535}
}




def process_areas():
    all_types = random.sample(list(PROTECTED_AREAS['national_parks_only'].keys()), 4)
    correct_r = random.choice(list(PROTECTED_AREAS['reserved_areas'].keys()))
    all_types.append(correct_r)
    random.shuffle(all_types)
    return all_types, correct_r



def main():
    st.title('Áreas Protegidas de Argentina')
    st.subheader('De las 5 opciones, 4 son Parques Nacionales y la restante es solo Reserva')

    # Initialize state
    if 'question' not in st.session_state:
        st.session_state.question = process_areas()
    if 'correct_answers' not in st.session_state:
        st.session_state.correct_answers = 0
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False

    all_types, correct_r = st.session_state.question

    c1, c2 = st.columns(2)

    with c1:
        # Disable radio options if the user has already responded
        selected_type = st.radio(
            'Marcá la opción que es solamente Reserva',
            all_types,
            index=None,
            disabled=st.session_state.answered
        )

        if selected_type and not st.session_state.answered:
            st.session_state.answered = True
            st.session_state.attempts += 1
            if selected_type == correct_r:
                st.session_state.correct_answers += 1

        if st.session_state.answered:
            if selected_type == correct_r:
                st.success(f'¡Correcto! {correct_r} es solo Reserva.')
            else:
                st.error(f'Incorrecto. La respuesta era: **{correct_r}**')

            if st.button('Siguiente pregunta →'):
                st.session_state.question = process_areas()
                st.session_state.answered = False
                st.rerun()

    with c2:
        st.metric('Respuestas correctas', st.session_state.correct_answers)
        st.metric('Número de intentos', st.session_state.attempts)



if __name__ == "__main__":
    main()
