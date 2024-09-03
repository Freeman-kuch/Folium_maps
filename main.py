from flask import Flask, render_template_string

import folium

app = Flask(__name__)

image = folium.CustomIcon(
    "http://media-cache-ec0.pinimg.com/736x/19/52/4d/19524ddf1e4aa4c4b723ce603e606071.jpg",
    icon_size=(38, 95),
)


@app.route("/")
def fullscreen():
    """Simple example of a fullscreen map."""
    m = folium.Map(
        location=(6.510235738797816, 3.3718822564828392),
        zoom_start=12,
    )
    folium.Marker(
        location=[
            6.4639,
            3.3953,
        ],
        icon=folium.Icon(color="green"),
        popup="Testing the image link option in this pop-up",
    ).add_to(m)
    folium.Marker(
        location=[
            6.5101,
            3.3718,
        ],
        popup=folium.Popup("Let's try quotes", parse_html=True, max_width=100),
    ).add_to(m)

    folium.Marker(
        location=[
            6.5102,
            3.3720,
        ],
        icon=folium.Icon(color="blue"),
        popup=folium.Popup("something about Tissot", parse_html=True, max_width="100%"),
    ).add_to(m)
    folium.Marker(
        location=[
            6.514193,
            3.308678,
        ],
        icon=folium.Icon(color="black"),
        popup=folium.Popup("Ça c'est chouette", parse_html=True, max_width="100%"),
    ).add_to(m)
    folium.Marker(
        location=[
            6.43639,
            3.53556,
        ],
        icon=folium.Icon(color="brown"),
        popup=folium.Popup("random point 2", parse_html=True, max_width="100%"),
    ).add_to(m)
    folium.Marker(
        location=[
            6.4442,
            3.4054,
        ],
        icon=folium.Icon(color="red"),
        popup=folium.Popup("anywhere is nowhere, stop looking", parse_html=True, max_width="100%"),
    ).add_to(m)

    return m.get_root().render()


if __name__ == "__main__":
    app.run(debug=True)
