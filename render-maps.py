import folium

mapa = folium.Map(
    location=[-22.951803, -43.210328],
    tiles='Stamen Terrain', 
    zoom_start=16
)

folium.Marker(
    [-22.951803, -43.210328],
    popup='<i>Estátua do Cristo Redentor</i>', 
    tooltip='Click aqui!'
).add_to(mapa)

mapa.save(r'mapa.html')