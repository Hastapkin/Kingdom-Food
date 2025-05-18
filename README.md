## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Email Processing**: Flask-Mail
- **Environment Variables**: python-dotenv

## Project Structure

kingdomfoods/
├── app.py              
├── config.py              
├── email.py              
├── language.py            
├── requirements.txt       
├── .env                   
├── static/               
│   ├── css/
│   │   └── styles.css   
│   ├── js/
│   │   ├── enhanced-slideshow.js  
│   │   └── main.js                  
│   └── images/     
│       ├── logos/      
│       │       ├── Logo C.png       # Company logo C
│       │       └──Logo W.png       # Company logo W
│       ├── slide_images/
│       │       ├── ex_img_1.jpg
│       │       ├── ex_img_2.jpg
│       │       ├── ex_img_3.jpg
│       │       ├── ex_img_4.jpg
│       │       ├── ex_img_5.jpg
│       │       └── ...
│       └── background/
│               ├── BG1.jpg      
│               └── BG2.png     
└── templates/            
    ├── base.html         
    ├── index.html       
    ├── pages/
    │   ├── laos.html      
    │   ├── vietnamese.html
    │   └── thai.html      
    ├── contact.html      
    ├── thank_you.html   
    ├── 404.html          
    └── 500.html

## Set up to run on local

1. python -m venv venv

2. venv\Scripts\activate

3. pip install -r requirements.txt OR pip install -r PATH(requirements.txt)

4. python app.py

Running on http://127.0.0.1:5000/
