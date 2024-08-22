from flask import Flask, render_template_string

import folium

app = Flask(__name__)


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
            6.510235738797816, 3.3718822564828392
        ],
        tooltip="Freeman is calling on you!",
        popup="N.A is that you?",
        icon=folium.Icon(color="gray")
    ).add_to(m)
    return m.get_root().render()


if __name__ == "__main__":
    app.run(debug=True)
