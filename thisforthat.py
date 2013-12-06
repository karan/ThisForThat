import os
import random

# will move this to flask
# https://developers.google.com/appengine/
import webapp2
import jinja2

BUTTON = """
    <form action="/" method="get">
        <input type="submit" value="Refresh">
    </form>
    """

# get the templates directory
template_dir=os.path.join(os.path.dirname(__file__), 'templates')
# initialize my environment
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape']
)

THIS = ["Uber", "Skynet", "Digital Music Distribution", "FitBit",
        "Realtime Data", "ManPacks", "Landing Page", "Conversion Funnel",
        "Social Network", "Airbnb", "SnapChat", "Bang With Friends",
        "HTML5 App", "Google Analytics", "Mapreduce Query", "Node.js Server",
        "KickStarter", "Match.com", "Adultfriendfinder", "Pinterest",
        "Amber Alert System", "Groupon", "Appstore", "Digital Magazine",
        "Distributed Social Network", "Quadcopter", "Daring Fireball",
        "Content Distribution Network", "Analytics Platform", "OpenTable",
        "LinkedIn", "Brick and Mortar Solution", "Aggregator", "Social Game",
        "jQuery Plugin", "Game-based Incentive", "Foursquare", "YouTube",
        "WeedMaps", "Texts From Last Night", "Ponzi Scheme",
        "1-800-Flowers", "Cash4Gold", "Online Marketplace", "Viral Marketer",
        "Wearable Computer", "Google Glass App", "Facebook Marketplace",
        "Zivity", "Playboy", "Cloud Storage Provider", "Kindle Fire App",
        "Pandora", "Green Tech Program", "Eco-Friendly Marketplace",
        "Netflix", "Amazon", "Zappos", "Reddit", "Enron", "Wordpress",
        "iPhone App", "Android App", "Meme Generator", "Crowdsourcing App",
        "Mac App", "SEO Optimizer", "Apartment Guide", "Social CRM",
        "Database Abstraction Layer", "Microblogging Service",
        "Product Curation Service", "API", "New Social Platform", "Tumblr",
        "Deal Finder", "CPA Ad Network", "Collaborative Filter",
        "Shopping Site", "Digg 2.0", "Recommendation Engine",
        "News Recommender", "Neural Network", "Tesseract OCR engine",
        "Unreadable CAPTCHA", "Mobile Ecosystem", "Flickr", "Salesforce.com",
        "Twitter Filter", "Wikipedia", "Yelp", "Google App Engine",
        "Saturday Night Live", "BitTorrent", "Starbucks"]

THAT = ["Facebook Platform", "Erlang Enthusiasts", "Collegiate Jewish Women",
        "Ex-Girlfriends", "Binders Full of Women", "Mitt Romney's Hair",
        "Laundromats", "Celebrity Gossip", "Endangered Species", "Pandas",
        "Middle Schoolers", "Alpha Phi Girls", "Funeral Homes",
        "Chinese Take-out", "Ex-Convicts", "Fast Casual Restaurants",
        "Marketers", "Qualifying Leads", "Funeral Homes", "Farmers",
        "Cougars", "Pilots", "Gynecologists", "Cracked iPhone Apps",
        "Stolen Goods", "Adult Dancers", "People Who Hate Groupon",
        "Hunters", "High-End Pornography", "Sysadmins", "Bath Salts",
        "Nootropics", "California", "Gay Marriages", "Government Corruption",
        "Political Attack Ads", "Whiskey Lovers", "Parking Tickets",
        "Highway Accidents", "Traveling", "Airlines", "Presentation Tools",
        "Your Boss", "Ponzi Schemes", "Your Finances", "Restroom Attendants",
        "Your Aquarium", "Your Cat's Litter Box", "Pets", "Alcoholics",
        "Camp Counselors", "Nature Blogs", "World of Warcraft", "Models",
        "Family Guy Enthusiasts", "The Army", "Cheap Vodka",
        "Tech Incubators", "Star Trek Conventions", "Presentation Tools",
        "Small Businesses", "Beer", "Nightclub Lines", "Ugly People",
        "Attractive People", "Semi-Active Volcanoes", "Traveling Abroad",
        "Sanctimonial Artifacts", "Your Mom", "Billionaires", "Happy Hours",
        "Ugg Boots", "The Homeless", "Blacking Out", "Red Wine",
        "Christian Families", "Social Outcasts", "Sorority Chicks",
        "Surgeons", "Pounding Jagger Bombs", "Medicinal Marijuana",
        "Textbooks", "Coffee Shops", "Baristas"]


class MainPage(webapp2.RequestHandler):

    def one_this(self):
        return random.choice(THIS)


    def one_that(self):
        return random.choice(THAT)

    def get(self):
        template_values = {
            'this': self.one_this(),
            'that': self.one_that(),
        }
        template = JINJA_ENV.get_template('index.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)