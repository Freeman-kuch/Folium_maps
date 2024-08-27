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
        location=(
            6.510235738797816, 3.3718822564828392
        ),
        zoom_start=12,
    )
    folium.Marker(
        location=[
            6.510235738797400, 3.3718822564828392
        ],
        icon=image,
        popup="Testing the image link option in this pop-up",
    ).add_to(m)
    return m.get_root().render()


if __name__ == "__main__":
    app.run(debug=True)
