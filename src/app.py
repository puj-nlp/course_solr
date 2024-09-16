import streamlit as st
import pysolr
import pandas as pd
import re  # Importamos la librería re para limpiar las etiquetas HTML


# Configuración de Solr
def search_song_lyrics(core_url, search_term):
    """
    Consulta las canciones en Solr por el contenido de las letras (lyrics) y
    devuelve la canción que contiene el término de búsqueda.
    """
    try:
        # Conectarse al core de Solr
        solr = pysolr.Solr(core_url, always_commit=True, timeout=10)

        # Definir los parámetros de la consulta
        params = {
            'hl': 'true',  # Activar el resaltado de texto
            'hl.fl': 'lyrics',  # Resaltar coincidencias en el campo 'lyrics'
            'hl.snippets': 2,  # Mostrar dos frases donde se encontró el término
            'hl.simple.pre': '<b>',
            'hl.simple.post': '</b>',
            'fl': '* score'  # Incluir todos los campos y el score
        }

        # Realizar la búsqueda en el campo "lyrics"
        results = solr.search(f"lyrics:{search_term}", **params)

        # Procesar los resultados
        processed_results = []

        for result in results:
            # Verificar si existe el resaltado para el documento
            highlighted_lyrics = results.highlighting.get(result['id'], {}).get('lyrics', [])

            # Limpiar las etiquetas <b> y </b> del texto resaltado
            clean_lyrics = [re.sub(r'<.*?>', '', frag)[:200] + '...' for frag in
                            highlighted_lyrics]  # Limitar a 200 caracteres

            song_data = {
                'id': result.get('id'),
                'title': result.get('title')[0] if result.get('title') else 'N/A',
                'artists': result.get('artists')[0] if result.get('artists') else 'N/A',
                'language': result.get('language')[0] if result.get('language') else 'N/A',
                'url': result.get('url')[0] if result.get('url') else 'N/A',
                'type': result.get('type')[0] if result.get('type') else 'N/A',
                'lyrics_highlighted': clean_lyrics if clean_lyrics else ["No hay fragmentos destacados"],
                'score': result.get('score')
            }
            processed_results.append(song_data)

        return processed_results

    except Exception as e:
        st.error(f"Error al realizar la consulta: {e}")
        return []


# Streamlit App
def main():
    st.title("Consulta de Canciones en Solr")

    # Campo de entrada para la consulta
    search_term = st.text_input("Ingrese un término para buscar en las letras:", "")

    # Botón para iniciar la búsqueda
    if st.button("Buscar"):
        if search_term:
            # Realizar la consulta a Solr
            core_url = 'http://localhost:8983/solr/lyrics_example'
            results = search_song_lyrics(core_url, search_term)

            # Mostrar los resultados en forma de tabla
            if results:
                st.write(f"Resultados para : '{search_term.lower()}':")

                # Crear DataFrame para mostrar en tabla
                df = pd.DataFrame(results)

                # Convertir el DataFrame a HTML y aplicar estilos CSS para reducir el tamaño de la fuente
                table_html = df[['title', 'artists', 'language', 'url', 'type', 'score']].to_html(index=False)

                # Aplicar CSS para cambiar el tamaño de la tabla
                st.markdown("""
                <style>
                table {
                    font-size: 12px;
                    width: 100%;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)

                # Mostrar la tabla con los datos
                st.markdown(table_html, unsafe_allow_html=True)

                # Crear un botón para cada resultado que muestre los fragmentos destacados
                for result in results:
                    with st.expander(f"Mostrar fragmentos destacados para {result['title']}"):
                        st.markdown(f"**ID**: {result['id']}")
                        st.markdown(f"**Fragmentos destacados**:")

                        # Mostrar los fragmentos por separado y limitados
                        for i, fragment in enumerate(result['lyrics_highlighted']):
                            st.markdown(f"**Fragmento {i + 1}:**")
                            st.markdown(f"<div style='font-size:12px;'>{fragment}</div>", unsafe_allow_html=True)
                            st.divider()  # Añadir separador entre fragmentos

            else:
                st.write("No se encontraron resultados.")
        else:
            st.warning("Por favor, ingrese un término para buscar.")


if __name__ == "__main__":
    main()
