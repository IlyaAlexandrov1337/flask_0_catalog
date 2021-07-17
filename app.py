from flask import Flask, render_template
from data import title, subtitle, description, departures, tours
from random import sample


# функция для определения окончания слова "ночь" рядом с количеством
def word_night(num_night):
    num = num_night % 100
    if 10 < num < 15:
        term = "ей"
    else:
        num = num_night % 10
        if num == 1:
            term = "ь"
        elif 1 < num < 5:
            term = "и"
        else:
            term = "ей"
    return f"ноч{term}"


app = Flask(__name__)


@app.route("/")
def main_render():
    keys = sample(dict.fromkeys(tours).keys(), 6)
    new_tours = {x: tours[x] for x in keys}
    return render_template('index.html', title=title, tours=new_tours, subtitle=subtitle, description=description)


@app.route("/departures/<departure>/")
def departures_render(departure):
    new_tours = {x: tours[x] for x in tours.keys() if tours[x]["departure"] == departure}
    return render_template('departure.html', dep_id=departure, title=title, tours=new_tours, departures=departures,
                           f=word_night)


@app.route("/tours/<int:id>/")
def tours_render(id):
    return render_template('tour.html', title=title, hotel=tours[id], departures=departures)


if __name__ == "__main__":
    app.run()
