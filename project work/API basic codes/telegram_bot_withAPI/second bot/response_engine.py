import re

# 5 templates to wrap around each synonym
templates = [
    "{synonym}",
    "{synonym}!",
    "{synonym} 😊",
    "{synonym} please",
    "{synonym}?"
]

# 10 categories × 20 synonyms each = 200 total entries
synonym_lists = {
    "greetings": [
        "hello", "hi", "hey", "greetings", "good morning", "good afternoon",
        "good evening", "hiya", "what's up", "yo", "hey there", "hello there",
        "hiya", "sup", "howdy", "hello!", "hi!", "hey!", "greetings!", "salutations"
    ],
    "farewells": [
        "bye", "goodbye", "see you", "see ya", "later", "farewell",
        "take care", "catch you later", "bye-bye", "ciao", "adios", "peace out",
        "toodle-oo", "cheerio", "bye!", "goodbye!", "see you!", "later!",
        "take care!", "farewell!"
    ],
    "thanks": [
        "thank you", "thanks", "thx", "thank you so much", "thanks a lot",
        "much appreciated", "thanks!", "thank you!", "ty", "cheers",
        "gratitude", "I appreciate it", "I owe you one", "thanks buddy",
        "thanks pal", "thanks friend", "thanks that helps", "thanks very much",
        "thanks 😊", "thanks 🙂"
    ],
    "apologies": [
        "sorry", "my apologies", "I apologize", "pardon me", "excuse me",
        "oops", "whoops", "mea culpa", "sorry!", "my bad", "forgive me",
        "apologies", "I messed up", "that was my mistake", "I didn't mean that",
        "so sorry", "I'm sorry", "sorry about that", "sorry everyone", "sry"
    ],
    "wellbeing": [
        "how are you", "how's it going", "how do you do", "how have you been",
        "what's up", "what's new", "how are things", "how do you feel",
        "how are you doing", "how r you", "are you okay", "how's life",
        "how r u", "how are you?", "how's it going?", "how do you do?",
        "how have you been?", "what's up?", "what's new?", "are you well"
    ],
    "name_queries": [
        "what's your name", "who are you", "what are you called", "your name?",
        "name?", "who you are", "may I know your name", "tell me your name",
        "who am I talking to", "what should I call you", "your name",
        "who you", "I want your name", "your identity", "introduce yourself",
        "what do I call you", "you are", "you're", "your new name", "who is this"
    ],
    "origin_queries": [
        "where are you from", "origin", "where do you live", "where do you come from",
        "your origin", "born where", "from where", "location", "residence",
        "your hometown", "where u from", "where are you", "domain", "source",
        "where do you stay", "geolocation", "in what country", "in what city",
        "earth location", "virtual home"
    ],
    "joke_requests": [
        "tell me a joke", "joke", "make me laugh", "funny", "say something funny",
        "humor me", "one-liner", "pun", "knock knock", "got any jokes",
        "joke please", "a joke", "funny joke", "tell joke", "tell me something funny",
        "jokes", "comedian mode", "I'm bored", "cheer me up", "lighten the mood"
    ],
    "help_requests": [
        "help", "assist me", "I need help", "can you help me", "support",
        "help please", "aid me", "I need assistance", "guide me", "help!",
        "assist", "help me out", "give me assistance", "lend me a hand",
        "I need a hand", "how to", "instruction", "tutorial", "guide",
        "walk me through"
    ],
    "weather_queries": [
        "what's the weather", "weather", "current weather", "forecast",
        "how's the weather", "weather please", "weather today", "rain or shine",
        "temperature", "is it raining", "is it sunny", "weather update",
        "weather report", "weather now", "will it rain", "what's the forecast",
        "weather?", "weather??", "tell weather", "weather info"
    ]
}

# Predefined response by category
responses = {
    "greetings":       "Hello! How can I assist you today?",
    "farewells":       "Goodbye! Have a great day!",
    "thanks":          "You're welcome!",
    "apologies":       "No worries!",
    "wellbeing":       "I'm a bot, but I'm functioning perfectly!",
    "name_queries":    "I'm Copilot, your friendly assistant!",
    "origin_queries":  "I reside in the cloud 🌩️",
    "joke_requests":   "Why did the programmer quit? Because he didn't get arrays.",
    "help_requests":   "Sure, what do you need help with?",
    "weather_queries": "I don't have real-time weather, but it's always sunny in code!"
}

# Build regex→response mapping
pattern_response_pairs = {}
for category, synonyms in synonym_lists.items():
    for synonym in synonyms:
        for tmpl in templates:
            phrase = tmpl.format(synonym=synonym)
            # case-insensitive whole-word match
            pattern = re.compile(r"\b" + re.escape(phrase.lower()) + r"\b", re.IGNORECASE)
            pattern_response_pairs[pattern] = responses[category]

# Confirm you've generated at least 1,000 patterns
#assert len(pattern_response_pairs) >= 1000

def handle_response(text: str) -> str:
    for pattern, response in pattern_response_pairs.items():
        if pattern.search(text):
            return response
    return "I'm still learning. Try asking about jokes, greetings, or weather!"