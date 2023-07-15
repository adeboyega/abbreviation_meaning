from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
abbreviations = {
    'HTML': 'HyperText Markup Language',
    'CSS': 'Cascading Style Sheets',
    'JS': 'JavaScript',
    'LOL': 'Laugh Out Loud',
    'API': 'Application Programming Interface',
    'PDF': 'Portable Document Format',
    'URL': 'Uniform Resource Locator',
    'VPN': 'Virtual Private Network',
    'HTTP': 'Hypertext Transfer Protocol',
    'AFK': 'Away From Keyboard',
    'ASAP': 'As Soon As Possible',
    'BFF': 'Best Friends Forever',
    'BRB': 'Be Right Back',
    'BTW': 'By The Way',
    'FAQ': 'Frequently Asked Questions',
    'FYI': 'For Your Information',
    'GG': 'Good Game',
    'GTG': 'Got To Go',
    'IDK': 'I Don\'t Know',
    'IMO': 'In My Opinion',
    'IRL': 'In Real Life',
    'JK': 'Just Kidding',
    'LMAO': 'Laughing My Ass Off',
    'LOL': 'Laugh Out Loud',
    'NP': 'No Problem',
    'OMG': 'Oh My God',
    'ROFL': 'Rolling On the Floor Laughing',
    'TTYL': 'Talk To You Later',
    'WTF': 'What The F***',
    'YW': 'You\'re Welcome',
    'AF': 'As F***',
    'ASL': 'Age, Sex, Location',
    'ATB': 'All The Best',
    'B4': 'Before',
    'BAE': 'Before Anyone Else',
    'BB': 'Bye Bye',
    'BC': 'Because',
    'BIO': 'Biography',
    'BR': 'Best Regards',
    'CUL8R': 'See You Later',
    'CYA': 'See Ya',
    'DAE': 'Does Anyone Else',
    'DIY': 'Do It Yourself',
    'DM': 'Direct Message',
    'ETA': 'Estimated Time of Arrival',
    'FB': 'Facebook',
    'FOMO': 'Fear Of Missing Out',
    'FTW': 'For The Win',
    'FWIW': 'For What It\'s Worth',
    'GF': 'Girlfriend',
    'GM': 'Good Morning',
    'GN': 'Good Night',
    'GR8': 'Great',
    'HAND': 'Have A Nice Day',
    'HF': 'Have Fun',
    'HMU': 'Hit Me Up',
    'ICYMI': 'In Case You Missed It',
    'IDC': 'I Don\'t Care',
    'ILY': 'I Love You',
    'IMHO': 'In My Humble Opinion',
    'IRL': 'In Real Life',
    'ISO': 'In Search Of',
    'JK': 'Just Kidding',
    'JSYK': 'Just So You Know',
    'K': 'Okay',
    'L8R': 'Later',
    'LMK': 'Let Me Know',
    'MCM': 'Man Crush Monday',
    'MT': 'Modified Tweet',
    'NBD': 'No Big Deal',
    'NVM': 'Never Mind',
    'OFC': 'Of Course',
    'OMW': 'On My Way',
    'OOTD': 'Outfit Of The Day',
    'OP': 'Original Poster',
    'PPL': 'People',
    'RN': 'Right Now',
    'ROFLMAO': 'Rolling On the Floor Laughing My Ass Off',
    'SMH': 'Shaking My Head',
    'SFW': 'Safe For Work',
    'TBH': 'To Be Honest',
    'TGIF': 'Thank God It\'s Friday',
    'TMI': 'Too Much Information',
    'TBT': 'Throwback Thursday',
    'TTYL': 'Talk To You Later',
    'TY': 'Thank You',
    'WB': 'Welcome Back',
    'WCW': 'Woman Crush Wednesday',
    'WDYM': 'What Do You Mean',
    'WYD': 'What You Doing',
    'YOLO': 'You Only Live Once',
    'ZZZ': 'Sleeping or Bored',
    '4EVA': 'Forever',
    'AFAIK': 'As Far As I Know',
    'AMA': 'Ask Me Anything',
    'BBL': 'Be Back Later',
    'BRH': 'Be Right Here',
    'BTDT': 'Been There, Done That',
    'BTT': 'Back To Topic',
    'CTA': 'Call To Action',
    'DIKU': 'Do I Know You',
    'EM': 'Email',
    'FBO': 'Facebook Official',
    'FTFY': 'Fixed That For You',
    'GRATZ': 'Congratulations',
    'HBD': 'Happy Birthday',
    'ICYMI': 'In Case You Missed It',
    'ILYSM': 'I Love You So Much',
    'IMNSHO': 'In My Not So Humble Opinion',
    'IMO': 'In My Opinion',
    'IRL': 'In Real Life',
    'ISTG': 'I Swear To God',
    'JFYI': 'Just For Your Information',
    'KOTD': 'Kicks Of The Day',
    'L8': 'Late',
    'LMFAO': 'Laughing My Freaking Ass Off',
    'LMK': 'Let Me Know',
    'LOLZ': 'Laughing Out Loud',
    'MIA': 'Missing In Action',
    'NAGI': 'Not A Good Idea',
    'NGL': 'Not Gonna Lie',
    'NM': 'Never Mind',
    'NVM': 'Never Mind',
    'OMG': 'Oh My God',
    'OOTD': 'Outfit Of The Day',
    'OP': 'Original Poster',
    'OT': 'Off Topic',
    'OTL': 'Out To Lunch',
    'POTD': 'Photo Of The Day',
    'ROFL': 'Rolling On the Floor Laughing',
    'ROTFL': 'Rolling On the Floor Laughing',
    'SMH': 'Shaking My Head',
    'SO': 'Significant Other',
    'SRSLY': 'Seriously',
    'TBH': 'To Be Honest',
    'TBT': 'Throwback Thursday',
    'TFW': 'That Feeling When',
    'TIL': 'Today I Learned',
    'TL;DR': 'Too Long; Didn\'t Read',
    'TMI': 'Too Much Information',
    'TTYL': 'Talk To You Later',
    'WBU': 'What About You',
    'WDYM': 'What Do You Mean',
    'WYD': 'What You Doing',
    'WYWH': 'Wish You Were Here',
    'XOXO': 'Hugs and Kisses',
    'YMMV': 'Your Mileage May Vary',
    'YOLO': 'You Only Live Once',
    'YW': 'You\'re Welcome',
    '404': 'Not Found',
    '911': 'Emergency',
    '2BZ4UQT': 'Too Busy For You, Cutie',
    '2FAB': 'Too Fabulous',
    '2G2BT': 'Too Good To Be True',
    '2M2H': 'Too Much To Handle',
    '2MI': 'Too Much Information',
    '2MORO': 'Tomorrow',
    '2NITE': 'Tonight',
    '4COL': 'For Crying Out Loud',
    '6Y': 'Sexy',
    '8': 'Cool',
    '10Q': 'Thank You'
    # Add more abbreviations and their full names here
    # ...
}

# API endpoint to handle abbreviation requests
@app.route('/api/abbreviation/<abbr>')
def get_abbreviation(abbr):
    abbreviation = abbr.upper()
    full_name = abbreviations.get(abbreviation) or abbreviations.get(abbreviation.lower())

    if full_name:
        response = jsonify({'abbreviation': abbreviation, 'fullName': full_name})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return make_response(jsonify({'error': 'Abbreviation not found'}), 404)

# Start the server
if __name__ == '__main__':
    app.run(port=7000)
