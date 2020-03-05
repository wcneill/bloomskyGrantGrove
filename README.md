# BloomSky Camera Feed Script
A small script for pulling down the live camera feed from our new BloomSky cam at Grant Grove Village

# Directions
The relative path where you run the script should look like this: 

.

├── bloomskyGGV.py (or whatever name you save my script as)

├── html

│   └── final.html  (or whatever the page name is that will be finally displayed when the server sends a response)

└── templates

    └── template.html (or whatever you want to call your template html)
    

./templates/template.html should be a template version of the visitsequoia.com page where you want to display the feed. 

Inside template.html, wherever you want the URL to go, format that space with {{photo_url}}, for example: 

<img src=”{{photo_url}}” alt =”Live Weather at Grant Grove”>

The script will then write the final product to ./html/final.html, which the server can send out.

As a side note, template.html and final.html are optional file names. Just change them to whatever you want in the last line of the script: 

generate_html('template.html', 'final.html')

and make sure that it matches the names in your file system. 
