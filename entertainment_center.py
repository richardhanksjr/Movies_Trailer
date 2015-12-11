import media
import fresh_tomatoes

# Create instances to be used as data in fresh_tomatoes.py
smokey_bandit = media.Movie(
    "Smokey and the Bandit",
    "Big Enos (Pat McCormick) wants to drink Coors at"
    "a truck show, but in 1977 it was illegal to" +
    "sell Coors east of the Mississippi River" +
    "without a permit.",
    "http://www.atlantatimemachine.com/images/smokey%20poster.jpg",
    "https://www.youtube.com/watch?v=OH5KNcFRZLQ")


ferris = media.Movie(
    "Ferris Bueller's Day Off",
    "Ferris Bueller (Matthew Broderick) has an uncanny skill at cutting" +
    "classes and getting away with it.",
    "http://ecx.images-amazon.com/images/I/51VSX1b53oL._SY355_.jpg",
    "https://www.youtube.com/watch?v=R-P6p86px6U")

money_pit = media.Movie(
    "The Money Pit",
    "Needing a new home, they settle on buying a country estate outside the" +
    "city, which is available for a suspiciously low price. It soon becomes" +
    "apparent why, as doors fall off their hinges, staircases come tumbling" +
    "down and a bathtub falls through the floor. The couple's relationship" +
    "suffers similarly.",
    "http://bit.ly/1OUOkZZ",
    "hhttps://www.youtube.com/watch?v=TLLQquBdU8M")


back_to_future = media.Movie(
    "Back to the Future",
    "Small-town California teen Marty McFly (Michael J. Fox) is thrown back" +
    "into the '50s when an experiment by his eccentric scientist friend Doc" +
    "Brown (Christopher Lloyd) goes awry.",
    "http://bit.ly/1NYEsj9",
    "www.youtube.com/watch?v=JWyOC4n4qSc")

jaws = media.Movie(
    "Jaws",
    "When a young woman is killed by a shark while skinny-dipping near" +
    "the New England tourist town of Amity Island, police chief Martin" +
    "Brody (Roy Scheider) wants to close the beaches, but mayor Larry" +
    "Vaughn (Murray Hamilton) overrules him, fearing that the loss of" +
    "tourist revenue will cripple the town.",
    "http://s.ecrater.com/stores/233341/4f14e939989ad_233341n.jpg",
    "https://www.youtube.com/watch?v=U1fu_sA7XhE")

ghostbusters = media.Movie(
    "Ghostbusters",
    "After the members of a team of scientists (Harold Ramis, Dan Aykroyd" +
    ", Bill Murray) lose their cushy positions at a university in New York" +
    "City, they decide to become 'ghostbusters' to wage a high-tech battle" +
    "with the supernatural for money.",
    "http://bit.ly/1WjpEu1",
    "www.youtube.com/watch?v=UiBxtRuwf7I")

# List of all movies
movies = [smokey_bandit, ferris, money_pit, back_to_future, jaws, ghostbusters]

#A call open the webpage and populate with the information contained in
#entertainment_center.py
fresh_tomatoes.open_movies_page(movies)

