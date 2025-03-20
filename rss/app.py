from flask import Flask, render_template
import feedparser

app = Flask(__name__)

rss_feeds = {
    'gma': 'https://www.gmanetwork.com/news/24oras/rss/news/',
    'abscbn': 'https://news.abs-cbn.com/rss/tvpatrol-feed',
    'tv5': 'https://interaksyon.philstar.com/feed/',
    'rappler': 'https://www.rappler.com/rss',
    'manilatimes': 'https://www.manilatimes.net/rss.xml',
    'inquirer': 'https://newsinfo.inquirer.net/feed',
    'buhaymuntinlupa': 'https://www.buhaymuntinlupa.com/feed',
    'dzbb': 'https://www.gmanetwork.com/news/dzbb/rss',
    'news5': 'https://www.news5.com.ph/rss',
}

default_news = {
    "title": "No Recent News Found",
    "published": "N/A",
    "summary": "There are no available news reports from this source at the moment. Please check back later.",
    "link": "#"
}

def get_news(publication):
    feed = feedparser.parse(rss_feeds.get(publication, ""))

    print(f"Fetching news from {publication.upper()} - Feed Status: {feed.bozo}")

    articles = feed.entries[:5] if feed.entries else [default_news]

    news_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Latest News from {publication.upper()}</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #d4a1f9, #fcd3fc, #a1c8fc);
                color: #333;
                margin: 0;
                padding: 0;
            }}
            header {{
                background-color: #6a1b9a;
                color: white;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .container {{
                max-width: 800px;
                margin: 30px auto;
                padding: 20px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
            }}
            .article {{
                margin-bottom: 20px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }}
            .article h2 {{
                color: #6a1b9a;
                margin-bottom: 10px;
            }}
            .article i {{
                color: #888;
                font-size: 0.9em;
            }}
            .article p {{
                color: #555;
                line-height: 1.6;
                margin: 10px 0;
            }}
            .article a {{
                color: #1a73e8; /* Lighter blue */
                text-decoration: underline; /* Underline links */
                font-weight: bold;
            }}
            .article a:hover {{
                color: #0049b7; /* Darker blue on hover */
                text-decoration: underline; /* Keep underline */
            }}
            footer {{
                text-align: center;
                margin-top: 30px;
                padding: 10px;
                color: #555;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Latest News from {publication.upper()}</h1>
        </header>
        <div class="container">
    """

    for article in articles:
        news_html += f"""
            <div class="article">
                <h2>{article.get("title", "No Title")}</h2>
                <i>{article.get("published", "No date available")}</i>
                <p>{article.get("summary", "No summary available")}</p>
                <a href="{article.get('link', '#')}" target="_blank">Read more</a>
            </div>
        """

    news_html += """
        </div>
        <footer>
            <p>&copy; 2025 News Portal. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return news_html



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/gma")
def gma_news():
    return get_news('gma')

@app.route("/abscbn")
def abscbn_news():
    return get_news('abscbn')

@app.route("/tv5")
def tv5_news():
    return get_news('tv5')

@app.route("/rappler")
def rappler_news():
    return get_news('rappler')

@app.route("/manilatimes")
def manilatimes_news():
    return get_news('manilatimes')

@app.route("/inquirer")
def inquirer_news():
    return get_news('inquirer')

@app.route("/buhaymuntinlupa")
def buhaymuntinlupa_news():
    return get_news('buhaymuntinlupa')

@app.route("/dzbb")
def dzbb_news():
    return get_news('dzbb')

@app.route("/news5")
def news5_news():
    return get_news('news5')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
